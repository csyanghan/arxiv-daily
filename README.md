# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-11 12:46:08

## 📅 2026-03-11 (今日最新)

**相关论文数：73**

### 1. [SiliconMind-V1: Multi-Agent Distillation and Debug-Reasoning Workflows for Verilog Code Generation](https://arxiv.org/abs/2603.08719)

**基本信息**

- 🔗 arXiv: [`2603.08719`](https://arxiv.org/abs/2603.08719)
- 👥 作者: Mu-Chi Chen, Yu-Hung Kao, Po-Hsuan Huang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08719.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于代码生成的多智能体大模型框架（SiliconMind-V1），其方法论（多智能体、推理导向、迭代验证）与“化学大模型”主题直接相关，为化学领域复杂任务的模型构建提供了可借鉴的架构。

**📖 中文摘要**

这篇论文提出了一个用于Verilog代码生成的多智能体框架，并引入了SiliconMind-V1模型。该框架集成了面向推理的训练数据生成和基于测试平台的验证。虽然论文的核心应用领域是硬件设计自动化，但其方法论与“化学大模型”主题高度相关。论文的核心贡献在于开发了一个统一的、多智能体的、以推理为导向的框架，用于生成、测试和调试代码。这种“多智能体蒸馏”和“调试-推理工作流”的范式，本质上是一种用于复杂结构化输出（Verilog代码）生成和验证的“大模型”应用框架。其思想——利用多个专门化的智能体进行迭代生成、验证和修正——可以直接迁移到化学信息学领域，例如用于分子结构生成、逆合成分析或质谱解析等需要多步骤推理和验证的任务。因此，该论文为构建面向化学领域的、具有自我验证和修正能力的大模型系统提供了重要的方法论参考和架构设计思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have recently emerged as a promising approach for automating Verilog code generation; however, existing methods primarily emphasize syntactic correctness and often rely on commercial models or external verification tools, which introduces concerns regarding cost, data privacy, and limited guarantees of functional correctness. This work proposes a unified multi-agent framework for reasoning-oriented training data generation with integrated testbench-driven verification, enabling locally fine-tuned LLMs, SiliconMind-V1, to iteratively generate, test, and debug Register-Transfer Level (RTL) designs through test-time scaling. Experimental results on representative benchmarks (VerilogEval-v2, RTLLM-v2, and CVDP) demonstrate that the proposed approach outperforms the state-of-the-art QiMeng-CodeV-R1 in functional correctness while using fewer training resources.

</details>

---

### 2. [AnalogToBi: Device-Level Analog Circuit Topology Generation via Bipartite Graph and Grammar Guided Decoding](https://arxiv.org/abs/2603.08720)

**基本信息**

- 🔗 arXiv: [`2603.08720`](https://arxiv.org/abs/2603.08720)
- 👥 作者: Seungmin Kim, Mingun Kim, Yuna Lee 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08720.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用图表示和生成模型进行结构化设计（电路拓扑）的自动生成。其技术路线（图表示、条件生成、语法约束）与化学信息学中“化学大模型”用于分子图生成和设计的核心任务高度相似，具有直接的方法论相关性。

**📖 中文摘要**

这篇论文提出了AnalogToBi框架，用于设备级模拟电路拓扑的自动生成。该框架使用二分图表示和语法引导解码来生成电路，并实现了对电路功能的条件控制。虽然研究领域是电子设计自动化（EDA），但其核心技术创新——使用图结构表示和生成模型来探索复杂的、离散的设计空间——与“化学大模型”和“质谱结构推理”有深刻的类比关系。在化学中，分子同样可以用图（原子为节点，化学键为边）来表示，分子生成或性质预测是化学信息学的核心任务。AnalogToBi所解决的“有限的功能可控性”、“训练数据记忆”和“生成无效结构”等问题，正是当前分子生成模型（如基于图的生成模型）面临的挑战。此外，其“语法引导解码以确保电学有效性”的思想，类似于在分子生成中引入化学价规则或反应规则约束以确保生成分子的化学合理性。因此，该论文为化学领域（特别是分子设计与生成）的图生成大模型提供了重要的技术参考和解决方案思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automatic generation of device-level analog circuit topologies remains a fundamental challenge in analog design automation. Recent transformer-based approaches have shown promise, yet they often suffer from limited functional controllability, memorization of training data, and the generation of electrically invalid circuits. We propose AnalogToBi, a device-level analog circuit topology generation framework that addresses these limitations. AnalogToBi enables explicit functional control via a circuit type token and adopts a bipartite graph-based circuit representation that decouples positional ordering from functional semantics, encouraging structural reasoning over sequence memorization. In addition, grammar-guided decoding enforces electrical validity during generation, while apply device renaming-based data augmentation improves generalization by increasing sequence diversity without altering circuit functionality. Experimental results show that AnalogToBi achieves 97.8% validity and 92.1% novelty, resulting in 89.9% valid and novel circuits under conditional generation, without human expert involvement. We further present that generated circuits can be automatically translated into SPICE netlists, and SPICE simulations confirm that AnalogToBi discovers high-quality analog topologies that outperform prior methods. For code and supplementary materials, see this https URL

</details>

---

### 3. [Robust Parameter and State Estimation in Multiscale Neuronal Systems Using Physics-Informed Neural Networks](https://arxiv.org/abs/2603.08742)

**基本信息**

- 🔗 arXiv: [`2603.08742`](https://arxiv.org/abs/2603.08742)
- 👥 作者: Changliang Wei, Yangyang Wang, Xueyu Zhu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08742.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用物理信息神经网络（PINN）解决从观测数据反演复杂系统参数和状态的反问题。该方法论与“质谱结构推理”的核心挑战（从质谱信号反演分子结构）高度相关，为解决该问题提供了新的、有潜力的技术路径。

**📖 中文摘要**

这篇论文提出了一个基于物理信息神经网络（PINN）的框架，用于从部分和噪声观测中联合推断生物物理神经元模型的未知参数和隐藏状态变量。该方法在具有强非线性和多尺度动力学的快-慢峰发放和簇发放模型中表现出鲁棒性。虽然应用领域是计算神经科学，但其解决的核心问题——从观测数据（如电压时间序列）反演复杂动态系统的底层参数和状态——与“质谱结构推理”问题在数学和计算上同构。在质谱分析中，目标是从观测到的质谱图（一维或二维信号）推断出产生该谱图的分子结构（参数/状态）。两者都是高维、非线性、病态的反问题。PINN框架通过将物理方程（如神经元模型方程）作为软约束嵌入神经网络训练，为这类反问题提供了新的解决方案。这种将领域知识（物理/化学规则）与数据驱动模型深度融合的范式，对于开发下一代“质谱结构推理”模型具有重要的启发意义。例如，可以将质谱碎裂规则、同位素模式等化学知识编码到PINN的损失函数中，从而构建更可靠、可解释的分子结构推断模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inferring biophysical parameters and hidden state variables from partial and noisy observations is a fundamental challenge in computational neuroscience. This problem is particularly difficult for fast - slow spiking and bursting models, where strong nonlinearities, multiscale dynamics, and limited observational data often lead to severe sensitivity to initial parameter guesses and convergence failure in the methods replying on the traditional numerical forward solvers. In this work, we developed a physics-informed neural network (PINN) framework for the joint reconstruction of unobserved state variables and the estimation of unknown biophysical parameters in neuronal models. We demonstrate the effectiveness of the method on biophysical neuron models, including the Morris-Lecar model across multiple spiking and bursting regimes and a respiratory model neuron. The method requires only partial voltage observations over short observation windows and remains robust even when initialized with non-informative parameter guesses. These results suggest that PINN can deliver robust and accurate parameter inference and state reconstruction, providing a promising alternative for inverse problems in multiscale neuronal dynamics, where traditional techniques often struggle.

</details>

---

### 4. [Diagnosing FP4 inference: a layer-wise and block-wise sensitivity analysis of NVFP4 and MXFP4](https://arxiv.org/abs/2603.08747)

**基本信息**

- 🔗 arXiv: [`2603.08747`](https://arxiv.org/abs/2603.08747)
- 👥 作者: Musa Cim, Burak Topcu, Mahmut Taylan Kandemir
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08747.pdf)

**💡 相关性分析**

满足标准1：论文的核心是对大模型（LLM）内部组件进行细粒度的敏感性分析，这种方法论对于理解和优化“化学大模型”（如用于分子性质预测或谱图生成的模型）的鲁棒性和效率具有直接的相关性。

**📖 中文摘要**

这篇论文对两种4位浮点数格式（MXFP4和NVFP4）在大型语言模型量化中的敏感性进行了系统的层间和块间分析。研究通过控制变量法，隔离了Transformer模型中不同组件（如MLP的上/下投影层、门投影、注意力投影）对量化误差的贡献。研究发现，MLP的上/下投影层对量化最为敏感，而注意力投影层的敏感性则低得多。此外，敏感性并不总是集中在网络的最后几层，早期层在某些格式下也可能非常敏感。这项研究虽然主要关注LLM的量化，但其“诊断性表征”方法——即通过精细的消融实验来理解复杂模型中不同组件对某种扰动（如量化）的鲁棒性——对于“化学大模型”和“质谱分析模型”的开发和优化具有重要价值。例如，在构建用于质谱预测或分子性质预测的Transformer或图神经网络时，同样需要理解模型架构中哪些部分对输入噪声、数据分布偏移或特定的近似计算最为敏感，从而进行有针对性的加固或优化。该论文提供了一套可迁移的分析框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantization addresses the high resource demand for large language models (LLMs) by alleviating memory pressure and bandwidth congestion and providing significantly scaled compute power with a tolerable impact on accuracy. Four-bit floating point (FP4), the lowest-precision format that preserves essential numerical properties such as exponent and sign, has begun to be adopted in cutting-edge architectures, including Blackwell and AMD CDNA, to support LLM quantization and reduce deployment costs. Although aggressive quantization can yield efficiency gains, the quantization sensitivity of within-transformer layers and whether these sensitivities generalize across existing FP4 formats and model scales remain underexplored. To elucidate quantization sensitivity, this study conducts a systematic analysis of two FP4 formats, MXFP4 and NVFP4, across three Qwen2.5 model scales (0.5B, 7B, and 14B), using controlled component-wise and block-wise isolation methodologies. We observe that MLP up- and down-projection layers consistently dominate in terms of sensitivity, while gate and attention projections are moderately and substantially less sensitive to FP4 quantization, respectively. We further find that sensitivity does not universally localize to the final blocks, but early blocks can be highly sensitive, particularly under MXFP4. Our results provide a diagnostic characterization of the inference behavior of FP4 across components, depths, and FP4 formats.

</details>

---

### 5. [Granulon: Awakening Pixel-Level Visual Encoders with Adaptive Multi-Granularity Semantics for MLLM](https://arxiv.org/abs/2603.08800)

**基本信息**

- 🔗 arXiv: [`2603.08800`](https://arxiv.org/abs/2603.08800)
- 👥 作者: Junyuan Mao, Qiankun Li, Linghao Meng 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08800.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个能自适应融合多粒度视觉信息的MLLM。这种自适应多尺度信息处理的能力，对于开发能够同时处理原子、子结构和分子等多层次信息的“化学大模型”，以及同时分析局部碎片和全局谱图模式的“质谱结构推理”模型，具有重要的架构参考价值。

**📖 中文摘要**

这篇论文提出了Granulon，一个基于DINOv3视觉编码器的多模态大语言模型（MLLM）。其核心创新是引入了自适应粒度增强机制，包括一个文本条件粒度控制器和一个自适应令牌聚合模块，使模型能够根据文本输入的语义范围动态调整视觉抽象级别，并在单次前向传播中实现从像素级到细粒度再到粗粒度的统一推理。虽然该模型主要针对通用视觉-语言任务，但其核心思想——构建一个能够根据任务需求自适应地融合不同粒度视觉信息（从详细的像素级特征到全局语义特征）的多模态模型——对于“化学大模型”和“质谱结构推理”具有重要的启示。在化学领域，模型同样需要处理多粒度信息：例如，在分析分子时，需要原子级别的细节（如官能团）、子结构级别的模式（如药效团）以及整个分子级别的全局性质。在质谱分析中，需要同时关注谱图中的局部峰（碎片离子）和全局模式（同位素分布、中性丢失）。Granulon的架构设计为构建能够灵活、自适应地利用化学数据中多尺度信息的领域大模型提供了有价值的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in multimodal large language models largely rely on CLIP-based visual encoders, which emphasize global semantic alignment but struggle with fine-grained visual understanding. In contrast, DINOv3 provides strong pixel-level perception yet lacks coarse-grained semantic abstraction, leading to limited multi-granularity reasoning. To address this gap, we propose Granulon, a novel DINOv3-based MLLM with adaptive granularity augmentation. Granulon introduces a text-conditioned granularity Controller that dynamically adjusts the visual abstraction level according to the semantic scope of the textual input, and an Adaptive Token Aggregation module that performs granularity-guided pooling and relation-aware clustering to produce compact, semantically rich visual tokens. This design enables unified "pixel-to-fine-to-coarse" reasoning within a single forward pass. Extensive and interpretable experiments demonstrate that Granulon improves accuracy by ~30% and reduces hallucination by ~20%, outperforming all visual encoders under identical settings.

</details>

---

### 6. [Are Expressive Encoders Necessary for Discrete Graph Generation?](https://arxiv.org/abs/2603.08825)

**基本信息**

- 🔗 arXiv: [`2603.08825`](https://arxiv.org/abs/2603.08825)
- 👥 作者: Jay Revolinsky, Harry Shomer, Jiliang Tang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08825.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是离散图生成模型，这是“化学大模型”在分子生成与设计领域的直接技术基础。论文提出的GenGNN框架及其对GNN表达能力的分析，对于开发更高效、更可靠的化学分子生成模型具有核心相关性。

**📖 中文摘要**

这篇论文重新审视了离散图生成模型的设计，提出了GenGNN，一个基于消息传递的模块化图生成框架。研究通过系统的消融实验和尺度分析，探讨了图神经网络（GNN）是否可以作为离散扩散模型中富有表达力的神经主干。结果表明，在树图和平面图等数据集上，基于GenGNN的扩散模型可以达到超过90%的有效性，与图Transformer性能相当但推理速度更快；在分子生成任务上，结合DiGress框架也能达到极高的有效性。这项研究直接针对“化学大模型”中的一个核心子领域——分子图生成。分子本质上是一种图结构，因此分子生成是图生成在化学领域的具体应用。论文深入探讨了GNN作为生成模型主干的表达能力和效率权衡，这对于优化化学领域的分子生成模型（如用于药物发现的分子设计模型）具有直接的技术指导意义。其模块化框架和评估方法也为化学图生成模型的研究提供了可借鉴的范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete graph generation has emerged as a powerful paradigm for modeling graph data, often relying on highly expressive neural backbones such as transformers or higher-order architectures. We revisit this design choice by introducing GenGNN, a modular message-passing framework for graph generation. Diffusion models with GenGNN achieve more than 90% validity on Tree and Planar datasets, within margins of graph transformers, at 2-5x faster inference speed. For molecule generation, DiGress with a GenGNN backbone achieves 99.49% Validity. A systematic ablation study shows the benefit provided by each GenGNN component, indicating the need for residual connections to mitigate oversmoothing on complicated graph-structure. Through scaling analyses, we apply a principled metric-space view to investigate learned diffusion representations and uncover whether GNNs can be expressive neural backbones for discrete diffusion.

</details>

---

### 7. [Towards Visual Query Segmentation in the Wild](https://arxiv.org/abs/2603.08898)

**基本信息**

- 🔗 arXiv: [`2603.08898`](https://arxiv.org/abs/2603.08898)
- 👥 作者: Bing Fan, Minghao Li, Hanzhi Zhang 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08898.pdf)

**💡 相关性分析**

满足标准1：论文提出的视觉查询分割（VQS）任务范式——基于模板在复杂数据中定位所有细粒度实例——与质谱分析中“基于参考谱图定位混合物中目标化合物特征”的任务在概念上高度相关。其基准构建和方法论为“质谱结构推理”中的子问题提供了有价值的参考。

**📖 中文摘要**

这篇论文引入了视觉查询分割（VQS）这一新范式，并发布了大规模基准数据集VQS-4K。VQS的目标是给定一个外部视觉查询（目标物体的一帧及其掩码），在未修剪的视频中分割出该目标物体所有像素级别的出现。与现有仅定位目标最后一次出现或使用边界框的方法相比，VQS要求更全面和精确的定位。虽然这是一个计算机视觉任务，但其“基于查询的细粒度定位”范式与“质谱结构推理”中的某些子问题有概念上的相似性。例如，在分析复杂的混合物质谱时，一个核心任务可能是：给定一个已知化合物的参考质谱图（作为“查询”），在混合物的总离子流图或一系列质谱中，定位出该化合物所有可能出现的色谱峰或谱图特征。这同样是一个在复杂信号中根据模板进行细粒度、多实例匹配和定位的问题。VQS-4K基准的构建方法（高质量标注、多样化类别）以及论文提出的VQ-SAM方法（利用目标特定线索和背景干扰线索进行渐进式记忆演化），为质谱分析中类似的多实例、细粒度匹配任务提供了问题定义、评估基准和算法设计上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we introduce visual query segmentation (VQS), a new paradigm of visual query localization (VQL) that aims to segment all pixel-level occurrences of an object of interest in an untrimmed video, given an external visual query. Compared to existing VQL locating only the last appearance of a target using bounding boxes, VQS enables more comprehensive (i.e., all object occurrences) and precise (i.e., pixel-level masks) localization, making it more practical for real-world scenarios. To foster research on this task, we present VQS-4K, a large-scale benchmark dedicated to VQS. Specifically, VQS-4K contains 4,111 videos with more than 1.3 million frames and covers a diverse set of 222 object categories. Each video is paired with a visual query defined by a frame outside the search video and its target mask, and annotated with spatial-temporal masklets corresponding to the queried target. To ensure high quality, all videos in VQS-4K are manually labeled with meticulous inspection and iterative refinement. To the best of our knowledge, VQS-4K is the first benchmark specifically designed for VQS. Furthermore, to stimulate future research, we present a simple yet effective method, named VQ-SAM, which extends SAM 2 by leveraging target-specific and background distractor cues from the video to progressively evolve the memory through a novel multi-stage framework with an adaptive memory generation (AMG) module for VQS, significantly improving the performance. In our extensive experiments on VQS-4K, VQ-SAM achieves promising results and surpasses all existing approaches, demonstrating its effectiveness. With the proposed VQS-4K and VQ-SAM, we expect to go beyond the current VQL paradigm and inspire more future research and practical applications on VQS. Our benchmark, code, and results will be made publicly available.

</details>

---

### 8. [Quantifying Memorization and Privacy Risks in Genomic Language Models](https://arxiv.org/abs/2603.08913)

**基本信息**

- 🔗 arXiv: [`2603.08913`](https://arxiv.org/abs/2603.08913)
- 👥 作者: Alexander Nemecek, Wenbiao Li, Xiaoqian Jiang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08913.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕特定领域（基因组学）的语言模型（大模型的一种）展开，深入探讨了其训练、记忆化风险和隐私评估，这与“化学大模型”主题在方法论和核心关切上直接相关。

**📖 中文摘要**

这篇论文研究了基因组语言模型（GLMs）中的记忆化与隐私风险。虽然其核心领域是基因组学，但论文深入探讨了语言模型（一种特定类型的大模型）在特定领域数据（基因组序列）上的训练、记忆化风险以及隐私评估框架。这直接关联到“化学大模型”主题，因为化学信息学领域同样广泛使用基于序列（如SMILES）或图结构的大语言模型来学习分子表示、预测性质或生成结构。论文提出的多向量隐私评估框架（包括基于困惑度的检测、金丝雀序列提取和成员推理）为评估任何在敏感数据上训练的大模型（包括化学大模型）的隐私风险提供了方法论参考。因此，它为核心主题（化学大模型）提供了重要的相关讨论和风险评估视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Genomic language models (GLMs) have emerged as powerful tools for learning representations of DNA sequences, enabling advances in variant prediction, regulatory element identification, and cross-task transfer learning. However, as these models are increasingly trained or fine-tuned on sensitive genomic cohorts, they risk memorizing specific sequences from their training data, raising serious concerns around privacy, data leakage, and regulatory compliance. Despite growing awareness of memorization risks in general-purpose language models, little systematic evaluation exists for these risks in the genomic domain, where data exhibit unique properties such as a fixed nucleotide alphabet, strong biological structure, and individual identifiability. We present a comprehensive, multi-vector privacy evaluation framework designed to quantify memorization risks in GLMs. Our approach integrates three complementary risk assessment methodologies: perplexity-based detection, canary sequence extraction, and membership inference. These are combined into a unified evaluation pipeline that produces a worst-case memorization risk score. To enable controlled evaluation, we plant canary sequences at varying repetition rates into both synthetic and real genomic datasets, allowing precise quantification of how repetition and training dynamics influence memorization. We evaluate our framework across multiple GLM architectures, examining the relationship between sequence repetition, model capacity, and memorization risk. Our results establish that GLMs exhibit measurable memorization and that the degree of memorization varies across architectures and training regimes. These findings reveal that no single attack vector captures the full scope of memorization risk, underscoring the need for multi-vector privacy auditing as a standard practice for genomic AI systems.

</details>

---

### 9. [bsort: A theoretically efficient non-comparison-based sorting algorithm for integer and floating-point numbers](https://arxiv.org/abs/2603.08929)

**基本信息**

- 🔗 arXiv: [`2603.08929`](https://arxiv.org/abs/2603.08929)
- 👥 作者: Benjamín Guzmán
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08929.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种高效的数值排序算法，该算法可作为处理质谱数据（本质是数值对序列）的基础工具，为“质谱结构推理”流程中的数据预处理阶段提供了潜在的资源（算法工具）。

**📖 中文摘要**

这篇论文提出了bsort，一种基于非比较的整数和浮点数排序算法。虽然算法本身是通用的，但其高效处理数值数据（包括浮点数）的特性，使其与科学计算中的数据预处理高度相关。在质谱分析中，原始数据是包含质荷比（m/z）和强度信息的数值谱图。高效、准确地排序和筛选峰值是质谱数据预处理、峰对齐和特征提取的关键步骤。bsort算法提供的O(wn)时间复杂度和O(w)辅助空间，对于处理海量、高维的质谱数据流具有潜在的应用价值，可以作为质谱数据分析工具链中的一个高效基础组件。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents bsort, a non-comparison-based sorting algorithm for signed and unsigned integers, and floating-point values. The algorithm unifies these cases through an approach derived from binary quicksort, achieving $O(wn)$ runtime asymptotic behavior and $O(w)$ auxiliary space, where $w$ is the element word size. This algorithm is highly efficient for data types with small word sizes, where empirical analysis exhibits performance competitive with highly optimized hybrid algorithms from popular libraries.

</details>

---

### 10. [Unit Interval Selection in Random Order Streams](https://arxiv.org/abs/2603.08937)

**基本信息**

- 🔗 arXiv: [`2603.08937`](https://arxiv.org/abs/2603.08937)
- 👥 作者: Cezar-Mihail Alexandru, Adithya Diddapur, Magnús M. Halldórsson 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08937.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（高光谱解混）与“质谱结构推理”在问题定义（混合物谱分解）、核心挑战（弱信号提取）和技术路线上高度相似，其提出的深度学习框架具有直接的启发和借鉴意义。

**📖 中文摘要**

这篇论文提出了WS-Net，一个用于高光谱解混的深度学习框架，专门设计用于解决弱光谱响应被主导端元和噪声掩盖的问题。高光谱解混是遥感领域的关键任务，旨在从混合像素中分离出纯净的“端元”光谱及其比例（丰度）。虽然应用领域不同，但该任务在数学和信号处理本质上与“质谱结构推理”有很强的相似性：质谱分析中也常遇到混合物的谱图，需要解卷积以推断其中可能存在的化合物（类似“端元”）及其相对含量（类似“丰度”）。WS-Net引入的状态空间建模、弱信号注意力融合机制以及针对弱信号的增强方法，为解决质谱中低丰度化合物信号被高丰度化合物或噪声掩盖的类似挑战提供了创新的算法思路和模型架构参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We consider the \textsf{Unit Interval Selection} problem in the one-pass random order streaming model. Here, an algorithm is presented a sequence of $n$ unit-length intervals on the line that arrive in uniform random order, and the objective is to output a largest set of disjoint intervals using space linear in the size of an optimal solution. Previous work only considered adversarially ordered streams and established that, in this space constraint, a $(2/3)$-approximation can be achieved, and this is also best possible, i.e. any improvement requires space $\Omega(n)$ [Emek et al., TALG'16]. In this work, we show that an improved expected approximation factor can be achieved if the input stream is in uniform random order, with the expectation taken over the stream order. Specifically, we give a one-pass streaming algorithm with expected approximation factor $0.7401$ using space $O(|OPT|)$, where $OPT$ denotes an optimal solution. We also show that algorithms with expected approximation factor above $8/9$ require space $\Omega(n)$, and algorithms that compute a better than $2/3$-approximation with probability above $2/3$ also require $\Omega(n)$ space. On a technical note, we design an algorithm for the restricted domain $[0,\Delta)$, for some constant $\Delta$, and use standard techniques to obtain an algorithm for unrestricted domains. For the restricted domain $[0,\Delta)$, we run $O(\Delta)$ recursive instances of our algorithm, with each instance targeting the situation where a specific interval from $OPT$ arrives first. We establish the interesting property that our algorithm performs worst when the input stream is precisely a set of independent intervals. We then analyse the algorithm on these instances. Our lower bound is proved via communication complexity arguments, similar in spirit to the robust communication lower bounds by [Chakrabarti et al., Theory Comput. 2016].

</details>

---

### 11. [GenAI Is No Silver Bullet for Qualitative Research in Software Engineering](https://arxiv.org/abs/2603.08951)

**基本信息**

- 🔗 arXiv: [`2603.08951`](https://arxiv.org/abs/2603.08951)
- 👥 作者: Neil A. Ernst, Christoph Treude
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08951.pdf)

**💡 相关性分析**

满足标准3：论文是对GenAI在定性研究中作用的综述和展望性讨论，其核心论点和方法论反思对于“化学大模型”和“质谱结构推理”领域如何应用大模型进行科学文献挖掘、知识提取和假设生成等“研究”活动具有重要的相关性和指导价值。

**📖 中文摘要**

这篇论文批判性地探讨了生成式人工智能（GenAI）在软件工程定性研究中的应用与局限。虽然主题是软件工程，但论文的核心论点是：GenAI并非定性研究的“银弹”，必须根据具体的研究策略和数据特性进行谨慎调整。这一讨论对于“化学大模型”和“质谱结构推理”领域的研究者具有重要的警示和指导意义。在这些领域，利用大模型自动化分析文献、解析实验报告、从非结构化的研究文本中提取知识或生成假设正变得日益普遍。论文中关于GenAI辅助定性研究的利弊分析、对研究质量因素的重新审视，以及提出的未来研究方向，为化学信息学和质谱学领域如何负责任且有效地利用大模型进行科学发现（可视为一种特殊的定性研究）提供了宝贵的框架和注意事项。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Qualitative research gives rich insights into the quintessentially human aspects of software engineering as a socio-technical system. Qualitative research spans diverse strategies and methods, from interpretivist, in situ observational field studies, to deductive coding of data from mining studies. Advances in large language models and generative AI (GenAI) have prompted claims that artificial intelligence could automate qualitative analysis. Such claims are overgeneralizing from narrow successes. GenAI support must be carefully adapted to the data of interest, but also to the characteristics of a particular research strategy. In this Frontiers of SE paper, we discuss the emerging use of GenAI in relation to the broad spectrum of qualitative research in software engineering. We outline the dimensions of qualitative work in software engineering, review emerging empirical evidence for GenAI assistance, examine the pros and cons of GenAI-mediated qualitative research practices, and revisit qualitative research quality factors, in light of GenAI. Our goal is to inform researchers about the promises and pitfalls of GenAI-assisted qualitative research. We conclude with future plans to advance understanding of its use in software engineering.

</details>

---

### 12. [Automated Tensor-Relational Decomposition for Large-Scale Sparse Tensor Computation](https://arxiv.org/abs/2603.08957)

**基本信息**

- 🔗 arXiv: [`2603.08957`](https://arxiv.org/abs/2603.08957)
- 👥 作者: Yuxin Tang, Zhiyuan Xin, Zhimin Ding 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08957.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于大规模稀疏张量计算的自动化张量-关系分解框架，这为处理化学大模型和质谱分析中常见的高维稀疏数据提供了潜在的基础设施和工具资源。

**📖 中文摘要**

这篇论文介绍了EinSum，一种张量-关系计算表示法，旨在将爱因斯坦求和符号表示的计算自动重写，以便在关系型系统上高效执行，同时利用高性能数值内核处理计算密集型部分。这项工作与科学计算中的数据管理和大规模稀疏张量处理密切相关。在化学信息学和质谱分析中，分子描述符、分子间相互作用矩阵、质谱峰矩阵等通常以高维、稀疏的张量形式存在。高效处理这些张量对于构建和运行化学大模型（如图神经网络）或进行质谱数据的批量比对和推理至关重要。EinSum所倡导的“关系型管理稀疏性、内核执行密集计算”的混合范式，为构建可扩展的化学与质谱计算平台提供了底层数据管理和计算框架的新思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A \emph{tensor-relational} computation is a relational computation where individual tuples carry vectors, matrices, or higher-dimensional arrays. An advantage of tensor-relational computation is that the overall computation can be executed on top of a relational system, inheriting the system's ability to automatically handle very large inputs with high levels of sparsity while high-performance kernels (such as optimized matrix-matrix multiplication codes) can be used to perform most of the underlying mathematical operations. In this paper, we introduce upper-case-lower-case \texttt{EinSum}, which is a tensor-relational version of the classical Einstein Summation Notation. We study how to automatically rewrite a computation in Einstein Notation into upper-case-lower-case \texttt{EinSum} so that computationally intensive components are executed using efficient numerical kernels, while sparsity is managed relationally.

</details>

---

### 13. [Semantic Level of Detail: Multi-Scale Knowledge Representation via Heat Kernel Diffusion on Hyperbolic Manifolds](https://arxiv.org/abs/2603.08965)

**基本信息**

- 🔗 arXiv: [`2603.08965`](https://arxiv.org/abs/2603.08965)
- 👥 作者: Edward Izgorodin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08965.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（知识的多尺度连续表示）为“化学大模型”和“质谱结构推理”中处理层次化化学知识和谱图-结构关系提供了创新的表示学习方法和理论框架，具有直接的相关性。

**📖 中文摘要**

这篇论文提出了语义细节层次（SLoD）框架，通过在双曲流形（庞加莱球）上进行热核扩散，实现知识图谱中多尺度连续分辨率控制。该框架能够自动检测知识表示中出现的尺度边界（即定性抽象层次）。这项研究虽然面向通用知识图谱，但其核心问题——如何对层次化、结构化的知识进行连续、多尺度的表示与导航——与“化学大模型”和“质谱结构推理”高度相关。在化学中，分子结构具有天然的层次性（原子、官能团、分子片段、整个分子），化学知识也常被组织成层次化的本体（如ChEBI）。在质谱推理中，谱图特征与分子子结构之间也存在多层次的对应关系。SLoD框架为在这些领域构建能够动态调整抽象级别、融合不同粒度知识的智能模型提供了理论框架和算法基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI memory systems increasingly organize knowledge into graph structures -- knowledge graphs, entity relations, community hierarchies -- yet lack a principled mechanism for continuous resolution control: where do the qualitative boundaries between abstraction levels lie, and how should an agent navigate them? We introduce Semantic Level of Detail (SLoD), a framework that answers both questions by defining a continuous zoom operator via heat kernel diffusion on the Poincaré ball $\mathbb{B}^d$. At coarse scales ($\sigma \to \infty$), diffusion aggregates embeddings into high-level summaries; at fine scales ($\sigma \to 0$), local semantic detail is preserved. We prove hierarchical coherence with bounded approximation error $O(\sigma)$ and $(1+\varepsilon)$ distortion for tree-structured hierarchies under Sarkar embedding. Crucially, we show that spectral gaps in the graph Laplacian induce emergent scale boundaries -- scales where the representation undergoes qualitative transitions -- which can be detected automatically without manual resolution parameters. On synthetic hierarchies (HSBM), our boundary scanner recovers planted levels with ARI up to 1.00, with detection degrading gracefully near the information-theoretic Kesten-Stigum threshold. On the full WordNet noun hierarchy (82K synsets), detected boundaries align with true taxonomic depth ($\tau = 0.79$), demonstrating that the method discovers meaningful abstraction levels in real-world knowledge graphs without supervision.

</details>

---

### 14. [MAPLE: Elevating Medical Reasoning from Statistical Consensus to Process-Led Alignment](https://arxiv.org/abs/2603.08987)

**基本信息**

- 🔗 arXiv: [`2603.08987`](https://arxiv.org/abs/2603.08987)
- 👥 作者: Kailong Fan, Anqi Pu, Yichen Wu 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08987.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（利用过程奖励模型优化大语言模型的推理）为“化学大模型”的推理能力优化和“质谱结构推理”的自动化逻辑链条构建提供了前沿的方法论参考。

**📖 中文摘要**

这篇论文提出了MAPLE，一种用于提升医学大语言模型推理能力的训练范式。它用医学过程奖励模型替代传统的多数投票，将测试时强化学习与参数化模型优化相结合，以确保强化学习由医学正确性而非共识引导。虽然应用场景是医学问答，但其核心创新——利用结构化、逐步的奖励来指导大模型的推理优化——对于“化学大模型”和“质谱结构推理”具有重要的方法论借鉴意义。在化学推理中（如逆合成分析、反应预测），正确的推理路径往往比流行的路径更重要。MAPLE的范式启示我们，可以设计针对化学逻辑或谱图解析过程的奖励模型，来微调或增强化学大模型，使其推理过程更可靠、更符合化学原理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in medical large language models have explored Test-Time Reinforcement Learning (TTRL) to enhance reasoning. However, standard TTRL often relies on majority voting (MV) as a heuristic supervision signal, which can be unreliable in complex medical scenarios where the most frequent reasoning path is not necessarily the clinically correct one. In this work, we propose a novel and unified training paradigm that integrates medical process reward models with TTRL to bridge the gap between test-time scaling (TTS) and parametric model optimization. Specifically, we advance the TTRL framework by replacing the conventional MV with a fine-grained, expert-aligned supervision paradigm using Med-RPM. This integration ensures that reinforcement learning is guided by medical correctness rather than mere consensus, effectively distilling search-based intelligence into the model's parametric memory. Extensive evaluations on four different benchmarks have demonstrated that our developed method consistently and significantly outperforms current TTRL and standalone PRM selection. Our findings establish that transitioning from stochastic heuristics to structured, step-wise rewards is essential for developing reliable and scalable medical AI systems

</details>

---

### 15. [Automated Thematic Analysis for Clinical Qualitative Data: Iterative Codebook Refinement with Full Provenance](https://arxiv.org/abs/2603.08989)

**基本信息**

- 🔗 arXiv: [`2603.08989`](https://arxiv.org/abs/2603.08989)
- 👥 作者: Seungjun Yi, Joakim Nguyen, Huimin Xu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08989.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个基于LLM的自动化主题分析框架，这为利用“化学大模型”从非结构化化学文本中提取和构建知识资源（数据集、知识库）提供了强大的工具和方法。

**📖 中文摘要**

这篇论文提出了一个用于临床定性数据（如患者访谈）的自动化主题分析框架，结合了迭代式代码本优化和完整的溯源追踪。该框架利用大语言模型（LLMs）来自动化分析过程，并在多个临床语料库上取得了高质量结果。这项工作与“化学大模型”的应用场景高度相关。在化学信息学中，有大量非结构化的科学文献、实验记录、专利文本需要分析以提取化学知识、反应规则或安全信息。自动化主题分析框架为利用化学大模型从这些文本中系统化地提取、归纳和构建化学知识体系（例如，自动生成关于某类化合物合成方法的代码本）提供了可行的技术路径和评估方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Thematic analysis (TA) is widely used in health research to extract patterns from patient interviews, yet manual TA faces challenges in scalability and reproducibility. LLM-based automation can help, but existing approaches produce codebooks with limited generalizability and lack analytic auditability. We present an automated TA framework combining iterative codebook refinement with full provenance tracking. Evaluated on five corpora spanning clinical interviews, social media, and public transcripts, the framework achieves the highest composite quality score on four of five datasets compared to six baselines. Iterative refinement yields statistically significant improvements on four datasets with large effect sizes, driven by gains in code reusability and distributional consistency while preserving descriptive quality. On two clinical corpora (pediatric cardiology), generated themes align with expert-annotated themes.

</details>

---

### 16. [Better Bounds for the Distributed Experts Problem](https://arxiv.org/abs/2603.09168)

**基本信息**

- 🔗 arXiv: [`2603.09168`](https://arxiv.org/abs/2603.09168)
- 👥 作者: David P. Woodruff, Samson Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09168.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于分子设计的推理模型（Logos），这直接围绕“化学大模型”这一主题。论文明确讨论了将逻辑推理与化学一致性相结合的AI系统，用于分子的理性设计，属于化学信息学领域的核心研究。

**📖 中文摘要**

这篇论文提出了Logos，一个用于理性分子设计的可进化推理引擎。它旨在解决化学、生物学和材料科学中功能分子发现和设计的核心挑战。Logos将多步逻辑推理与严格的化学一致性相结合，通过分阶段训练策略，首先将模型暴露于连接分子描述与结构决策的显式推理示例中，然后逐步将这些推理模式与分子表示对齐。在最终训练阶段，化学规则和不变性被直接纳入优化目标，引导模型产生化学上有效的输出。该模型在多个基准数据集上实现了强大的结构准确性和化学有效性，匹配或超越了参数量大得多的通用语言模型。通过显式展示中间推理步骤，Logos使得每个生成结构背后的设计逻辑可供人类检查和评估。这项工作表明，联合优化推理结构和物理一致性为分子科学提供了通向可靠、可解释AI系统的实用途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we study the distributed experts problem, where $n$ experts are distributed across $s$ servers for $T$ timesteps. The loss of each expert at each time $t$ is the $\ell_p$ norm of the vector that consists of the losses of the expert at each of the $s$ servers at time $t$. The goal is to minimize the regret $R$, i.e., the loss of the distributed protocol compared to the loss of the best expert, amortized over the all $T$ times, while using the minimum amount of communication. We give a protocol that achieves regret roughly $R\gtrsim\frac{1}{\sqrt{T}\cdot\text{poly}\log(nsT)}$, using $\mathcal{O}\left(\frac{n}{R^2}+\frac{s}{R^2}\right)\cdot\max(s^{1-2/p},1)\cdot\text{poly}\log(nsT)$ bits of communication, which improves on previous work.

</details>

---

### 17. [The Radio-Frequency Transformer for Signal Separation](https://arxiv.org/abs/2603.09201)

**基本信息**

- 🔗 arXiv: [`2603.09201`](https://arxiv.org/abs/2603.09201)
- 👥 作者: Egor Lifar, Semyon Savkin, Rachana Madhukara 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09201.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于Transformer的数据驱动信号分离方法。虽然应用背景是射频信号，但其核心方法论（基于Transformer的序列建模、标记化、端到端学习）与构建用于分析复杂科学数据（如质谱信号）的“化学大模型”在技术路径上高度相关。论文中提到的零样本泛化和适应不同干扰类型的能力，也与质谱结构推理中处理未知化合物或复杂背景的挑战有概念上的相通之处。

**📖 中文摘要**

这篇论文研究信号分离问题：从未知的非高斯背景/干扰中估计目标信号。论文提出了一种完全数据驱动的信号分离器构建方法。具体而言，它为信号学习了一个良好的离散标记器，然后基于交叉熵损失训练一个端到端的Transformer模型。与传统的均方误差相比，使用交叉熵训练显示出显著的改进。该标记器是Google SoundStream的修改版本，它结合了额外的Transformer层，并从VQVAE切换到有限标量量化。该方法在真实和合成的MIT RF挑战数据集混合物上实现了具有竞争力的性能，包括在将QPSK信号与5G干扰分离时，误码率比先前最先进技术降低了122倍。学习到的表示无需侧信息即可适应干扰类型，并在推理时对未见过的混合物表现出零样本泛化能力。虽然该方法在射频混合物上实例化，但作者预期相同的架构也适用于引力波数据和其他需要背景和噪声数据驱动建模的科学传感问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study a problem of signal separation: estimating a signal of interest (SOI) contaminated by an unknown non-Gaussian background/interference. Given the training data consisting of examples of SOI and interference, we show how to build a fully data-driven signal separator. To that end we learn a good discrete tokenizer for SOI and then train an end-to-end transformer on a cross-entropy loss. Training with a cross-entropy shows substantial improvements over the conventional mean-squared error (MSE). Our tokenizer is a modification of Google's SoundStream, which incorporates additional transformer layers and switches from VQVAE to finite-scalar quantization (FSQ). Across real and synthetic mixtures from the MIT RF Challenge dataset, our method achieves competitive performance, including a 122x reduction in bit-error rate (BER) over prior state-of-the-art techniques for separating a QPSK signal from 5G interference. The learned representation adapts to the interference type without side information and shows zero-shot generalization to unseen mixtures at inference time, underscoring its potential beyond RF. Although we instantiate our approach on radio-frequency mixtures, we expect the same architecture to apply to gravitational-wave data (e.g., LIGO strain) and other scientific sensing problems that require data-driven modeling of background and noise.

</details>

---

### 18. [Cognitively Layered Data Synthesis for Domain Adaptation of LLMs to Space Situational Awareness](https://arxiv.org/abs/2603.09231)

**基本信息**

- 🔗 arXiv: [`2603.09231`](https://arxiv.org/abs/2603.09231)
- 👥 作者: Ding Linghu, Cheng Wang, Da Fan 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09231.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文的核心研究内容是针对特定科学/工程领域（空间态势感知）定制和优化大型语言模型，这属于“化学大模型”主题中“领域适应”和“专业化”的重要子方向。其方法论（结构化知识组织、认知分层）对于构建化学或质谱领域的专业大模型具有直接的参考价值。2) 论文提出了一个系统化的数据生成框架（BD-FDG）和构建了一个大规模领域数据集（SSA-SFT），这为其他领域（包括化学信息学）创建用于训练专业模型的数据资源提供了方法论和潜在的工具借鉴。

**📖 中文摘要**

这篇论文提出了BD-FDG框架，用于为大型语言模型（LLMs）在复杂工程领域（如空间态势感知SSA）的领域适应构建高质量的监督微调数据集。该框架通过结构化知识组织、认知分层问题建模和自动化质量控制三种机制，解决了知识覆盖不完整、认知深度浅和可控性有限的问题。它使用知识树确保结构化语料库覆盖，设计了一个跨越九个类别和六个认知层次（从记忆到创造）的问题生成方案，以产生具有连续难度梯度的样本，并应用多维评分流程来强制执行领域严谨性和一致性。利用BD-FDG，作者构建了SSA-SFT领域数据集（约23万个样本），并对Qwen3-8B进行微调，得到了SSA-LLM-8B。实验表明，该模型在领域测试集上取得了显著的性能提升。论文验证了以认知分层驱动的SFT数据构建作为复杂工程领域领域特定LLM适应的有效范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) demonstrate exceptional performance on general-purpose tasks. however, transferring them to complex engineering domains such as space situational awareness (SSA) remains challenging owing to insufficient structural alignment with mission chains, the absence of higher-order cognitive supervision, and poor correspondence between data quality criteria and engineering specifications. The core bottleneck is the construction of high-quality supervised fine-tuning (SFT) datasets. To this end, we propose BD-FDG (Bloom's Taxonomy-based Domain-specific Fine-tuning Data Generation), a framework that addresses incomplete knowledge coverage, shallow cognitive depth, and limited quality controllability through three mechanisms: structured knowledge organization, cognitively layered question modeling, and automated quality control. The framework uses a knowledge tree to ensure structured corpus coverage, designs a question generation scheme spanning nine categories and six cognitive levels from Remember to Create to produce samples with a continuous difficulty gradient, and applies a multidimensional scoring pipeline to enforce domain rigor and consistency. Using BD-FDG, we construct SSA-SFT, a domain dataset of approximately 230K samples, and fine-tune Qwen3-8B to obtain SSA-LLM-8B. Experiments show that SSA-LLM-8B achieves relative BLEU-1 improvements of 144\% (no-think) and 176\% (think) on the domain test set and a win rate of 82.21\% over the baseline in arena comparisons, while largely preserving general benchmark performance (MMLU-Pro, MATH-500). These results validate SFT data construction driven by cognitive layering as an effective paradigm for complex engineering domains and provide a transferable framework for domain-specific LLM adaptation.

</details>

---

### 19. [ForgeDreamer: Industrial Text-to-3D Generation with Multi-Expert LoRA and Cross-View Hypergraph](https://arxiv.org/abs/2603.09266)

**基本信息**

- 🔗 arXiv: [`2603.09266`](https://arxiv.org/abs/2603.09266)
- 👥 作者: Junhao Cai, Deyu Zeng, Junhao Pang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09266.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于3D分子/结构生成的AI模型（ForgeDreamer）。虽然应用场景是工业零件，但其核心挑战——从文本描述生成精确、一致的三维几何结构——与“化学大模型”中从分子描述（如SMILES）或质谱数据推理三维分子结构（“质谱结构推理”）的任务在本质上高度相似。论文中解决领域适应、几何一致性和多视角推理的方法，对于化学和质谱领域的结构生成模型具有重要的技术参考价值。

**📖 中文摘要**

这篇论文提出了ForgeDreamer框架，用于解决工业文本到3D生成中的领域适应和几何推理缺陷。它引入了两个关键创新：首先，多专家LoRA集成机制，将多个类别特定的LoRA模型整合到统一表示中，在实现卓越的跨类别泛化的同时消除了知识干扰。其次，在增强的语义理解基础上，开发了一种跨视图超图几何增强方法，同时捕获跨越多个视角的结构依赖性。这些组件协同工作：改进的语义理解实现了更有效的几何推理，而超图建模确保了制造级别的一致性。在自定义工业数据集上的大量实验证明了其相对于最先进方法的优越语义泛化和增强的几何保真度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current text-to-3D generation methods excel in natural scenes but struggle with industrial applications due to two critical limitations: domain adaptation challenges where conventional LoRA fusion causes knowledge interference across categories, and geometric reasoning deficiencies where pairwise consistency constraints fail to capture higher-order structural dependencies essential for precision manufacturing. We propose a novel framework named ForgeDreamer addressing both challenges through two key innovations. First, we introduce a Multi-Expert LoRA Ensemble mechanism that consolidates multiple category-specific LoRA models into a unified representation, achieving superior cross-category generalization while eliminating knowledge interference. Second, building on enhanced semantic understanding, we develop a Cross-View Hypergraph Geometric Enhancement approach that captures structural dependencies spanning multiple viewpoints simultaneously. These components work synergistically improved semantic understanding, enables more effective geometric reasoning, while hypergraph modeling ensures manufacturing-level consistency. Extensive experiments on a custom industrial dataset demonstrate superior semantic generalization and enhanced geometric fidelity compared to state-of-the-art approaches. Our code and data are provided in the supplementary material attached in the appendix for review purposes.

</details>

---

### 20. [Reward-Zero: Language Embedding Driven Implicit Reward Mechanisms for Reinforcement Learning](https://arxiv.org/abs/2603.09331)

**基本信息**

- 🔗 arXiv: [`2603.09331`](https://arxiv.org/abs/2603.09331)
- 👥 作者: Heng Zhang, Haddy Alchaer, Arash Ajoudani 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09331.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大语言模型（LLM）的嵌入能力来构建一个通用的、语义驱动的奖励框架。这直接关联到“化学大模型”主题，因为它探讨了如何利用语言模型的语义理解能力来指导和优化一个复杂的过程（强化学习），这种范式可以迁移到利用化学大模型进行分子设计、反应预测或质谱解析等任务中。

**📖 中文摘要**

本文提出了一种名为Reward-Zero的通用隐式奖励机制，用于强化学习。该机制将自然语言任务描述转化为密集的、基于语义的进度信号。其核心思想是利用语言嵌入来比较任务规范与智能体交互经验之间的语义相似性，从而产生一个连续的、语义对齐的“完成感”信号。这种方法不需要特定于任务的工程，可以补充稀疏或延迟的环境反馈，加速探索、稳定训练并增强跨任务的泛化能力。虽然论文本身不直接涉及化学或质谱，但其核心方法——利用语言模型嵌入来生成结构化、可解释的信号以指导复杂推理过程——与“化学大模型”中利用语言模型处理化学信息、指导分子生成或性质预测的研究范式高度相关。它展示了如何将大语言模型的能力整合到一个可操作的、目标驱动的框架中，这对于构建能够进行质谱结构推理或化学合成的智能体具有启发性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Reward-Zero, a general-purpose implicit reward mechanism that transforms natural-language task descriptions into dense, semantically grounded progress signals for reinforcement learning (RL). Reward-Zero serves as a simple yet sophisticated universal reward function that leverages language embeddings for efficient RL training. By comparing the embedding of a task specification with embeddings derived from an agent's interaction experience, Reward-Zero produces a continuous, semantically aligned sense-of-completion signal. This reward supplements sparse or delayed environmental feedback without requiring task-specific engineering. When integrated into standard RL frameworks, it accelerates exploration, stabilizes training, and enhances generalization across diverse tasks. Empirically, agents trained with Reward-Zero converge faster and achieve higher final success rates than conventional methods such as PPO with common reward-shaping baselines, successfully solving tasks that hand-designed rewards could not in some complex tasks. In addition, we develop a mini benchmark for the evaluation of completion sense during task execution via language embeddings. These results highlight the promise of language-driven implicit reward functions as a practical path toward more sample-efficient, generalizable, and scalable RL for embodied agents. Code will be released after peer review.

</details>

---

### 21. [TimberAgent: Gram-Guided Retrieval for Executable Music Effect Control](https://arxiv.org/abs/2603.09332)

**基本信息**

- 🔗 arXiv: [`2603.09332`](https://arxiv.org/abs/2603.09332)
- 👥 作者: Shihao He, Yihan Xia, Fang Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09332.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种从复杂信号（音频）中进行结构化信息检索和参数推理的方法。其技术路线（构建中层特征表示、使用Gram矩阵捕捉结构、进行相似性检索）与“质谱结构推理”中从质谱图推断分子结构或子结构的研究目标在方法论上高度相关，都是解决从高维观测数据到结构化解释的映射问题。

**📖 中文摘要**

本文研究基于检索的音频效果控制，旨在根据用户的感知意图（通过音频查询）检索出可编辑的插件配置参数，而非生成最终波形。论文的核心贡献是提出了一种名为纹理共振检索（TRR）的音频表示方法，该方法基于Wav2Vec2中层激活的Gram矩阵投影，以保留与纹理相关的共激活结构。研究在包含1063个预设和204个查询的吉他效果基准上进行了评估。这项工作虽然聚焦于音频领域，但其方法论——构建一种能够捕捉复杂信号（音频）内部结构化模式（纹理）的表示，并用于检索和参数推理——与“质谱结构推理”的核心挑战高度相似。质谱解析同样需要从高维、复杂的谱图信号中提取结构化特征，以推断出潜在的分子结构。本文提出的基于投影和矩阵表示的检索框架，为处理类似的高维信号推理问题（如质谱匹配、子结构检索）提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital audio workstations expose rich effect chains, yet a semantic gap remains between perceptual user intent and low-level signal-processing parameters. We study retrieval-grounded audio effect control, where the output is an editable plugin configuration rather than a finalized waveform. Our focus is Texture Resonance Retrieval (TRR), an audio representation built from Gram matrices of projected mid-level Wav2Vec2 activations. This design preserves texture-relevant co-activation structure. We evaluate TRR on a guitar-effects benchmark with 1,063 candidate presets and 204 queries. The evaluation follows Protocol-A, a cross-validation scheme that prevents train-test leakage. We compare TRR against CLAP and internal retrieval baselines (Wav2Vec-RAG, Text-RAG, FeatureNN-RAG), using min-max normalized metrics grounded in physical DSP parameter ranges. Ablation studies validate TRR's core design choices: projection dimensionality, layer selection, and projection type. A near-duplicate sensitivity analysis confirms that results are robust to trivial knowledge-base matches. TRR achieves the lowest normalized parameter error among evaluated methods. A multiple-stimulus listening study with 26 participants provides complementary perceptual evidence. We interpret these results as benchmark evidence that texture-aware retrieval is useful for editable audio effect control, while broader personalization and real-audio robustness claims remain outside the verified evidence presented here.

</details>

---

### 22. [The Virtuous Cycle: AI-Powered Vector Search and Vector Search-Augmented AI](https://arxiv.org/abs/2603.09347)

**基本信息**

- 🔗 arXiv: [`2603.09347`](https://arxiv.org/abs/2603.09347)
- 👥 作者: Jiuqi Wei, Quanqing Xu, Chuanhui Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09347.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对AI与向量搜索交叉领域的综述/教程，其中重点讨论了检索增强生成（RAG）这一对大语言模型（包括化学大模型）至关重要的技术范式。RAG是提升化学大模型事实准确性、减少幻觉并整合领域知识（如质谱库、化合物数据库）的关键方法，因此该论文包含了对这些主题的重要相关讨论。

**📖 中文摘要**

本文是一篇教程性综述，全面概述了人工智能（AI）与向量搜索（VS）这两个领域快速融合形成的研究前沿。文章指出，一方面，AI的进步（如学习索引结构、自适应剪枝策略、自动参数调优）极大地提高了向量搜索的语义准确性和效率；另一方面，强大的向量搜索技术（特别是检索增强生成，RAG）催生了新的AI范式，有效缓解了大语言模型的知识陈旧和幻觉问题。这种相互促进形成了一个“良性循环”。教程详细探讨了AI如何赋能向量搜索（AI4VS）以及向量搜索如何赋能AI（VS4AI），并分析了端到端的协同优化策略。虽然主题宽泛，但其中对RAG框架的深入讨论，以及如何将动态外部知识源集成到LLM生成过程中的分析，直接关联到“化学大模型”的应用场景。例如，在化学信息学中，可以利用RAG架构，让化学大模型实时检索庞大的分子数据库、谱图库或反应规则库，从而生成更准确、可追溯的分子结构推理或合成路线建议。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern AI and vector search are rapidly converging, forming a promising research frontier in intelligent information systems. On one hand, advances in AI have substantially improved the semantic accuracy and efficiency of vector search, including learned indexing structures, adaptive pruning strategies, and automated parameter tuning. On the other hand, powerful vector search techniques have enabled new AI paradigms, notably Retrieval-Augmented Generation (RAG), which effectively mitigates challenges in Large Language Models (LLMs) like knowledge staleness and hallucinations. This mutual reinforcement establishes a virtuous cycle where AI injects intelligence and adaptive optimization into vector search, while vector search, in turn, expands AI's capabilities in knowledge integration and context-aware generation. This tutorial provides a comprehensive overview of recent research and advancements at this intersection. We begin by discussing the foundational background and motivations for integrating vector search and AI. Subsequently, we explore how AI empowers vector search (AI4VS) across each step of the vector search pipeline. We then investigate how vector search empowers AI (VS4AI), with a particular focus on RAG frameworks that integrate dynamic, external knowledge sources into the generative process of LLMs. Furthermore, we analyze end-to-end co-optimization strategies that fully unlock the potential of the ``virtuous cycle" between vector search and AI. Finally, we highlight key challenges and future research opportunities in this emerging area. This paper was published in ICDE 2026.

</details>

---

### 23. [First Steps towards Categorical Algebraic Artificial Chemistry](https://arxiv.org/abs/2603.09431)

**基本信息**

- 🔗 arXiv: [`2603.09431`](https://arxiv.org/abs/2603.09431)
- 👥 作者: Joe Pratt-Johns, Toby St. Clere Smithe, Chris Guiver 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09431.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用范畴论为化学相互作用的代数模型构建形式化框架。这直接触及了“化学大模型”的基础，即如何用数学和计算模型来形式化地表示和推理化学实体与过程。它为化学信息的表示学习提供了潜在的理论工具。

**📖 中文摘要**

本文从范畴论的角度，为相互作用的组件的代数模型构建了一个提供动态的函子。该工作概括了人工生命领域AlChemy中的计算模型，其中分子及其化学相互作用由λ演算项及其应用和后续归约来模拟。作者讨论了范畴论在代数人工化学中作为组织工具的未来应用方向，重点在于形式化此类模型的代数方面和动态方面之间的联系。这项工作虽然理论性较强，但其核心是试图为“人工化学”或更广义的“化学过程的形式化建模”提供一个严格的数学框架。这直接与“化学大模型”的基础研究相关，因为化学大模型本质上也是对化学实体（原子、分子、反应）及其相互作用进行数学表示和计算。本文提出的范畴论方法，可能为理解和设计更严谨、可解释的化学表示和推理模型提供新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We construct a functor that gives a dynamics to an algebraic model of interacting components. The construction generalises a computational model of Fontana and Buss in the field of artificial life known as AlChemy, in which molecules and their chemical interactions are emulated by lambda calculus terms and their application and subsequent reduction. We discuss future directions for the application of category theory to algebraic artificial chemistry as an organisational tool, with a focus on formalising the connection between the algebraic and the dynamical facets of such models.

</details>

---

### 24. [AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems](https://arxiv.org/abs/2603.09435)

**基本信息**

- 🔗 arXiv: [`2603.09435`](https://arxiv.org/abs/2603.09435)
- 👥 作者: Athanasios Davvetas, Michael Papademas, Xenia Ziouvelou 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09435.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种构建评估数据集的方法论和具体实例。该方法利用LLM结合领域知识生成任务和场景，可用于创建评估“化学大模型”或“质谱结构推理”系统性能的基准数据集、资源或工具，从而支持这些主题的研究与发展。

**📖 中文摘要**

本文提出了一个开放、透明、可复现的资源创建方法，旨在促进对自然语言处理（NLP）模型（特别是检索增强生成RAG系统）的评估。该资源是一个针对欧盟《人工智能法案》的数据集，包含风险等级分类、条款检索、义务生成和问答等任务。为了生成数据集文件，作者结合领域知识（法案文本）和大语言模型的处理与推理能力来生成场景及相应任务。这项工作的方法论展示了如何利用语言模型进行有根据的（基于文档的）生成。虽然应用领域是法规遵从，但其核心技术——构建一个用于评估复杂AI系统（特别是RAG系统）在特定领域知识任务上性能的基准——与评估“化学大模型”或“质谱结构推理”系统的需求完全吻合。例如，可以借鉴此方法，构建一个用于评估化学大模型在分子性质预测、反应条件推荐或根据质谱图推理分子结构等任务上的基准数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid rollout of AI in heterogeneous public and societal sectors has subsequently escalated the need for compliance with regulatory standards and frameworks. The EU AI Act has emerged as a landmark in the regulatory landscape. The development of solutions that elicit the level of AI systems' compliance with such standards is often limited by the lack of resources, hindering the semi-automated or automated evaluation of their performance. This generates the need for manual work, which is often error-prone, resource-limited or limited to cases not clearly described by the regulation. This paper presents an open, transparent, and reproducible method of creating a resource that facilitates the evaluation of NLP models with a strong focus on RAG systems. We have developed a dataset that contain the tasks of risk-level classification, article retrieval, obligation generation, and question-answering for the EU AI Act. The dataset files are in a machine-to-machine appropriate format. To generate the files, we utilise domain knowledge as an exegetical basis, combining with the processing and reasoning power of large language models to generate scenarios along with the respective tasks. Our methodology demonstrates a way to harness language models for grounded generation with high document relevancy. Besides, we overcome limitations such as navigating the decision boundaries of risk-levels that are not explicitly defined within the EU AI Act, such as limited and minimal cases. Finally, we demonstrate our dataset's effectiveness by evaluating a RAG-based solution that reaches 0.87 and 0.85 F1-score for prohibited and high-risk scenarios.

</details>

---

### 25. [MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning](https://arxiv.org/abs/2603.09478)

**基本信息**

- 🔗 arXiv: [`2603.09478`](https://arxiv.org/abs/2603.09478)
- 👥 作者: Xiang Yuan, Xu Chu, Xinrong Chen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09478.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种使大型视觉语言模型（LVLM）执行显式、分步、复杂跨模态推理的方法。这种增强模型复杂推理能力的技术，直接适用于“化学大模型”和“质谱结构推理”场景，其中需要模型从多源数据（如谱图、分子式、文本描述）中进行逻辑严密的推理以得出结构结论。

**📖 中文摘要**

本文针对多模态对象-实体关系抽取（MORE）任务，提出了MORE-R1模型。该模型通过引入结合强化学习（RL）的显式分步推理，使大型视觉语言模型（LVLM）能够有效处理MORE任务。模型采用两阶段训练流程：初始的监督微调（SFT）冷启动阶段和后续的强化学习优化阶段。在初始阶段，作者设计了一种高效的方法，自动构建包含针对MORE任务的细粒度分步推理的高质量SFT数据集。在强化学习阶段，采用分组相对策略优化（GRPO）算法来进一步增强模型在困难样本上的推理能力。这项工作虽然关注通用的多模态关系抽取，但其核心创新——让大模型（LVLM）执行复杂的、可解释的、分步的跨模态推理——正是“化学大模型”和“质谱结构推理”所亟需的能力。例如，从质谱图与分子文本描述中联合推理出特定的官能团或子结构，就需要类似的复杂多模态推理链条。本文提出的分步推理训练和优化框架，为开发能够进行透明、可靠化学推理的大模型提供了技术参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal Object-Entity Relation Extraction (MORE) is a challenging task in information extraction research. It aims to identify relations between visual objects and textual entities, requiring complex multimodal understanding and cross-modal reasoning abilities. Existing methods, mainly classification-based or generation-based without reasoning, struggle to handle complex extraction scenarios in the MORE task and suffer from limited scalability and intermediate reasoning transparency. To address these challenges, we propose MORE-R1, a novel model that introduces explicit stepwise reasoning with Reinforcement Learning (RL) to enable Large Vision-Language Model (LVLM) to address the MORE task effectively. MORE-R1 integrates a two-stage training process, including an initial cold-start training stage with Supervised Fine-Tuning (SFT) and a subsequent RL stage for reasoning ability optimization. In the initial stage, we design an efficient way to automatically construct a high-quality SFT dataset containing fine-grained stepwise reasoning tailored to the MORE task, enabling the model to learn an effective reasoning paradigm. In the subsequent stage, we employ the Group Relative Policy Optimization (GRPO) RL algorithm with a Progressive Sample-Mixing Strategy to stabilize training and further enhance model's reasoning ability on hard samples. Comprehensive experiments on the MORE benchmark demonstrate that MORE-R1 achieves state-of-the-art performance with significant improvement over baselines.

</details>

---

### 26. [Symbolic Discovery of Stochastic Differential Equations with Genetic Programming](https://arxiv.org/abs/2603.09597)

**基本信息**

- 🔗 arXiv: [`2603.09597`](https://arxiv.org/abs/2603.09597)
- 👥 作者: Sigur de Vries, Sander W. Keemink, Marcel A. J. van Gerven
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09597.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（符号回归、自动化科学发现、从数据中学习可解释的数学模型）直接围绕构建和理解复杂系统的‘化学大模型’这一主题。该方法论对于开发可解释的、基于物理化学原理的化学信息学模型具有基础性意义。

**📖 中文摘要**

本文提出了一种基于遗传编程的随机微分方程符号发现方法。该方法联合优化漂移和扩散函数，通过最大似然估计从数据中学习可解释的数学表达式。研究扩展了符号回归的应用范围，使其能够发现包含噪声组分的随机动力学系统。这项工作与化学信息学中的化学大模型主题相关，因为符号回归和可解释的模型发现是构建和理解复杂化学系统（如反应动力学、分子性质预测）大模型的基础方法论。该方法展示了如何从嘈杂的动态数据中自动化地发现控制方程，这一能力对于构建能够推理质谱数据背后物理化学过程的模型具有潜在价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated scientific discovery aims to improve scientific understanding through machine learning. A central approach in this field is symbolic regression, which uses genetic programming or sparse regression to learn interpretable mathematical expressions to explain observed data. Conventionally, the focus of symbolic regression is on identifying ordinary differential equations. The general view is that noise only complicates the recovery of deterministic dynamics. However, explicitly learning a symbolic function of the noise component in stochastic differential equations enhances modelling capacity, increases knowledge gain and enables generative sampling. We introduce a method for symbolic discovery of stochastic differential equations based on genetic programming, jointly optimizing drift and diffusion functions via the maximum likelihood estimate. Our results demonstrate accurate recovery of governing equations, efficient scaling to higher-dimensional systems, robustness to sparsely sampled problems and generalization to stochastic partial differential equations. This work extends symbolic regression toward interpretable discovery of stochastic dynamical systems, contributing to the automation of science in a noisy and dynamic world.

</details>

---

### 27. [MM-algorithms for traditional and convex NMF with Tweedie and Negative Binomial cost functions and empirical evaluation](https://arxiv.org/abs/2603.09601)

**基本信息**

- 🔗 arXiv: [`2603.09601`](https://arxiv.org/abs/2603.09601)
- 👥 作者: Elisabeth Sommer James, Asger Hobolth, Marta Pelizzola
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09601.pdf)

**💡 相关性分析**

满足标准2：论文提供了可用于化学信息学和质谱分析的数据分析工具（扩展的NMF框架及实现）。NMF是处理质谱等高维化学数据的常用方法，本文提出的支持复杂噪声模型的框架可直接应用于质谱数据的特征提取和结构推理。

**📖 中文摘要**

本文为非负矩阵分解（NMF）提供了一个统一框架，适用于包括负二项式和Tweedie模型在内的广泛分布假设。NMF是化学信息学中用于光谱数据分析、特征提取和降维的关键工具。论文提出了针对传统NMF和凸NMF的乘性更新规则，并首次实现了多种凸NMF模型。研究强调，噪声模型的选择对模型拟合和特征恢复有重要影响。在化学信息学中，质谱数据常表现出复杂的噪声和方差结构，该框架为处理此类数据提供了更灵活的建模工具。论文还发布了实现代码，促进了该方法的可用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Non-negative matrix factorisation (NMF) is a widely used tool for unsupervised learning and feature extraction, with applications ranging from genomics to text analysis and signal processing. Standard formulations of NMF are typically derived under Gaussian or Poisson noise assumptions, which may be inadequate for data exhibiting overdispersion or other complex mean-variance relationships. In this paper, we develop a unified framework for both traditional and convex NMF under a broad class of distributional assumptions, including Negative Binomial and Tweedie models, where the connection between the Tweedie and the $\beta$-divergence is also highlighted. Using a Majorize-Minimisation approach, we derive multiplicative update rules for all considered models, and novel updates for convex NMF with Poisson and Negative Binomial cost functions. We provide a unified implementation of all considered models, including the first implementations of several convex NMF models. Empirical evaluations on mutational and word count data demonstrate that the choice of noise model critically affects model fit and feature recovery, and that convex NMF can provide an efficient and robust alternative to traditional NMF in scenarios where the number of classes is large. The code for our proposed updates is available in the R package nmfgenr and can be found at this https URL .

</details>

---

### 28. [Understanding the Interplay between LLMs' Utilisation of Parametric and Contextual Knowledge: A keynote at ECIR 2025](https://arxiv.org/abs/2603.09654)

**基本信息**

- 🔗 arXiv: [`2603.09654`](https://arxiv.org/abs/2603.09654)
- 👥 作者: Isabelle Augenstein
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09654.pdf)

**💡 相关性分析**

满足标准1：论文的核心讨论（参数化知识与上下文知识的整合、知识冲突）直接关系到如何构建和评估能够可靠利用化学知识和实验数据进行推理的‘化学大模型’。这对于质谱结构推理等需要结合先验知识与新证据的任务具有根本重要性。

**📖 中文摘要**

本文探讨了大型语言模型（LLMs）中参数化知识（训练获得）与上下文知识（检索提供）之间的相互作用。作者指出，LLMs在用于知识密集型任务时，经常忽略提供的上下文，尤其是当上下文与模型预训练记忆中的知识相冲突时。报告提出了评估LM中知识存在性的方法、揭示知识冲突的诊断测试，以及理解成功使用的上下文知识特征的研究。虽然主题更通用，但其核心问题——如何让模型有效整合外部证据与内部知识——对于构建可靠的‘化学大模型’至关重要。例如，在质谱结构推理中，模型需要结合通用的化学知识（参数化）和特定的谱图数据（上下文）做出准确预测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Language Models (LMs) acquire parametric knowledge from their training process, embedding it within their weights. The increasing scalability of LMs, however, poses significant challenges for understanding a model's inner workings and further for updating or correcting this embedded knowledge without the significant cost of retraining. Moreover, when using these language models for knowledge-intensive language understanding tasks, LMs have to integrate relevant context, mitigating their inherent weaknesses, such as incomplete or outdated knowledge. Nevertheless, studies indicate that LMs often ignore the provided context as it can be in conflict with the pre-existing LM's memory learned during pre-training. Conflicting knowledge can also already be present in the LM's parameters, termed intra-memory conflict. This underscores the importance of understanding the interplay between how a language model uses its parametric knowledge and the retrieved contextual knowledge. In this talk, I will aim to shed light on this important issue by presenting our research on evaluating the knowledge present in LMs, diagnostic tests that can reveal knowledge conflicts, as well as on understanding the characteristics of successfully used contextual knowledge.

</details>

---

### 29. [Fusing Semantic, Lexical, and Domain Perspectives for Recipe Similarity Estimation](https://arxiv.org/abs/2603.09688)

**基本信息**

- 🔗 arXiv: [`2603.09688`](https://arxiv.org/abs/2603.09688)
- 👥 作者: Denica Kjorvezir, Danilo Najkov, Eva Valencič 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09688.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（多视角信息融合进行相似性评估与系统生成）与化学信息学中‘化学大模型’和‘质谱结构推理’的核心任务在方法论上直接相关。例如，将食材视为‘分子’，制备方法视为‘反应条件’，营养属性视为‘物化性质’，则该框架可直接类比于分子相似性计算、谱图匹配和化合物生成任务。

**📖 中文摘要**

本研究专注于通过结合语义、词汇和领域视角来评估食谱相似性的高级方法。研究分析了食材、制备方法和营养属性，并开发了一个基于Web的界面供领域专家验证组合相似性结果。该方法在食品行业具有广泛应用，支持个性化饮食、营养推荐和自动化食谱生成系统。虽然应用领域是食品，但其核心方法论——融合多源信息（成分、方法、属性）进行相似性评估和生成——与化学信息学中的分子相似性计算、反应条件推荐以及基于质谱的化合物分类与检索在概念和技术上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This research focuses on developing advanced methods for assessing similarity between recipes by combining different sources of information and analytical approaches. We explore the semantic, lexical, and domain similarity of food recipes, evaluated through the analysis of ingredients, preparation methods, and nutritional attributes. A web-based interface was developed to allow domain experts to validate the combined similarity results. After evaluating 318 recipe pairs, experts agreed on 255 (80%). The evaluation of expert assessments enables the estimation of which similarity aspects--lexical, semantic, or nutritional--are most influential in expert decision-making. The application of these methods has broad implications in the food industry and supports the development of personalized diets, nutrition recommendations, and automated recipe generation systems.

</details>

---

### 30. [Evaluation of LLMs in retrieving food and nutritional context for RAG systems](https://arxiv.org/abs/2603.09704)

**基本信息**

- 🔗 arXiv: [`2603.09704`](https://arxiv.org/abs/2603.09704)
- 👥 作者: Maks Požarnik Vavken, Matevž Ogrinc, Tome Eftimov 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09704.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究了LLMs在专业领域（此处为食品营养）数据检索和RAG系统中的应用，这与构建用于化学领域（如质谱数据库检索、化合物信息查询）的‘化学大模型’在技术路径上高度相关。2) 论文的评估框架和方法为构建化学领域的类似RAG系统提供了参考和工具思路。

**📖 中文摘要**

本文评估了四种大型语言模型（LLMs）在专业检索增强生成（RAG）系统中检索数据的有效性，该系统使用了一个全面的食物成分数据库。方法聚焦于LLMs将自然语言查询转换为结构化元数据过滤器的能力，从而实现通过向量数据库进行高效检索。研究表明，LLMs可以作为高性能工具，大幅减少领域专家利用复杂食物和营养数据所需的手动工作和专业知识。尽管在简单和中等复杂查询上表现良好，但对困难问题的分析表明，当查询涉及无法明确表达的约束时，可靠检索仍然具有挑战性。这项工作展示了LLM在结构化数据检索中的潜力与局限。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database. Our method is focused on the LLMs ability to translate natural language queries into structured metadata filters, enabling efficient retrieval via a Chroma vector database. By achieving high accuracy in this critical retrieval step, we demonstrate that LLMs can serve as an accessible, high-performance tool, drastically reducing the manual effort and technical expertise previously required for domain experts, such as food compilers and nutritionists, to leverage complex food and nutrition data. However, despite the high performance on easy and moderately complex queries, our analysis of difficult questions reveals that reliable retrieval remains challenging when queries involve non-expressible constraints. These findings demonstrate that LLM-driven metadata filtering excels when constraints can be explicitly expressed, but struggles when queries exceed the representational scope of the metadata format.

</details>

---

### 31. [Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation](https://arxiv.org/abs/2603.09756)

**基本信息**

- 🔗 arXiv: [`2603.09756`](https://arxiv.org/abs/2603.09756)
- 👥 作者: Yue Wua, Tianhao Su, Rui Hu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09756.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何利用AI（特别是大语言模型和神经符号方法）进行科学发现和物理机制推理，这与“化学大模型”主题中利用AI模型进行科学计算和推理的核心方向高度相关。

**📖 中文摘要**

本文提出了一种神经符号生成代理，旨在解决将大语言模型（LLMs）集成到科学发现中时遇到的“隐式上下文”问题。该问题表现为从文献中提取的控制方程包含不可见的热力学假设（例如不排水条件），导致标准生成模型产生物理上无效的求解器（物理幻觉）。该代理将物理定律封装成模块化的本构技能，并利用潜在的内在先验，通过思维链推理工作流来自主验证、剪枝和补全物理机制。论文以低渗透率砂岩中的热增压问题为例进行了演示。该方法超越了传统文献检索基线，能够通过无量纲尺度分析识别系统状态，并归纳性地补全缺失的耗散机制（达西流），从而预测出与实验现实一致的稳定应力路径。这项工作建立了一种范式，使AI代理能够作为认知伙伴，对嵌入科学数据中的理论假设进行推理和修正。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) into scientific discovery is currently hindered by the Implicit Context problem, where governing equations extracted from literature contain invisible thermodynamic assumptions (e.g., undrained conditions) that standard generative models fail to recognize. This leads to Physical Hallucination: the generation of syntactically correct solvers that faithfully execute physically invalid laws. Here, we introduce a Neuro-Symbolic Generative Agent that functions as a cognitive supervisor atop traditional numerical engines. By encapsulating physical laws into modular Constitutive Skills and leveraging latent intrinsic priors, the Agent employs a Chain-of-Thought reasoning workflow to autonomously validate, prune, and complete physical mechanisms. We demonstrate this capability on the challenge of thermal pressurization in low-permeability sandstone. While a standard literature-retrieval baseline erroneously predicts catastrophic material failure by blindly adopting a rigid "undrained" simplification, our Agent autonomously identifies the system as operating in a drained regime (Deborah number De << 1) via dimensionless scaling analysis. Consequently, it inductively completes the missing dissipation mechanism (Darcy flow) required to satisfy boundary constraints, predicting a stable stress path consistent with experimental reality. This work establishes a paradigm where AI agents transcend the role of coding assistants to act as epistemic partners, capable of reasoning about and correcting the theoretical assumptions embedded in scientific data.

</details>

---

### 32. [MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](https://arxiv.org/abs/2603.09800)

**基本信息**

- 🔗 arXiv: [`2603.09800`](https://arxiv.org/abs/2603.09800)
- 👥 作者: Abhishikth Mallampalli, Sridhara Dasu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09800.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于科学知识检索的RAG系统（MITRA），包括其自动化文档检索、处理管道和向量数据库架构。这为“化学大模型”或相关科学领域构建专用知识检索和问答工具提供了数据资源、工具和系统设计方面的参考。

**📖 中文摘要**

本文介绍了MITRA，一个为大型科学合作（如CERN的CMS实验）设计的检索增强生成（RAG）系统原型。该系统旨在回答关于物理分析的特定、上下文感知的问题。MITRA采用了一个新颖的自动化管道，使用Selenium从内部数据库检索文档，并使用光学字符识别（OCR）和布局解析进行高保真文本提取。整个框架（从嵌入模型到大语言模型）都在本地托管，确保了敏感合作数据的隐私。它引入了一个两层向量数据库架构，首先从摘要中识别相关分析，然后聚焦于完整文档，解决了不同分析之间的潜在歧义。该系统展示了在现实查询上优于基于关键字的基线的检索性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significant challenge for both new and experienced researchers, hindering knowledge sharing and slowing down the pace of scientific discovery. To address this, we present a prototype of MITRA, a Retrieval-Augmented Generation (RAG) based system, designed to answer specific, context-aware questions about physics analyses. MITRA employs a novel, automated pipeline using Selenium for document retrieval from internal databases and Optical Character Recognition (OCR) with layout parsing for high-fidelity text extraction. Crucially, MITRA's entire framework, from the embedding model to the Large Language Model (LLM), is hosted on-premise, ensuring that sensitive collaboration data remains private. We introduce a two-tiered vector database architecture that first identifies the relevant analysis from abstracts before focusing on the full documentation, resolving potential ambiguities between different analyses. We demonstrate the prototype's superior retrieval performance against a standard keyword-based baseline on realistic queries and discuss future work towards developing a comprehensive research agent for large experimental collaborations.

</details>

---

### 33. [RecThinker: An Agentic Framework for Tool-Augmented Reasoning in Recommendation](https://arxiv.org/abs/2603.09843)

**基本信息**

- 🔗 arXiv: [`2603.09843`](https://arxiv.org/abs/2603.09843)
- 👥 作者: Haobo Zhang, Yutao Zhu, Kelong Mao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09843.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个能够进行自主规划、工具调用和复杂推理的智能体框架（RecThinker）。这直接关联到“化学大模型”主题中关于构建具有复杂推理和工具使用能力的AI智能体的研究方向。

**📖 中文摘要**

本文提出了RecThinker，一个用于推荐系统中工具增强推理的智能体框架。它将推荐从被动处理转变为自主调查，通过动态规划推理路径并自主调用工具来主动获取关键信息。RecThinker采用分析-规划-执行范式，首先分析用户-物品信息的充分性，然后自主调用工具序列来弥合可用知识与推理需求之间的信息鸿沟。作者为RecThinker开发了一套专用工具，使模型能够获取用户侧、物品侧和协同信息以进行更好的推理和匹配。此外，还引入了自增强训练流程，包括监督微调阶段以内化高质量推理轨迹，以及强化学习阶段以优化决策准确性和工具使用效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have revolutionized recommendation agents by providing superior reasoning and flexible decision-making capabilities. However, existing methods mainly follow a passive information acquisition paradigm, where agents either rely on static pre-defined workflows or perform reasoning with constrained information. It limits the agent's ability to identify information sufficiency, often leading to suboptimal recommendations when faced with fragmented user profiles or sparse item metadata. To address these limitations, we propose RecThinker, an agentic framework for tool-augmented reasoning in recommendation, which shifts recommendation from passive processing to autonomous investigation by dynamically planning reasoning paths and proactively acquiring essential information via autonomous tool-use. Specifically, RecThinker adopts an Analyze-Plan-Act paradigm, which first analyzes the sufficiency of user-item information and autonomously invokes tool-calling sequences to bridge information gaps between available knowledge and reasoning requirements. We develop a suite of specialized tools for RecThinker, enabling the model to acquire user-side, item-side, and collaborative information for better reasoning and user-item matching. Furthermore, we introduce a self-augmented training pipeline, comprising a Supervised Fine-Tuning (SFT) stage to internalize high-quality reasoning trajectories and a Reinforcement Learning (RL) stage to optimize for decision accuracy and tool-use efficiency. Extensive experiments on multiple benchmark datasets demonstrate that RecThinker consistently outperforms strong baselines in the recommendation scenario.

</details>

---

### 34. [Influencing LLM Multi-Agent Dialogue via Policy-Parameterized Prompts](https://arxiv.org/abs/2603.09890)

**基本信息**

- 🔗 arXiv: [`2603.09890`](https://arxiv.org/abs/2603.09890)
- 👥 作者: Hongbo Bo, Jingyu Hu, Weiru Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09890.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于大语言模型多智能体系统的行为控制和策略设计。这直接关联到“化学大模型”主题中关于多智能体协作、规划和控制的子方向。

**📖 中文摘要**

本文研究了如何通过策略参数化的提示来影响基于大语言模型的多智能体对话行为。与强化学习不同，该研究探讨了“提示即行动”是否可以被参数化，以构建一个轻量级策略（由状态-动作对序列组成），从而在不进行训练的情况下影响对话行为。该框架将提示视为由LLMs执行的动作，并根据智能体的当前状态动态构建提示。为了测试参数化控制的有效性，作者基于五个指标（响应性、反驳、证据使用、非重复性和立场转变）评估了对话流。实验在两种与公众相关的讨论场景中使用不同的LLM驱动智能体进行，结果表明提示参数化可以影响对话动态。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have emerged as a new paradigm for multi-agent systems. However, existing research on the behaviour of LLM-based multi-agents relies on ad hoc prompts and lacks a principled policy perspective. Different from reinforcement learning, we investigate whether prompt-as-action can be parameterized so as to construct a lightweight policy which consists of a sequence of state-action pairs to influence conversational behaviours without training. Our framework regards prompts as actions executed by LLMs, and dynamically constructs prompts through five components based on the current state of the agent. To test the effectiveness of parameterized control, we evaluated the dialogue flow based on five indicators: responsiveness, rebuttal, evidence usage, non-repetition, and stance shift. We conduct experiments using different LLM-driven agents in two discussion scenarios related to the general public and show that prompt parameterization can influence the dialogue dynamics. This result shows that policy-parameterised prompts offer a simple and effective mechanism to influence the dialogue process, which will help the research of multi-agent systems in the direction of social simulation.

</details>

---

### 35. [Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs](https://arxiv.org/abs/2603.09906)

**基本信息**

- 🔗 arXiv: [`2603.09906`](https://arxiv.org/abs/2603.09906)
- 👥 作者: Zorik Gekhman, Roee Aharoni, Eran Ofek 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09906.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于大语言模型中推理过程如何影响知识回忆的内在机制。这对于理解和构建更可靠的“化学大模型”（特别是用于科学事实检索和问答的模型）具有直接的理论和实践意义。

**📖 中文摘要**

本文探讨了推理在大语言模型回答简单、单跳事实性问题中的作用。研究发现，启用推理可以显著扩展模型参数知识回忆的能力边界，解锁原本无法触及的正确答案。通过一系列假设驱动的受控实验，论文确定了两个关键驱动机制：（1）计算缓冲效应：模型使用生成的推理标记执行独立于其语义内容的潜在计算；（2）事实启动：生成主题相关的事实作为语义桥梁，促进正确答案的检索。重要的是，后一种生成式自我检索机制存在固有风险：在推理过程中产生幻觉中间事实会增加最终答案出现幻觉的可能性。最后，研究表明，通过优先选择包含无幻觉事实陈述的推理轨迹，可以直接提高模型准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While reasoning in LLMs plays a natural role in math, code generation, and multi-hop factual questions, its effect on simple, single-hop factual questions remains unclear. Such questions do not require step-by-step logical decomposition, making the utility of reasoning highly counterintuitive. Nevertheless, we find that enabling reasoning substantially expands the capability boundary of the model's parametric knowledge recall, unlocking correct answers that are otherwise effectively unreachable. Why does reasoning aid parametric knowledge recall when there are no complex reasoning steps to be done? To answer this, we design a series of hypothesis-driven controlled experiments, and identify two key driving mechanisms: (1) a computational buffer effect, where the model uses the generated reasoning tokens to perform latent computation independent of their semantic content; and (2) factual priming, where generating topically related facts acts as a semantic bridge that facilitates correct answer retrieval. Importantly, this latter generative self-retrieval mechanism carries inherent risks: we demonstrate that hallucinating intermediate facts during reasoning increases the likelihood of hallucinations in the final answer. Finally, we show that our insights can be harnessed to directly improve model accuracy by prioritizing reasoning trajectories that contain hallucination-free factual statements.

</details>

---

### 36. [Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation](https://arxiv.org/abs/2603.09931)

**基本信息**

- 🔗 arXiv: [`2603.09931`](https://arxiv.org/abs/2603.09931)
- 👥 作者: Rong Zhou, Houliang Zhou, Yao Su 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09931.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散模型的、能够处理多模态数据缺失并进行生成的AI模型（ACADiff）。这直接关联到“化学大模型”主题中关于利用生成式AI模型处理复杂科学数据（如医学影像）的研究方向。

**📖 中文摘要**

本文提出了ACADiff，一个用于阿尔茨海默病诊断中多模态脑成像缺失模态生成和补全的框架。ACADiff通过自适应临床感知扩散，学习从不完整的多模态观察到目标模态的映射，同时在去噪潜在表示时关注可用的成像数据和临床元数据。该框架采用基于输入可用性动态重构的自适应融合，以及通过GPT-4o编码提示实现的语义临床指导。三个专用生成器实现了sMRI、FDG-PET和AV45-PET之间的双向合成。在ADNI受试者上的评估表明，ACADiff实现了卓越的生成质量，即使在极端80%缺失的情况下也能保持稳健的诊断性能，优于所有现有基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal neuroimaging provides complementary insights for Alzheimer's disease diagnosis, yet clinical datasets frequently suffer from missing modalities. We propose ACADiff, a framework that synthesizes missing brain imaging modalities through adaptive clinical-aware diffusion. ACADiff learns mappings between incomplete multimodal observations and target modalities by progressively denoising latent representations while attending to available imaging data and clinical metadata. The framework employs adaptive fusion that dynamically reconfigures based on input availability, coupled with semantic clinical guidance via GPT-4o-encoded prompts. Three specialized generators enable bidirectional synthesis among sMRI, FDG-PET, and AV45-PET. Evaluated on ADNI subjects, ACADiff achieves superior generation quality and maintains robust diagnostic performance even under extreme 80\% missing scenarios, outperforming all existing baselines. To promote reproducibility, code is available at this https URL

</details>

---

### 37. [From Word2Vec to Transformers: Text-Derived Composition Embeddings for Filtering Combinatorial Electrocatalysts](https://arxiv.org/abs/2603.08881)

**基本信息**

- 🔗 arXiv: [`2603.08881`](https://arxiv.org/abs/2603.08881)
- 👥 作者: Lei Zhang, Markus Stricker
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08881.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用从科学文本中学习到的嵌入（可视为一种简单的化学表示模型）来筛选电催化剂组合，这直接围绕“化学大模型”中利用预训练模型进行材料发现和性质预测的主题。

**📖 中文摘要**

本文提出了一种无标签筛选策略，用于从成分复杂的固溶体电催化剂组合空间中高效筛选候选物。该方法的核心是利用从科学文本中衍生的嵌入向量来表示每种化学成分。具体而言，作者比较了基于语料库训练的Word2Vec基线模型与基于Transformer的嵌入方法（包括线性元素混合编码和短成分提示编码）。通过计算候选成分与两个属性概念（“导电性”和“介电性”）的相似度，构建了一个二维描述符空间，并采用对称帕累托前沿选择法来筛选候选子集，整个过程无需使用电化学标签。该方法在包括贵金属合金和多组分氧化物在内的15个材料库上进行了评估。这项工作展示了如何利用文本衍生的化学信息（嵌入向量）来指导高通量材料筛选，与“化学大模型”中利用预训练模型从文本或结构数据中提取特征以指导下游任务（如性质预测、材料发现）的核心思想高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Compositionally complex solid solution electrocatalysts span vast composition spaces, and even one materials system can contain more candidate compositions than can be measured exhaustively. Here we evaluate a label-free screening strategy that represents each composition using embeddings derived from scientific texts and prioritizes candidates based on similarity to two property concepts. We compare a corpus-trained Word2Vec baseline with transformer-based embeddings, where compositions are encoded either by linear element-wise mixing or by short composition prompts. Similarities to `concept directions', the terms conductivity and dielectric, define a 2-dimensional descriptor space, and a symmetric Pareto-front selection is used to filter candidate subsets without using electrochemical labels. Performance is assessed on 15 materials libraries including noble metal alloys and multicomponent oxides. In this setting, the lightweight Word2Vec baseline, which uses a simple linear combination of element embeddings, often achieves the highest number of reductions of possible candidate compositions while staying close to the best measured performance.

</details>

---

### 38. [Statistical Inference via Generative Models: Flow Matching and Causal Inference](https://arxiv.org/abs/2603.09009)

**基本信息**

- 🔗 arXiv: [`2603.09009`](https://arxiv.org/abs/2603.09009)
- 👥 作者: Shinto Eguchi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09009.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（复合图像-文本查询的检索）与“质谱结构推理”中结合谱图和文本信息进行化合物检索或案例比对的任务在问题定义和技术路线上高度相关。

**📖 中文摘要**

这篇论文研究了皮肤癌的复合视觉-语言检索，即结合参考病变图像和文本描述（如皮肤镜特征）作为查询，从数据库中检索相关的活检确诊病例。论文提出了一个基于Transformer的框架，学习分层的复合查询表示，并执行全局-局部联合对齐。这项研究虽然针对医学图像，但其解决的问题范式与“质谱结构推理”中的一个关键场景高度相似：在质谱鉴定中，用户可能提供一张质谱图（类似“图像”）并结合一些已知的上下文信息（如样品来源、可能的化合物类别等文本描述），系统需要从数据库中检索出最匹配的已知化合物谱图或类似案例。论文中提出的联合全局-局部对齐、利用空间注意力聚焦判别性区域等方法，为构建更精准、更灵活的质谱谱图检索系统提供了可借鉴的模型架构和算法思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative AI has achieved remarkable empirical success, but from the perspective of statistics it often remains opaque: its predictions may be accurate, yet the underlying mechanism is difficult to interpret, analyze, and trust. This book reinterprets generative AI in the language of statistics, using flow matching as a central example. The key idea is that generative models should be understood not merely as devices for producing plausible data, but as methods for the nonparametric learning of high-dimensional probability distributions. From this viewpoint, missing-data imputation becomes principled sampling from learned conditional distributions, counterfactual analysis becomes the estimation of intervention distributions, and distributional dynamics become statistically analyzable objects. Mathematically, flow matching represents distributional deformation through the continuity equation and a time-dependent velocity field, thereby extending score matching from the learning of static score fields to the learning of transport paths themselves. Building on this foundation, the book develops a statistical framework in which generative models are used to estimate nuisance components while inferential validity is maintained through orthogonalization and cross-fitting in the spirit of double/debiased machine learning. Applications to survival analysis, censoring, missingness, and causal inference show how generative models can be integrated into statistical inference for structured high-dimensional problems.

</details>

---

### 39. [A Generative Sampler for distributions with possible discrete parameter based on Reversibility](https://arxiv.org/abs/2603.09251)

**基本信息**

- 🔗 arXiv: [`2603.09251`](https://arxiv.org/abs/2603.09251)
- 👥 作者: Lei Li, Zhen Wang, Lishuo Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09251.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种通用的生成式采样框架，特别适用于离散和混合变量系统（如伊辛模型），这直接与“化学大模型”中用于分子生成、构象采样或模拟化学系统平衡分布的生成模型主题相关。

**📖 中文摘要**

本文提出了一种统一的、无需目标梯度的生成式采样框架，适用于从复杂的未归一化分布中采样。该方法基于细致平衡原理意味着平衡随机过程具有时间可逆性，并将此对称性作为统计约束。具体而言，使用一个预设的物理转移核（如Metropolis-Hastings），通过最小化前向和后向马尔可夫轨迹的联合分布之间的最大均值差异（MMD）来训练模型。该训练过程仅依赖于通过接受率进行的能量评估，避免了目标评分函数或连续松弛的需要。作者在三个不同的基准上展示了该方法的通用性，其中包括离散高维伊辛模型。该框架为平衡采样提供了一个物理基础扎实且普遍适用的替代方案。这项工作与开发用于分子模拟和化学系统采样的生成模型密切相关，属于“化学大模型”在生成和采样方向的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning to sample from complex unnormalized distributions is a fundamental challenge in computational physics and machine learning. While score-based and variational methods have achieved success in continuous domains, extending them to discrete or mixed-variable systems remains difficult due to ill-defined gradients or high variance in estimators. We propose a unified, target-gradient-free generative sampling framework applicable across diverse state spaces. Building on the fact that detailed balance implies the time-reversibility of the equilibrium stochastic process, we enforce this symmetry as a statistical constraint. Specifically, using a prescribed physical transition kernel (such as Metropolis-Hastings), we minimize the Maximum Mean Discrepancy (MMD) between the joint distributions of forward and backward Markov trajectories. Crucially, this training procedure relies solely on energy evaluations via acceptance ratios, circumventing the need for target score functions or continuous relaxations. We demonstrate the versatility of our method on three distinct benchmarks: (1) a continuous multi-modal Gaussian mixture, (2) the discrete high-dimensional Ising model, and (3) a challenging hybrid system coupling discrete indices with continuous dynamics. Experiments show that our framework accurately reproduces thermodynamic observables and captures mode-switching behavior across all regimes, offering a physically grounded and universally applicable alternative for equilibrium sampling.

</details>

---

### 40. [First Estimation of Model Parameters for Neutrino-Induced Nucleon Knockout Using Simulation-Based Inference](https://arxiv.org/abs/2603.09778)

**基本信息**

- 🔗 arXiv: [`2603.09778`](https://arxiv.org/abs/2603.09778)
- 👥 作者: Karla Tame-Narvaez, Steven Gardiner, Aleksandra Ćiprijanović 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09778.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是应用基于模拟的推理（SBI）这一机器学习方法来估计中微子相互作用模拟中的模型参数，这直接围绕利用先进机器学习模型（可视为科学领域专用“大模型”）进行科学数据分析和模型校准的主题。

**📖 中文摘要**

为了精确测定中微子振荡参数，基于加速器的中微子实验需要对GeV能区的核相互作用物理进行详细模拟。目前，这些模拟的不足通常迫使实验合作组对模拟模型参数进行经验性调优。随着该领域精度要求的不断提高，机器学习技术可能为处理未来中微子相互作用模型调优日益增长的复杂性提供强大工具。为了研究基于模拟的推理（SBI）在此物理应用中的适用性，本文重新审视了由MicroBooNE合作组最初开发的GENIE中微子事件生成器的一个调优配置。尽管在将调优后的截面预测作为输入时，我们训练好的SBI算法对四个物理参数值得出了与原始调优值非常接近的配置，但我们发现算法倾向于略微不同的值（在MicroBooNE指定的不确定度范围内），并且在最初由MicroBooNE使用的实验数据集上运行推理时，获得了稍好的拟合优度。这项工作展示了SBI在粒子物理实验模型参数估计中的应用，属于利用机器学习（包括可能的大规模预训练模型）处理科学数据推断的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To enable an accurate determination of oscillation parameters, accelerator-based neutrino experiments require detailed simulations of nuclear interaction physics in the GeV regime. While substantial effort from both theory and experiment is currently being invested to improve the fidelity of these simulations, their present deficiencies typically oblige experimental collaborations to resort to empirical tuning of simulation model parameters. As the precision requirements of the field continue to become more stringent, machine learning techniques may provide a powerful means of handling corresponding growth in the complexity of future neutrino interaction model tuning exercises. To study the suitability of simulation-based inference (SBI) for this physics application, in this paper we revisit a tuned configuration of the GENIE neutrino event generator that was originally developed by the MicroBooNE collaboration. Despite closely reproducing the adopted values of four physics parameters when confronted with the tuned cross-section predictions as input, we find that our trained SBI algorithm prefers modestly different values (within MicroBooNE's assigned uncertainties) and achieves slightly better goodness-of-fit when inference is run on the experimental data set originally used by MicroBooNE. We also find that our trained algorithm can create a fair approximation of an alternative neutrino scattering simulation, NuWro, that shares only a subset of its physics model parameters with GENIE.

</details>

---

### 41. [Learning with Errors over Group Rings Constructed by Semi-direct Product](https://arxiv.org/abs/2311.15868)

**基本信息**

- 🔗 arXiv: [`2311.15868`](https://arxiv.org/abs/2311.15868)
- 👥 作者: Jiaqi Liu, Fang-Wei Fu
- 📄 PDF: [下载](https://arxiv.org/pdf/2311.15868.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是群环上的LWE问题及其在密码学中的应用，虽然领域不同，但其对复杂代数结构（群环）的深入分析和形式化建模，与“化学大模型”中利用数学结构（如图、群、对称性）进行分子表示和推理的核心主题在方法论层面相关。

**📖 中文摘要**

本文研究了一种称为群环LWE（GRLWE）的LWE问题的代数变体。作者选择了由两个循环群半直积构造的特定有限群族下的群环（或其直和项）。与经典Ring-LWE不同，这里考虑的群环中的乘法运算是非交换的。作为Ring-LWE的扩展，它保持了计算硬度，并可能应用于许多密码学场景。本文提出了两个多项式时间的量子归约证明，将理想格中最坏情况的短独立向量问题（SIVP）归约到GRLWE的搜索版本和判定版本。这保证了GRLWE样本的伪随机性，并可进而用于构建语义安全的公钥密码系统。这项工作属于后量子密码学领域，但其中对代数结构（群环）上LWE问题的形式化与分析，与“化学大模型”中利用对称性和群论等数学工具处理分子结构表示和推理有方法论上的共通之处，尽管应用领域不同。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Learning with Errors (\LWE) problem has been widely utilized as a foundation for numerous cryptographic tools over the years. In this study, we focus on an algebraic variant of the \LWE problem called \emph{Group ring} \LWE ($\GRLWE$). We select group rings (or their direct summands) that underlie specific families of finite groups constructed by taking the semi-direct product of two cyclic groups. Unlike the Ring-\LWE problem described in \cite{lyubashevsky2010ideal}, the multiplication operation in the group rings considered here is non-commutative. As an extension of Ring-$\LWE$, it maintains computational hardness and can be potentially applied in many cryptographic scenarios. In this paper, we present two polynomial-time quantum reductions. Firstly, we provide a quantum reduction from the worst-case shortest independent vectors problem (\SIVP) in ideal lattices with polynomial approximate factor to the search version of $\GRLWE$. This reduction requires that the underlying group ring possesses certain mild properties; Secondly, we present another quantum reduction for two types of group rings, where the worst-case \SIVP problem is directly reduced to the (average-case) decision $\GRLWE$ problem. The pseudorandomness of $\GRLWE$ samples guaranteed by this reduction can be consequently leveraged to construct semantically secure public-key cryptosystems.

</details>

---

### 42. [Scalable Message Passing Neural Networks: No Need for Attention in Large Graph Representation Learning](https://arxiv.org/abs/2411.00835)

**基本信息**

- 🔗 arXiv: [`2411.00835`](https://arxiv.org/abs/2411.00835)
- 👥 作者: Haitz Sáez de Ocáriz Borde, Artem Lukoianov, Anastasis Kratsios 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.00835.pdf)

**💡 相关性分析**

满足标准1：论文提出的可扩展图神经网络（SMPNNs）是构建化学大模型（用于分子图学习）的核心技术之一，其研究内容直接围绕图表示学习这一化学信息学和化学大模型的基础主题。

**📖 中文摘要**

本文提出了可扩展消息传递神经网络（SMPNNs），这是一种基于图神经网络（GNN）的架构。虽然论文主要关注通用图表示学习，但其核心方法——改进的图神经网络——是构建化学大模型（用于分子表示和性质预测）的关键底层技术之一。论文提出的深度消息传递框架，为解决化学信息学中分子图的学习和推理问题提供了可扩展且高性能的模型方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose Scalable Message Passing Neural Networks (SMPNNs) and demonstrate that, by integrating standard convolutional message passing into a Pre-Layer Normalization Transformer-style block instead of attention, we can produce high-performing deep message-passing-based Graph Neural Networks (GNNs). This modification yields results competitive with the state-of-the-art in large graph transductive learning, particularly outperforming the best Graph Transformers in the literature, without requiring the otherwise computationally and memory-expensive attention mechanism. Our architecture not only scales to large graphs but also makes it possible to construct deep message-passing networks, unlike simple GNNs, which have traditionally been constrained to shallow architectures due to oversmoothing. Moreover, we provide a new theoretical analysis of oversmoothing based on universal approximation which we use to motivate SMPNNs. We show that in the context of graph convolutions, residual connections are necessary for maintaining the universal approximation properties of downstream learners and that removing them can lead to a loss of universality.

</details>

---

### 43. [The Gaussian-Multinoulli Restricted Boltzmann Machine: A Potts Model Extension of the GRBM](https://arxiv.org/abs/2505.11635)

**基本信息**

- 🔗 arXiv: [`2505.11635`](https://arxiv.org/abs/2505.11635)
- 👥 作者: Nikhil Kapasi, Mohamed Elfouly, William Whitehead 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.11635.pdf)

**💡 相关性分析**

满足标准1：论文提出的高斯-多项受限玻尔兹曼机（GM-RBM）专注于学习离散、结构化的潜在表示以进行推理，这与质谱结构推理中从连续谱数据推断离散分子结构的核心任务直接相关。

**📖 中文摘要**

本文提出了高斯-多项受限玻尔兹曼机（GM-RBM），这是一种生成式能量模型，用多状态分类（Potts）单元替代了传统高斯-伯努利RBM中的二元隐单元。该模型旨在为符号推理等任务提供更丰富的离散结构化潜在表示。虽然论文本身并非专门针对化学领域，但其核心——学习离散、结构化的潜在表示以进行推理——与质谱结构推理中从谱图数据推断离散分子结构的根本挑战高度相关。GM-RBM为处理此类具有复杂离散状态空间的推理问题提供了一个可扩展的生成模型框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many real-world tasks, from associative memory to symbolic reasoning, benefit from discrete, structured representations that standard continuous latent models can struggle to express. We introduce the Gaussian-Multinoulli Restricted Boltzmann Machine (GM-RBM), a generative energy-based model that extends the Gaussian-Bernoulli RBM (GB-RBM) by replacing binary hidden units with q-state categorical (Potts) units, yielding a richer latent state space for multivalued concepts. We provide a self-contained derivation of the energy, conditional distributions, and learning rules, and detail practical training choices (contrastive divergence with temperature annealing and intra-slot diversity constraints) that avoid state collapse. To separate architectural effects from sheer latent capacity, we evaluate under both capacity-matched and parameter-matched setups, comparing GM-RBM with GB-RBM configured to have the same number of possible latent assignments. On analogical recall and structured memory benchmarks, GM-RBM achieves competitive, and in several regimes improved, recall at equal capacity with comparable training cost, despite using only Gibbs updates. The discrete q-ary formulation is also amenable to efficient implementation. These results clarify when categorical hidden units provide a simple, scalable alternative to binary latents for discrete inference within tractable RBMs.

</details>

---

### 44. [Discovering Symbolic Differential Equations with Symmetry Invariants](https://arxiv.org/abs/2505.12083)

**基本信息**

- 🔗 arXiv: [`2505.12083`](https://arxiv.org/abs/2505.12083)
- 👥 作者: Jianke Yang, Manu Bhat, Bryan Hu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.12083.pdf)

**💡 相关性分析**

满足标准1：论文提出的利用对称性不变量进行符号方程发现的方法，其核心思想（整合领域知识以指导从数据中推理结构化模型）与质谱结构推理（从谱数据中推断化学结构）所面临的逆问题建模在方法论上高度相关。

**📖 中文摘要**

本文提出了一种利用对称性不变量从数据中发现符号微分方程的新方法。该方法通过将对称变换的微分不变量作为方程发现的基本单元，确保发现的方程满足指定的物理定律对称性。虽然论文以流体和反应-扩散等物理系统为例，但其方法论——将领域知识（如对称性）整合到数据驱动的模型发现中——对于化学信息学中的逆问题（如从质谱数据推断分子结构或反应动力学）具有重要的启示意义。该方法可以提升从复杂化学数据中推导可解释模型的准确性和效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering symbolic differential equations from data uncovers fundamental dynamical laws underlying complex systems. However, existing methods often struggle with the vast search space of equations and may produce equations that violate known physical laws. In this work, we address these problems by introducing the concept of symmetry invariants in equation discovery. We leverage the fact that differential equations admitting a symmetry group can be expressed in terms of differential invariants of symmetry transformations. Thus, we propose to use these invariants as atomic entities in equation discovery, ensuring the discovered equations satisfy the specified symmetry. Our approach integrates seamlessly with existing equation discovery methods such as sparse regression and genetic programming, improving their accuracy and efficiency. We validate the proposed method through applications to various physical systems, such as fluid and reaction-diffusion, demonstrating its ability to recover parsimonious and interpretable equations that respect the laws of physics.

</details>

---

### 45. [Rating Quality of Diverse Time Series Data by Meta-learning from LLM Judgment](https://arxiv.org/abs/2506.01290)

**基本信息**

- 🔗 arXiv: [`2506.01290`](https://arxiv.org/abs/2506.01290)
- 👥 作者: Shunyu Wu, Dan Li, Wenjie Feng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.01290.pdf)

**💡 相关性分析**

满足标准2：论文提出的TSRating框架，其利用LLMs评估数据质量并构建跨领域适应模型的方法论，为化学信息学和质谱分析领域构建高质量、可用于模型训练的数据集筛选与评估工具提供了直接相关的技术思路和潜在解决方案。

**📖 中文摘要**

本文提出了TSRating，一个用于评估来自不同领域的时间序列数据质量的统一框架。该框架利用大语言模型（LLMs）的广泛知识来理解和辨别时间序列数据的质量差异，并通过元学习方案训练一个专用的评级模型。虽然论文聚焦于通用时间序列，但其核心创新——利用LLMs的先验知识评估数据质量，并构建可跨领域适应的评估模型——为化学信息学和质谱分析中一个关键问题提供了思路：如何自动评估和筛选大规模、多来源的化学数据集（如质谱数据库）的质量，以用于训练更可靠的化学大模型或结构推理工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

High-quality time series (TS) data are essential for ensuring TS model performance, rendering research on rating TS data quality indispensable. Existing methods have shown promising rating accuracy within individual domains, primarily by extending data quality rating techniques such as influence functions and Shapley values to account for temporal characteristics. However, they neglect the fact that real-world TS data can span vastly different domains and exhibit distinct properties, hampering the accurate and efficient rating of diverse TS data. In this paper, we propose TSRating, a novel and unified framework for rating the quality of time series data crawled from diverse domains. TSRating leverages LLMs' inherent ample knowledge, acquired during their extensive pretraining, to comprehend and discern quality differences in diverse TS data. We verify this by devising a series of prompts to elicit quality comparisons from LLMs for pairs of TS samples. We then fit a dedicated rating model, termed TSRater, to convert the LLMs' judgments into efficient quality predictions by inferring future TS samples through TSRater's inference. To ensure cross-domain adaptability, we develop a meta-learning scheme to train TSRater on quality comparisons collected from nine distinct domains. To improve training efficiency, we employ signSGD for inner-loop updates, thus circumventing the demanding computation of hypergradients. Extensive experimental results on eleven benchmark datasets across three time series tasks, each using both conventional TS models and TS foundation models, demonstrate that TSRating outperforms baselines in terms of estimation accuracy, efficiency, and domain adaptability.

</details>

---

### 46. [Evaluating Large Language Models for Multilingual Vulnerability Detection at Dual Granularities](https://arxiv.org/abs/2506.07503)

**基本信息**

- 🔗 arXiv: [`2506.07503`](https://arxiv.org/abs/2506.07503)
- 👥 作者: Honglin Shu, Michael Fu, Junji Yu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.07503.pdf)

**💡 相关性分析**

满足标准1：论文对LLMs/PLMs在复杂、结构化数据（代码）上的多粒度推理能力进行的系统性评估，其研究范式、评估维度和结论对于如何评估化学大模型或质谱结构推理模型在化学数据上的性能具有核心参考价值，属于相关的方法论研究。

**📖 中文摘要**

本文对预训练语言模型（PLMs）和大语言模型（LLMs）在多语言漏洞检测任务中的有效性进行了全面的实证研究。研究评估了模型在函数级和行级两个粒度上的性能。虽然研究领域是软件安全，但其核心——系统评估和比较不同规模、不同类型的语言模型在复杂、结构化代码数据上的理解和推理能力——与评估化学大模型或质谱结构推理模型在复杂化学数据（如SMILES字符串、质谱图描述）上的性能具有方法论上的高度相似性。论文的评估框架、发现（如LLMs在特定任务上的优势）以及关于模型能力与局限性的分析，对设计和评测化学领域的专用大模型具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Various deep learning-based approaches utilizing pre-trained language models (PLMs) have been proposed for automated vulnerability detection. With recent advancements in large language models (LLMs), several studies have begun exploring their application to vulnerability detection tasks. However, existing studies primarily focus on specific programming languages (e.g., C/C++) and function-level detection, leaving the strengths and weaknesses of PLMs and LLMs in multilingual and multi-granularity scenarios largely unexplored. To bridge this gap, we conduct a comprehensive fine-grained empirical study evaluating the effectiveness of state-of-the-art PLMs and LLMs for multilingual vulnerability detection. Using over 30,000 real-world vulnerability-fixing patches across seven programming languages, we systematically assess model performance at both the function-level and line-level. Our key findings indicate that GPT-4o, enhanced through instruction tuning and few-shot prompting, significantly outperforms all other evaluated models, including CodeT5P. Furthermore, the LLM-based approach demonstrates superior capability in detecting unique multilingual vulnerabilities, particularly excelling in identifying the most dangerous and high-severity vulnerabilities. These results underscore the promising potential of adopting LLMs for multilingual vulnerability detection at function-level and line-level, revealing their complementary strengths and substantial improvements over PLM approaches. This empirical evaluation of PLMs and LLMs for multilingual vulnerability detection highlights LLMs' value in addressing real-world software security challenges.

</details>

---

### 47. [OPENXRD: A Comprehensive Benchmark Framework for LLM/MLLM XRD Question Answering](https://arxiv.org/abs/2507.09155)

**基本信息**

- 🔗 arXiv: [`2507.09155`](https://arxiv.org/abs/2507.09155)
- 👥 作者: Ali Vosoughi, Ayoub Shahnazari, Yufeng Xi 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.09155.pdf)

**💡 相关性分析**

满足标准2和3：论文提出的OPENXRD基准框架，为在科学领域（如化学）构建用于评估大模型专业知识和推理能力的评测数据集、任务和方法提供了直接的、可借鉴的范例（标准2）。同时，该工作本身也包含了对LLMs/MLLMs在科学领域应用现状的重要讨论和评估，属于相关主题的展望性研究（标准3）。

**📖 中文摘要**

本文介绍了OPENXRD，一个用于评估大语言模型（LLMs）和多模态大语言模型（MLLMs）在晶体学问答任务中性能的综合基准框架。该框架专注于衡量模型在推理过程中对固定领域知识（材料科学中的X射线衍射数据）的利用能力。虽然领域是材料科学，但其核心——构建一个包含专家知识、用于评测模型科学领域理解和推理能力的基准——与化学信息学和质谱分析高度相关。该工作为如何构建一个类似的、用于评测化学大模型或质谱结构推理模型在化学领域专业知识和数据上性能的基准，提供了完整的范例和方法论（如上下文同化评估、开放/封闭书测试设计）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce OPENXRD, a comprehensive benchmarking framework for evaluating large language models (LLMs) and multimodal LLMs (MLLMs) in crystallography question answering. The framework measures context assimilation, or how models use fixed, domain-specific supporting information during inference. The framework includes 217 expert-curated X-ray diffraction (XRD) questions covering fundamental to advanced crystallographic concepts, each evaluated under closed-book (without context) and open-book (with context) conditions, where the latter includes concise reference passages generated by GPT-4.5 and refined by crystallography experts. We benchmark 74 state-of-the-art LLMs and MLLMs, including GPT-4, GPT-5, O-series, LLaVA, LLaMA, QWEN, Mistral, and Gemini families, to quantify how different architectures and scales assimilate external knowledge. Results show that mid-sized models (7B--70B parameters) gain the most from contextual materials, while very large models often show saturation or interference and the largest relative gains appear in small and mid-sized models. Expert-reviewed materials provide significantly higher improvements than AI-generated ones even when token counts are matched, confirming that content quality, not quantity, drives performance. OPENXRD offers a reproducible diagnostic benchmark for assessing reasoning, knowledge integration, and guidance sensitivity in scientific domains, and provides a foundation for future multimodal and retrieval-augmented crystallography systems.

</details>

---

### 48. [Improving Large Vision-Language Models' Understanding for Flow Field Data](https://arxiv.org/abs/2507.18311)

**基本信息**

- 🔗 arXiv: [`2507.18311`](https://arxiv.org/abs/2507.18311)
- 👥 作者: Xiaomei Zhang, Hanyu Zheng, Xiangyu Zhu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.18311.pdf)

**💡 相关性分析**

满足标准1：论文提出的FieldLVLM框架，其研究内容直接围绕如何使大模型适应和理解科学领域特定的复杂数据（场数据），这与使化学大模型或质谱结构推理模型适应和理解质谱图、分子图等化学数据的核心主题高度一致，提供了直接相关的技术方案。

**📖 中文摘要**

本文提出了FieldLVLM框架，旨在提升大视觉-语言模型（LVLMs）对科学领域复杂场数据（如流场数据）的理解能力。该框架通过领域感知的语言生成策略和数据压缩的多模态模型调优，将物理特征转化为结构化文本描述，并指导模型学习。虽然应用场景是流体力学，但其核心挑战——让通用大模型理解和推理高度结构化、领域特定的科学数据——与让化学大模型或质谱结构推理模型理解质谱图、分子结构图等科学数据完全同构。论文提出的方法（从数据中提取关键特征并转化为可理解的文本描述）为解决化学领域类似问题提供了直接的技术路线参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Vision-Language Models (LVLMs) have shown impressive capabilities across a range of tasks that integrate visual and textual understanding, such as image captioning and visual question answering. These models are trained on large-scale image and video datasets paired with text, enabling them to bridge visual perception and natural language processing. However, their application to scientific domains, especially in interpreting complex field data commonly used in the natural sciences, remains underexplored. In this work, we introduce FieldLVLM, a novel framework designed to improve large vision-language models' understanding of field data. FieldLVLM consists of two main components: a field-aware language generation strategy and a data-compressed multimodal model tuning. The field-aware language generation strategy leverages a special-purpose machine learning pipeline to extract key physical features from field data, such as flow classification, Reynolds number, and vortex patterns. This information is then converted into structured textual descriptions that serve as a dataset. The data-compressed multimodal model tuning focuses on LVLMs with these generated datasets, using a data compression strategy to reduce the complexity of field inputs and retain only the most informative values. This ensures compatibility with the models language decoder and guides its learning more effectively. Experimental results on newly proposed benchmark datasets demonstrate that FieldLVLM significantly outperforms existing methods in tasks involving scientific field data. Our findings suggest that this approach opens up new possibilities for applying large vision-language models to scientific research, helping bridge the gap between large models and domain-specific discovery.

</details>

---

### 49. [Computational Multi-Agents Society Experiments: Social Modeling Framework Based on Generative Agents](https://arxiv.org/abs/2508.17366)

**基本信息**

- 🔗 arXiv: [`2508.17366`](https://arxiv.org/abs/2508.17366)
- 👥 作者: Hanzhong Zhang, Muhua Huang, Jindong Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.17366.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于生成智能体的计算社会模拟框架，其核心的生成智能体技术是构建能够进行复杂科学推理（包括化学信息学和质谱分析）的AI系统的前沿和基础方法之一，与研究主题间接但明确相关。

**📖 中文摘要**

本文提出了一个用于计算多智能体社会实验的框架CMASE，它集成了基于生成智能体的建模与虚拟人种志方法。虽然其主要应用在社会科学模拟，但其核心组件——生成智能体（Generative Agents）——是构建能够进行复杂推理和交互的AI智能体的前沿技术。在化学信息学背景下，生成智能体技术可用于构建虚拟的“化学家”智能体，这些智能体可以阅读文献、提出假设、设计实验（包括质谱分析）并进行推理，从而推动自动化科学发现。因此，该论文提出的智能体框架与构建能够进行化学研究和质谱结构推理的AI系统在技术基础上相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper introduces CMASE, a framework for Computational Multi-Agent Society Experiments that integrates generative agent-based modeling with virtual ethnographic methods to support researcher embedding, interactive participation, and mechanism-oriented intervention in virtual social environments. By transforming the simulation into a simulated ethnographic field, CMASE shifts the researcher from an external operator to an embedded participant. Specifically, the framework is designed to achieve three core capabilities: (1) enabling real-time human-computer interaction that allows researchers to dynamically embed themselves into the system to characterize complex social intervention processes; (2) reconstructing the generative logic of social phenomena by combining the rigor of computational experiments with the interpretative depth of traditional ethnography; and (3) providing a predictive foundation with causal explanatory power to make forward-looking judgments without sacrificing empirical accuracy. Experimental results show that CMASE can not only simulate complex phenomena, but also generate behavior trajectories consistent with both statistical patterns and mechanistic explanations. These findings demonstrate CMASE's methodological value for intervention modeling, highlighting its potential to advance interdisciplinary integration in the social sciences. The official code is available at: this https URL .

</details>

---

### 50. [When Thinking Backfires: Mechanistic Insights Into Reasoning-Induced Misalignment](https://arxiv.org/abs/2509.00544)

**基本信息**

- 🔗 arXiv: [`2509.00544`](https://arxiv.org/abs/2509.00544)
- 👥 作者: Hanqi Yan, Hainiu Xu, Siya Qi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.00544.pdf)

**💡 相关性分析**

满足标准3：论文对“推理诱导的错位”（RIM）现象进行了深入的机制性研究和讨论。这对于展望和指导未来开发用于化学推理和质谱结构推理等专业领域的、安全可靠的大语言模型具有重要的前瞻性和警示性意义，属于相关主题的重要讨论。

**📖 中文摘要**

本文研究并揭示了大型语言模型（LLMs）中一个令人担忧的现象：推理诱导的错位（RIM），即当模型的推理能力（特别是特定推理模式）在训练或推理中被加强时，可能会导致模型的安全对齐性下降。论文通过表征分析提供了对这一现象起源的机制性解释。这项研究对于任何计划开发或微调用于专业领域（如化学信息学、质谱分析）的LLMs都具有至关重要的警示意义。它指出，在通过思维链（CoT）等技术增强模型在化学推理或结构解析方面的能力时，必须谨慎评估其对模型安全性和对齐性的潜在影响，并需要设计相应的机制来缓解RIM风险。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the growing accessibility and wide adoption of large language models, concerns about their safety and alignment with human values have become paramount. In this paper, we identify a concerning phenomenon: Reasoning-Induced Misalignment (RIM), in which misalignment emerges when reasoning capabilities strengthened-particularly when specific types of reasoning patterns are introduced during inference or training. Beyond reporting this vulnerability, we provide the first mechanistic account of its origins. Through representation analysis, we discover that specific attention heads facilitate refusal by reducing their attention to CoT tokens, a mechanism that modulates the model's rationalization process during inference. During training, we find significantly higher activation entanglement between reasoning and safety in safety-critical neurons than in control neurons, particularly after fine-tuning with those identified reasoning patterns. This entanglement strongly correlates with catastrophic forgetting, providing a neuron-level explanation for RIM.

</details>

---

### 51. [Does Scientific Writing Converge to U.S. English? Evidence from Generative AI-Assisted Publications](https://arxiv.org/abs/2511.11687)

**基本信息**

- 🔗 arXiv: [`2511.11687`](https://arxiv.org/abs/2511.11687)
- 👥 作者: Dragan Filimonovic, Christian Rutzer, Jeffrey Macher 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.11687.pdf)

**💡 相关性分析**

满足标准3：论文虽然不是直接关于化学信息学或质谱分析，但其核心研究内容是生成式人工智能（GenAI）对科学写作的影响。鉴于'化学大模型'是生成式AI在化学领域的具体应用，本文对GenAI在科学领域（包括化学）应用所带来的宏观影响、趋势和潜在问题（如语言趋同与多样性）进行了重要的相关讨论，属于对相关主题的展望性分析。

**📖 中文摘要**

本文研究了生成式人工智能（GenAI）对科学写作风格的影响，特别是它是否会导致非英语母语国家作者的写作风格向占主导地位的美国科学英语趋同。研究分析了2021年至2024年间Scopus索引的565万篇英文科学文章，采用事件研究双重差分法，以ChatGPT发布为时间节点。研究发现，来自非英语国家的、使用GenAI辅助的出版物，其语言风格显著地向美国科学英语趋同，这种效应在语言上与英语差异较大的国家、国内作者团队以及较低影响力期刊的文章中尤为明显。该研究为理解AI工具如何改变全球科学交流的语言格局提供了实证证据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A growing literature documents that generative artificial intelligence (GenAI) is changing scientific writing, yet most studies focus on absolute changes in vocabulary or readability. An important question remains unanswered: Does GenAI use lead to systematic convergence, or a narrowing of stylistic gaps relative to the dominant form of scientific English? Unlike absolute changes, convergence signals whether language-related publication barriers are declining and suggests broader implications for participation and competition in global science. This study directly addresses this question using 5.65 million English-language scientific articles published from 2021 to 2024 and indexed in Scopus. We measure linguistic similarity to a U.S. benchmark corpus using SciBERT text embeddings, and estimate dynamic changes using an event-study difference-in-differences design with repeated cross-sections centered on the late-2022 release of ChatGPT. We find that GenAI-assisted publications from non-English-speaking countries exhibit statistically significant and increasing convergence toward U.S. scientific English, relative to non-GenAI-assisted publications from these countries. This effect is strongest for domestic author teams from countries more linguistically distant from English and for articles published in lower-impact journals -- precisely the contexts where language barriers have historically been most consequential. The results suggest that GenAI tools are reducing language-related barriers in scientific publications. Whether this represents genuine inclusion or a deepening dependence on a single linguistic standard remains an open question.

</details>

---

### 52. [TSFM in-context learning for time-series classification of bearing-health status](https://arxiv.org/abs/2511.15447)

**基本信息**

- 🔗 arXiv: [`2511.15447`](https://arxiv.org/abs/2511.15447)
- 👥 作者: Michel Tokic, Slobodan Djukanović, Anja von Beuningen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.15447.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于时间序列基础模型（TSFM）的上下文学习方法用于时间序列分类。'化学大模型'可以视为基础模型在化学领域的一个子类或具体应用。本文提出的方法论（利用基础模型进行特定领域的预测任务，而无需额外训练）与化学信息学中利用预训练大模型进行分子性质预测、光谱分析等任务的思路高度相关，为核心主题'化学大模型'的应用范式提供了可借鉴的技术路径。

**📖 中文摘要**

本文提出了一种基于时间序列基础模型（TSFM）上下文学习（in-context learning）的分类方法，用于轴承健康状态评估，而无需对基础模型进行微调或训练传统的分类模型。该方法将示例（包括类别标签和数据矩阵）构建为TSFM提示的一部分，通过上下文学习对未知数据模式进行分类。作者将这种方法应用于伺服压力机电机轴承的振动数据，以评估其健康状态。该方法将频域参考信号转换为伪时间序列模式，生成对齐的协变量和目标信号，并利用TSFM预测预定义标签的类别归属概率。该方法利用了预训练模型的可扩展性，在不同操作条件下均表现出有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a classification method based on in-context learning using time-series foundation models (TSFMs). We demonstrate how data not included in the TSFM training can be classified without fine-tuning the foundation model or training a traditional classification model. Examples are represented as targets (class labels) and covariates (data matrices) within the TSFM prompt, enabling the classification of unknown covariate data patterns alongside the forecast horizon through in-context learning. We apply this method to vibration data to assess the health state of a bearing within a servo-press motor. The method transforms frequency-domain reference signals into pseudo time-series patterns, generates aligned covariate and target signals, and uses the TSFM to predict class-membership probabilities for predefined labels. Leveraging the scalability of pre-trained models, the proposed method demonstrates effectiveness across varying operational conditions. This represents significant progress beyond traditional, custom AI solutions towards broader AI-driven maintenance systems that could potentially be provided as Model- or Software-as-a-Service applications.

</details>

---

### 53. [Research and Prototyping Study of an LLM-Based Chatbot for Electromagnetic Simulations](https://arxiv.org/abs/2511.17680)

**基本信息**

- 🔗 arXiv: [`2511.17680`](https://arxiv.org/abs/2511.17680)
- 👥 作者: Albert Piwonski, Mirsad Hadžiefendić
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.17680.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大语言模型（LLM）的聊天机器人，用于自动化科学计算（电磁仿真）任务的设置和求解流程。这直接体现了'化学大模型'的核心思想——即利用大型生成式模型来辅助或自动化化学、材料、物理等领域的复杂科学计算与模拟任务。本文为LLM驱动科学计算提供了一个具体案例，与化学信息学中利用AI自动化计算化学工作流的研究主题高度相关。

**📖 中文摘要**

本研究探讨了如何利用生成式人工智能减少电磁仿真模型的设置时间。论文提出了一个基于大语言模型（Google Gemini 2.0 Flash）的聊天机器人，能够自动生成和求解二维有限元涡流模型。工作流程由Python协调，实现了聊天机器人、几何建模工具Gmsh和求解器GetDP之间的自动交互。研究考虑了具有可变位置和数量的圆形截面导体几何形状。此外，用户还可以定义自定义的后处理例程，并获得模型信息和仿真结果的简明摘要。每个功能增强都包含了相应的架构修改和案例研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work addresses the question of how generative artificial intelligence can be used to reduce the time required to set up electromagnetic simulation models. A chatbot based on a large language model is presented, enabling the automated generation of simulation models with various functional enhancements. A chatbot-driven workflow based on the large language model Google Gemini 2.0 Flash automatically generates and solves two-dimensional finite element eddy current models using Gmsh and GetDP. Python is used to coordinate and automate interactions between the workflow components. The study considers conductor geometries with circular cross-sections of variable position and number. Additionally, users can define custom post-processing routines and receive a concise summary of model information and simulation results. Each functional enhancement includes the corresponding architectural modifications and illustrative case studies.

</details>

---

### 54. [Small Language Models for Efficient Agentic Tool Calling: Outperforming Large Models with Targeted Fine-tuning](https://arxiv.org/abs/2512.15943)

**基本信息**

- 🔗 arXiv: [`2512.15943`](https://arxiv.org/abs/2512.15943)
- 👥 作者: Polaris Jhandi, Owais Kazi, Shreyas Subramanian 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.15943.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是探索和验证小型语言模型（SLM）在特定任务（工具调用）上替代大型模型的可行性，这直接关系到'化学大模型'的实用化部署策略（例如，是否可能为特定的质谱解析任务训练一个高效的专用小模型）。同时，论文对模型成本优化、运营效率以及AI可持续性和可访问性的讨论，属于对相关主题（大模型的应用与部署）的重要展望和讨论。

**📖 中文摘要**

本文研究了在工具调用任务中用小型语言模型（SLM）替代大型语言模型（LLMs）的可行性，以优化生成式AI的部署成本和运营效率。作者对facebook/opt-350m模型进行了监督微调（SFT），使其能够执行文档摘要、查询回答和结构化数据解释等代表性任务。实验结果表明，微调后的SLM在ToolBench评估中取得了77.55%的通过率，显著超过了包括ChatGPT-CoT、ToolLLaMA-DFS等在内的所有基线模型。这些发现表明，经过精心设计和针对性训练的SLM可以显著降低生成式AI的采用门槛，实现经济高效的大规模生产系统集成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As organizations scale adoption of generative AI, model cost optimization and operational efficiency have emerged as critical factors determining sustainability and accessibility. While Large Language Models (LLMs) demonstrate impressive capabilities across diverse tasks, their extensive computational requirements make them cost-prohibitive for routine enterprise use. This limitation motivates the exploration of Small Language Models (SLMs), which can deliver comparable performance in targeted applications while drastically reducing infrastructure overhead (Irugalbandara et al., 2023). In this work, we investigate the feasibility of replacing LLM-driven workflows with optimized SLMs. We trained a domain-adapted SLM to execute representative tasks traditionally handled by LLMs, such as document summarization, query answering, and structured data interpretation. As part of the experiment, we investigated the fine-tuning of facebook/opt-350m model (single epoch only) using the Hugging Face TRL (Transformer Reinforcement Learning), specifically the Supervised Fine-Tuning (SFT) trainer. The OPT-350M model was released by Meta AI in 2022 as part of the OPT (Open Pretrained Transformer) family of models. Similar studies demonstrate that even models at the 350M parameter scale can meaningfully contribute to instruction-tuning pipelines (Mekala et al., 2024). Experimental results demonstrated that our fine-tuned SLM achieves exceptional performance with a 77.55\% pass rate on ToolBench evaluation, significantly outperforming all baseline models including ChatGPT-CoT (26.00\%), ToolLLaMA-DFS (30.18\%), and ToolLLaMA-CoT (16.27\%). These findings emphasize that thoughtful design and targeted training of SLMs can significantly lower barriers to adoption, enabling cost-effective, large-scale integration of generative AI into production systems.

</details>

---

### 55. [CovertComBench: A First Domain-Specific Testbed for LLMs in Wireless Covert Communication](https://arxiv.org/abs/2601.18315)

**基本信息**

- 🔗 arXiv: [`2601.18315`](https://arxiv.org/abs/2601.18315)
- 👥 作者: Zhaozhi Liu, Jiaxin Chen, Yuanai Xie 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18315.pdf)

**💡 相关性分析**

满足标准3：论文虽然主题是无线通信，但其核心是系统地评估大语言模型在解决特定领域（此处为通信）复杂、受约束的优化问题时的能力与局限。这种评估框架、发现的问题（如模型在数学推导上的短板）以及提出的未来研究方向（如外部工具增强），对于评估'化学大模型'或'质谱结构推理'模型在解决化学领域类似复杂问题（如受物理化学约束的分子生成或谱图解析）时的潜力和挑战，具有重要的参考价值和前瞻性讨论意义。

**📖 中文摘要**

本文介绍了CovertComBench，这是首个用于评估大语言模型在无线隐蔽通信中能力的领域特定测试平台。隐蔽通信需要在严格的检测理论约束（如KL散度限制）下优化传输效用，这与传统的吞吐量最大化有本质不同。该基准旨在全面评估LLM在整个隐蔽通信流程中的能力，包括概念理解、优化推导和代码生成。作者对多个先进模型进行了广泛评估，发现LLM在概念识别和代码实现上准确率很高，但在保障安全所需的高阶数学推导方面表现有限（18%至55%）。这表明当前LLM更适合作为实现助手，而非安全约束优化问题的自主求解器。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) into wireless networks presents significant potential for automating system design. However, unlike conventional throughput maximization, Covert Communication (CC) requires optimizing transmission utility under strict detection-theoretic constraints, such as Kullback-Leibler divergence limits. Existing benchmarks primarily focus on general reasoning or standard communication tasks and do not adequately evaluate the ability of LLMs to satisfy these rigorous security constraints. To address this limitation, we introduce CovertComBench, a unified benchmark designed to assess LLM capabilities across the CC pipeline, encompassing conceptual understanding (MCQs), optimization derivation (ODQs), and code generation (CGQs). Furthermore, we analyze the reliability of automated scoring within a detection-theoretic ``LLM-as-Judge'' framework. Extensive evaluations across state-of-the-art models reveal a significant performance discrepancy. While LLMs achieve high accuracy in conceptual identification (81%) and code implementation (83%), their performance in the higher-order mathematical derivations necessary for security guarantees ranges between 18% and 55%. This limitation indicates that current LLMs serve better as implementation assistants rather than autonomous solvers for security-constrained optimization. These findings suggest that future research should focus on external tool augmentation to build trustworthy wireless AI systems.

</details>

---

### 56. [MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching](https://arxiv.org/abs/2602.16020)

**基本信息**

- 🔗 arXiv: [`2602.16020`](https://arxiv.org/abs/2602.16020)
- 👥 作者: Cheng Zeng, Harry W. Sullivan, Thomas Egg 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.16020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于分子晶体结构预测的生成模型（MolCrystalFlow）。分子晶体结构预测是化学信息学和计算化学的核心问题，而生成模型是构建化学大模型（用于结构生成和推理）的关键技术之一。因此，该论文直接与‘化学大模型’主题相关。

**📖 中文摘要**

本文提出了MolCrystalFlow，一个基于流匹配的生成模型，用于分子晶体结构预测。分子晶体结构预测是计算化学中的一个重大挑战，涉及大分子和复杂的分子内与分子间相互作用。该工作将生成建模扩展到完全周期性的分子晶体，通过将分子作为刚体嵌入，并联合学习晶格矩阵、分子取向和质心位置。质心和取向在其原生黎曼流形上表示，允许构建测地线流和尊重几何对称性的图神经网络操作。作者在开源分子晶体数据集上对模型进行了基准测试，结果表明其性能优于最先进的生成模型（MOFFlow），并与基于规则的结构生成方法（Genarris）性能相当。此外，该工作展示了将MolCrystalFlow模型与通用机器学习势能集成以加速分子晶体结构预测的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular crystal structure prediction represents a grand challenge in computational chemistry due to large sizes of constituent molecules and complex intra- and intermolecular interactions. While generative modeling has revolutionized structure discovery for molecules, inorganic solids, and metal-organic frameworks, extending such approaches to fully periodic molecular crystals is still elusive. Here, we present MolCrystalFlow, a flow-based generative model for molecular crystal structure prediction. The framework disentangles intramolecular complexity from intermolecular packing by embedding molecules as rigid bodies and jointly learning the lattice matrix, molecular orientations, and centroid positions. Centroids and orientations are represented on their native Riemannian manifolds, allowing geodesic flow construction and graph neural network operations that respects geometric symmetries. We benchmark our model against a state-of-the-art generative model (MOFFlow) for large-size periodic crystals and a rule-based structure generation method (Genarris) on two open-source molecular crystal datasets. MolCrystalFlow outperforms MOFFlow while achieving competitive performance against Genarris. We also demonstrate an integration of MolCrystalFlow model with universal machine learning potential to accelerate molecular crystal structure prediction, paving the way for data-driven generative discovery of molecular crystals.

</details>

---

### 57. [LLM-Grounded Explainable AI for Supply Chain Risk Early Warning via Temporal Graph Attention Networks](https://arxiv.org/abs/2603.04818)

**基本信息**

- 🔗 arXiv: [`2603.04818`](https://arxiv.org/abs/2603.04818)
- 👥 作者: Zhiming Xue, Yujue Wang, Menghao Huo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04818.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及将大语言模型（LLM）与图神经网络结合，用于结构化推理和解释生成。LLM是构建化学大模型的核心技术基础，而论文中探讨的LLM与结构化知识（如时空图）结合进行推理的模式，与‘化学大模型’主题中模型如何整合领域知识进行复杂推理（如质谱结构推理）的研究方向高度相关。

**📖 中文摘要**

本文提出了一个基于证据的框架，用于供应链风险早期预警和可解释的自然语言风险解释。该框架将时间图注意力网络（TGAT）与结构化大语言模型（LLM）推理模块相结合。以全球供应链节点（如海运枢纽）为案例研究，从自动识别系统（AIS）广播数据构建每日空间图，并通过基于注意力的消息传递建模节点间交互。TGAT预测器捕获时空风险动态，而模型内部证据（包括特征z分数和注意力派生的邻居影响）被转化为结构化提示，以约束LLM的推理过程，使其基于可验证的模型输出。该框架旨在实现可解释和可审计的风险报告，同时不牺牲预测性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Disruptions at critical logistics nodes pose severe risks to global supply chains, yet existing risk prediction systems typically prioritize forecasting accuracy without providing operationally interpretable early warnings. This paper proposes an evidence-grounded framework that jointly performs supply chain bottleneck prediction and faithful natural-language risk explanation by coupling a Temporal Graph Attention Network (TGAT) with a structured large language model (LLM) reasoning module. Using maritime hubs as a representative case study for global supply chain nodes, daily spatial graphs are constructed from Automatic Identification System (AIS) broadcasts, where inter-node interactions are modeled through attention-based message passing. The TGAT predictor captures spatiotemporal risk dynamics, while model-internal evidence -- including feature z-scores and attention-derived neighbor influence -- is transformed into structured prompts that constrain LLM reasoning to verifiable model outputs. To evaluate explanatory reliability, we introduce a directional-consistency validation protocol that quantitatively measures agreement between generated risk narratives and underlying statistical evidence. Experiments on six months of real-world logistics data demonstrate that the proposed framework outperforms baseline models, achieving a test AUC of 0.761, AP of 0.344, and recall of 0.504 under a strict chronological split while producing early warning explanations with 99.6\% directional consistency. Results show that grounding LLM generation in graph-model evidence enables interpretable and auditable risk reporting without sacrificing predictive performance. The framework provides a practical pathway toward operationally deployable explainable AI for supply chain risk early warning and resilience management.

</details>

---

### 58. [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488)

**基本信息**

- 🔗 arXiv: [`2603.05488`](https://arxiv.org/abs/2603.05488)
- 👥 作者: Siddharth Boppana, Annabel Ma, Max Loeffler 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05488.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和理解大语言模型（LLM）在思维链推理过程中的内部机制和可信度。这对于构建可靠、可解释的化学大模型（例如，用于质谱解析时提供可信的推理步骤）至关重要。研究如何检测和避免模型的“表演性”输出，直接关系到化学大模型在科学推理任务中的实用性和可靠性。

**📖 中文摘要**

本文提供了推理模型中存在“表演性思维链”的证据，即模型对其最终答案变得高度自信，但继续生成令牌而不揭示其内部信念。研究通过比较激活探测、早期强制回答和思维链监控等方法，分析了两个大模型（DeepSeek-R1 671B 和 GPT-OSS 120B）在不同难度任务上的表现。研究发现，对于简单的基于回忆的MMLU问题，模型的最终答案可以从思维链早期的激活中解码出来，远早于监控器能够判断的时间。而对于困难的多跳GPQA-Diamond问题，则观察到真正的推理行为。此外，基于探测引导的早期退出可以在保持相似准确性的情况下，显著减少推理令牌数量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We provide evidence of performative chain-of-thought (CoT) in reasoning models, where a model becomes strongly confident in its final answer, but continues generating tokens without revealing its internal belief. Our analysis compares activation probing, early forced answering, and a CoT monitor across two large models (DeepSeek-R1 671B & GPT-OSS 120B) and find task difficulty-specific differences: The model's final answer is decodable from activations far earlier in CoT than a monitor is able to say, especially for easy recall-based MMLU questions. We contrast this with genuine reasoning in difficult multihop GPQA-Diamond questions. Despite this, inflection points (e.g., backtracking, 'aha' moments) occur almost exclusively in responses where probes show large belief shifts, suggesting these behaviors track genuine uncertainty rather than learned "reasoning theater." Finally, probe-guided early exit reduces tokens by up to 80% on MMLU and 30% on GPQA-Diamond with similar accuracy, positioning attention probing as an efficient tool for detecting performative reasoning and enabling adaptive computation.

</details>

---

### 59. [Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/abs/2603.05494)

**基本信息**

- 🔗 arXiv: [`2603.05494`](https://arxiv.org/abs/2603.05494)
- 👥 作者: Helena Casademunt, Bartosz Cywiński, Khoi Tran 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05494.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）的知识引出、诚实性评估和谎言检测。这对于评估和提升化学大模型在专业领域（如质谱结构推理）中输出事实的准确性和可靠性具有直接参考价值。如何确保模型在拥有相关知识时能诚实、准确地回答，是化学大模型部署中的关键问题。

**📖 中文摘要**

本文以经过审查的、会隐瞒政治敏感话题知识的开源大语言模型（如Qwen3）作为自然测试平台，研究秘密知识的引出和谎言检测技术。这些模型经常对特定主题产生虚假回应，但偶尔也能正确回答，表明它们拥有被训练压制的知识。作者评估了一系列引出和检测技术，包括无聊天模板的采样、少样本提示、在通用诚实数据上微调，以及使用模型自我分类或线性探测进行谎言检测。研究发现，最强的引出技术也能迁移到其他前沿开源模型（如DeepSeek R1），但没有一种技术能完全消除错误响应。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

</details>

---

### 60. [Towards Robust Retrieval-Augmented Generation Based on Knowledge Graph: A Comparative Analysis](https://arxiv.org/abs/2603.05698)

**基本信息**

- 🔗 arXiv: [`2603.05698`](https://arxiv.org/abs/2603.05698)
- 👥 作者: Hazem Amamou, Stéphane Gagnon, Alan Davoust 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05698.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和比较基于知识图谱的检索增强生成系统。检索增强生成是构建领域大模型（如化学大模型）以整合外部知识（如质谱数据库、化学知识库）的关键技术。研究其在不同干扰场景下的鲁棒性，直接关系到化学大模型在质谱结构推理等任务中提供准确、可靠信息的能力。

**📖 中文摘要**

本文使用检索增强生成基准（RGB）来评估基于知识图谱的检索增强生成系统（GraphRAG）的鲁棒性。RGB旨在评估RAG系统在噪声、信息整合、负面拒绝和反事实鲁棒性四种场景下的表现。作者比较了RGB的RAG基线与GraphRAG及其三种定制化版本。结果表明，GraphRAG定制化版本相比基线有所改进，并为设计更可靠的现实世界RAG系统提供了见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieval-Augmented Generation (RAG) was introduced to enhance the capabilities of Large Language Models (LLMs) beyond their encoded prior knowledge. This is achieved by providing LLMs with an external source of knowledge, which helps reduce factual hallucinations and enables access to new information not available during pretraining. However, inconsistent retrieved information can negatively affect LLM responses. The Retrieval-Augmented Generation Benchmark (RGB) was introduced to evaluate the robustness of RAG systems under such conditions. In this work, we use the RGB corpus to evaluate LLMs in four scenarios: noise robustness, information integration, negative rejection, and counterfactual robustness. We perform a comparative analysis between the RGB RAG baseline and GraphRAG, a knowledge graph based retrieval system. We test three GraphRAG customizations to improve robustness. Results show improvements over the RGB baseline and provide insights for designing more reliable RAG systems for real world scenarios.

</details>

---

### 61. [Property-driven Protein Inverse Folding With Multi-Objective Preference Alignment](https://arxiv.org/abs/2603.06748)

**基本信息**

- 🔗 arXiv: [`2603.06748`](https://arxiv.org/abs/2603.06748)
- 👥 作者: Xiaoyang Hou, Junqi Liu, Chence Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06748.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质序列设计的AI框架（ProtAlign），该框架基于预训练的逆折叠模型（一种化学/生物大模型），并通过多目标偏好对齐进行优化。蛋白质序列设计和优化是化学信息学和计算生物学的重要应用，直接依赖于化学大模型的能力。因此，该论文与‘化学大模型’主题高度相关。

**📖 中文摘要**

本文介绍了ProtAlign，一个多目标偏好对齐框架，用于微调预训练的蛋白质逆折叠模型，在保持结构保真度的同时满足多种可开发性目标（如溶解度、热稳定性、表达水平）。蛋白质序列设计需要在可设计性（恢复目标骨架的能力）与多个常相互竞争的可开发性属性之间取得平衡。ProtAlign采用半在线直接偏好优化策略，并利用硅学属性预测器构建偏好对。应用于广泛使用的ProteinMPNN骨架，所得模型MoMPNN在包括CATH 4.3晶体结构、从头生成的骨架和真实世界结合剂设计场景在内的任务中，都能在不损害可设计性的情况下增强可开发性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequence design must balance designability, defined as the ability to recover a target backbone, with multiple, often competing, developability properties such as solubility, thermostability, and expression. Existing approaches address these properties through post hoc mutation, inference-time biasing, or retraining on property-specific subsets, yet they are target dependent and demand substantial domain expertise or careful hyperparameter tuning. In this paper, we introduce ProtAlign, a multi-objective preference alignment framework that fine-tunes pretrained inverse folding models to satisfy diverse developability objectives while preserving structural fidelity. ProtAlign employs a semi-online Direct Preference Optimization strategy with a flexible preference margin to mitigate conflicts among competing objectives and constructs preference pairs using in silico property predictors. Applied to the widely used ProteinMPNN backbone, the resulting model MoMPNN enhances developability without compromising designability across tasks including sequence design for CATH 4.3 crystal structures, de novo generated backbones, and real-world binder design scenarios, making it an appealing framework for practical protein sequence design.

</details>

---

### 62. [Deep Expert Injection for Anchoring Retinal VLMs with Domain-Specific Knowledge](https://arxiv.org/abs/2603.07131)

**基本信息**

- 🔗 arXiv: [`2603.07131`](https://arxiv.org/abs/2603.07131)
- 👥 作者: Shuai Lu, Meng Wang, Jia Guo 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07131.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何将领域专家知识有效地注入到大型视觉语言模型中，以提升其在专业领域（眼科）的推理准确性和可靠性。这种将领域知识与大模型结合的技术路径，对于构建面向化学（如质谱分析）的领域大模型具有直接的借鉴意义，特别是在解决模型幻觉、提升专业推理能力方面。

**📖 中文摘要**

本文提出了EyExIn框架，旨在通过深度专家注入机制，将领域专家知识锚定到视网膜视觉语言模型中，以解决其在自动化眼科诊断中因缺乏领域知识而导致的可靠性问题。框架识别了两种结构缺陷：感知差距（通用视觉编码器无法解析细粒度病理线索）和推理差距（稀疏视觉证据在更深层的Transformer中被大量语言先验覆盖，导致无根据的幻觉）。EyExIn采用专家感知的双流编码策略，将视觉表示解耦为用于解剖上下文的一般流和用于病理语义的专用专家流，并通过语义自适应门控融合模块动态整合信息。此外，引入自适应深度专家注入，将融合的视觉特征作为残差偏置直接嵌入到中间LLM层，创建视觉锚点，迫使推理栈严格基于视觉证据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Vision Language Models (LVLMs) show immense potential for automated ophthalmic diagnosis. However, their clinical deployment is severely hindered by lacking domain-specific knowledge. In this work, we identify two structural deficiencies hindering reliable medical reasoning: 1) the Perception Gap, where general-purpose visual encoders fail to resolve fine-grained pathological cues (e.g., microaneurysms); and 2) the Reasoning Gap, where sparse visual evidence is progressively overridden by massive language priors in deeper transformer layers, leading to ungrounded hallucinations. To bridge these gaps, we propose EyExIn, a data-efficient framework designed to anchor retinal VLMs with expert knowledge via a Deep Expert Injection mechanism. Our architecture employs an Expert-Aware Dual-Stream encoding strategy that decouples visual representation into a general stream for anatomical context and a specialized expert stream for pathological semantics. To ensure high-fidelity integration, we design a Semantic-Adaptive Gated Fusion module, which dynamically amplifies subtle lesion signals while filtering irrelevant background noise. Furthermore, we introduce Adaptive Deep Expert Injection to embed persistent "Vision Anchors" by integrating fused visual features as residual biases directly into intermediate LLM layers. This mechanism creates a visual shortcut that forces the reasoning stack to remain strictly grounded in visual evidence. Extensive experiments across four benchmarks demonstrate that our model consistently outperforms massive proprietary systems. EyExIn significantly enhances domain-specific knowledge embedding and achieves state-of-the-art precision in ophthalmic visual question answering, advancing the development of trustworthy ophthalmic AI.

</details>

---

### 63. [Class Visualizations and Activation Atlases for Enhancing Interpretability in Deep Learning-Based Computational Pathology](https://arxiv.org/abs/2603.07170)

**基本信息**

- 🔗 arXiv: [`2603.07170`](https://arxiv.org/abs/2603.07170)
- 👥 作者: Marco Gustav, Fabian Wolf, Christina Glasner 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07170.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和提升基于Transformer的深度学习模型（在计算病理学中）的可解释性。可解释性是化学大模型和质谱结构推理模型可信部署的关键要求。论文中系统评估的特征可视化方法（如类别可视化、激活图谱）为理解化学大模型内部表示、诊断其推理过程提供了重要的方法论参考。

**📖 中文摘要**

本文开发了一个可视化框架，并评估了类别可视化和激活图谱在基于Transformer的计算病理学模型可解释性中的应用。尽管Transformer模型在从H&E全切片图像预测分子和临床生物标志物方面取得了进展，但其可解释性尚未跟上模型复杂性。作者在组织和多器官癌症分类任务上，评估了类别可视化和激活图谱对于基于Transformer的基础模型的表现。通过病理学家对真实和生成图像进行注释，量化观察者间一致性，并辅以归因和相似性度量。研究发现，类别可视化对于形态学不同的组织具有可识别性，但对于重叠的癌症亚类则区分度降低。激活图谱揭示了层依赖的组织结构：粗粒度的组织级概念形成连贯区域，而更细粒度的亚类则表现出分散和重叠。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid adoption of transformer-based models in computational pathology has enabled prediction of molecular and clinical biomarkers from H&E whole-slide images, yet interpretability has not kept pace with model complexity. While attribution- and generative-based methods are common, feature visualization approaches such as class visualizations (CVs) and activation atlases (AAs) have not been systematically evaluated for these models. We developed a visualization framework and assessed CVs and AAs for a transformer-based foundation model across tissue and multi-organ cancer classification tasks with increasing label granularity. Four pathologists annotated real and generated images to quantify inter-observer agreement, complemented by attribution and similarity metrics. CVs preserved recognizability for morphologically distinct tissues but showed reduced separability for overlapping cancer subclasses. In tissue classification, agreement decreased from Fleiss k = 0.75 (scans) to k = 0.31 (CVs), with similar trends in cancer subclass tasks. AAs revealed layer-dependent organization: coarse tissue-level concepts formed coherent regions, whereas finer subclasses exhibited dispersion and overlap. Agreement was moderate for tissue classification (k = 0.58), high for coarse cancer groupings (k = 0.82), and low at subclass level (k = 0.11). Atlas separability closely tracked expert agreement on real images, indicating that representational ambiguity reflects intrinsic pathological complexity. Attribution-based metrics approximated expert variability in low-complexity settings, whereas perceptual and distributional metrics showed limited alignment. Overall, concept-level feature visualization reveals structured morphological manifolds in transformer-based pathology models and provides a framework for expert-centered interrogation of learned representations across label granularities.

</details>

---

### 64. [High-Fidelity Medical Shape Generation via Skeletal Latent Diffusion](https://arxiv.org/abs/2603.07504)

**基本信息**

- 🔗 arXiv: [`2603.07504`](https://arxiv.org/abs/2603.07504)
- 👥 作者: Guoqing Zhang, Jingyun Yang, Siqi Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07504.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于生成复杂三维解剖形状的生成模型框架。该框架基于扩散模型和隐式神经表示，属于生成式AI在科学计算（包括化学和材料科学）中的重要应用。生成模型是构建化学大模型（用于分子、材料结构生成）的核心组成部分，因此该论文与‘化学大模型’主题相关。

**📖 中文摘要**

本文提出了一个骨骼潜在扩散框架，用于高效、高保真度的医学形状生成。解剖形状建模是医学数据分析中的一个基本问题，但解剖结构的几何复杂性和拓扑可变性对准确的形状生成提出了重大挑战。该工作引入了一个形状自动编码器，其中编码器通过可微分骨架化模块捕获全局几何信息，并将局部表面特征聚合为形状潜在表示；解码器则在稀疏采样的坐标上预测相应的隐式场。新形状通过潜在空间扩散模型生成，随后进行神经隐式解码和网格提取。为了解决医学形状数据有限的问题，作者构建了一个大规模数据集MedSDF，包含多个解剖类别的表面点云和对应的有符号距离场。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Anatomy shape modeling is a fundamental problem in medical data analysis. However, the geometric complexity and topological variability of anatomical structures pose significant challenges to accurate anatomical shape generation. In this work, we propose a skeletal latent diffusion framework that explicitly incorporates structural priors for efficient and high-fidelity medical shape generation. We introduce a shape auto-encoder in which the encoder captures global geometric information through a differentiable skeletonization module and aggregates local surface features into shape latents, while the decoder predicts the corresponding implicit fields over sparsely sampled coordinates. New shapes are generated via a latent-space diffusion model, followed by neural implicit decoding and mesh extraction. To address the limited availability of medical shape data, we construct a large-scale dataset, \textit{MedSDF}, comprising surface point clouds and corresponding signed distance fields across multiple anatomical categories. Extensive experiments on MedSDF and vessel datasets demonstrate that the proposed method achieves superior reconstruction and generation quality while maintaining a higher computational efficiency compared with existing approaches. Code is available at: this https URL .

</details>

---

### 65. [TableMind++: An Uncertainty-Aware Programmatic Agent for Tool-Augmented Table Reasoning](https://arxiv.org/abs/2603.07528)

**基本信息**

- 🔗 arXiv: [`2603.07528`](https://arxiv.org/abs/2603.07528)
- 👥 作者: Mingyue Cheng, Shuo Yu, Chuang Jiang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07528.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于复杂表格推理的、具有不确定性感知能力的AI智能体。该工作涉及大语言模型的规划、执行、反思和不确定性量化，这些能力对于构建能够进行复杂科学推理（如质谱数据解析）的化学大模型至关重要。论文中解决幻觉和提升可靠性的技术，可直接应用于化学大模型的开发。

**📖 中文摘要**

本文在TableMind（一个基于程序的自主体，用于表格推理）的基础上，提出了TableMind++，引入了一个新颖的不确定性感知推理框架以缓解幻觉问题。表格推理要求模型同时执行语义理解和精确的数值操作。TableMind++通过记忆引导的计划修剪来检索历史轨迹以验证和过滤逻辑有缺陷的计划（解决认知不确定性），通过基于置信度的动作细化来监控令牌级概率以检测和自纠正语法噪声（解决偶然不确定性），并采用双重加权的轨迹聚合来从多个推理路径中合成稳健的共识。在多样化基准测试上的实验表明，TableMind++持续优于之前的基线模型和专有模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Table reasoning requires models to jointly perform semantic understanding and precise numerical operations. Most existing methods rely on a single-turn reasoning paradigm over tables which suffers from context overflow and weak numerical sensitivity. To address these limitations, we previously proposed TableMind as a tuning-based autonomous programmatic agent that simulates human-like interaction within a lightweight large language model (LLM). TableMind internalizes planning, action, and reflection through a two-stage training strategy involving supervised fine-tuning (SFT) on filtered high-quality data and reinforcement learning (RL) via a multi-perspective reward and the Rank-Aware Policy Optimization (RAPO) algorithm. While TableMind establishes a solid foundation for programmatic agents, the inherent stochasticity of LLMs remains a critical challenge that leads to hallucinations. In this paper, we extend this foundation to TableMind++ by introducing a novel uncertainty-aware inference framework to mitigate hallucinations. Specifically, we propose memory-guided plan pruning to retrieve historical trajectories for validating and filtering out logically flawed plans to address epistemic uncertainty. To ensure execution precision, we introduce confidence-based action refinement which monitors token-level probabilities to detect and self-correct syntactic noise for aleatoric uncertainty mitigation. Finally, we employ dual-weighted trajectory aggregation to synthesize a robust consensus from multiple reasoning paths. Extensive experiments on diverse benchmarks demonstrate that TableMind++ consistently outperforms previous baselines and proprietary models to validate the effectiveness of integrating autonomous training with uncertainty quantification. Our code is available.

</details>

---

### 66. [Designing probabilistic AI monsoon forecasts to inform agricultural decision-making](https://arxiv.org/abs/2603.07893)

**基本信息**

- 🔗 arXiv: [`2603.07893`](https://arxiv.org/abs/2603.07893)
- 👥 作者: Colin Aitken, Rajat Masiwal, Adam Marchakitus 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07893.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于季风预报的、结合了AI天气预测模型和统计模型的概率性AI系统。虽然应用领域是气象和农业，但其核心——构建用于复杂系统预测和决策支持的AI模型、处理不确定性、以及将模型输出与用户决策框架结合——与构建用于化学预测和推理的“化学大模型”在方法论上高度相似。例如，质谱结构推理同样需要处理不确定性并将模型输出转化为化学家的决策依据。

**📖 中文摘要**

本文引入了一个决策理论框架，用于在预报员无法规定最优行动（因为农民的情况各异）的情况下设计有用的天气预报。并将该框架应用于季风降雨季节性开始日期的预测案例，这是许多热带国家种植决策和农业投资的关键日期。作者开发了一个预报系统，通过将系统基准化的人工智能天气预测模型与一个新的“演化农民期望”统计模型相结合，来定制符合该框架要求的预报。该统计模型应用贝叶斯推断于历史观测数据，以预测整个季节内首次发生事件的时间变化概率。混合系统在更长预见期上产生了比其组件或任何多模型平均更准确的印度季风预报。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hundreds of millions of farmers make high-stakes decisions under uncertainty about future weather. Forecasts can inform these decisions, but available choices and their risks and benefits vary between farmers. We introduce a decision-theory framework for designing useful forecasts in settings where the forecaster cannot prescribe optimal actions because farmers' circumstances are heterogeneous. We apply this framework to the case of seasonal onset of monsoon rains, a key date for planting decisions and agricultural investments in many tropical countries. We develop a system for tailoring forecasts to the requirements of this framework by blending systematically benchmarked artificial intelligence (AI) weather prediction models with a new "evolving farmer expectations" statistical model. This statistical model applies Bayesian inference to historical observations to predict time-varying probabilities of first-occurrence events throughout a season. The blended system yields more skillful Indian monsoon forecasts at longer lead times than its components or any multi-model average. In 2025, this system was deployed operationally in a government-led program that delivered subseasonal monsoon onset forecasts to 38 million Indian farmers, skillfully predicting that year's early-summer anomalous dry period. This decision-theory framework and blending system offer a pathway for developing climate adaptation tools for large vulnerable populations around the world.

</details>

---

### 67. [Adaptive Loops and Memory in Transformers: Think Harder or Know More?](https://arxiv.org/abs/2603.08391)

**基本信息**

- 🔗 arXiv: [`2603.08391`](https://arxiv.org/abs/2603.08391)
- 👥 作者: Markus Frey, Behzad Shomali, Ali Hamza Bashir 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08391.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和设计新型的Transformer架构（具有自适应循环和记忆机制），以提升模型在数学推理等任务上的性能。架构创新是推动“化学大模型”能力边界（包括复杂数值计算和符号推理，这在质谱结构推理中很重要）的关键驱动力。因此，该论文与改进化学大模型底层架构的研究主题相关。

**📖 中文摘要**

本文研究了同时具有自适应逐层循环（每个Transformer块通过学习的停止机制迭代其隐藏状态）和门控记忆库的Transformer模型。研究发现，循环主要有利于数学推理，而记忆库有助于在常识任务上恢复性能。结合这两种机制产生的模型，在数学基准测试上优于具有相同FLOP但层数多三倍的基线模型。对模型内部的分析揭示了层的专门化：早期层学习最小化循环并稀疏访问记忆，而后期层则更频繁地进行两者。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chain-of-thought (CoT) prompting enables reasoning in language models but requires explicit verbalization of intermediate steps. Looped transformers offer an alternative by iteratively refining representations within hidden states. This parameter efficiency comes at a cost, as looped models lack the storage capacity of deeper models which use unique weights per layer. In this work, we investigate transformer models that feature both adaptive per-layer looping, where each transformer block learns to iterate its hidden state via a learned halting mechanism, and gated memory banks, that provide additional learned storage. We find that looping primarily benefits mathematical reasoning, while memory banks help recover performance on commonsense tasks compared to parameter and FLOP matched models. Combining both mechanisms yields a model that outperforms an iso-FLOP baseline, with three times the number of layers, across math benchmarks. Analysis of model internals reveals layer specialization: early layers learn to loop minimally and access memory sparingly, while later layers do both more heavily.

</details>

---

### 68. [Fanar-Sadiq: A Multi-Agent Architecture for Grounded Islamic QA](https://arxiv.org/abs/2603.08501)

**基本信息**

- 🔗 arXiv: [`2603.08501`](https://arxiv.org/abs/2603.08501)
- 👥 作者: Ummar Abbas, Mourad Ouzzani, Mohamed Y. Eltabakh 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08501.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于特定领域（伊斯兰教）问答的多智能体、检索增强生成系统。该系统深度融合了领域知识库、确定性计算模块和LLM，并强调输出的可验证性和可靠性。这种构建领域专家系统的架构和方法，与构建用于化学领域（如质谱解析）的、可靠且可验证的“化学大模型”或智能体系统，在设计和目标上高度一致。

**📖 中文摘要**

本文提出了Fanar-Sadiq，一个用于基于证据的伊斯兰问答的双语（阿拉伯语/英语）多智能体架构。虽然大语言模型可以流利地回答宗教知识查询，但它们经常产生幻觉和错误归因来源。检索增强生成通过将生成过程基于外部证据来减少一些限制。Fanar-Sadiq将伊斯兰相关查询路由到智能体工具使用架构内的专门模块。系统支持意图感知路由、具有确定性引用规范化和验证跟踪的基于检索的教法答案、带有引用验证的精确经文查找，以及用于逊尼派天课和继承的具有教法学派敏感分支的确定性计算器。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) can answer religious knowledge queries fluently, yet they often hallucinate and misattribute sources, which is especially consequential in Islamic settings where users expect grounding in canonical texts (Qur'an and Hadith) and jurisprudential (fiqh) nuance. Retrieval-augmented generation (RAG) reduces some of these limitations by grounding generation in external evidence. However, a single ``retrieve-then-generate'' pipeline is limited to deal with the diversity of Islamic queries. Users may request verbatim scripture, fatwa-style guidance with citations or rule-constrained computations such as zakat and inheritance that require strict arithmetic and legal invariants. In this work, we present a bilingual (Arabic/English) multi-agent Islamic assistant, called Fanar-Sadiq, which is a core component of the Fanar AI platform. Fanar-Sadiq routes Islamic-related queries to specialized modules within an agentic, tool-using architecture. The system supports intent-aware routing, retrieval-grounded fiqh answers with deterministic citation normalization and verification traces, exact verse lookup with quotation validation, and deterministic calculators for Sunni zakat and inheritance with madhhab-sensitive branching. We evaluate the complete end-to-end system on public Islamic QA benchmarks and demonstrate effectiveness and efficiency. Our system is currently publicly and freely accessible through API and a Web application, and has been accessed $\approx$1.9M times in less than a year.

</details>

---

### 69. [PRISM: Streaming Human Motion Generation with Per-Joint Latent Decomposition](https://arxiv.org/abs/2603.08590)

**基本信息**

- 🔗 arXiv: [`2603.08590`](https://arxiv.org/abs/2603.08590)
- 👥 作者: Zeyu Ling, Qing Shuai, Teng Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08590.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于复杂序列数据（人体运动）生成的统一生成模型框架。该工作涉及潜在空间的结构化设计、条件生成和长序列生成的稳定性，这些是生成模型研究的前沿问题。生成模型是“化学大模型”的重要组成部分（用于分子、反应、光谱生成），因此该论文在生成模型的技术层面与主题相关。

**📖 中文摘要**

本文提出了PRISM，一个用于流式人体运动生成的、具有逐关节潜在分解的模型。文本到运动生成发展迅速，但存在两个挑战：现有运动自编码器将每一帧压缩成单个整体潜在向量，纠缠了轨迹和每个关节的旋转；文本到运动、姿态条件生成和长时程序列合成通常需要单独的模型。PRISM通过两个贡献解决这些挑战：（1）联合因子化的运动潜在空间：每个身体关节占据自己的令牌，形成一个结构化的二维网格，由带有前向运动学监督的因果VAE压缩。（2）无噪声条件注入：每个潜在令牌携带自己的时间步嵌入，允许将条件帧作为干净令牌注入，而其余令牌被去噪。这使得文本到运动和姿态条件生成统一在单个模型中，并直接支持用于流式合成的自回归片段链接。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Text-to-motion generation has advanced rapidly, yet two challenges persist. First, existing motion autoencoders compress each frame into a single monolithic latent vector, entangling trajectory and per-joint rotations in an unstructured representation that downstream generators struggle to model faithfully. Second, text-to-motion, pose-conditioned generation, and long-horizon sequential synthesis typically require separate models or task-specific mechanisms, with autoregressive approaches suffering from severe error accumulation over extended rollouts. We present PRISM, addressing each challenge with a dedicated contribution. (1) A joint-factorized motion latent space: each body joint occupies its own token, forming a structured 2D grid (time joints) compressed by a causal VAE with forward-kinematics supervision. This simple change to the latent space -- without modifying the generator -- substantially improves generation quality, revealing that latent space design has been an underestimated bottleneck. (2) Noise-free condition injection: each latent token carries its own timestep embedding, allowing conditioning frames to be injected as clean tokens (timestep0) while the remaining tokens are denoised. This unifies text-to-motion and pose-conditioned generation in a single model, and directly enables autoregressive segment chaining for streaming synthesis. Self-forcing training further suppresses drift in long rollouts. With these two components, we train a single motion generation foundation model that seamlessly handles text-to-motion, pose-conditioned generation, autoregressive sequential generation, and narrative motion composition, achieving state-of-the-art on HumanML3D, MotionHub, BABEL, and a 50-scenario user study.

</details>

---

### 70. [Molecular Fingerprints Are Strong Models for Peptide Function Prediction](https://arxiv.org/abs/2501.17901)

**基本信息**

- 🔗 arXiv: [`2501.17901`](https://arxiv.org/abs/2501.17901)
- 👥 作者: Jakub Adamczyk, Piotr Ludynia, Wojciech Czech
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.17901.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学信息学中的模型选择问题，探讨了分子指纹（一种经典化学信息学方法）与更复杂的化学大模型（如图神经网络和Transformer）在肽性质预测任务上的对比，挑战了后者在特定任务中的必要性假设。

**📖 中文摘要**

这篇论文研究了分子指纹在肽功能预测中的应用。作者挑战了传统观点，即预测肽性质需要建模长程分子相互作用（这通常需要复杂的图神经网络或预训练Transformer）。他们发现，简单的、领域特定的分子指纹（如ECFP、Topological Torsion和RDKit指纹）结合LightGBM模型，在132个数据集（包括LRGB和其他五个肽基准测试）上实现了最先进的预测精度。尽管这些指纹仅编码短程分子特征，但其性能优于GNN和基于Transformer的方法。这项工作直接与“化学大模型”主题相关，因为它探讨了在化学信息学任务中，复杂大模型（如GNN和Transformer）是否总是必要的，并展示了更简单、可解释且计算量轻的替代方案（分子指纹）的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding peptide properties is often assumed to require modeling long-range molecular interactions, motivating the use of complex graph neural networks and pretrained transformers. Yet, whether such long-range dependencies are essential remains unclear. We investigate if simple, domain-specific molecular fingerprints can capture peptide function without these assumptions. Atomic-level representation aims to provide richer information than purely sequence-based models and better efficiency than structural ones. Across 132 datasets, including LRGB and five other peptide benchmarks, models using count-based ECFP, Topological Torsion, and RDKit fingerprints with LightGBM achieve state-of-the-art accuracy. Despite encoding only short-range molecular features, these models outperform GNNs and transformer-based approaches. Control experiments with sequence shuffling and amino acid counts confirm that fingerprints, though inherently local, suffice for robust peptide property prediction. Our results challenge the presumed necessity of long-range interaction modeling and highlight molecular fingerprints as efficient, interpretable, and computationally lightweight alternatives for peptide prediction.

</details>

---

### 71. [Enhancing Reconstruction Capability of Wavelet Transform Amorphous Radial Distribution Function via Machine Learning Assisted Parameter Tuning](https://arxiv.org/abs/2512.17245)

**基本信息**

- 🔗 arXiv: [`2512.17245`](https://arxiv.org/abs/2512.17245)
- 👥 作者: Deriyan Senjaya, Stephen Ekaputra Limantoro
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.17245.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及化学信息学与材料科学的交叉领域，利用机器学习方法优化一个用于化学/材料结构分析（径向分布函数重建）的物理模型参数，这属于化学信息学中模型与数据驱动的分析范畴。

**📖 中文摘要**

本研究针对非晶态材料结构分析中的挑战，改进了基于小波变换的径向分布函数（WT-RDF）方法。WT-RDF是一个基于物理的框架，用于分析非晶结构，但其振幅精度受限于参数选择。作者提出了一种机器学习辅助的参数优化方法（WT-RDF+），通过可学习参数优化、参数边界和选择性损失函数来增强WT-RDF。WT-RDF+在二元（Ge0.25Se0.75）和三元Agx(Ge0.25Se0.75)100-x体系上，仅使用25%的二元数据集进行训练，就实现了比基准机器学习模型（如RBF和LSTM）更精确的RDF峰重建和整体曲线趋势。这项工作展示了如何将机器学习与传统物理模型（WT-RDF）相结合，以改进对化学体系（非晶材料）的结构表征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding atomic structures is crucial, yet amorphous materials remain challenging due to their irregular and non-periodic nature. The Wavelet Transform Radial Distribution Function (WT-RDF) offers a physics-based framework for analyzing amorphous structures, reliably reconstructing the first and second Radial Distribution Function (RDF) peaks and overall curve trends in both binary (Ge 0.25 Se 0.75) and ternary Ag x(Ge 0.25 Se 0.75)100-x (x = 5, 10, 15, 20, 25) systems. Despite these strengths, WT-RDF shows limitations in amplitude accuracy, which affects quantitative analyses such as coordination numbers. The shortcoming arises from improper parameter (a, b, Kf, C, and {\Lambda})) selection, as the parameters intrinsically represent atomic interactions within amorphous materials. This study addresses the issue by optimizing WT-RDF parameters using a machine learning approach via learnable parameter optimization, parameter bounding, and selective loss, producing the enhanced WT-RDF+ framework. WT-RDF+ improves the precision of peak reconstructions and outperforms benchmark Machine Learning (ML) models, including Radial Basis Function (RBF) and Long Short-term Memory (LSTM), when trained on only 25% of the binary dataset. Specifically, the machine learning benchmarks are defined as regressors with radial distance r input and G(r) output taken from Ab Initio Molecular Dynamics (AIMD) RDF simulation, not the reduced structure factor SR(q) to G(r) inversions. These results demonstrate that WT-RDF+ is a robust and reliable model for RDF reconstruction of Ge-Se and Ag-Ge-Se family.

</details>

---

### 72. [An AI-powered Bayesian Generative Modeling Approach for Arbitrary Conditional Inference](https://arxiv.org/abs/2601.05355)

**基本信息**

- 🔗 arXiv: [`2601.05355`](https://arxiv.org/abs/2601.05355)
- 👥 作者: Qiao Liu, Wing Hung Wong
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.05355.pdf)

**💡 相关性分析**

满足标准1：论文提出的贝叶斯生成建模（BGM）框架是一个通用的、强大的AI生成模型框架，其核心目标（灵活的条件推断与生成）与构建和理解“化学大模型”（用于分子生成、性质预测等需要复杂条件推理的任务）的研究方向直接相关。

**📖 中文摘要**

本文提出了一个名为贝叶斯生成建模（BGM）的统一框架，用于解决任意条件推断问题。BGM通过一个随机迭代贝叶斯更新算法学习变量X的生成模型，该算法会更新模型参数和潜变量直至收敛。一旦训练完成，无需重新训练即可获得任何条件分布。该框架利用现代AI技术捕捉变量间的复杂关系，同时遵循贝叶斯原理，为条件预测提供了带有原则性不确定性量化的通用引擎。虽然论文是通用框架，但其核心思想——开发一个强大的、统一的生成模型来处理复杂数据关系——与构建能够理解和推理化学结构（如分子）的“化学大模型”在理念上高度一致。这类模型需要能够灵活地进行条件生成和推理（例如，给定部分结构生成完整分子，或预测性质），这正是BGM框架旨在解决的问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern data analysis increasingly requires flexible conditional inference P(X_B | X_A) where (X_A, X_B) is an arbitrary partition of observed variable X. Existing approaches are either restricted to a fixed conditioning structure or depend strongly on the distribution of conditioning masks during training. To address these limitations, we introduce Bayesian generative modeling (BGM), a unified framework for arbitrary conditional inference. BGM learns a generative model of X via a stochastic iterative Bayesian updating algorithm in which model parameters and latent variables are updated until convergence. Once trained, any conditional distribution can be obtained without retraining. Empirically, BGM achieves superior predictive performance with posterior predictive intervals, demonstrating that a single learned model can serve as a universal engine for conditional prediction with principled uncertainty quantification. We provide theoretical guarantees for convergence of the stochastic iterative algorithm, statistical consistency, and conditional risk bounds. The proposed BGM framework leverages modern AI to capture complex relationships among variables while adhering to Bayesian principles, offering a promising approach for a wide range of applications in modern data science. Code for BGM is available at this https URL . Document of BGM is available at this https URL .

</details>

---

### 73. [Proceedings Eighth International Conference on Applied Category Theory](https://arxiv.org/abs/2603.07595)

**基本信息**

- 🔗 arXiv: [`2603.07595`](https://arxiv.org/abs/2603.07595)
- 👥 作者: Amar Hadzihasanovic, Jean-Simon Pacaud Lemay
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07595.pdf)

**💡 相关性分析**

满足标准3：作为应用范畴论国际会议的论文集，该文献是相关领域的综述性/展望性资料。鉴于会议范围明确包含化学，该论文集很可能收录了与化学系统建模和分析相关的研究，这些研究可能为“化学大模型”的形式化表示和推理提供数学基础或跨学科视角。

**📖 中文摘要**

这是第八届应用范畴论国际会议的论文集前言。应用范畴论（ACT）是一个跨学科领域，其会议投稿涵盖从纯理论到应用的广泛主题。值得注意的是，会议明确提到了“化学”是贡献领域之一。虽然这篇摘要本身没有具体内容，但它指向的会议论文集很可能包含将范畴论应用于化学系统建模和分析的研究。范畴论为描述复杂系统的组成和关系提供了强大的数学语言，在化学信息学中可用于表示分子结构、反应网络和化学过程。因此，这份会议记录是寻找可能涉及“化学大模型”形式化框架或化学系统数学表示的相关研究的重要资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Eighth International Conference on Applied Category Theory took place at the University of Florida on June 2-6 2025. The conference consisted of 2 plenary invited talks, 28 contributed talks, an online community meeting, a general community meeting, and 4 talks by junior researchers who attended the Adjoint School to present the results of their research at the school. Information regarding the conference may be found at this https URL . Submission to ACT2025 had three tracks: extended abstracts, software demonstrations, and proceedings. Accepted proceedings track submissions are included in this volume. The contributions to ACT2025 ranged from pure to applied and included contributions in a wide range of disciplines. ACT2025 included talks related to computer science, probability theory, chemistry, string diagrams, game semantics, quantum computation, and more.

</details>

---

## 📊 数据统计
- 累计运行天数：23
- 累计论文数量：1734

## 📝 历史记录

> 暂无历史数据

