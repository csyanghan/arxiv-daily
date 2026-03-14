# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-14 12:38:40

## 📅 2026-03-14 (今日最新)

**相关论文数：62**

### 1. [Graph Tokenization for Bridging Graphs and Transformers](https://arxiv.org/abs/2603.11099)

**基本信息**

- 🔗 arXiv: [`2603.11099`](https://arxiv.org/abs/2603.11099)
- 👥 作者: Zeyuan Guo, Enmao Diao, Cheng Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11099.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个通用的图标记化框架，以连接图结构数据和Transformer大模型。这直接与“化学大模型”主题相关，因为化学分子通常用图表示，该工作为解决如何将分子图有效输入化学大模型这一关键问题提供了方法论基础。

**📖 中文摘要**

本文提出了一种用于将图结构数据转换为序列表示的图标记化框架，旨在弥合图与Transformer模型之间的鸿沟。该框架结合了可逆图序列化和字节对编码（BPE），通过图子结构的全局统计信息来指导序列化过程，确保频繁出现的子结构在序列中更常见，从而能被BPE合并为有意义的标记。实验表明，该标记化器使得BERT等Transformer模型无需架构修改即可直接应用于图基准测试，并在14个基准数据集上取得了最先进的结果，经常优于图神经网络和专门的图Transformer。这项工作为化学信息学领域（特别是分子图表示学习）提供了将图数据整合到序列模型生态系统中的通用方法，与“化学大模型”主题相关，因为大模型处理化学结构（通常表示为图）需要有效的图到序列的转换策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of large pretrained Transformers is closely tied to tokenizers, which convert raw input into discrete symbols. Extending these models to graph-structured data remains a significant challenge. In this work, we introduce a graph tokenization framework that generates sequential representations of graphs by combining reversible graph serialization, which preserves graph information, with Byte Pair Encoding (BPE), a widely adopted tokenizer in large language models (LLMs). To better capture structural information, the graph serialization process is guided by global statistics of graph substructures, ensuring that frequently occurring substructures appear more often in the sequence and can be merged by BPE into meaningful tokens. Empirical results demonstrate that the proposed tokenizer enables Transformers such as BERT to be directly applied to graph benchmarks without architectural modifications. The proposed approach achieves state-of-the-art results on 14 benchmark datasets and frequently outperforms both graph neural networks and specialized graph transformers. This work bridges the gap between graph-structured data and the ecosystem of sequence models. Our code is available at \href{ this https URL }{\color{blue}here}.

</details>

---

### 2. [Learning Tree-Based Models with Gradient Descent](https://arxiv.org/abs/2603.11117)

**基本信息**

- 🔗 arXiv: [`2603.11117`](https://arxiv.org/abs/2603.11117)
- 👥 作者: Sascha Marton
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11117.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、可扩展的树模型学习方法，该方法与基于梯度的优化（如深度学习）兼容。这直接与“化学大模型”主题相关，因为树模型和基于梯度的模型（如神经网络）的融合是构建更强大、更可解释的化学预测模型（例如，用于性质预测或反应结果预测的混合模型）的一个重要方向。

**📖 中文摘要**

本文提出了一种通过梯度下降学习硬性、轴对齐决策树的新方法。该方法利用带有直通算子的反向传播在密集的决策树表示上进行优化，从而能够联合优化所有树参数。这解决了传统决策树算法的两个主要限制：1）梯度训练不受局部最优分割顺序选择的约束；2）通过利用梯度下降进行优化，可以无缝集成到现有的机器学习方法中。该方法在多个领域实现了最先进的结果，包括用于小型表格数据集的可解释决策树、用于复杂表格数据的先进模型、多模态学习以及无损的可解释强化学习。这项工作通过弥合决策树和基于梯度的优化之间的差距，显著提高了基于树的模型在各种机器学习领域的性能和适用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tree-based models are widely recognized for their interpretability and have proven effective in various application domains, particularly in high-stakes domains. However, learning decision trees (DTs) poses a significant challenge due to their combinatorial complexity and discrete, non-differentiable nature. As a result, traditional methods such as CART, which rely on greedy search procedures, remain the most widely used approaches. These methods make locally optimal decisions at each node, constraining the search space and often leading to suboptimal tree structures. Additionally, their demand for custom training methods precludes a seamless integration into modern machine learning (ML) approaches. In this thesis, we propose a novel method for learning hard, axis-aligned DTs through gradient descent. Our approach utilizes backpropagation with a straight-through operator on a dense DT representation, enabling the joint optimization of all tree parameters, thereby addressing the two primary limitations of traditional DT algorithms. First, gradient-based training is not constrained by the sequential selection of locally optimal splits but, instead, jointly optimizes all tree parameters. Second, by leveraging gradient descent for optimization, our approach seamlessly integrates into existing ML approaches e.g., for multimodal and reinforcement learning tasks, which inherently rely on gradient descent. These advancements allow us to achieve state-of-the-art results across multiple domains, including interpretable DTs rees for small tabular datasets, advanced models for complex tabular data, multimodal learning, and interpretable reinforcement learning without information loss. By bridging the gap between DTs and gradient-based optimization, our method significantly enhances the performance and applicability of tree-based models across various ML domains.

</details>

---

### 3. [H2LooP Spark Preview: Continual Pretraining of Large Language Models for Low-Level Embedded Systems Code](https://arxiv.org/abs/2603.11139)

**基本信息**

- 🔗 arXiv: [`2603.11139`](https://arxiv.org/abs/2603.11139)
- 👥 作者: Amit Singh, Vedant Nipane, Pulkit Agrawal 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用持续预训练技术，使大型语言模型专门化并精通一个高度专业化的领域（嵌入式系统代码）。这直接体现了“化学大模型”主题的一个关键方面：如何通过领域特定的持续预训练或微调，使通用大模型适应化学信息学等专业领域，以执行诸如代码生成（用于化学模拟）、文献解析或分子设计等任务。

**📖 中文摘要**

本文介绍了H2LooP Spark Preview，这是一个针对嵌入式系统代码领域的持续预训练（CPT）管道。该工作将完全开放的语言模型OLMo-3-7B适配到嵌入式系统领域，使用的训练语料库由仓库-数据手册对构建，涵盖了100B个原始嵌入式系统数据令牌。通过使用高阶LoRA进行持续预训练，模型在领域内困惑度降低了70.4%，在保留仓库困惑度上降低了66.1%。在涵盖13个嵌入式领域的生成式代码完成基准测试中，该7B模型在8个类别上的令牌准确率超过了Claude Opus 4.6和Qwen3-Coder-30B。这表明有针对性的持续预训练使得较小的开放权重模型能够在专业的技术任务上与前沿系统竞争。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) demonstrate strong code generation abilities in general-purpose programming languages but remain limited in specialized domains such as low-level embedded systems programming. This domain involves hardware register manipulation, vendor-specific SDKs, real-time operating system APIs, and hardware abstraction layers that are underrepresented in standard pretraining corpora. We introduce H2LooP Spark Preview, a continual pretraining (CPT) pipeline that adapts the OLMo-3-7B-a fully open language model to the embedded systems domain using BF16 LoRA with rank-stabilized scaling on 8 NVIDIA H100 GPUs. Our training corpus is constructed from repository-datasheet pairs covering 100B tokens of raw embedded systems data across 117 manufacturers, processed using the hierarchical datasheet-to-code mapping approach proposed in SpecMap (Nipane et al., 2026). The resulting curated dataset split contains 23.5B tokens across 13 embedded domains. Continual pretraining with high-rank LoRA (r=512) yields substantial gains, reducing in-domain perplexity by 70.4% and held-out repository perplexity by 66.1%. On generative code completion benchmarks spanning 13 embedded domains, our 7B model outperforms Claude Opus 4.6 and Qwen3-Coder-30B on 8 categories in token accuracy, showing that targeted continual pretraining enables smaller open-weight models to rival frontier systems on specialized technical tasks. We release the production training checkpoint on Huggingface as an open-source artifact.

</details>

---

### 4. [Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models](https://arxiv.org/abs/2603.11149)

**基本信息**

- 🔗 arXiv: [`2603.11149`](https://arxiv.org/abs/2603.11149)
- 👥 作者: Xiangwen Wang, Ananth Balashankar, Varun Chandrasekaran
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11149.pdf)

**💡 相关性分析**

满足标准3：论文是对大型语言模型安全漏洞（越狱攻击）的系统性、前瞻性综述和分析。它包含了对不同攻击范式、缩放行为和安全影响的深入讨论。这与“化学大模型”主题高度相关，因为确保化学领域大模型（例如，用于分子设计或实验规划）的安全性、可靠性和对抗性鲁棒性至关重要，该综述为理解和评估此类模型的安全风险提供了重要的背景和框架。

**📖 中文摘要**

本文对大型语言模型中的越狱攻击进行了系统的缩放分析。研究提出了一个越狱攻击的缩放定律框架，将每次攻击视为计算受限的优化过程，并在共享的FLOPs轴上衡量进展。系统评估涵盖了四种代表性的越狱范式，包括基于优化的攻击、自我优化提示、基于采样的选择和遗传优化，并在多样化的有害目标集上跨越多个模型系列和规模进行测试。研究调查了将攻击者预算与攻击成功分数相关联的缩放定律，并通过将简单的饱和指数函数拟合到FLOPs-成功轨迹来从拟合曲线中得出可比较的效率总结。实证结果表明，基于提示的范式往往比基于优化的方法更具计算效率。此外，攻击占据着不同的成功-隐蔽性操作点，基于提示的方法占据高成功、高隐蔽性区域。最后，研究发现漏洞强烈依赖于目标：涉及错误信息的危害通常比其他非错误信息危害更容易引发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models remain vulnerable to jailbreak attacks, yet we still lack a systematic understanding of how jailbreak success scales with attacker effort across methods, model families, and harm types. We initiate a scaling-law framework for jailbreaks by treating each attack as a compute-bounded optimization procedure and measuring progress on a shared FLOPs axis. Our systematic evaluation spans four representative jailbreak paradigms, covering optimization-based attacks, self-refinement prompting, sampling-based selection, and genetic optimization, across multiple model families and scales on a diverse set of harmful goals. We investigate scaling laws that relate attacker budget to attack success score by fitting a simple saturating exponential function to FLOPs--success trajectories, and we derive comparable efficiency summaries from the fitted curves. Empirically, prompting-based paradigms tend to be the most compute-efficient compared to optimization-based methods. To explain this gap, we cast prompt-based updates into an optimization view and show via a same-state comparison that prompt-based attacks more effectively optimize in prompt space. We also show that attacks occupy distinct success--stealthiness operating points with prompting-based methods occupying the high-success, high-stealth region. Finally, we find that vulnerability is strongly goal-dependent: harms involving misinformation are typically easier to elicit than other non-misinformation harms.

</details>

---

### 5. [Bridging Behavioral Biometrics and Source Code Stylometry: A Survey of Programmer Attribution](https://arxiv.org/abs/2603.11150)

**基本信息**

- 🔗 arXiv: [`2603.11150`](https://arxiv.org/abs/2603.11150)
- 👥 作者: Marek Horvath, Emilia Pietrikova, Diomidis Spinellis
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11150.pdf)

**💡 相关性分析**

满足标准3：论文是对程序员归因领域（与代码风格分析密切相关）的系统性综述和分类。虽然不直接针对化学，但“质谱结构推理”和“化学大模型”中涉及处理和分析化学数据（如质谱、分子结构）的代码、算法和模型。理解代码风格、作者归因以及相关分析技术，对于构建和维护化学信息学领域的软件工具、确保代码质量以及可能的知识产权分析具有潜在价值。该综述提供了该领域的方法论概览。

**📖 中文摘要**

本文对基于源代码分析的程序员归因研究进行了系统的图谱研究。该研究从2012年至2025年间发表的47项研究中，分析了作者身份任务、特征类别、学习与建模方法、数据集来源和评估实践等多个维度。基于此分析，研究推导了一个将风格和行为特征类型与常用机器学习技术相关联的分类法，并提供了该领域出版趋势、基准和编程语言的描述性概述。内容层面的分析突出了该领域的主要主题集群。结果表明，该领域强烈关注使用风格计量学特征的封闭世界作者身份归因，并严重依赖少量基准数据集，而行为信号、作者身份验证和可重复性则探索较少。该研究将现有研究整合到一个统一的框架中，并概述了可以指导未来工作的方法论空白。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Programmer attribution seeks to identify or verify the author of a source code artifact using stylistic, structural, or behavioural characteristics. This problem has been studied across software engineering, security, and digital forensics, resulting in a growing and methodologically diverse set of publications. This paper presents a systematic mapping study of programmer attribution research focused on source code analysis. From an initial set of 135 candidate publications, 47 studies published between 2012 and 2025 were selected through a structured screening process. The included works are analysed along several dimensions, including authorship tasks, feature categories, learning and modelling approaches, dataset sources, and evaluation practices. Based on this analysis, we derive a taxonomy that relates stylistic and behavioural feature types to commonly used machine learning techniques and provide a descriptive overview of publication trends, benchmarks, programming languages. A content-level analysis highlights the main thematic clusters in the field. The results indicate a strong focus on closed-world authorship attribution using stylometric features and a heavy reliance on a small number of benchmark datasets, while behavioural signals, authorship verification, and reproducibility remain less explored. The study consolidates existing research into a unified framework and outlines methodological gaps that can guide future work. This manuscript is currently under review. The present version is a preprint.

</details>

---

### 6. [DeReason: A Difficulty-Aware Curriculum Improves Decoupled SFT-then-RL Training for General Reasoning](https://arxiv.org/abs/2603.11193)

**基本信息**

- 🔗 arXiv: [`2603.11193`](https://arxiv.org/abs/2603.11193)
- 👥 作者: Hanxu Hu, Yuxuan Wang, Maggie Huan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11193.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化大型语言模型在STEM（包括化学）领域复杂推理能力的训练策略，特别是SFT和RL的协同使用。这直接与“化学大模型”主题相关，因为提高模型在化学推理（如反应机理、性质预测、谱图解析）方面的能力是核心目标，而该论文提出的课程学习和数据分配策略为此提供了方法论指导。

**📖 中文摘要**

本文针对通用科学（STEM）领域的推理，提出了DeReason，一种基于难度的数据解耦策略。DeReason通过基于LLM的评分估计推理强度，将训练数据划分为推理密集型和非推理密集型子集。它将广泛覆盖的非推理密集型问题分配给监督微调（SFT）以建立基础领域知识，并保留一部分困难问题用于强化学习（RL）以培养复杂推理。研究表明，这种有原则的解耦比随机分割数据用于顺序SFT和RL能产生更好的性能。在通用STEM和数学基准上的大量实验表明，这种解耦课程训练显著优于仅SFT、仅RL和随机分割基线。这项工作为通用推理中SFT和RL之间的相互作用提供了系统研究，提供了一个高效且通用的后训练方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement learning with Verifiable Rewards (RLVR) has emerged as a powerful paradigm for eliciting reasoning capabilities in large language models, particularly in mathematics and coding. While recent efforts have extended this paradigm to broader general scientific (STEM) domains, the complex interplay between supervised fine-tuning (SFT) and RL in these contexts remains underexplored. In this paper, we conduct controlled experiments revealing a critical challenge: for general STEM domains, RL applied directly to base models is highly sample-inefficient and is consistently surpassed by supervised fine-tuning (SFT) on moderate-quality responses. Yet sequential SFT followed by RL can further improve performance, suggesting that the two stages play complementary roles, and that how training data is allocated between them matters. Therefore, we propose DeReason, a difficulty-based data decoupling strategy for general reasoning. DeReason partitions training data by reasoning intensity estimated via LLM-based scoring into reasoning-intensive and non-reasoning-intensive subsets. It allocates broad-coverage, non-reasoning-intensive problems to SFT to establish foundational domain knowledge, and reserves a focused subset of difficult problems for RL to cultivate complex reasoning. We demonstrate that this principled decoupling yields better performance than randomly splitting the data for sequential SFT and RL. Extensive experiments on general STEM and mathematical benchmarks demonstrate that our decoupled curriculum training significantly outperforms SFT-only, RL-only, and random-split baselines. Our work provides a systematic study of the interplay between SFT and RL for general reasoning, offering a highly effective and generalized post-training recipe.

</details>

---

### 7. [DNS-GT: A Graph-based Transformer Approach to Learn Embeddings of Domain Names from DNS Queries](https://arxiv.org/abs/2603.11200)

**基本信息**

- 🔗 arXiv: [`2603.11200`](https://arxiv.org/abs/2603.11200)
- 👥 作者: Massimiliano Altieri, Ronan Hamon, Roberto Corizzo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11200.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于Transformer的模型，用于从序列数据（DNS查询）中学习表示。虽然应用领域是网络安全，但其核心技术——序列建模、自监督预训练和表示学习——与“化学大模型”和“质谱结构推理”高度相关。例如，质谱数据可以视为峰值序列，分子结构可以表示为SMILES序列或图序列。该论文的方法论（Transformer处理序列以学习有意义的表示）可直接类比或应用于化学序列数据的表示学习。

**📖 中文摘要**

本文提出了DNS-GT，一种基于Transformer的新模型，用于从DNS查询序列中学习域名嵌入。该模型首先以自监督方式进行预训练，以学习DNS活动的一般行为。然后，它可以在特定的下游任务上进行微调，利用给定序列中与其他相关查询的交互。使用真实世界DNS数据的实验展示了该方法学习有效域名表示的能力。在域名分类和僵尸网络检测任务上的定量评估表明，与相关基线相比，我们的方法取得了更好的结果。这项工作为探索用于入侵检测系统的大规模语言模型创造了机会。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Network intrusion detection systems play a crucial role in the security strategy employed by organisations to detect and prevent cyberattacks. Such systems usually combine pattern detection signatures with anomaly detection techniques powered by machine learning methods. However, the commonly proposed machine learning methods present drawbacks such as over-reliance on labeled data and limited generalization capabilities. To address these issues, embedding-based methods have been introduced to learn representations from network data, such as DNS traffic, mainly due to its large availability, that generalise effectively to many downstream tasks. However, current approaches do not properly consider contextual information among DNS queries. In this paper, we tackle this issue by proposing DNS-GT, a novel Transformer-based model that learns embeddings for domain names from sequences of DNS queries. The model is first pre-trained in a self-supervised fashion in order to learn the general behavior of DNS activity. Then, it can be finetuned on specific downstream tasks, exploiting interactions with other relevant queries in a given sequence. Our experiments with real-world DNS data showcase the ability of our method to learn effective domain name representations. A quantitative evaluation on domain name classification and botnet detection tasks shows that our approach achieves better results compared to relevant baselines, creating opportunities for further exploration of large-scale language models for intrusion detection systems. Our code is available at: this https URL .

</details>

---

### 8. [Security-by-Design for LLM-Based Code Generation: Leveraging Internal Representations for Concept-Driven Steering Mechanisms](https://arxiv.org/abs/2603.11212)

**基本信息**

- 🔗 arXiv: [`2603.11212`](https://arxiv.org/abs/2603.11212)
- 👥 作者: Maximilian Wendlinger, Daniel Kowatsch, Konstantin Böttinger 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11212.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是理解和改进代码大语言模型的安全性，通过分析其内部表示并实施概念引导机制。这直接与“化学大模型”主题相关，因为化学领域的大模型（例如，用于生成实验方案、合成路径或分析代码）同样面临生成不安全、不正确或有偏见内容的挑战。该工作为构建更安全、可靠的化学领域专用大模型提供了重要的技术思路（即可解释性和可控性）。

**📖 中文摘要**

本文研究了代码大语言模型（CodeLLMs）内部安全概念的表示，揭示了模型在生成不安全代码时通常意识到漏洞。通过系统评估，研究表明CodeLLMs可以区分安全子概念，从而实现比先前黑盒方法更细粒度的分析。利用这些见解，我们提出了用于CodeLLMs的安全概念引导（SCS-Code）。在令牌生成过程中，SCS-Code将LLMs的内部表示引导向安全和功能性的代码输出，实现了一种轻量级和模块化的机制，可以集成到现有的代码模型中。我们的方法在多个安全编码基准测试中实现了优于最先进方法的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) show remarkable capabilities in understanding natural language and generating complex code. However, as practitioners adopt CodeLLMs for increasingly critical development tasks, research reveals that these models frequently generate functionally correct yet insecure code, posing significant security risks. While multiple approaches have been proposed to improve security in AI-based code generation, combined benchmarks show these methods remain insufficient for practical use, achieving only limited improvements in both functional correctness and security. This stems from a fundamental gap in understanding the internal mechanisms of code generation and the root causes of security vulnerabilities, forcing researchers to rely on heuristics and empirical observations. In this work, we investigate the internal representation of security concepts in CodeLLMs, revealing that models are often aware of vulnerabilities as they generate insecure code. Through systematic evaluation, we demonstrate that CodeLLMs can distinguish between security subconcepts, enabling a more fine-grained analysis than prior black-box approaches. Leveraging these insights, we propose Secure Concept Steering for CodeLLMs (SCS-Code). During token generation, SCS-Code steers LLMs' internal representations toward secure and functional code output, enabling a lightweight and modular mechanism that can be integrated into existing code models. Our approach achieves superior performance compared to state-of-the-art methods across multiple secure coding benchmarks.

</details>

---

### 9. [ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning](https://arxiv.org/abs/2603.11226)

**基本信息**

- 🔗 arXiv: [`2603.11226`](https://arxiv.org/abs/2603.11226)
- 👥 作者: Lingxiao Tang, He Ye, Zhaoyang Chu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11226.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型的代码执行和推理能力，通过结合可验证的、基于执行轨迹的奖励进行强化学习。这与“化学大模型”主题高度相关，因为化学领域的推理（如计算化学模拟、谱图解析算法、反应条件优化）本质上涉及复杂的、多步骤的符号操作和计算过程。提升模型对此类过程的精确推理能力，是构建能够进行可靠化学计算和分析的大模型的关键。

**📖 中文摘要**

本文介绍了ExecVerify，这是一个用于代码执行推理的框架，超越了文本模仿，结合了从执行轨迹中衍生的可验证白盒奖励，包括下一语句预测和变量值/类型预测。我们的工作首先通过基于约束的程序合成构建了一个具有多个难度级别的数据集。然后，我们应用强化学习（RL）来奖励关于中间执行步骤和最终输出的正确答案，使训练目标与每个执行步骤的语义正确性保持一致。最后，我们采用了一个两阶段训练流程，首先增强执行推理能力，然后转移到代码生成。实验表明，使用ExecVerify训练的7B模型在代码推理基准测试中实现了与32B模型相当的性能，并且在代码生成任务上的pass@1比强大的后训练基线提高了5.9%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Code LLMs still struggle with code execution reasoning, especially in smaller models. Existing methods rely on supervised fine-tuning (SFT) with teacher-generated explanations, primarily in two forms: (1) input-output (I/O) prediction chains and (2) natural-language descriptions of execution traces. However, intermediate execution steps cannot be explicitly verified during SFT, so the training objective can reduce to merely matching teacher explanations. Moreover, training data is typically collected without explicit control over task difficulty. We introduce ExecVerify, which goes beyond text imitation by incorporating verifiable white-box rewards derived from execution traces, including next-statement prediction and variable value/type prediction. Our work first builds a dataset with multiple difficulty levels via constraint-based program synthesis. Then, we apply reinforcement learning (RL) to reward correct answers about both intermediate execution steps and final outputs, aligning the training objective with semantic correctness at each execution step. Finally, we adopt a two-stage training pipeline that first enhances execution reasoning and then transfers to code generation. Experiments demonstrate that a 7B model trained with ExecVerify achieves performance comparable to 32B models on code reasoning benchmarks and improves pass@1 by up to 5.9\% on code generation tasks over strong post-training baselines.

</details>

---

### 10. [Differentiable Thermodynamic Phase-Equilibria for Machine Learning](https://arxiv.org/abs/2603.11249)

**基本信息**

- 🔗 arXiv: [`2603.11249`](https://arxiv.org/abs/2603.11249)
- 👥 作者: Karim K. Ben Hicham, Moreno Ascani, Jan G. Rittig 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11249.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种可微分的、保证热力学一致性的机器学习方法，用于相平衡计算。这直接处于“化学信息学”和“化学大模型”的交汇点。它展示了如何将物理原理（热力学）嵌入到机器学习模型中，以解决化学工程和材料科学中的核心问题。这种方法论对于构建能够可靠预测物质相行为、溶解度等性质的“化学大模型”具有重要的示范和参考价值。

**📖 中文摘要**

本文提出了DISCOMAX，一种用于相平衡计算的可微分算法，该算法在训练和推断时都保证热力学一致性。该方法植根于统计热力学，通过离散枚举和随后的掩码softmax聚合可行状态来工作，并结合直通梯度估计器，以实现神经$g^{E}$-模型的物理一致端到端学习。我们在二元液-液相平衡数据上评估了该方法，并证明其优于现有的基于代理的方法，同时为从不同种类的平衡数据中学习提供了一个通用框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of phase equilibria remains a central challenge in chemical engineering. Physics-consistent machine learning methods that incorporate thermodynamic structure into neural networks have recently shown strong performance for activity-coefficient modeling. However, extending such approaches to equilibrium data arising from an extremum principle, such as liquid-liquid equilibria, remains difficult. Here we present DISCOMAX, a differentiable algorithm for phase-equilibrium calculation that guarantees thermodynamic consistency at both training and inference, only subject to a user-specified discretization. The method is rooted in statistical thermodynamics, and works via a discrete enumeration with subsequent masked softmax aggregation of feasible states, and together with a straight-through gradient estimator to enable physics-consistent end-to-end learning of neural $g^{E}$-models. We evaluate the approach on binary liquid-liquid equilibrium data and demonstrate that it outperforms existing surrogate-based methods, while offering a general framework for learning from different kinds of equilibrium data.

</details>

---

### 11. [A Machine Learning-Enhanced Hopf-Cole Formulation for Nonlinear Gas Flow in Porous Media](https://arxiv.org/abs/2603.11250)

**基本信息**

- 🔗 arXiv: [`2603.11250`](https://arxiv.org/abs/2603.11250)
- 👥 作者: V. S. Maduru, K. B. Nakshatrala
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11250.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合了物理模型（PDEs）和机器学习（神经网络）的混合建模框架，用于解决多孔介质中的气体流动问题。这直接属于“化学信息学”和更广泛的“科学机器学习”范畴。该方法展示了如何将领域知识（物理方程）与数据驱动方法相结合，以构建更准确、更高效的模型。这种“物理信息机器学习”范式是构建用于复杂化学和物理过程预测的“化学大模型”的重要技术路径之一。

**📖 中文摘要**

本文提出了一个用于多孔介质中气体传输的集成建模框架，该框架结合了Klinkenberg增强的本构关系、Hopf-Cole变换的混合形式线性控制方程、共享主干神经网络架构和深度最小二乘（DeepLS）求解器。Hopf-Cole变换将原始非线性流动方程重新表述为与达西模型密切相关的等效线性系统，而混合公式与共享主干神经架构一起，能够同时准确预测压力场和速度场。重要的是，所提出的框架还自然地促进了从有限或间接观测中反演压力依赖性渗透率和滑移参数，从而能够有效估计难以通过实验测量的流动特性。数值结果证明了在广泛的压力范围内准确恢复流动动力学和参数的能力，突出了该框架在致密地层中气体传输建模和反演方面的鲁棒性、准确性和计算效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate modeling of gas flow through porous media is critical for many technological applications, including reservoir performance prediction, carbon capture and sequestration, and fuel cells and batteries. However, such modeling remains challenging due to strong nonlinear behavior and uncertainty in model parameters. In particular, gas slippage effects described by the Klinkenberg model introduce pressure-dependent permeability, which complicates numerical simulation and obscures deviations from classical Darcy flow behavior. To address these challenges, we present an integrated modeling framework for gas transport in porous media that combines a Klinkenberg-enhanced constitutive relation, Hopf-Cole-transformed mixed-form linear governing equations, a shared-trunk neural network architecture, and a Deep Least-Squares (DeepLS) solver. The Hopf-Cole transformation reformulates the original nonlinear flow equations into an equivalent linear system closely related to the Darcy model, while the mixed formulation, together with a shared-trunk neural architecture, enables simultaneous and accurate prediction of both pressure and velocity fields. A rigorous convergence analysis is performed both theoretically and numerically, establishing the stability and convergence properties of the proposed solver. Importantly, the proposed framework also naturally facilitates inverse modeling of pressure-dependent permeability and slippage parameters from limited or indirect observations, enabling efficient estimation of flow properties that are difficult to measure experimentally. Numerical results demonstrate accurate recovery of flow dynamics and parameters across a wide range of pressure regimes, highlighting the framework's robustness, accuracy, and computational efficiency for gas transport modeling and inversion in tight formations.

</details>

---

### 12. [Heavy-Tailed Principle Component Analysis](https://arxiv.org/abs/2603.11308)

**基本信息**

- 🔗 arXiv: [`2603.11308`](https://arxiv.org/abs/2603.11308)
- 👥 作者: Mario Sayde, Christopher Khater, Jihad Fahs 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11308.pdf)

**💡 相关性分析**

满足标准2：论文提出的针对重尾数据的稳健PCA方法，为化学信息学中常见的高维、噪声数据（如质谱数据）的降维和特征提取提供了潜在的工具和理论框架，可用于后续的质谱结构推理等任务。

**📖 中文摘要**

本文研究了在重尾数据（如多元t分布和亚高斯α稳定律）下的主成分分析（PCA）问题。经典PCA依赖于二阶矩，在存在重尾数据和脉冲噪声时非常脆弱。作者提出了一个基于对数损失的PCA框架，该框架即使在矩不存在时也定义良好。理论结果表明，在这种损失下，重尾观测的主成分与应用于底层高斯生成器协方差矩阵的标准PCA得到的主成分一致。基于此，作者提出了直接从重尾数据中稳健估计该协方差矩阵的方法。这项工作为处理化学信息学（如质谱数据常呈现重尾特性）和质谱分析中的高维、噪声数据提供了理论基础和稳健的降维工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Principal Component Analysis (PCA) is a cornerstone of dimensionality reduction, yet its classical formulation relies critically on second-order moments and is therefore fragile in the presence of heavy-tailed data and impulsive noise. While numerous robust PCA variants have been proposed, most either assume finite variance, rely on sparsity-driven decompositions, or address robustness through surrogate loss functions without a unified treatment of infinite-variance models. In this paper, we study PCA for high-dimensional data generated according to a superstatistical dependent model of the form $\mathbf{X} = A^{1/2}\mathbf{G}$, where $A$ is a positive random scalar and $\mathbf{G}$ is a Gaussian vector. This framework captures a wide class of heavy-tailed distributions, including multivariate $t$ and sub-Gaussian $\alpha$-stable laws. We formulate PCA under a logarithmic loss, which remains well defined even when moments do not exist. Our main theoretical result shows that, under this loss, the principal components of the heavy-tailed observations coincide with those obtained by applying standard PCA to the covariance matrix of the underlying Gaussian generator. Building on this insight, we propose robust estimators for this covariance matrix directly from heavy-tailed data and compare them with the empirical covariance and Tyler's scatter estimator. Extensive experiments, including background denoising tasks, demonstrate that the proposed approach reliably recovers principal directions and significantly outperforms classical PCA in the presence of heavy-tailed and impulsive noise, while remaining competitive under Gaussian noise.

</details>

---

### 13. [Harnessing Data Asymmetry: Manifold Learning in the Finsler World](https://arxiv.org/abs/2603.11396)

**基本信息**

- 🔗 arXiv: [`2603.11396`](https://arxiv.org/abs/2603.11396)
- 👥 作者: Thomas Dagès, Simon Weber, Daniel Cremers 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11396.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的非对称流形学习框架，为化学信息学中处理复杂、非对称的数据关系（例如分子相似性、质谱峰之间的关联）提供了新的数据分析和可视化工具。

**📖 中文摘要**

本文提出了一种利用数据非对称性的流形学习新框架。传统方法依赖于对称的黎曼几何，迫使使用对称的相异度和嵌入空间（如欧几里得空间），这丢弃了数据样本非均匀性所固有的有价值的非对称信息。作者建议通过转向芬斯勒几何（一种非对称的黎曼几何推广）来利用这种非对称性，并提出了一个芬斯勒流形学习流程，该流程构建非对称相异度并在芬斯勒空间中嵌入。这极大地扩展了现有非对称嵌入器的适用性。作者还将当前的主流方法（如t-SNE和Umap）推广到非对称版本。在合成和真实数据集上的实验表明，该非对称流程揭示了传统流程中丢失的有价值信息（如密度层次结构），并持续提供优于其欧几里得对应物的嵌入质量。该方法为分析具有内在方向性或非对称关系的复杂数据（如分子结构或质谱中的峰强度关系）提供了新的视角和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Manifold learning is a fundamental task at the core of data analysis and visualisation. It aims to capture the simple underlying structure of complex high-dimensional data by preserving pairwise dissimilarities in low-dimensional embeddings. Traditional methods rely on symmetric Riemannian geometry, thus forcing symmetric dissimilarities and embedding spaces, e.g. Euclidean. However, this discards in practice valuable asymmetric information inherent to the non-uniformity of data samples. We suggest to harness this asymmetry by switching to Finsler geometry, an asymmetric generalisation of Riemannian geometry, and propose a Finsler manifold learning pipeline that constructs asymmetric dissimilarities and embeds in a Finsler space. This greatly broadens the applicability of existing asymmetric embedders beyond traditionally directed data to any data. We also modernise asymmetric embedders by generalising current reference methods to asymmetry, like Finsler t-SNE and Finsler Umap. On controlled synthetic and large real datasets, we show that our asymmetric pipeline reveals valuable information lost in the traditional pipeline, e.g. density hierarchies, and consistently provides superior quality embeddings than their Euclidean counterparts.

</details>

---

### 14. [MaterialFigBENCH: benchmark dataset with figures for evaluating college-level materials science problem-solving abilities of multimodal large language models](https://arxiv.org/abs/2603.11414)

**基本信息**

- 🔗 arXiv: [`2603.11414`](https://arxiv.org/abs/2603.11414)
- 👥 作者: Michiko Yoshitake, Yuta Suzuki, Ryo Igarashi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11414.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心主题是评估和提升多模态大模型对科学图表（包括可能的光谱、相图等）的理解和推理能力，这与“化学大模型”需要处理和理解化学图表、谱图的核心挑战直接相关。同时，论文的工作也包含了对当前模型在该领域能力的深入讨论和展望。

**📖 中文摘要**

本文提出了MaterialFigBench，一个用于评估多模态大语言模型解决大学级材料科学问题能力的基准数据集，这些问题需要准确解读图表（如相图、应力-应变曲线、阿伦尼乌斯图、衍射图案和微观结构示意图）。该数据集包含137个改编自标准材料科学教科书的自由回答问题，涵盖晶体结构、机械性能、扩散、相图、相变和材料电子性能等广泛主题。作者评估了包括ChatGPT和GPT系列在内的多个最先进的多模态LLM，分析了它们在问题类别和模型版本上的性能。结果表明，尽管总体准确性随着模型更新而提高，但当前的LLM在材料科学图表的真实视觉理解和定量解释方面仍然存在困难。该基准为推进材料科学中的多模态推理能力提供了系统且特定领域的基础。虽然焦点是材料科学，但其核心挑战——让AI模型理解和推理科学图表（包括化学中常见的谱图、相图等）——与“化学大模型”和“质谱结构推理”中所需的跨模态理解和推理能力高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MaterialFigBench, a benchmark dataset designed to evaluate the ability of multimodal large language models (LLMs) to solve university-level materials science problems that require accurate interpretation of figures. Unlike existing benchmarks that primarily rely on textual representations, MaterialFigBench focuses on problems in which figures such as phase diagrams, stress-strain curves, Arrhenius plots, diffraction patterns, and microstructural schematics are indispensable for deriving correct answers. The dataset consists of 137 free-response problems adapted from standard materials science textbooks, covering a broad range of topics including crystal structures, mechanical properties, diffusion, phase diagrams, phase transformations, and electronic properties of materials. To address unavoidable ambiguity in reading numerical values from images, expert-defined answer ranges are provided where appropriate. We evaluate several state-of-the-art multimodal LLMs, including ChatGPT and GPT models accessed via OpenAI APIs, and analyze their performance across problem categories and model versions. The results reveal that, although overall accuracy improves with model updates, current LLMs still struggle with genuine visual understanding and quantitative interpretation of materials science figures. In many cases, correct answers are obtained by relying on memorized domain knowledge rather than by reading the provided images. MaterialFigBench highlights persistent weaknesses in visual reasoning, numerical precision, and significant-digit handling, while also identifying problem types where performance has improved. This benchmark provides a systematic and domain-specific foundation for advancing multimodal reasoning capabilities in materials science and for guiding the development of future LLMs with stronger figure-based understanding.

</details>

---

### 15. [LLM-Assisted Causal Structure Disambiguation and Factor Extraction for Legal Judgment Prediction](https://arxiv.org/abs/2603.11446)

**基本信息**

- 🔗 arXiv: [`2603.11446`](https://arxiv.org/abs/2603.11446)
- 👥 作者: Yuzhi Liang, Lixiang Ma, Xinrong Zhu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11446.pdf)

**💡 相关性分析**

满足标准2和3：论文提出的LLM辅助要素提取和因果结构消歧框架，为构建领域特定的、可解释的推理模型提供了方法论工具，可直接应用于化学信息学中从文本或数据中提取化学实体、关系，并构建用于质谱结构推理的因果或逻辑模型。同时，论文对现有方法瓶颈的讨论也属于相关的重要讨论。

**📖 中文摘要**

本文针对法律判决预测任务，提出了一种融合大语言模型先验与统计因果发现的增强因果推理框架。主流基于预训练语言模型的方法严重依赖案件事实与判决结果之间的统计相关性，缺乏对法律构成要素和底层因果逻辑的显式建模。现有因果法律判决预测方法面临两个关键瓶颈：法律要素提取不准确且噪声严重，以及在稀疏特征下因果结构发现因马尔可夫等价而存在显著不确定性。为此，作者首先设计了一种结合统计采样和LLM语义推理的从粗到细的混合提取机制，以准确识别和净化标准的法律构成要素。其次，为了解决结构不确定性，引入了LLM辅助的因果结构消歧机制，利用LLM作为约束先验知识库，对模糊的因果方向进行概率评估和剪枝，生成符合法律规定的候选因果图。最后，通过生成的因果图显式约束文本注意力强度，构建因果感知的判决预测模型。这项工作展示了如何利用LLM的先验知识来增强特定领域（法律）的因果建模和要素提取，其方法论对于“化学大模型”和“质谱结构推理”具有重要的借鉴意义，例如利用LLM辅助从化学文献或谱图中提取关键特征（官能团、碎片离子等）并构建推理逻辑。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mainstream methods for Legal Judgment Prediction (LJP) based on Pre-trained Language Models (PLMs) heavily rely on the statistical correlation between case facts and judgment results. This paradigm lacks explicit modeling of legal constituent elements and underlying causal logic, making models prone to learning spurious correlations and suffering from poor robustness. While introducing causal inference can mitigate this issue, existing causal LJP methods face two critical bottlenecks in real-world legal texts: inaccurate legal factor extraction with severe noise, and significant uncertainty in causal structure discovery due to Markov equivalence under sparse features. To address these challenges, we propose an enhanced causal inference framework that integrates Large Language Model (LLM) priors with statistical causal discovery. First, we design a coarse-to-fine hybrid extraction mechanism combining statistical sampling and LLM semantic reasoning to accurately identify and purify standard legal constituent elements. Second, to resolve structural uncertainty, we introduce an LLM-assisted causal structure disambiguation mechanism. By utilizing the LLM as a constrained prior knowledge base, we conduct probabilistic evaluation and pruning on ambiguous causal directions to generate legally compliant candidate causal graphs. Finally, a causal-aware judgment prediction model is constructed by explicitly constraining text attention intensity via the generated causal graphs. Extensive experiments on multiple benchmark datasets, including LEVEN , QA, and CAIL, demonstrate that our proposed method significantly outperforms state-of-the-art baselines in both predictive accuracy and robustness, particularly in distinguishing confusing charges.

</details>

---

### 16. [Slack More, Predict Better: Proximal Relaxation for Probabilistic Latent Variable Model-based Soft Sensors](https://arxiv.org/abs/2603.11473)

**基本信息**

- 🔗 arXiv: [`2603.11473`](https://arxiv.org/abs/2603.11473)
- 👥 作者: Zehua Zou, Yiran Ma, Yulong Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11473.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进概率隐变量模型的训练和推断方法。虽然应用场景是工业软传感器，但其提出的变分推断策略和模型优化框架，在方法论层面与构建更稳健、更准确的“化学大模型”（特别是生成模型或概率模型）直接相关。

**📖 中文摘要**

本文提出了一种名为KProxNPLVM的新型非线性概率隐变量模型，旨在通过松弛学习目标和引入Wasserstein距离作为近端算子来改进软传感器建模的准确性。虽然论文的核心应用是工业过程监控，但其核心贡献在于提出了一种新的变分推断策略，用于改进概率隐变量模型的训练。该方法通过理论证明和实验验证了其有效性。从广义的“化学大模型”角度看，该论文提出的改进概率模型训练和变分推断的方法，对于构建和训练化学领域的生成模型或表示学习模型具有潜在的理论和方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Nonlinear Probabilistic Latent Variable Models (NPLVMs) are a cornerstone of soft sensor modeling due to their capacity for uncertainty delineation. However, conventional NPLVMs are trained using amortized variational inference, where neural networks parameterize the variational posterior. While facilitating model implementation, this parameterization converts the distributional optimization problem within an infinite-dimensional function space to parameter optimization within a finite-dimensional parameter space, which introduces an approximation error gap, thereby degrading soft sensor modeling accuracy. To alleviate this issue, we introduce KProxNPLVM, a novel NPLVM that pivots to relaxing the objective itself and improving the NPLVM's performance. Specifically, we first prove the approximation error induced by the conventional approach. Based on this, we design the Wasserstein distance as the proximal operator to relax the learning objective, yielding a new variational inference strategy derived from solving this relaxed optimization problem. Based on this foundation, we provide a rigorous derivation of KProxNPLVM's optimization implementation, prove the convergence of our algorithm can finally sidestep the approximation error, and propose the KProxNPLVM by summarizing the abovementioned content. Finally, extensive experiments on synthetic and real-world industrial datasets are conducted to demonstrate the efficacy of the proposed KProxNPLVM.

</details>

---

### 17. [Leveraging Phytolith Research using Artificial Intelligence](https://arxiv.org/abs/2603.11476)

**基本信息**

- 🔗 arXiv: [`2603.11476`](https://arxiv.org/abs/2603.11476)
- 👥 作者: Andrés G. Mejía Ramón, Kate Dudgeon, Nina Witteveen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11476.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于分析微观颗粒（植硅体）的多模态人工智能模型（ConvNeXt + PointNet++）。虽然研究对象是植硅体，但其核心任务是“结构推理”——从2D和3D数据中推断出颗粒的形态类型和来源。这与“质谱结构推理”在核心任务（从复杂数据中推断结构信息）上高度相似，可以视为在显微镜图像模态上的“结构推理”研究，因此与指定主题相关。

**📖 中文摘要**

本文提出了Sorometry，一个基于人工智能的端到端流水线，用于高通量数字化、推断和解释植硅体（植物微化石）。该工作流处理光学显微镜扫描图像，自动生成同步的2D正射影像和3D点云。作者开发了一个多模态融合模型，结合了用于2D图像分析的ConvNeXt和用于3D点云分析的PointNet++。该模型在24种诊断形态类型上实现了77.9%的全局分类准确率。此外，该平台还集成了贝叶斯有限混合模型，用于在组合层面预测植物来源贡献。这项工作将植硅体研究转变为一个“组学”规模的学科。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phytolith analysis is a crucial tool for reconstructing past vegetation and human activities, but traditional methods are severely limited by labour-intensive, time-consuming manual microscopy. To address this bottleneck, we present Sorometry: a comprehensive end-to-end artificial intelligence pipeline for the high-throughput digitisation, inference, and interpretation of phytoliths. Our workflow processes z-stacked optical microscope scans to automatically generate synchronised 2D orthoimages and 3D point clouds of individual microscopic particles. We developed a multimodal fusion model that combines ConvNeXt for 2D image analysis and PointNet++ for 3D point cloud analysis, supported by a graphical user interface for expert annotation and review. Tested on reference collections and archaeological samples from the Bolivian Amazon, our fusion model achieved a global classification accuracy of 77.9\% across 24 diagnostic morphotypes and 84.5% for segmentation quality. Crucially, the integration of 3D data proved essential for distinguishing complex morphotypes (such as grass silica short cell phytoliths) whose diagnostic features are often obscured by their orientation in 2D projections. Beyond individual object classification, Sorometry incorporates Bayesian finite mixture modelling to predict overall plant source contributions at the assemblage level, successfully identifying specific plants like maize and palms in complex mixed samples. This integrated platform transforms phytolith research into an "omics"-scale discipline, dramatically expanding analytical capacity, standardising expert judgements, and enabling reproducible, population-level characterisations of archaeological and paleoecological assemblages.

</details>

---

### 18. [AutoVeriFix+: High-Correctness RTL Generation via Trace-Aware Causal Fix and Semantic Redundancy Pruning](https://arxiv.org/abs/2603.11489)

**基本信息**

- 🔗 arXiv: [`2603.11489`](https://arxiv.org/abs/2603.11489)
- 👥 作者: Yan Tan, Xiangchen Meng, Zijun Jiang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11489.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大语言模型（LLM）生成和修正硬件描述代码（Verilog）。虽然领域是硬件设计，但其核心是探索和利用“大模型”（此处是LLM）在特定结构化输出（代码）生成和推理方面的能力。这属于“化学大模型”主题的广义外延，即大模型在科学和工程领域的结构化任务中的应用。

**📖 中文摘要**

本文提出了AutoVeriFix+，一个用于生成功能正确的Verilog RTL代码的三阶段框架。该框架集成了高级语义推理和状态空间探索。第一阶段，使用LLM生成定义预期电路行为的Python参考模型。第二阶段，另一个LLM生成初始的Verilog RTL候选并迭代修复语法错误。第三阶段，引入Concolic测试引擎来执行深度顺序逻辑并识别边界情况漏洞。通过提供周期精确的执行轨迹和内部寄存器快照，AutoVeriFix+为LLM提供了解决复杂状态转换错误所需的因果上下文。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated impressive capabilities in generating software code for high-level programming languages such as Python and C++. However, their application to hardware description languages, such as Verilog, is challenging due to the scarcity of high-quality training data. Current approaches to Verilog code generation using LLMs often focus on syntactic correctness, resulting in code with functional errors. To address these challenges, we propose AutoVeriFix+, a novel three-stage framework that integrates high-level semantic reasoning with state-space exploration to enhance functional correctness and design efficiency. In the first stage, an LLM is employed to generate high-level Python reference models that define the intended circuit behavior. In the second stage, another LLM generates initial Verilog RTL candidates and iteratively fixes syntactic errors. In the third stage, we introduce a Concolic testing engine to exercise deep sequential logic and identify corner-case vulnerabilities. With cycle-accurate execution traces and internal register snapshots, AutoVeriFix+ provides the LLM with the causal context necessary to resolve complex state-transition errors. Furthermore, it will generate a coverage report to identify functionally redundant branches, enabling the LLM to perform semantic pruning for area optimization. Experimental results demonstrate that AutoVeriFix+ achieves over 80% functional correctness on rigorous benchmarks, reaching a pass@10 score of 90.2% on the VerilogEval-machine dataset. In addition, it eliminates an average of 25% redundant logic across benchmarks through trace-aware optimization.

</details>

---

### 19. [PRMB: Benchmarking Reward Models in Long-Horizon CBT-based Counseling Dialogue](https://arxiv.org/abs/2603.11494)

**基本信息**

- 🔗 arXiv: [`2603.11494`](https://arxiv.org/abs/2603.11494)
- 👥 作者: Yougen Zhou, Qin Chen, Ningning Zhou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11494.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和优化用于对齐大语言模型（LLM）的奖励模型。虽然应用领域是心理健康，但其核心是研究“大模型”（LLM）的对齐技术（通过奖励模型）。这直接属于“化学大模型”主题中关于大模型训练、对齐和评估的方法论研究范畴。

**📖 中文摘要**

本文提出了PRMB，一个用于评估在多轮认知行为疗法（CBT）咨询对话中奖励模型的综合基准。该基准涵盖6个会话和21种不同的负面场景，包含成对和Best-of-N偏好评估。作者基于此基准对最先进的奖励模型进行了广泛分析，揭示了它们未被先前基准发现的泛化缺陷，并突出了生成式奖励模型的潜力。此外，论文还深入研究了推理时策略对奖励模型评估的有效性，并分析了生成式奖励模型的影响因素。这项工作通过建立心理健康对话中奖励模型评估框架，推进了个性化医疗的智能信息学。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) hold potential for mental healthcare applications, particularly in cognitive behavioral therapy (CBT)-based counseling, where reward models play a critical role in aligning LLMs with preferred therapeutic behaviors. However, existing reward model evaluations often fail to capture alignment effectiveness in long-horizon interventions due to limited coverage of process-oriented datasets and misalignment between evaluation targets and psychological alignment objectives. To address these limitations, we present PRMB, a comprehensive benchmark tailored for evaluating reward models in multi-session CBT counseling. PRMB spans 6 sessions and 21 diverse negative scenarios, incorporating both pairwise and Best-of-N preference evaluations. We demonstrate a positive correlation between our benchmark and downstream counseling dialogue performance. Based on our benchmark, we conduct extensive analysis on the state-of-the-art reward models, revealing their generalization defects that were not discovered by previous benchmarks and highlighting the potential of generative reward models. Furthermore, we delve into examining the effectiveness of inference-time strategy for the evaluation of reward models and analyzing the impact factors of generative reward models. This work advances intelligent informatics for personalized healthcare by establishing a framework for reward model assessment in mental health dialogues. Evaluation code and datasets are publicly available at this https URL

</details>

---

### 20. [Leveraging Large Language Models and Survival Analysis for Early Prediction of Chemotherapy Outcomes](https://arxiv.org/abs/2603.11594)

**基本信息**

- 🔗 arXiv: [`2603.11594`](https://arxiv.org/abs/2603.11594)
- 👥 作者: Muhammad Faisal Shahid, Asad Afzal, Abdullah Faiz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11594.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大语言模型（LLM）从非结构化临床文本中提取结构化信息（表型和结果），以构建预测模型。这直接体现了“大模型”在化学信息学/生物医学信息学领域的应用，即利用LLM处理科学文本和数据，服务于下游的化学/生物医学分析任务（此处是治疗结果预测）。

**📖 中文摘要**

本研究利用大语言模型（LLM）和生存分析，从电子病历（EMR）数据中早期预测乳腺癌化疗结果。研究使用LLM和基于本体的技术从患者笔记中提取表型和治疗结果标签（如癌症进展和毒性），解决了真实世界数据中缺乏明确表型和结果标签的挑战。提取的特征包括生命体征、人口统计学、分期、生物标志物和性能评分。药物方案及其组合从EMR数据中的化疗计划中提取。使用随机生存森林预测失效时间，并在特定时间点用作分类器来预测治疗结果。该方法显著减少了表型稀疏性并提高了预测准确性。研究还将该方法扩展到其他四种癌症类型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemotherapy for cancer treatment is costly and accompanied by severe side effects, highlighting the critical need for early prediction of treatment outcomes to improve patient management and informed decision-making. Predictive models for chemotherapy outcomes using real-world data face challenges, including the absence of explicit phenotypes and treatment outcome labels such as cancer progression and toxicity. This study addresses these challenges by employing Large Language Models (LLMs) and ontology-based techniques for phenotypes and outcome label extraction from patient notes. We focused on one of the most frequently occurring cancers, breast cancer, due to its high prevalence and significant variability in patient response to treatment, making it a critical area for improving predictive modeling. The dataset included features such as vitals, demographics, staging, biomarkers, and performance scales. Drug regimens and their combinations were extracted from the chemotherapy plans in the EMR data and shortlisted based on NCCN guidelines, verified with NIH standards, and analyzed through survival modeling. The proposed approach significantly reduced phenotypes sparsity and improved predictive accuracy. Random Survival Forest was used to predict time-to-failure, achieving a C-index of 73%, and utilized as a classifier at a specific time point to predict treatment outcomes, with accuracy and F1 scores above 70%. The outcome probabilities were validated for reliability by calibration curves. We extended our approach to four other cancer types. This research highlights the potential of early prediction of treatment outcomes using LLM-based clinical data extraction enabling personalized treatment plans with better patient outcomes.

</details>

---

### 21. [Performance Evaluation of Open-Source Large Language Models for Assisting Pathology Report Writing in Japanese](https://arxiv.org/abs/2603.11597)

**基本信息**

- 🔗 arXiv: [`2603.11597`](https://arxiv.org/abs/2603.11597)
- 👥 作者: Masataka Kawai, Singo Sakashita, Shumpei Ishikawa 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11597.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大语言模型（LLM）在专业科学文本（病理报告）生成、信息提取和纠错方面的能力。这直接属于“化学大模型”主题的范畴，即探索大模型在化学、生物医学等科学领域的文本处理和专业内容生成方面的应用潜力。

**📖 中文摘要**

本文评估了开源大语言模型（LLM）在辅助日语病理报告撰写方面的性能。评估从三个角度进行：(A) 按照预定义格式生成和提取病理诊断文本，(B) 纠正日语病理报告中的拼写错误，(C) 由病理学家和临床医生对模型生成的解释性文本进行主观评价。实验发现，思维模型和医学专用模型在需要推理的结构化报告任务和拼写纠正方面表现出优势。尽管LLM的效用因任务而异，但研究结果表明，开源LLM在有限但临床相关的场景下可用于辅助日语病理报告撰写。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The performance of large language models (LLMs) for supporting pathology report writing in Japanese remains unexplored. We evaluated seven open-source LLMs from three perspectives: (A) generation and information extraction of pathology diagnosis text following predefined formats, (B) correction of typographical errors in Japanese pathology reports, and (C) subjective evaluation of model-generated explanatory text by pathologists and clinicians. Thinking models and medical-specialized models showed advantages in structured reporting tasks that required reasoning and in typo correction. In contrast, preferences for explanatory outputs varied substantially across raters. Although the utility of LLMs differed by task, our findings suggest that open-source LLMs can be useful for assisting Japanese pathology report writing in limited but clinically relevant scenarios.

</details>

---

### 22. [Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](https://arxiv.org/abs/2603.11627)

**基本信息**

- 🔗 arXiv: [`2603.11627`](https://arxiv.org/abs/2603.11627)
- 👥 作者: Yichi Zhang, Le Xue, Wenbo Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11627.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文的核心研究内容是开发用于3D医学图像（PET）通用分割的“基础模型”（SegAnyPET）。这属于“大模型”在科学数据（此处是医学影像）分析中的应用。2) 论文贡献了一个大规模、高质量的PET分割数据集（11041个扫描，59831个掩码），这为相关领域的研究提供了宝贵的“数据资源”。该数据集可用于训练或评估其他医学影像分析模型，包括可能涉及分子结构或代谢信息推理的模型，与化学信息学有潜在关联。

**📖 中文摘要**

本文开发了用于3D全身正电子发射断层扫描（PET）通用分割的基础模型。作者首先构建了迄今为止最大、最全面的PET数据集，包含11041个3D全身PET扫描和59831个分割掩码。基于此数据集，提出了SegAnyPET，一个具有通用适用性的创新基础模型，用于多样化的分割任务。SegAnyPET基于3D架构和用于掩码生成的提示工程策略，实现了通用且可扩展的器官和病变分割，支持以最小工作量进行高效的人工校正，并实现了临床人机交互工作流。在多中心、多示踪剂、多疾病数据集上的广泛评估表明，SegAnyPET在广泛的分割任务中实现了强大的零样本性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Positron emission tomography (PET) is a key nuclear medicine imaging modality that visualizes radiotracer distributions to quantify in vivo physiological and metabolic processes, playing an irreplaceable role in disease management. Despite its clinical importance, the development of deep learning models for quantitative PET image analysis remains severely limited, driven by both the inherent segmentation challenge from PET's paucity of anatomical contrast and the high costs of data acquisition and annotation. To bridge this gap, we develop generalist foundational models for universal segmentation from 3D whole-body PET imaging. We first build the largest and most comprehensive PET dataset to date, comprising 11041 3D whole-body PET scans with 59831 segmentation masks for model development. Based on this dataset, we present SegAnyPET, an innovative foundational model with general-purpose applicability to diverse segmentation tasks. Built on a 3D architecture with a prompt engineering strategy for mask generation, SegAnyPET enables universal and scalable organ and lesion segmentation, supports efficient human correction with minimal effort, and enables a clinical human-in-the-loop workflow. Extensive evaluations on multi-center, multi-tracer, multi-disease datasets demonstrate that SegAnyPET achieves strong zero-shot performance across a wide range of segmentation tasks, highlighting its potential to advance the clinical applications of molecular imaging.

</details>

---

### 23. [PolyCrysDiff: Controllable Generation of Three-Dimensional Computable Polycrystalline Material Structures](https://arxiv.org/abs/2603.11695)

**基本信息**

- 🔗 arXiv: [`2603.11695`](https://arxiv.org/abs/2603.11695)
- 👥 作者: Chi Chen, Tianle Jiang, Xiaodong Wei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11695.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成和推理多晶材料的3D微观结构，这直接属于化学信息学（材料信息学）领域，并涉及结构推理（从目标属性生成结构）。

**📖 中文摘要**

本文提出PolyCrysDiff，一个基于条件潜在扩散的框架，用于端到端生成可计算的3D多晶材料微观结构。该工作直接面向材料科学中的结构生成与推理，属于化学信息学中材料信息学的重要分支。论文的核心是生成具有可控晶粒形态、取向分布和空间相关性的3D多晶结构，并通过晶体塑性有限元模拟验证了生成结构的物理有效性。这项工作为阐明材料微观结构与宏观性能之间的关系提供了关键工具，其可控生成能力可用于加速数据驱动的多晶材料优化与设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The three-dimensional (3D) microstructures of polycrystalline materials exert a critical influence on their mechanical and physical properties. Realistic, controllable construction of these microstructures is a key step toward elucidating structure-property relationships, yet remains a formidable challenge. Herein, we propose PolyCrysDiff, a framework based on conditional latent diffusion that enables the end-to-end generation of computable 3D polycrystalline microstructures. Comprehensive qualitative and quantitative evaluations demonstrate that PolyCrysDiff faithfully reproduces target grain morphologies, orientation distributions, and 3D spatial correlations, while achieving an $R^2$ over 0.972 on grain attributes (e.g., size and sphericity) control, thereby outperforming mainstream approaches such as Markov random field (MRF)- and convolutional neural network (CNN)-based methods. The computability and physical validity of the generated microstructures are verified through a series of crystal plasticity finite element method (CPFEM) simulations. Leveraging PolyCrysDiff's controllable generative capability, we systematically elucidate how grain-level microstructural characteristics affect the mechanical properties of polycrystalline materials. This development is expected to pave a key step toward accelerated, data-driven optimization and design of polycrystalline materials.

</details>

---

### 24. [EvoFlows: Evolutionary Edit-Based Flow-Matching for Protein Engineering](https://arxiv.org/abs/2603.11703)

**基本信息**

- 🔗 arXiv: [`2603.11703`](https://arxiv.org/abs/2603.11703)
- 👥 作者: Nicolas Deutschmann, Constance Ferragu, Jonathan D. Ziegler 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11703.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是蛋白质序列的生成与编辑模型（EvoFlows），这直接属于化学信息学中的生物信息学子领域，并涉及分子（蛋白质）结构的推理与生成。

**📖 中文摘要**

本文介绍了EvoFlows，一种用于蛋白质工程的变长序列到序列建模方法。与自回归和掩码语言模型不同，EvoFlows通过对模板蛋白质序列执行有限、可控数量的插入、删除和替换来预测突变。该方法利用编辑流来学习进化相关蛋白质序列之间的突变轨迹，同时模拟相关天然蛋白质的分布以及连接它们的突变路径。通过广泛的计算机评估，证明EvoFlows能够以与常用于蛋白质工程的领先掩码语言模型相当的质量捕获蛋白质序列分布，同时显示出从给定模板蛋白质生成非平凡且类天然突变体的改进能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce EvoFlows, a variable-length sequence-to-sequence protein modeling approach uniquely suited to protein engineering. Unlike autoregressive and masked language models, EvoFlows perform a limited, controllable number of insertions, deletions, and substitutions on a template protein sequence. In other words, EvoFlows predict not only _which_ mutation to perform, but also _where_ it should occur. Our approach leverages edit flows to learn mutational trajectories between evolutionarily-related protein sequences, simultaneously modeling distributions of related natural proteins and the mutational paths connecting them. Through extensive _in silico_ evaluation on diverse protein communities from UNIREF and OAS, we demonstrate that EvoFlows capture protein sequence distributions with a quality comparable to leading masked language models commonly used in protein engineering, while showing improved ability to generate non-trivial yet natural-like mutants from a given template protein.

</details>

---

### 25. [PhiPlot: A Web-Based Interactive EDA Environment for Atmospherically Relevant Molecules](https://arxiv.org/abs/2603.11751)

**基本信息**

- 🔗 arXiv: [`2603.11751`](https://arxiv.org/abs/2603.11751)
- 👥 作者: Matias Loukojärvi, Ananth Mahadevan, Katsiaryna Haitsiukevich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11751.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个专门用于探索大气化学相关分子数据集的交互式工具（PhiPlot），这是一个可用于化学信息学分析的数据资源和可视化工具。

**📖 中文摘要**

本文介绍了PhiPlot，一个用于大气相关分子数据交互式探索和基于知识的降维的Web环境。该工具集成了可视化、聚类和领域知识引导的嵌入细化，旨在帮助发现数据中的模式并支持假设生成。该应用程序连接到一个现有的、不断发展的分子数据库集合，为大气化学中的数据驱动研究提供了一个可访问的界面。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advances in computational chemistry have produced high-dimensional datasets on atmospherically relevant molecules. To aid exploration of such datasets, particularly for the study of atmospheric aerosol formation, we introduce PhiPlot: a web-based environment for interactive exploration and knowledge-based dimensionality reduction. The integration of visualisation, clustering, and domain knowledge-guided embedding refinement enables the discovery of patterns in the data and supports hypothesis generation. The application connects to an existing, evolving collection of molecular databases, offering an accessible interface for data-driven research in atmospheric chemistry.

</details>

---

### 26. [OMNIA: Closing the Loop by Leveraging LLMs for Knowledge Graph Completion](https://arxiv.org/abs/2603.11820)

**基本信息**

- 🔗 arXiv: [`2603.11820`](https://arxiv.org/abs/2603.11820)
- 👥 作者: Frédéric Ieng, Soror Sahri, Mourad Ouzzani 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11820.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是知识图谱补全，这是一种结构推理任务。虽然不直接针对化学或质谱，但其方法论（结合嵌入和LLM进行结构推理）与化学信息学中的分子知识图谱补全或质谱解析中的结构推断在原理上相关。

**📖 中文摘要**

本文提出了OMNIA，一个用于知识图谱补全的两阶段方法，它弥合了结构推理和语义推理。该方法首先通过在知识图谱内部对语义相关的实体和关系进行聚类来生成候选三元组，然后通过轻量级嵌入过滤和基于LLM的语义验证来验证它们。OMNIA专门针对知识图谱中隐含的语义进行补全，无需依赖外部数据源。这项工作涉及从现有结构中进行推理以补全缺失信息，属于广义的结构推理范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge Graphs (KGs) are widely used to represent structured knowledge, yet their automatic construction, especially with Large Language Models (LLMs), often results in incomplete or noisy outputs. Knowledge Graph Completion (KGC) aims to infer and add missing triples, but most existing methods either rely on structural embeddings that overlook semantics or language models that ignore the graph's structure and depend on external sources. In this work, we present OMNIA, a two-stage approach that bridges structural and semantic reasoning for KGC. It first generates candidate triples by clustering semantically related entities and relations within the KG, then validates them through lightweight embedding filtering followed by LLM-based semantic validation. OMNIA performs on the internal KG, without external sources, and specifically targets implicit semantics that are most frequent in LLM-generated graphs. Extensive experiments on multiple datasets demonstrate that OMNIA significantly improves F1-score compared to traditional embedding-based models. These results highlight OMNIA's effectiveness and efficiency, as its clustering and filtering stages reduce both search space and validation cost while maintaining high-quality completion.

</details>

---

### 27. [A Decade of Generative Adversarial Networks for Porous Material Reconstruction](https://arxiv.org/abs/2603.11836)

**基本信息**

- 🔗 arXiv: [`2603.11836`](https://arxiv.org/abs/2603.11836)
- 👥 作者: Ali Sadeghkhani, Brandon Bennett, Masoud Babaei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11836.pdf)

**💡 相关性分析**

满足标准3：论文是关于生成对抗网络在多孔材料重建领域的综述，这属于化学信息学和材料信息学的交叉领域。虽然不直接涉及“化学大模型”或“质谱结构推理”，但它全面回顾了用于材料结构生成的深度生成模型，与关注主题中的“模型”和“结构”高度相关。

**📖 中文摘要**

本文系统回顾了2017年至2026年初发表的96篇同行评议文章，分析了生成对抗网络在多孔材料图像重建中的演变和应用。综述将GAN架构分为六类，并揭示了在孔隙度精度、渗透率预测和可重建体积方面的显著进展。尽管取得了这些进展，但在计算效率、大规模重建的内存限制以及2D到3D转换中的结构连续性方面仍然存在持续挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital reconstruction of porous materials has become increasingly critical for applications ranging from geological reservoir characterization to tissue engineering and electrochemical device design. While traditional methods such as micro-computed tomography and statistical reconstruction approaches have established foundations in this field, the emergence of deep learning techniques, particularly Generative Adversarial Networks (GANs), has revolutionized porous media reconstruction capabilities. This review systematically analyzes 96 peer-reviewed articles published from 2017 to early 2026, examining the evolution and applications of GAN-based approaches for porous material image reconstruction. We categorize GAN architectures into six distinct classes, namely Vanilla GANs, Multi-Scale GANs, Conditional GANs, Attention-Enhanced GANs, Style-based GANs, and Hybrid Architecture GANs. Our analysis reveals substantial progress including improvements in porosity accuracy (within 1% of original samples), permeability prediction (up to 79% reduction in mean relative errors), and achievable reconstruction volumes (from initial $64^3$ to current $2{,}200^3$ voxels). Despite these advances, persistent challenges remain in computational efficiency, memory constraints for large-scale reconstruction, and maintaining structural continuity in 2D-to-3D transformations. This systematic analysis provides a comprehensive framework for selecting appropriate GAN architectures based on specific application requirements.

</details>

---

### 28. [Inverse Neural Operator for ODE Parameter Optimization](https://arxiv.org/abs/2603.11854)

**基本信息**

- 🔗 arXiv: [`2603.11854`](https://arxiv.org/abs/2603.11854)
- 👥 作者: Zhi-Song Liu, Wenqing Peng, Helmi Toropainen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11854.pdf)

**💡 相关性分析**

满足标准1：论文的核心是逆向问题求解，即从观测数据（轨迹）推理出底层系统参数。这本质上是“结构推理”的一种形式（推理动力学系统的参数化结构）。虽然应用场景是ODE系统，但其方法论（神经算子、参数推理）与从质谱数据推理分子结构或校准化学动力学模型在概念上相通。

**📖 中文摘要**

本文提出了逆向神经算子，一个用于从稀疏、部分观测中恢复隐藏ODE参数的两阶段框架。第一阶段，一个带有交叉注意力的条件傅里叶神经算子学习一个可微分的代理模型，从任意稀疏输入重建完整的ODE轨迹。第二阶段，一个摊销漂移模型在参数空间中学习一个核加权的速度场，将随机参数初始化向真实值传输，而无需通过代理模型反向传播。该方法在真实世界的大气化学基准和合成基因调控网络上进行了实验。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose the Inverse Neural Operator (INO), a two-stage framework for recovering hidden ODE parameters from sparse, partial observations. In Stage 1, a Conditional Fourier Neural Operator (C-FNO) with cross-attention learns a differentiable surrogate that reconstructs full ODE trajectories from arbitrary sparse inputs, suppressing high-frequency artifacts via spectral regularization. In Stage 2, an Amortized Drifting Model (ADM) learns a kernel-weighted velocity field in parameter space, transporting random parameter initializations toward the ground truth without backpropagating through the surrogate, avoiding the Jacobian instabilities that afflict gradient-based inversion in stiff regimes. Experiments on a real-world stiff atmospheric chemistry benchmark (POLLU, 25 parameters) and a synthetic Gene Regulatory Network (GRN, 40 parameters) show that INO outperforms gradient-based and amortized baselines in parameter recovery accuracy while requiring only 0.23s inference time, a 487x speedup over iterative gradient descent.

</details>

---

### 29. [AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization](https://arxiv.org/abs/2603.11873)

**基本信息**

- 🔗 arXiv: [`2603.11873`](https://arxiv.org/abs/2603.11873)
- 👥 作者: Qiyang Li, Rui Kong, Yuchen Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11873.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大型语言模型的动态适配器集成与高效推理展开。虽然应用场景是通用LLM，但其提出的动态适配器集成、参数高效微调（LoRA）等方法论，是构建和优化“化学大模型”的关键技术路径之一，因此与核心主题相关。

**📖 中文摘要**

论文提出AdaFuse框架，旨在加速大型语言模型（LLM）中动态、稀疏结构（如混合专家MoE）与参数高效适配器（如LoRA）的集成推理。该框架通过令牌级预门控策略和融合内核优化，解决了动态路由带来的严重延迟开销，实现了高效的动态适配器执行。虽然论文主要关注LLM的推理加速，但其核心方法涉及动态适配器（如LoRA）的集成与优化，这与“化学大模型”中模型微调、适配器技术等主题在方法论上高度相关。论文提出的算法与硬件协同设计思想，对于构建高效、可扩展的化学领域大模型具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of dynamic, sparse structures like Mixture-of-Experts (MoE) with parameter-efficient adapters (e.g., LoRA) is a powerful technique for enhancing Large Language Models (LLMs). However, this architectural enhancement comes at a steep cost: despite minimal increases in computational load, the inference latency often skyrockets, leading to decoding speeds slowing by over 2.5 times. Through a fine-grained performance analysis, we pinpoint the primary bottleneck not in the computation itself, but in the severe overhead from fragmented, sequential CUDA kernel launches required for conventional dynamic routing. To address this challenge, we introduce AdaFuse, a framework built on a tight co-design between the algorithm and the underlying hardware system to enable efficient dynamic adapter execution. Departing from conventional layer-wise or block-wise routing, AdaFuse employs a token-level pre-gating strategy, which makes a single, global routing decision for all adapter layers before a token is processed. This "decide-once, apply-everywhere" approach effectively staticizes the execution path for each token, creating an opportunity for holistic optimization. We capitalize on this by developing a custom CUDA kernel that performs a fused switching operation, merging the parameters of all selected LoRA adapters into the backbone model in a single, efficient pass. Experimental results on popular open-source LLMs show that AdaFuse achieves accuracy on par with state-of-the-art dynamic adapters while drastically cutting decoding latency by a factor of over 2.4x, thereby bridging the gap between model capability and inference efficiency.

</details>

---

### 30. [Bielik-Minitron-7B: Compressing Large Language Models via Structured Pruning and Knowledge Distillation for the Polish Language](https://arxiv.org/abs/2603.11881)

**基本信息**

- 🔗 arXiv: [`2603.11881`](https://arxiv.org/abs/2603.11881)
- 👥 作者: Remigiusz Kinas, Paweł Kiszczak, Sergio P. Perez 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11881.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型的压缩与高效化，这直接关系到“化学大模型”的构建、优化与部署。论文中使用的技术（如知识蒸馏、结构化剪枝）是开发高效领域大模型的通用关键技术。

**📖 中文摘要**

论文详细介绍了Bielik-Minitron-7B模型的创建过程，这是一个针对波兰语等欧洲语言优化的压缩大型语言模型。通过结合结构化混合剪枝和知识蒸馏的两阶段压缩方法，将参数从110.4亿减少到73.5亿。该方法展示了为资源较少语言创建高效语言模型的途径。虽然论文聚焦于自然语言处理，但其核心——大型语言模型的压缩、知识蒸馏和高效部署——是“化学大模型”领域同样面临的关键挑战。论文提供的方法论（结构化剪枝、蒸馏）和结果（性能恢复、推理加速）对于开发领域专用的、高效的化学大模型具有直接的参考意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This report details the creation of Bielik-Minitron-7B, a compressed 7.35B parameter version of the Bielik-11B-v3.0 model, specifically optimized for European languages. By leveraging a two-stage compression methodology inspired by the NVIDIA Minitron approach, we combined structured hybrid pruning and knowledge distillation to reduce the model's parameter count by 33.4%, from 11.04B to 7.35B. We utilized the NVIDIA Model Optimizer for structural pruning and the NVIDIA NeMo Framework for logit-based distillation for quality recovery. Following distillation, the model underwent a rigorous alignment pipeline consisting of Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO-P), and Reinforcement Learning (GRPO). Our final model successfully recovered approximately 90% of the baseline model's performance while providing up to 50% inference speedup. This approach demonstrates an efficient pathway to create language models for less-represented languages, preserving the original model quality while reducing inference deployment costs.

</details>

---

### 31. [Chem4DLLM: 4D Multimodal LLMs for Chemical Dynamics Understanding](https://arxiv.org/abs/2603.11924)

**基本信息**

- 🔗 arXiv: [`2603.11924`](https://arxiv.org/abs/2603.11924)
- 👥 作者: Xinyu Li, Zhen Zhang, Qi Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11924.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题高度相关：论文明确提出并构建了用于“化学大模型”（Chem4DLLM）的新任务（ChemDU）和模型架构，旨在实现动态化学过程的多模态理解与推理。2) 数据资源相关：论文构建并提供了Chem4DBench数据集，这是用于训练和评估化学动态理解大模型的重要资源。

**📖 中文摘要**

论文针对现有化学理解任务主要依赖静态分子表示的局限性，引入了化学动力学理解（ChemDU）新任务。该任务旨在将4D分子轨迹转化为可解释的自然语言描述。为此，论文构建了首个配对4D分子轨迹与专家解释的数据集Chem4DBench，并提出了统一模型Chem4DLLM。该模型将等变图编码器与预训练大语言模型相结合，显式捕获分子几何和旋转动力学。这项工作将化学动态现象（如键断裂、构象变化）与多模态大语言模型推理相结合，是“化学大模型”在理解和推理动态化学过程方面的前沿探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing chemical understanding tasks primarily rely on static molecular representations, limiting their ability to model inherently dynamic phenomena such as bond breaking or conformational changes, which are essential for a chemist to understand chemical reactions. To address this gap, we introduce Chemical Dynamics Understanding (ChemDU), a new task that translates 4D molecular trajectories into interpretable natural-language explanations. ChemDU focuses on fundamental dynamic scenarios, including gas-phase and catalytic reactions, and requires models to reason about key events along molecular trajectories, such as bond formation and dissociation, and to generate coherent, mechanistically grounded narratives. To benchmark this capability, we construct Chem4DBench, the first dataset pairing 4D molecular trajectories with expert-authored explanations across these settings. We further propose Chem4DLLM, a unified model that integrates an equivariant graph encoder with a pretrained large language model to explicitly capture molecular geometry and rotational dynamics. We hope that ChemDU, together with Chem4DBench and Chem4DLLM, will stimulate further research in dynamic chemical understanding and multimodal scientific reasoning.

</details>

---

### 32. [Making Chant Computing Easy: CantusCorpus v1.0 and the PyCantus Library](https://arxiv.org/abs/2603.11933)

**基本信息**

- 🔗 arXiv: [`2603.11933`](https://arxiv.org/abs/2603.11933)
- 👥 作者: Anna Dvořáková, Tim Eipert, Debra Lacoste 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11933.pdf)

**💡 相关性分析**

满足标准2：论文提供了可用于特定领域（圣咏研究）的大规模数据集（CantusCorpus）和配套处理工具（PyCantus）。虽然领域不同，但其构建统一领域数据集、提供计算库以支持模型训练和研究的范式，为化学信息学领域构建类似的数据资源（如统一的质谱数据库、化学结构数据库）提供了可借鉴的范例和思路。

**📖 中文摘要**

论文介绍了CantusCorpus v1.0数据集和PyCantus库，旨在解决格里高利圣咏数字学术研究中大规模数据难以进行计算的瓶颈。CantusCorpus整合了来自Cantus索引网络下多个数据库的近90万首圣咏数据，而PyCantus则提供了一个轻量级库来处理这些数据。这项工作虽然属于数字人文领域，但其核心是构建一个统一、可计算的大型领域数据集（CantusCorpus）并提供配套工具（PyCantus），以支持透明、可复现的研究。这种为特定领域构建大规模、结构化数据集并提供处理工具的模式，与“化学大模型”和“质谱结构推理”研究中对于高质量、大规模化学数据集和计算工具的需求在方法论上完全一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital Gregorian chant scholarship has for decades enjoyed the privilege of a large digital resource cataloguing chant sources: the Cantus ecosystem, with nearly 900,000 chants catalogued across more than 2000 sources. The Cantus Database data model and the Cantus ID mechanism has been adopted by 18 more chant databases, jointly accessible through the Cantus Index interface. However, this data has only been available piecemeal via the individual online user interfaces; computational methods have so far had only a limited opportunity to process these immense resources. To overcome this hurdle, we compiled CantusCorpus v1.0, a dataset that combines everything that was available across the Cantus Index-centered network of databases as of mid-2025, and we have also provided the code for updating the dataset as the databases grow. We then created the lightweight PyCantus library for working with this data. PyCantus decouples the data model from the Cantus codebase and thus allows integration of further chant data sources, which we illustrate with harmonising pilot data from the Corpus Monodicum project. Computational chant research is attractive - and CantusCorpus v1.0 and PyCantus are infrastructures that should make work in this field more transparent, replicable, and accessible to digital humanities practitioners beyond chant scholars themselves.

</details>

---

### 33. [Learning Transferable Sensor Models via Language-Informed Pretraining](https://arxiv.org/abs/2603.11950)

**基本信息**

- 🔗 arXiv: [`2603.11950`](https://arxiv.org/abs/2603.11950)
- 👥 作者: Yuliang Chen, Arvind Pillai, Yu Yvonne Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11950.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用语言模型进行多模态（传感器数据）表征学习与对齐。这种方法论与“化学大模型”和“质谱结构推理”中旨在利用大语言模型理解和推理质谱、分子结构等多模态化学信息的核心目标直接相关，提供了可行的技术框架参考。

**📖 中文摘要**

论文提出了SLIP框架，一个用于学习与语言对齐的传感器表征的开源框架。该框架通过对比对齐和传感器条件描述生成，支持跨不同传感器设置的泛化。它重新利用了一个预训练的仅解码器语言模型，并通过交叉注意力和灵活的补丁嵌入器，在推理时支持不同的时间分辨率和可变长度输入，而无需重新训练。SLIP在多个数据集的零样本迁移、信号描述和问答任务中表现出色。这项工作将预训练语言模型与多模态（传感器）数据相结合，学习可迁移的表征。其核心思想——利用语言模型对齐多模态数据以进行下游推理——与“化学大模型”中利用LLM理解质谱、分子结构等多模态化学数据的思路高度吻合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern sensing systems generate large volumes of unlabeled multivariate time-series data. This abundance of unlabeled data makes self-supervised learning (SSL) a natural approach for learning transferable representations. However, most existing approaches are optimized for reconstruction or forecasting objectives and often fail to capture the semantic structure required for downstream classification and reasoning tasks. While recent sensor-language alignment methods improve semantic generalization through captioning and zero-shot transfer, they are limited to fixed sensor configurations, such as predefined channel sets, signal lengths, or temporal resolutions, which hinders cross-domain applicability. To address these gaps, we introduce \textbf{SLIP} (\textbf{S}ensor \textbf{L}anguage-\textbf{I}nformed \textbf{P}retraining), an open-source framework for learning language-aligned representations that generalize across diverse sensor setups. SLIP integrates contrastive alignment with sensor-conditioned captioning, facilitating both discriminative understanding and generative reasoning. By repurposing a pretrained decoder-only language model via cross-attention and introducing an elegant, flexible patch-embedder, SLIP supports different temporal resolutions and variable-length input at inference time without additional retraining. Across 11 datasets, SLIP demonstrates superior performance in zero-shot transfer, signal captioning, and question answering. It achieves a 77.14% average linear-probing accuracy, a 5.93% relative improvement over strong baselines, and reaches 64.83% accuracy in sensor-based question answering.

</details>

---

### 34. [Multimodal Emotion Recognition via Bi-directional Cross-Attention and Temporal Modeling](https://arxiv.org/abs/2603.11971)

**基本信息**

- 🔗 arXiv: [`2603.11971`](https://arxiv.org/abs/2603.11971)
- 👥 作者: Junhyeong Byeon, Jeongyeol Kim, Sejoon Lim
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11971.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是多模态（视觉+音频）信息的融合与推理。虽然应用场景不同，但其采用的技术路线（基于预训练模型的多模态融合、交叉注意力机制）是构建能够同时处理质谱、分子结构、文本描述等多种化学信息的“化学大模型”所需的关键技术，因此与核心主题相关。

**📖 中文摘要**

论文提出了一种用于野外视频数据多模态情感识别的框架。该框架利用大规模预训练模型（CLIP用于视觉，Wav2Vec 2.0用于音频）作为冻结骨干网络，并引入双向交叉注意力融合模块来增强跨模态上下文信息。虽然应用领域是情感分析，但其技术核心——整合视觉和音频预训练模型、进行跨模态融合以完成复杂推理任务——与“化学大模型”中整合多种化学数据模态（如质谱图、分子式、文本描述）进行联合推理的思路在技术路径上高度相似。论文中使用的多模态融合架构和方法，可以为化学多模态大模型的设计提供参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Emotion recognition in in-the-wild video data remains a challenging problem due to large variations in facial appearance, head pose, illumination, background noise, and the inherently dynamic nature of human affect. Relying on a single modality, such as facial expressions or speech, is often insufficient to capture these complex emotional cues. To address this issue, we propose a multimodal emotion recognition framework for the Expression (EXPR) Recognition task in the 10th Affective Behavior Analysis in-the-wild (ABAW) Challenge. Our approach leverages large-scale pre-trained models, namely CLIP for visual encoding and Wav2Vec 2.0 for audio representation learning, as frozen backbone networks. To model temporal dependencies in facial expression sequences, we employ a Temporal Convolutional Network (TCN) over fixed-length video windows. In addition, we introduce a bi-directional cross-attention fusion module, in which visual and audio features interact symmetrically to enhance cross-modal contextualization and capture complementary emotional information. A lightweight classification head is then used for final emotion prediction. We further incorporate a text-guided contrastive objective based on CLIP text features to encourage semantically aligned visual representations. Experimental results on the ABAW 10th EXPR benchmark show that the proposed framework provides a strong multimodal baseline and achieves improved performance over unimodal modeling. These results demonstrate the effectiveness of combining temporal visual modeling, audio representation learning, and cross-modal fusion for robust emotion recognition in unconstrained real-world environments.

</details>

---

### 35. [Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era](https://arxiv.org/abs/2603.12016)

**基本信息**

- 🔗 arXiv: [`2603.12016`](https://arxiv.org/abs/2603.12016)
- 👥 作者: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12016.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个强大的、可扩展的图像特征提取库（Nyxus）。虽然主要面向生物医学图像，但其处理大规模、高维图像数据并提取标准化特征的能力，对于“质谱结构推理”中处理质谱成像数据、提取与分子结构相关的空间-光谱特征具有直接的工具参考价值。该库可被视为一种可用于相关主题的数据处理工具资源。

**📖 中文摘要**

论文介绍了Nyxus，一个为大数据和AI时代设计的新一代图像特征提取库。Nyxus专为2D和3D图像数据的可扩展核外特征提取而构建，涵盖生物医学领域的多个特征集（如放射组学和细胞分析），并针对CPU和GPU进行了计算可扩展性设计。它提供了多种使用方式（Python包、命令行工具、Napari插件、容器）。在化学信息学和质谱分析中，质谱成像（MSI）会产生海量的空间-质谱数据，特征提取是后续分析的关键步骤。Nyxus所解决的大规模图像特征提取的准确性、效率和标准化问题，与质谱成像数据分析中面临的挑战高度一致。其设计理念和实现为开发针对质谱成像数据的专用特征提取工具提供了重要参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment. The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy. Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction libraries across scientific disciplines has made it difficult to compare the performance and accuracy of extracted features. To address these needs, we developed a novel feature extraction library called Nyxus. Nyxus is designed from the ground up for scalable out-of-core feature extraction for 2D and 3D image data and rigorously tested against established standards. The comprehensive feature set of Nyxus covers multiple biomedical domains including radiomics and cellular analysis, and is designed for computational scalability across CPUs and GPUs. Nyxus has been packaged to be accessible to users of various skill sets and needs: as a Python package for code developers, a command line tool, as a Napari plugin for low to no-code users or users that want to visualize results, and as an Open Container Initiative (OCI) compliant container that can be used in cloud or super-computing workflows aimed at processing large data sets. Further, Nyxus enables a new methodological approach to feature extraction allowing for programmatic tuning of many features sets for optimal computational efficiency or coverage for use in novel machine learning and deep learning applications.

</details>

---

### 36. [Chemical Reaction Networks Learn Better than Spiking Neural Networks](https://arxiv.org/abs/2603.12060)

**基本信息**

- 🔗 arXiv: [`2603.12060`](https://arxiv.org/abs/2603.12060)
- 👥 作者: Sophie Jaffard, Ivo F. Sbalzarini
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12060.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索化学反应网络作为一种机器学习模型。这为“化学大模型”的概念提供了一个非常规但极具启发性的视角，即模型本身可以是“化学的”。论文证明了这种化学计算模型在某些任务上优于传统神经网络，这与构建新型化学智能系统的主题高度相关。

**📖 中文摘要**

论文从数学上证明，无隐藏层的化学反应网络（CRNs）可以解决尖峰神经网络（SNNs）需要隐藏层才能完成的任务。研究使用确定性质量作用动力学公式化的CRNs，并通过数值实验证实了所提出的CRN在像素图像手写数字分类任务上的学习能力，其表现比带隐藏层的SNN更准确、高效。这项工作为化学计算机中的机器学习提供了动机，并数学解释了生化反应网络可能比神经元网络表现出更高效的学习行为。虽然论文偏重理论证明和基础模型比较，但其核心是探索一种不同于传统神经网络的新型计算模型（CRNs）用于机器学习。这为“化学大模型”提供了一个颠覆性的思考方向：是否可以利用内在的化学或生物分子过程来构建更高效的学习系统？

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We mathematically prove that chemical reaction networks without hidden layers can solve tasks for which spiking neural networks require hidden layers. Our proof uses the deterministic mass-action kinetics formulation of chemical reaction networks. Specifically, we prove that a certain reaction network without hidden layers can learn a classification task previously proved to be achievable by a spiking neural network with hidden layers. We provide analytical regret bounds for the global behavior of the network and analyze its asymptotic behavior and Vapnik-Chervonenkis dimension. In a numerical experiment, we confirm the learning capacity of the proposed chemical reaction network for classifying handwritten digits in pixel images, and we show that it solves the task more accurately and efficiently than a spiking neural network with hidden layers. This provides a motivation for machine learning in chemical computers and a mathematical explanation for how biological cells might exhibit more efficient learning behavior within biochemical reaction networks than neuronal networks.

</details>

---

### 37. [Paper Title: LoV3D: Grounding Cognitive Prognosis Reasoning in Longitudinal 3D Brain MRI via Regional Volume Assessments](https://arxiv.org/abs/2603.12071)

**基本信息**

- 🔗 arXiv: [`2603.12071`](https://arxiv.org/abs/2603.12071)
- 👥 作者: Zhaoyang Jiang, Zhizhong Fu, David McAllister 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12071.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于3D医学影像分析的、可解释的多模态大模型（LoV3D）。其技术路径（结合视觉编码器、语言模型、领域知识约束、可追溯推理）与构建用于“质谱结构推理”的化学多模态大模型（结合质谱编码器、语言模型、化学知识约束）在方法论上高度同构，提供了完整且先进的参考范例。

**📖 中文摘要**

论文提出了LoV3D，一个用于训练3D视觉-语言模型的流程，用于读取纵向3D脑部MRI，产生区域级解剖学评估，进行与先前扫描的纵向比较，并最终输出诊断类别和合成诊断摘要。该流程通过强制标签一致性、纵向连贯性和生物学合理性来夯实最终诊断，减少了幻觉风险。训练过程引入了一个临床加权的验证器，根据标准化体积指标自动评分候选输出，驱动无需人工标注的直接偏好优化。这项工作将3D视觉（MRI）、语言模型和领域知识（神经解剖学）深度融合，构建了一个用于医学影像分析的可解释、可追溯的大模型。其技术框架——多模态大模型在结构化领域知识引导下进行推理与报告生成——对于构建用于质谱解析、谱图推理的“化学大模型”具有极强的示范意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Longitudinal brain MRI is essential for characterizing the progression of neurological diseases such as Alzheimer's disease assessment. However, current deep-learning tools fragment this process: classifiers reduce a scan to a label, volumetric pipelines produce uninterpreted measurements, and vision-language models (VLMs) may generate fluent but potentially hallucinated conclusions. We present LoV3D, a pipeline for training 3D vision-language models, which reads longitudinal T1-weighted brain MRI, produces a region-level anatomical assessment, conducts longitudinal comparison with the prior scan, and finally outputs a three-class diagnosis (Cognitively Normal, Mild Cognitive Impairment, or Dementia) along with a synthesized diagnostic summary. The stepped pipeline grounds the final diagnosis by enforcing label consistency, longitudinal coherence, and biological plausibility, thereby reducing the risks of hallucinations. The training process introduces a clinically-weighted Verifier that scores candidate outputs automatically against normative references derived from standardized volume metrics, driving Direct Preference Optimization without a single human annotation. On a subject-level held-out ADNI test set (479 scans, 258 subjects), LoV3D achieves 93.7% three-class diagnostic accuracy (+34.8% over the no-grounding baseline), 97.2% on two-class diagnosis accuracy (+4% over the SOTA) and 82.6% region-level anatomical classification accuracy (+33.1% over VLM baselines). Zero-shot transfer yields 95.4% on MIRIAD (100% Dementia recall) and 82.9% three-class accuracy on AIBL, confirming high generalizability across sites, scanners, and populations. Code is available at this https URL .

</details>

---

### 38. [A Multi-Label Temporal Convolutional Framework for Transcription Factor Binding Characterization](https://arxiv.org/abs/2603.12073)

**基本信息**

- 🔗 arXiv: [`2603.12073`](https://arxiv.org/abs/2603.12073)
- 👥 作者: Pietro Demurtas, Ferdinando Zanchetta, Giovanni Perini 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用深度学习模型（TCN）对生物序列数据进行多标签预测与关联分析。这种方法论与“质谱结构推理”中利用深度学习模型从质谱数据中同时推断多个分子结构特征的任务在问题定义和技术路线上高度相关，可作为构建质谱多标签预测模型的参考。

**📖 中文摘要**

论文将DNA转录因子结合位点识别作为一个多标签分类问题进行研究，基于时间卷积网络构建深度学习模型，能够预测多个TF的结合谱，捕获TF之间的相关性及其协同调控机制。研究结果表明，多标签学习可以揭示具有生物学意义的基序和共结合模式。虽然研究领域是生物信息学，但其核心方法——使用深度学习模型（TCN）处理序列数据（DNA），以预测多个相关标签（TF结合）并揭示其内在关联——与“质谱结构推理”中利用深度学习模型处理质谱数据，以同时预测多个分子子结构或属性，并理解其谱图-结构关联的模式高度相似。论文为处理复杂的、多标签的谱图-结构映射问题提供了模型架构和思路上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transcription factors (TFs) regulate gene expression through complex and co-operative mechanisms. While many TFs act together, the logic underlying TFs binding and their interactions is not fully understood yet. Most current approaches for TF binding site prediction focus on individual TFs and binary classification tasks, without a full analysis of the possible interactions among various TFs. In this paper we investigate DNA TF binding site recognition as a multi-label classification problem, achieving reliable predictions for multiple TFs on DNA sequences retrieved in public repositories. Our deep learning models are based on Temporal Convolutional Networks (TCNs), which are able to predict multiple TF binding profiles, capturing correlations among TFs andtheir cooperative regulatory mechanisms. Our results suggest that multi-label learning leading to reliable predictive performances can reveal biologically meaningful motifs and co-binding patterns consistent with known TF interactions, while also suggesting novel relationships and cooperation among TFs.

</details>

---

### 39. [Hybrid Quantum-Classical Encoding for Accurate Residue-Level pKa Prediction](https://arxiv.org/abs/2603.11061)

**基本信息**

- 🔗 arXiv: [`2603.11061`](https://arxiv.org/abs/2603.11061)
- 👥 作者: Van Le, Tan Le
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11061.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕开发用于蛋白质性质（pKa）预测的混合量子-经典模型框架，这属于化学信息学中利用先进计算模型（包括大模型概念）进行分子性质预测和结构推理的范畴。

**📖 中文摘要**

本文提出了一种用于准确预测残基水平pKa值的可重现混合量子-经典框架。该框架通过高斯核基的量子启发特征映射来丰富残基水平的表示，这些量子增强描述符与归一化的结构特征相结合，形成统一的混合编码，并由深度量子神经网络（DQNN）进行处理。该架构捕获了残基微环境中经典模型无法访问的非线性关系。在多个精选描述符集上的基准测试表明，相对于经典基线模型，DQNN实现了改进的跨上下文泛化能力。在PKAD-R实验基准和Aβ40案例研究上的外部评估进一步凸显了量子启发表示的鲁棒性和可迁移性。通过将量子启发特征变换与经典生化描述符相结合，这项工作为残基水平pKa预测和蛋白质静电学中更广泛的应用建立了一种可扩展且具有实验可迁移性的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of residue-level pKa values is essential for understanding protein function, stability, and reactivity. While existing resources such as DeepKaDB and CpHMD-derived datasets provide valuable training data, their descriptors remain primarily classical and often struggle to generalize across diverse biochemical environments. We introduce a reproducible hybrid quantum-classical framework that enriches residue-level representations with a Gaussian kernel-based quantum-inspired feature mapping. These quantum-enhanced descriptors are combined with normalized structural features to form a unified hybrid encoding processed by a Deep Quantum Neural Network (DQNN). This architecture captures nonlinear relationships in residue microenvironments that are not accessible to classical models. Benchmarking across multiple curated descriptor sets demonstrates that the DQNN achieves improved cross-context generalization relative to classical baselines. External evaluation on the PKAD-R experimental benchmark and an A$\beta$40 case study further highlights the robustness and transferability of the quantum-inspired representation. By integrating quantum-inspired feature transformations with classical biochemical descriptors, this work establishes a scalable and experimentally transferable approach for residue-level pKa prediction and broader applications in protein electrostatics.

</details>

---

### 40. [From Phase Prediction to Phase Design: A ReAct Agent Framework for High-Entropy Alloy Discovery](https://arxiv.org/abs/2603.11068)

**基本信息**

- 🔗 arXiv: [`2603.11068`](https://arxiv.org/abs/2603.11068)
- 👥 作者: Iman Peivaste, Salim Belouettar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11068.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（LLM）智能体进行高熵合金的逆设计，这直接涉及化学信息学中利用“化学大模型”（LLM作为智能体核心）进行材料发现和设计的主题。

**📖 中文摘要**

本文提出了一种ReAct（推理+行动）大型语言模型（LLM）智能体框架，用于高熵合金（HEA）的发现。该智能体能够自主提出、验证并迭代优化HEA成分，以可靠地形成目标晶体相。它通过查询一个基于4,753个实验记录（涵盖FCC、BCC、BCC+FCC、BCC+IM四个相）训练并校准的XGBoost代理模型来实现，该模型准确率达到94.66%。与贝叶斯优化和随机搜索基线相比，该智能体在描述符空间中对于FCC、BCC和BCC+FCC相的重新发现率分别为38%、18%和38%，且其提出的成分比随机搜索更接近实验相流形。消融实验表明，领域先验知识引导智能体从回忆已知合金转向探索成分多样性。这项工作将LLM引导的智能体推理确立为一种有原则、透明且对流形敏感的逆合金设计方法，是对无梯度优化的补充。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering high-entropy alloy (HEA) compositions that reliably form a target crystal phase is a high-dimensional inverse design problem that conventional trial-and-error experimentation and forward-only machine learning models cannot efficiently solve. Here we present a ReAct (Reasoning + Acting) LLM agent that autonomously proposes, validates, and iteratively refines HEA compositions by querying a calibrated XGBoost surrogate trained on 4,753 experimental records across four phases (FCC, BCC, BCC+FCC, BCC+IM), achieving 94.66\% accuracy (F1 macro = 0.896). Against Bayesian optimisation (BO) and random search baselines, the full-prompt agent achieves descriptor-space rediscovery rates of 38\%, 18\%, and 38\% for FCC, BCC, and BCC+FCC (Mann--Whitney $p \leq 0.039$), with proposals lying 2.4--22.8$\times$ closer to the experimental phase manifold than random search. An ablation reveals that domain priors shift the agent from landmark-alloy recall toward compositionally diverse exploration -- an uninformed agent scores higher rediscovery by concentrating on literature-dense families, while the full-prompt agent explores underrepresented space (unique ratio 1.0 vs.\ 0.39 for BCC+FCC). These regimes represent distinct criteria: proximity to known literature versus genuine discovery. Spearman analysis confirms agent reasoning is statistically aligned with empirical phase distributions ($\rho = 0.736$, $p = 0.004$ for BCC). This work establishes LLM-guided agentic reasoning as a principled, transparent, and manifold-aware complement to gradient-free optimisation for inverse alloy design.

</details>

---

### 41. [Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction](https://arxiv.org/abs/2603.11125)

**基本信息**

- 🔗 arXiv: [`2603.11125`](https://arxiv.org/abs/2603.11125)
- 👥 作者: Yining Qian, Pengjie Wang, Yixiao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11125.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型的通用化药物-靶标亲和力预测框架。这直接涉及化学信息学中利用生成式模型（扩散模型作为一类重要的大模型）进行分子性质预测和相互作用推理的主题。

**📖 中文摘要**

本文提出了Co-Diffusion，一种新颖的亲和力感知框架，将药物-靶标亲和力（DTA）预测重新定义为约束潜在去噪过程以增强泛化能力。Co-Diffusion采用两阶段范式：第一阶段在显式监督目标下对齐药物和靶标嵌入，建立亲和力引导的潜在流形，确保潜在空间反映内在的结合景观。第二阶段引入模态特定的潜在扩散作为随机扰动-去噪正则化器，迫使模型从噪声结构表示中恢复一致的亲和力语义。该方法有效缓解了生成式DTA模型中常见的重建-回归冲突。理论分析表明，Co-Diffusion最大化了药物结构、蛋白质序列和结合强度的联合似然变分下界。在多个基准上的广泛实验表明，Co-Diffusion显著优于最先进的基线模型，特别是在未见过的分子支架和新蛋白质家族上表现出卓越的零样本泛化能力，为在未探索化学空间中进行计算机药物优先排序铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II introduces modality-specific latent diffusion as a stochastic perturb-and-denoise regularizer, forcing the model to recover consistent affinity semantics from noisy structural representations. This approach effectively mitigates the reconstruction-regression conflict common in generative DTA models. Theoretically, we show that Co-Diffusion maximizes a variational lower bound on the joint likelihood of drug structures, protein sequences, and binding strength. Extensive experiments across multiple benchmarks demonstrate that Co-Diffusion significantly outperforms state-of-the-art baselines, particularly yielding superior zero-shot generalization on unseen molecular scaffolds and novel protein families-paving a robust path for in silico drug prioritization in unexplored chemical spaces.

</details>

---

### 42. [A Unified Latent Space Disentanglement VAE Framework with Robust Disentanglement Effectiveness Evaluation](https://arxiv.org/abs/2603.11242)

**基本信息**

- 🔗 arXiv: [`2603.11242`](https://arxiv.org/abs/2603.11242)
- 👥 作者: Xiaoan Lang, Fang Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11242.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是开发一个用于生成和评估解耦潜在表示的通用框架。这在化学信息学中直接相关于构建可解释、稳健的化学大模型，因为化学大模型的核心目标之一就是从数据中学习有意义的、解耦的分子或材料表示。

**📖 中文摘要**

本文提出了一个统一的变分自编码器（VAE）框架bfVAE，用于生成有效的潜在空间解耦，特别适用于表格数据。为了评估VAE解耦技术的有效性，作者提出了两种无需真实生成因子知识的评估程序（FVH-LT和DBSR-LS）以及一个总体解耦指数（LSDI）。该工作与化学信息学中构建可解释的化学表示（化学大模型的核心任务之一）高度相关，因为它提供了一个通用的、可评估的框架来学习解耦的、语义有意义的潜在表示，这对于构建理解化学结构和性质的稳健模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating and interpreting latent representations, such as variational autoencoders (VAEs), remains a significant challenge for diverse data types, especially when ground-truth generative factors are unknown. To address this, we propose a general framework -- bfVAE -- that unifies several state-of-the-art disentangled VAE approaches and generates effective latent space disentanglement, especially for tabular data. To assess the effectiveness of a VAE disentanglement technique, we propose two procedures - Feature Variance Heterogeneity via Latent Traversal (FVH-LT) and Dirty Block Sparse Regression in Latent Space (DBSR-LS) for disentanglement assessment, along with the latent space disentanglement index (LSDI) which uses the outputs of FVH-LT and DBSR-LS to summarize the overall effectiveness of a VAE disentanglement method without requiring access to or knowledge of the ground-truth generative factors. To the best of our knowledge, these are the first assessment tools to achieve this. FVH-LT and DBSR-LS also enhance latent space interpretability and provide guidance on more efficient content generation. To ensure robust and consistent disentanglement, we develop a greedy alignment strategy (GAS) that mitigates label switching and aligns latent dimensions across runs to obtain aggregated results. We assess the bfVAE framework and validate FVH-LT, DBSR-LS, and LSDI in extensive experiments on tabular and image data. The results suggest that bfVAE surpasses existing disentangled VAE frameworks in terms of disentanglement quality, robustness, achieving a near-zero false discovery rate for informative latent dimensions, that FVH-LT and DBSR-LS reliably uncover semantically meaningful and domain-relevant latent structures, and that LSDI makes an effective overall quantitative summary on disentanglement effectiveness.

</details>

---

### 43. [A Standardized Framework For Evaluating Gene Expression Generative Models](https://arxiv.org/abs/2603.11244)

**基本信息**

- 🔗 arXiv: [`2603.11244`](https://arxiv.org/abs/2603.11244)
- 👥 作者: Andrea Rubbi, Andrea Giuseppe Di Francesco, Mohammad Lotfollahi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11244.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是建立生成模型的标准化评估框架。这与“化学大模型”领域直接相关，因为化学中的分子生成、性质预测等大模型同样迫切需要可靠、标准化且具有领域意义（如化学合理性）的评估方法。

**📖 中文摘要**

本文提出了一个用于评估单细胞基因表达生成模型的标准化框架GGE。它解决了当前评估实践中指标不一致、超参数不可比以及缺乏生物学基础指标的问题。GGE提供了一套全面的分布度量，并引入了基于差异表达基因（DEG）的分析和扰动效应相关性等生物学驱动的评估方法。虽然应用领域是生物信息学，但其核心贡献——为生成模型建立标准化、可重复的评估协议——与“化学大模型”主题高度相关。在化学领域，评估分子生成模型、性质预测模型等同样面临类似的挑战（如指标不一致、缺乏化学意义的评估）。该工作为如何系统评估生成模型提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid development of generative models for single-cell gene expression data has created an urgent need for standardised evaluation frameworks. Current evaluation practices suffer from inconsistent metric implementations, incomparable hyperparameter choices, and a lack of biologically-grounded metrics. We present Generated Genetic Expression Evaluator (GGE), an open-source Python framework that addresses these challenges by providing a comprehensive suite of distributional metrics with explicit computation space options and biologically-motivated evaluation through differentially expressed gene (DEG)-focused analysis and perturbation-effect correlation, enabling standardized reporting and reproducible benchmarking. Through extensive analysis of the single-cell generative modeling literature, we identify that no standardized evaluation protocol exists. Methods report incomparable metrics computed in different spaces with different hyperparameters. We demonstrate that metric values vary substantially depending on implementation choices, highlighting the critical need for standardization. GGE enables fair comparison across generative approaches and accelerates progress in perturbation response prediction, cellular identity modeling, and counterfactual inference.

</details>

---

### 44. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1：论文的核心是构建一个结合领域专用嵌入模型和大型语言模型的交互式分析框架。这直接对应于“化学大模型”的研究方向，即如何将化学领域的预训练模型（如分子表示模型）与LLM的能力相结合，以创建更强大、更可解释的化学AI工具。

**📖 中文摘要**

本文介绍了ELISA（Embedding-Linked Interactive Single-cell Agent），一个将单细胞RNA测序（scRNA-seq）数据嵌入（通过scGPT）与自然语言理解（通过BioBERT和LLM）相结合的可解释框架，用于交互式单细胞发现。它通过自动查询分类器将用户输入路由到不同的分析管道（如基因标记评分、语义匹配），并集成了通路活性评分、配体-受体相互作用预测等模块。该框架在多个scRNA-seq数据集上进行了验证。虽然应用于生物医学，但其核心思想——将领域特定的嵌入模型（scGPT）与大型语言模型（LLM）桥接，以创建可解释的、交互式的数据分析智能体——与“化学大模型”的主题高度契合。在化学信息学中，类似地可以将分子表示模型（如图神经网络）与LLM结合，构建用于分子设计、性质探索或质谱解析的交互式智能体。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 45. [Proof-Carrying Materials: Falsifiable Safety Certificates for Machine-Learned Interatomic Potentials](https://arxiv.org/abs/2603.12183)

**基本信息**

- 🔗 arXiv: [`2603.12183`](https://arxiv.org/abs/2603.12183)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12183.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和保证机器学习原子间势（一种重要的化学/材料大模型）的可靠性。它直接围绕如何使化学大模型在实际应用中更安全、更可信这一主题，提出了一个系统的审计和认证框架。

**📖 中文摘要**

本文提出了“Proof-Carrying Materials (PCM)”，一个为机器学习原子间势（MLIPs）提供可证伪安全证书的框架。PCM通过三个阶段（对抗性证伪、引导包络细化、Lean 4形式化认证）来审计MLIPs的可靠性，发现不同架构的MLIPs存在特定的盲点。该工作还训练了一个风险模型来预测未见材料的失败。在一个热电材料筛选的案例研究中，经过PCM审计的协议比单一MLIP筛选多发现了25%的稳定材料。这项工作直接针对机器学习在材料科学中的应用，其核心是提高化学/材料大模型（此处为原子间势）的可靠性和安全性，这是化学大模型投入实际应用（如高通量筛选）的关键前提。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learned interatomic potentials (MLIPs) are deployed for high-throughput materials screening without formal reliability guarantees. We show that a single MLIP used as a stability filter misses 93% of density functional theory (DFT)-stable materials (recall 0.07) on a 25,000-material benchmark. Proof-Carrying Materials (PCM) closes this gap through three stages: adversarial falsification across compositional space, bootstrap envelope refinement with 95% confidence intervals, and Lean 4 formal certification. Auditing CHGNet, TensorNet and MACE reveals architecture-specific blind spots with near-zero pairwise error correlations (r <= 0.13; n = 5,000), confirmed by independent Quantum ESPRESSO validation (20/20 converged; median DFT/CHGNet force ratio 12x). A risk model trained on PCM-discovered features predicts failures on unseen materials (AUC-ROC = 0.938 +/- 0.004) and transfers across architectures (cross-MLIP AUC-ROC ~ 0.70; feature importance r = 0.877). In a thermoelectric screening case study, PCM-audited protocols discover 62 additional stable materials missed by single-MLIP screening - a 25% improvement in discovery yield.

</details>

---

### 46. [drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network](https://arxiv.org/abs/2405.08979)

**基本信息**

- 🔗 arXiv: [`2405.08979`](https://arxiv.org/abs/2405.08979)
- 👥 作者: Yoshitaka Inoue, Hunmin Lee, Tianfan Fu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.08979.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个基于图注意力网络的、可解释的预测模型，用于处理药物、基因等化学/生物实体。这与化学信息学中构建可解释的、基于图的化学大模型（用于分子性质预测、反应预测等）的研究主题直接相关。

**📖 中文摘要**

本文提出了drGT模型，一个基于药物-细胞-基因异质图注意力网络的深度学习模型，用于预测药物反应并辅助生物标志物识别。模型利用注意力系数（ACs）来解释其预测，通过文本挖掘PubMed摘要来验证高系数基因与特定药物的共现关系，并利用ACs进行富集分析以识别药物影响的生物过程。虽然主要应用于药物发现和生物信息学，但其核心方法——使用图神经网络处理化学/生物实体（药物、基因）及其复杂关系，并利用注意力机制提供可解释性——与化学信息学中构建可解释的化学大模型（如预测分子性质、反应产率）高度相关。模型对异质图的处理和解释性分析为化学大模型的设计提供了参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A challenge in drug response prediction is result interpretation compared to established knowledge. drGT is a graph deep learning model that predicts sensitivity and aids in biomarker identification using attention coefficients (ACs). drGT leverages a heterogeneous graph composed of relationships drawn from drugs, genes, and cell line responses. The model is trained and evaluated using major benchmark datasets: Sanger GDSC, NCI60, and Broad CTRP, which cover a wide range of drugs and cancer cell lines. drGT demonstrates AUROC of up to 94.5% under random splitting, 84.4% for unseen drugs, and 70.6% for unseen cell lines, comparable to existing benchmark methods while also providing interpretability. Regarding interpretability, we review drug-gene co-occurrences by text-mining PubMed abstracts for high-coefficient genes mentioning particular drugs. Across 976 drugs from NCI60 with known drug-target interactions (DTIs), model predictions utilized both known DTIs (36.9%) as well as additional predictive associations, many supported by literature. In addition, we compare the drug-gene associations identified by drGT with those from an established DTI prediction model and find that 63.67% are supported by either PubMed literature or predictions from the DTI model. Further, we describe the utilization of ACs to identify affected biological processes by each drug via enrichment analyses, thereby enhancing biological interpretability. Code is available at this https URL .

</details>

---

### 47. [Using LLM-Generated Draft Replies to Support Human Experts in Responding to Stakeholder Inquiries in Maritime Industry: A Real-World Case Study of Industrial AI](https://arxiv.org/abs/2412.12732)

**基本信息**

- 🔗 arXiv: [`2412.12732`](https://arxiv.org/abs/2412.12732)
- 👥 作者: Tita Alissa Bach, Aleksandar Babic, Narae Park 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.12732.pdf)

**💡 相关性分析**

满足标准1：论文的核心是研究大型语言模型（LLM）在专业工业领域（航海）中作为人类专家助手的实际应用、效用和局限性。这直接关联到“化学大模型”主题中一个关键的研究方向：即化学领域的大模型（包括LLM和专用模型）如何在实际化学研究和工作流中有效地辅助化学家，并确保其输出的可靠性和安全性。

**📖 中文摘要**

本文是一项关于在航海工业中使用LLM生成草稿回复以支持人类专家处理利益相关者询价的真实案例研究。研究通过初步研究、调查和文本相似性分析，探讨了LLM在专业领域工作流中的效用。研究发现，LLM草稿可以简化工作流，但通常需要大量修改以满足专业通信的特定需求；LLM在无人监督的情况下尚未成熟到可用于安全关键应用，但可以作为有价值的增强工具。这项研究虽然领域特定，但其核心——探索LLM（作为大模型的一种）在专业、安全关键领域的增强作用、局限性以及人机协作模式——与“化学大模型”主题相关。在化学领域，类似地需要研究LLM或化学领域大模型如何辅助化学家进行研究、撰写报告或分析数据，并理解其可靠性和人机交互的最佳实践。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The maritime industry requires effective communication among diverse stakeholders to address complex, safety-critical challenges. Industrial AI, including Large Language Models (LLMs), has the potential to augment human experts' workflows in this specialized domain. Our case study investigated the utility of LLMs in drafting replies to stakeholder inquiries and supporting case handlers. We conducted a preliminary study (observations and interviews), a survey, and a text similarity analysis (LLM-as-a-judge and Semantic Embedding Similarity). We discover that while LLM drafts can streamline workflows, they often require significant modifications to meet the specific demands of maritime communications. Though LLMs are not yet mature enough for safety-critical applications without human oversight, they can serve as valuable augmentative tools. Final decision-making thus must remain with human experts. However, by leveraging the strengths of both humans and LLMs, fostering human-AI collaboration, industries can increase efficiency while maintaining high standards of quality and precision tailored to each case.

</details>

---

### 48. [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177)

**基本信息**

- 🔗 arXiv: [`2501.15177`](https://arxiv.org/abs/2501.15177)
- 👥 作者: Yi Su, Jisheng Bai, Qisheng Xu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.15177.pdf)

**💡 相关性分析**

满足标准3：论文是一篇专门针对音频-语言模型（一种特定领域的大模型）的系统性综述。它为“化学大模型”领域提供了重要的相关讨论和参考框架，包括如何分类模型基础、评估进展以及识别未来方向，属于针对相关主题的综述展望。

**📖 中文摘要**

本文对音频-语言模型（ALMs）进行了首次系统性综述。ALMs是在音频-文本配对数据上训练的模型，旨在处理、理解和推理以音频为中心的多模态内容。综述涵盖了语音、音乐和声音领域的工作，提出了一个统一的ALM基础分类法（包括模型架构和训练目标），并建立了一个捕捉不同研究方面相互促进和制约关系的研究图景。虽然主题是音频，但作为一篇针对特定领域（音频）大模型（ALMs）的全面综述，其组织框架、对模型基础（架构、目标）的分析以及对未来趋势的展望，为“化学大模型”领域提供了宝贵的参考和类比。化学大模型同样涉及多模态（如分子结构、光谱、文本描述）和特定的领域挑战，这篇综述的方法论具有借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio-Language Models (ALMs), trained on paired audio-text data, are designed to process, understand, and reason about audio-centric multimodal content. Unlike traditional supervised approaches that use predefined labels, ALMs leverage natural language supervision to better handle complex real-world audio scenes with multiple overlapping events. While demonstrating impressive zero-shot and task generalization capabilities, there is still a notable lack of systematic surveys that comprehensively organize and analyze developments. In this paper, we present the first systematic review of ALMs with three main contributions: (1) comprehensive coverage of ALM works across speech, music, and sound from a general audio perspective; (2) a unified taxonomy of ALM foundations, including model architectures and training objectives; (3) establishment of a research landscape capturing mutual promotion and constraints among different research aspects, aiding in summarizing evaluations, limitations, concerns and promising directions. Our review contributes to helping researchers understand the development of existing technologies and future trends, while also providing valuable references for implementation in practical applications.

</details>

---

### 49. [Tuning-Free LLM Can Build A Strong Recommender Under Sparse Connectivity And Knowledge Gap Via Extracting Intent](https://arxiv.org/abs/2505.10900)

**基本信息**

- 🔗 arXiv: [`2505.10900`](https://arxiv.org/abs/2505.10900)
- 👥 作者: Wenqing Zheng, Noah Fatsi, Daniel Barcklow 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10900.pdf)

**💡 相关性分析**

满足标准1：论文的核心是使用免调优的LLM流程从文本数据中提取结构化“意图”以构建知识图谱进行推荐。这种方法论与“质谱结构推理”中从复杂数据（质谱）中提取化学结构信息的目标在概念上相关，为如何利用大模型从非结构化/复杂数据中提取关键语义特征（在化学中是结构特征）提供了思路。

**📖 中文摘要**

本文提出了LLM-based Intent Knowledge Graph Recommender (IKGR)，一个新颖的推荐框架。它利用免调优、RAG引导的LLM流程从外部知识源和用户资料中提取意图，构建一个以意图为中心的知识图谱，将用户和物品显式地链接到意图节点。为了缓解稀疏性，提出了互意图连接致密化策略。最后，在意图增强的图谱上使用轻量级GNN层进行推荐。该工作的核心创新在于使用LLM从文本中提取结构化意图（intent）作为连接用户和物品的桥梁。这与“质谱结构推理”问题有潜在关联：在质谱解析中，一个核心挑战是从质谱信号中推断出化学结构（“意图”）。IKGR中利用LLM从非结构化/半结构化数据（用户资料、物品描述）中提取语义意图的方法，可以类比为利用模型从质谱数据（及其可能的文本元数据）中提取化学结构信息或子结构“意图”，从而辅助构建谱图-结构关联知识库或推理模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in recommendation with large language models (LLMs) often rely on either commonsense augmentation at the item-category level or implicit intent modeling on existing knowledge graphs. However, such approaches struggle to capture grounded user intents and to handle sparsity and cold-start scenarios. In this work, we present LLM-based Intent Knowledge Graph Recommender (IKGR), a novel framework that constructs an intent-centric knowledge graph where both users and items are explicitly linked to intent nodes extracted by a tuning-free, RAG-guided LLM pipeline. By grounding intents in external knowledge sources and user profiles, IKGR canonically represents what a user seeks and what an item satisfies as first-class entities. To alleviate sparsity, we further introduce a mutual-intent connectivity densification strategy, which shortens semantic paths between users and long-tail items without requiring cross-graph fusion. Finally, a lightweight GNN layer is employed on top of the intent-enhanced graph to produce recommendation signals with low latency. Extensive experiments on public and enterprise datasets demonstrate that IKGR consistently outperforms strong baselines, particularly on cold-start and long-tail slices, while remaining efficient through a fully offline LLM pipeline.

</details>

---

### 50. [LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models](https://arxiv.org/abs/2505.19240)

**基本信息**

- 🔗 arXiv: [`2505.19240`](https://arxiv.org/abs/2505.19240)
- 👥 作者: Aida Kostikova, Zhipin Wang, Deidamea Bajri 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.19240.pdf)

**💡 相关性分析**

满足标准3：这是一篇针对大型语言模型（作为大模型的一种）局限性的综述论文，其分析框架、趋势洞察和发布的数据集对于理解和评估‘化学大模型’的潜在能力边界、研究挑战和未来方向具有重要的参考价值。

**📖 中文摘要**

这篇论文对大型语言模型（LLM）局限性研究（LLLMs）进行了数据驱动的综述，涵盖了从2022年到2025年初的文献。通过对ACL和arXiv中25万篇论文进行半自动化分析，识别出14,648篇相关论文，并利用主题聚类方法（如HDBSCAN+BERTopic和LlooM）分析了研究趋势。研究发现，LLM相关论文的占比在2022年至2025年间大幅增长，其中关于LLM局限性的研究增长更快，到2025年已占LLM论文的30%以上。最受关注的局限性主题包括推理、泛化、幻觉、偏见和安全性。该论文提供了一个带注释的摘要数据集和经过验证的方法论，可作为研究化学信息学或质谱分析领域大模型（化学大模型）潜在缺陷、挑战和发展方向的重要参考资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains the most studied limitation, followed by generalization, hallucination, bias, and security. The distribution of topics in the ACL dataset stays relatively stable over time, while arXiv shifts toward security risks, alignment, hallucinations, knowledge editing, and multimodality. We offer a quantitative view of trends in LLLMs research and release a dataset of annotated abstracts and a validated methodology, available at: this https URL .

</details>

---

### 51. [Can Theoretical Physics Research Benefit from Language Agents?](https://arxiv.org/abs/2506.06214)

**基本信息**

- 🔗 arXiv: [`2506.06214`](https://arxiv.org/abs/2506.06214)
- 👥 作者: Sirui Lu, Zhijing Jin, Terry Jingchen Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.06214.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容围绕如何使大模型（LLM）适应并服务于特定科学领域（如物理学）的研究，这直接类比于‘化学大模型’的主题。同时，论文包含了对领域专业化大模型发展路径的重要讨论和展望，具有综述和展望性质。

**📖 中文摘要**

本文探讨了语言智能体在理论物理学研究中的应用潜力与当前局限。作者指出，尽管大语言模型在数学推理和代码生成方面表现出色，但在物理直觉、约束满足和可靠推理方面存在关键差距。物理研究需要近似判断、对称性利用和物理基础，这要求AI智能体经过专门的物理推理模式训练，并配备物理感知的验证工具。论文呼吁物理和AI社区合作，开发特定领域的训练数据集、捕捉物理推理质量的奖励信号以及编码基本原理的验证框架。虽然主题是理论物理，但其核心论点是关于如何为特定科学领域（如化学、质谱）构建领域专业化的大模型/智能体，这与‘化学大模型’的主题高度相关。文中提出的构建领域专用AI智能体的愿景、所需的基础设施（如特定领域数据集、验证框架）可直接类比并应用于化学信息学和质谱分析领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are rapidly advancing across diverse domains, yet their application in theoretical physics remains inadequate. While current models show competence in mathematical reasoning and code generation, we identify critical gaps in physical intuition, constraint satisfaction, and reliable reasoning that cannot be addressed through prompting alone. Physics demands approximation judgment, symmetry exploitation, and physical grounding that require AI agents specifically trained on physics reasoning patterns and equipped with physics-aware verification tools. We argue that LLM would require such domain-specialized training and tooling to be useful in real-world for physics research. We envision physics-specialized AI agents that seamlessly handle multimodal data, propose physically consistent hypotheses, and autonomously verify theoretical results. Realizing this vision requires developing physics-specific training datasets, reward signals that capture physical reasoning quality, and verification frameworks encoding fundamental principles. We call for collaborative efforts between physics and AI communities to build the specialized infrastructure necessary for AI-driven scientific discovery.

</details>

---

### 52. [Text-Trained LLMs Can Zero-Shot Extrapolate PDE Dynamics, Revealing a Three-Stage In-Context Learning Mechanism](https://arxiv.org/abs/2509.06322)

**基本信息**

- 🔗 arXiv: [`2509.06322`](https://arxiv.org/abs/2509.06322)
- 👥 作者: Jiajun Bao, Nicolas Boullé, Toni J.B. Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.06322.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容展示了大型语言模型（作为大模型的一种）在无需领域特定训练的情况下，对科学数据（PDE解）进行结构推理和动态预测的能力。这种‘从数据中推理结构/动态’的能力与‘质谱结构推理’（从质谱数据推理分子结构）的研究主题在方法论和核心挑战上高度相似。

**📖 中文摘要**

本研究表明，仅通过文本训练的基础大语言模型（LLMs）能够从离散化的偏微分方程（PDE）解中准确推断时空动力学，而无需微调或自然语言提示。预测准确性随着时间上下文长度的增加而提高，但在更精细的空间离散化下会下降。在多步推演中，误差随时间范围代数增长，类似于经典有限差分求解器中的全局误差累积。作者将其解释为上下文神经缩放定律。为了理解LLMs如何处理PDE解以进行推演，作者分析了令牌级输出分布，揭示了一致的三阶段上下文学习进展：从语法模式模仿开始，经过探索性高熵阶段，最终形成自信的、基于数值的预测。这项研究展示了LLMs在建模和预测复杂科学系统（用PDE描述）动态方面的‘涌现’能力。虽然应用场景是物理PDE，但其中关于大模型从结构化数据（如离散化的PDE解，可类比于质谱数据或分子描述符）中学习并推理潜在模式和动态的机制，与‘质谱结构推理’和利用‘化学大模型’进行科学发现的核心思想密切相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated emergent in-context learning (ICL) capabilities across a range of tasks, including zero-shot time-series forecasting. We show that text-trained foundation models can accurately extrapolate spatiotemporal dynamics from discretized partial differential equation (PDE) solutions without fine-tuning or natural language prompting. Predictive accuracy improves with longer temporal contexts but degrades at finer spatial discretizations. In multi-step rollouts, where the model recursively predicts future spatial states over multiple time steps, errors grow algebraically with the time horizon, reminiscent of global error accumulation in classical finite-difference solvers. We interpret these trends as in-context neural scaling laws, where prediction quality varies predictably with both context length and output length. To better understand how LLMs are able to internally process PDE solutions so as to accurately roll them out, we analyze token-level output distributions and uncover a consistent three-stage ICL progression: beginning with syntactic pattern imitation, transitioning through an exploratory high-entropy phase, and culminating in confident, numerically grounded predictions.

</details>

---

### 53. [From Next Token Prediction to (STRIPS) World Models](https://arxiv.org/abs/2509.13389)

**基本信息**

- 🔗 arXiv: [`2509.13389`](https://arxiv.org/abs/2509.13389)
- 👥 作者: Carlos Núñez-Molina, Vicenç Gómez, Hector Geffner
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.13389.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索基于Transformer的大模型如何从序列数据中学习和表示结构化的世界模型（STRIPS）。这直接关联到‘化学大模型’和‘质谱结构推理’的核心问题之一，即如何让大模型从化学序列数据（如分子表示、质谱信号）中学习并推理出潜在的化学结构、规则或动力学模型。

**📖 中文摘要**

本研究在一个受控的符号设置中探讨了下一个令牌预测是否能产生真正支持规划的世界模型，其中命题STRIPS动作模型仅从动作轨迹中学习，并且可以精确评估正确性。作者引入了两种架构：一种是基于符号对齐的STRIPS Transformer，另一种是没有内置显式符号结构的标准Transformer架构。评估表明，这两种方法都可以用于生成支持在指数级未见初始状态和目标上进行规划的模型。这项研究本质上是在探究大语言模型（通过下一个令牌预测训练）如何从序列数据（动作轨迹）中学习和表示结构化的世界模型（STRIPS模型）。这对于‘化学大模型’或‘质谱结构推理’具有启示意义：它展示了如何利用基于Transformer的模型从序列化或结构化的化学数据（如SMILES字符串、质谱峰序列）中学习潜在的、可推理的化学规则或结构模型，从而支持分子设计、反应预测或质谱解析等任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study whether next-token prediction can yield world models that truly support planning, in a controlled symbolic setting where propositional STRIPS action models are learned from action traces alone and correctness can be evaluated exactly. We introduce two architectures. The first is the STRIPS Transformer, a symbolically aligned model grounded in theoretical results linking transformers and the formal language structure of STRIPS domains. The second is a standard transformer architecture without explicit symbolic structure built in, for which we study different positional encoding schemes and attention aggregation mechanisms. We evaluate both architectures on five classical planning domains, measuring training accuracy, generalization, and planning performance across domains and problem sizes. Interestingly, both approaches can be used to produce models that support planning with off-the-shelf STRIPS planners over exponentially many unseen initial states and goals. Although the STRIPS Transformer incorporates a strong symbolic inductive bias, it is harder to optimize and requires larger datasets to generalize reliably. In contrast, a standard transformer with stick-breaking attention achieves near-perfect training accuracy and strong generalization. Finally, standard transformers without stick-breaking attention do not generalize to long traces, whereas a symbolic STRIPS model extracted from a transformer trained on shorter traces does.

</details>

---

### 54. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是构建和评估一个自主的AI科学家系统（Jr. AI Scientist），该系统本质上是一个由大语言模型驱动、用于自动化科学研究的‘大模型’应用。这直接属于‘化学大模型’的应用范畴。同时，论文对当前AI科学家系统的能力、局限性和风险进行了深入分析和展望，具有重要的综述和讨论价值。

**📖 中文摘要**

本文介绍了Jr. AI Scientist，一个最先进的自主AI科学家系统，它模拟了新手学生研究人员的核心研究工作流程：在给定人类导师的基线论文后，系统分析其局限性，提出改进的新假设，进行迭代实验直至取得改进，并撰写结果论文。该系统利用现代编码智能体处理复杂的多文件实现。作者通过实验使Jr. AI Scientist成功生成了基于真实NeurIPS、IJCV和ICLR工作的新研究论文。评估包括使用AI Reviewer进行自动评估、作者主导的评估以及向Agents4Science投稿。论文还全面报告了开发过程中发现的各种风险。这项研究阐明了当前AI科学家系统的角色和局限性，为了解哪些领域仍需要人类专业知识以及这些系统进化中可能出现的风险提供了见解。这项工作与‘化学大模型’主题高度相关，因为它展示了一个由大语言模型驱动的、能够进行假设生成、实验和论文撰写的自主科学研究框架。该框架可以应用于化学信息学和质谱分析领域，用于自动发现分子性质关系、优化质谱解析算法或生成新的研究假设。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the current capabilities and risks of AI Scientist systems (autoresearch) is essential for ensuring trustworthy and sustainable AI-driven scientific progress while preserving the integrity of the academic ecosystem. To this end, we develop Jr. AI Scientist, a state-of-the-art autonomous AI scientist system that mimics the core research workflow of a novice student researcher: Given the baseline paper from the human mentor, it analyzes its limitations, formulates novel hypotheses for improvement, iteratively experiments until improvements are achieved, and writes a paper with the results. Unlike previous approaches that assume full automation or operate on small-scale code, Jr. AI Scientist follows a well-defined research workflow and leverages modern coding agents to handle complex, multi-file implementations, leading to scientifically valuable contributions. Through our experiments, the Jr. AI Scientist successfully generated new research papers that build upon real NeurIPS, IJCV, and ICLR works by proposing and implementing novel methods. For evaluation, we conducted automated assessments using AI Reviewers, author-led evaluations, and submissions to Agents4Science, a venue dedicated to AI-driven contributions. The findings demonstrate that Jr. AI Scientist generates papers receiving higher review scores by DeepReviewer than existing fully automated systems. Nevertheless, we identify important limitations from the author evaluation and the Agents4Science reviews, indicating the potential risks of directly applying current AI Scientist systems and key challenges for future research. Finally, we comprehensively report various risks identified during development. We believe this study clarifies the current role and limitations of AI Scientist systems, offering insights into the areas that still require human expertise and the risks that may emerge as these systems evolve.

</details>

---

### 55. [Beyond the Black Box: A Survey on the Theory and Mechanism of Large Language Models](https://arxiv.org/abs/2601.02907)

**基本信息**

- 🔗 arXiv: [`2601.02907`](https://arxiv.org/abs/2601.02907)
- 👥 作者: Zeyu Gan, Ruifeng Ren, Wei Yao 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.02907.pdf)

**💡 相关性分析**

满足标准3：论文是关于大语言模型理论与机制的综合性综述，其内容为理解和构建“化学大模型”提供了重要的理论基础和系统性讨论。

**📖 中文摘要**

本文是一篇关于大语言模型理论与机制的综合综述。虽然不专门针对化学信息学，但它提出了一个基于生命周期的统一分类法，系统性地回顾了驱动LLM性能的基础理论和内部机制，涵盖了数据准备、模型准备、训练、对齐、推理和评估等六个阶段。论文分析了诸如数据混合的数学原理、各种架构的表征极限以及对齐算法的优化动力学等核心理论问题。对于旨在构建或理解“化学大模型”（即应用于化学领域的LLM或跨模态大模型）的研究者而言，这篇综述提供了关于大模型理论基础、内部工作机制和前沿挑战的全面、结构化的路线图，是重要的背景知识和理论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid emergence of Large Language Models (LLMs) has precipitated a profound paradigm shift in Artificial Intelligence, delivering monumental engineering successes that increasingly impact modern society. However, a critical paradox persists within the current field: despite the empirical efficacy, our theoretical understanding of LLMs remains disproportionately nascent, forcing these systems to be treated largely as ``black boxes''. To address this theoretical fragmentation, this survey proposes a unified lifecycle-based taxonomy that organizes the research landscape into six distinct stages: Data Preparation, Model Preparation, Training, Alignment, Inference, and Evaluation. Within this framework, we provide a systematic review of the foundational theories and internal mechanisms driving LLM performance. Specifically, we analyze core theoretical issues such as the mathematical justification for data mixtures, the representational limits of various architectures, and the optimization dynamics of alignment algorithms. Moving beyond current best practices, we identify critical frontier challenges, including the theoretical limits of synthetic data self-improvement, the mathematical bounds of safety guarantees, and the mechanistic origins of emergent intelligence. By connecting empirical observations with rigorous scientific inquiry, this work provides a structured roadmap for transitioning LLM development from engineering heuristics toward a principled scientific discipline.

</details>

---

### 56. [De novo molecular structure elucidation from mass spectra via flow matching](https://arxiv.org/abs/2602.19912)

**基本信息**

- 🔗 arXiv: [`2602.19912`](https://arxiv.org/abs/2602.19912)
- 👥 作者: Ghaith Mqawass, Tuan Le, Fabian Theis 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.19912.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，旨在解决从质谱数据中推断分子结构的逆问题。

**📖 中文摘要**

本文提出MSFlow，一个用于从质谱数据中从头解析分子结构的两阶段流匹配生成模型。该工作直接针对“质谱结构推理”这一核心主题，旨在解决将质谱翻译为完整分子结构这一困难且定义不明确的逆问题。模型第一阶段使用公式限制的Transformer将质谱编码为连续且具有化学信息性的嵌入空间；第二阶段训练一个解码器流匹配模型，从质谱的潜在嵌入中重建分子。作者进行了严格的评估，表明MSFlow能够将高达45%的分子质谱准确翻译为相应的分子表示，比现有技术水平提升了高达14倍。这项工作为质谱分析领域提供了强大的新工具，并公开了训练好的模型供非商业用户使用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedding space, while in the second stage, we train a decoder flow matching model to reconstruct molecules from latent embeddings of mass spectra. We present ablation studies demonstrating the importance of using information-preserving molecular descriptors for encoding mass spectra and motivate the use of our discrete flow-based decoder. Our rigorous evaluation demonstrates that MSFlow can accurately translate up to 45 percent of molecular mass spectra into their corresponding molecular representations - an improvement of up to fourteen-fold over the current state-of-the-art. A trained version of MSFlow is made publicly available on GitHub for non-commercial users.

</details>

---

### 57. [Beyond Explainable AI (XAI): An Overdue Paradigm Shift and Post-XAI Research Directions](https://arxiv.org/abs/2602.24176)

**基本信息**

- 🔗 arXiv: [`2602.24176`](https://arxiv.org/abs/2602.24176)
- 👥 作者: Saleh Afroogh, Seyd Ishtiaque Ahmed, Petra Ahrweiler 等49人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.24176.pdf)

**💡 相关性分析**

满足标准3：论文包含对当前AI（尤其是大模型）解释性方法的批判性讨论和重要的范式展望，这些讨论对于负责任地开发和应用“化学大模型”具有重要的相关性和指导意义。

**📖 中文摘要**

本文对可解释人工智能（XAI）领域进行了跨学科审视，重点讨论了深度神经网络和大语言模型，并指出了当前XAI在实证和概念上的局限性。作者揭示了该领域存在的根本问题（如两个悖论、两个概念混淆和五个错误假设），并提出了超越XAI局限性的综合范式转变。虽然论文主题是XAI，但其对当前大模型（包括LLMs）解释性方法的批判性分析，以及提出的向可靠和可认证AI发展的新研究方向（如交互式AI、AI认识论），对于任何计划开发或评估“化学大模型”的研究都具有高度相关性。在化学信息学中，模型的可信度、可解释性和可靠性至关重要，这篇论文提供的视角和未来方向有助于在该领域设计更可靠、用户可感知的AI系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study provides a cross-disciplinary examination of Explainable Artificial Intelligence (XAI) approaches-focusing on deep neural networks (DNNs) and large language models (LLMs)-and identifies empirical and conceptual limitations in current XAI. We discuss critical symptoms that stem from deeper root causes (i.e., two paradoxes, two conceptual confusions, and five false assumptions). These fundamental problems within the current XAI research field reveal three insights: experimentally, XAI exhibits significant flaws; conceptually, it is paradoxical; and pragmatically, further attempts to reform the paradoxical XAI might exacerbate its confusion-demanding fundamental shifts and new research directions. To move beyond XAI's limitations, we propose a four-pronged synthesized paradigm shift toward reliable and certified AI development. These four components include: verification-focused Interactive AI (IAI) to establish scientific community protocols for certifying AI system performance rather than attempting post-hoc explanations, AI Epistemology for rigorous scientific foundations, User-Sensible AI to create context-aware systems tailored to specific user communities, and Model-Centered Interpretability for faithful technical analysis-together offering comprehensive post-XAI research directions.

</details>

---

### 58. [On the Value of Tokeniser Pretraining in Physics Foundation Models](https://arxiv.org/abs/2603.05598)

**基本信息**

- 🔗 arXiv: [`2603.05598`](https://arxiv.org/abs/2603.05598)
- 👥 作者: Hadi Sotoudeh, Payel Mukhopadhyay, Ruben Ohana 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05598.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（分词器预训练、两阶段训练、领域对齐）对于构建和理解“化学大模型”的训练流程和效率优化具有直接的相关性和重要的参考价值。

**📖 中文摘要**

本文研究了分词器预训练对物理仿真基础模型精度和效率的影响。虽然论文主要关注物理仿真，但其核心方法——使用自编码目标预训练分词器，然后训练动力学模型——与构建“化学大模型”的训练范式高度相关。论文系统性地探讨了将高分辨率时空数据压缩为紧凑表示（分词/标记化）与学习底层物理动力学这两个任务的解耦与协同，这对于训练处理复杂化学数据（如分子结构、光谱）的大模型具有直接的借鉴意义。作者发现，在仿真任务之前对分词器进行预训练可以显著提高计算效率，并且预训练数据的领域对齐性至关重要。这些发现为训练高效的领域基础模型（包括化学大模型）提供了实用的指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the impact of tokeniser pretraining on the accuracy and efficiency of physics emulation. Modern high-resolution simulations produce vast volumes of data spanning diverse physical regimes and scales. Training foundation models to learn the dynamics underlying such data enables the modelling of complex multiphysics phenomena, especially in data-limited settings. The emerging class of physics foundation models typically aims to learn two tasks jointly: (i) extracting compact representations of high-resolution spatiotemporal data, and (ii) capturing governing physical dynamics. However, learning both tasks from scratch simultaneously can impede the effectiveness of either process. We show that pretraining the tokeniser with an autoencoding objective prior to training the dynamics model enhances computational efficiency for physics emulation. Notably, the magnitude of this benefit depends on domain alignment: pretraining on the same physical system as the emulation task yields the largest improvements, while pretraining on other systems provides moderate gains. In-domain pretraining reduces VRMSE by 64% after 10,500 training steps compared to training from scratch. To our knowledge, this is the first systematic investigation of tokeniser pretraining for physics foundation models. We further introduce flexible spatiotemporal compression operations that extend causal convolutions to support runtime-adjustable compression ratios, enabling efficient adaptation to diverse downstream tasks. Our findings provide practical guidance for training efficient physics emulators and highlight the importance of strategic pretraining data selection.

</details>

---

### 59. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种名为LatentChem的新框架，旨在改进化学大语言模型的推理效率和性能。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。它旨在解决当前化学大语言模型（LLMs）主要依赖显式自然语言思维链（CoT）进行复杂推理的局限性。作者认为，化学推理本质上是连续和结构化的，将其强制离散化为语言标记会引入根本性的表示不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中直接执行多步推理，而仅对最终输出生成语言。实验表明，当仅针对任务成功进行优化时，模型会自发地将推理内部化，逐步放弃冗长的文本推导，转而采用隐式的潜在计算。在多个化学推理基准测试中，LatentChem在性能上超越了基于CoT的基线模型，同时实现了显著的推理加速。这项工作为化学大模型提供了一种新的、更高效的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 60. [Semantics-Aware Caching for Concept Learning](https://arxiv.org/abs/2603.06506)

**基本信息**

- 🔗 arXiv: [`2603.06506`](https://arxiv.org/abs/2603.06506)
- 👥 作者: Louis Mozart Kamdem Teyou, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06506.pdf)

**💡 相关性分析**

满足标准2：论文提出的语义感知缓存方法是一种可用于化学信息学领域（特别是概念学习任务）的工具，旨在提高从知识库中学习分子概念等任务的效率，因此与“化学信息学”主题相关。

**📖 中文摘要**

本文提出了一种语义感知缓存方法，用于加速概念学习。概念学习是一种在描述逻辑知识库上运行的监督机器学习形式。最先进的概念学习者通常依赖于在可数无限概念空间中的迭代搜索，每次迭代都需要检索候选解决方案的实例。复杂的化学信息学学习问题（例如，从知识库中学习分子概念）可能需要数千次实例检索调用，导致运行时挑战。本文提出的缓存本质上是一个子包含感知映射，通过精确的集合操作将概念与实例集链接起来。实验表明，该缓存可以将概念检索和概念学习的运行时间减少一个数量级，并且对符号推理器和神经符号推理器都有效。这项工作为化学信息学中基于知识库的机器学习任务提供了实用的效率提升工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept learning is a form of supervised machine learning that operates on knowledge bases in description logics. State-of-the-art concept learners often rely on an iterative search through a countably infinite concept space. In each iteration, they retrieve instances of candidate solutions to select the best concept for the next iteration. While simple learning problems might require a few dozen instance retrieval calls to find a fitting solution, complex learning problems might necessitate thousands of calls. We alleviate the resulting runtime challenge by presenting a semantics-aware caching approach. Our cache is essentially a subsumption-aware map that links concepts to a set of instances via crisp set operations. Our experiments on 5 datasets with 4 symbolic reasoners, a neuro-symbolic reasoner, and 5 popular pagination policies demonstrate that our cache can reduce the runtime of concept retrieval and concept learning by an order of magnitude while being effective for both symbolic and neuro-symbolic reasoners.

</details>

---

### 61. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是开发用于机器学习原子间势（MLIPs）的新架构，这是计算化学和材料科学（化学信息学的核心应用领域）的关键工具。同时，提出的MoE/MoLE模型本身是可用于化学模拟的先进工具。

**📖 中文摘要**

本文系统地开发了用于机器学习原子间势（MLIPs）的混合专家（MoE）和混合线性专家（MoLE）架构，并分析了路由策略和专家设计的影响。MLIPs能够实现精确的大规模原子模拟，是计算化学和材料科学的核心工具。作者展示了稀疏激活与共享专家相结合能带来显著的性能提升，并且当存在共享专家时，非线性MoE公式优于MoLE。最终的元素级MoE模型在OMol25、OMat24和OC20M基准测试中达到了最先进的精度。对路由模式的分析揭示了与元素周期表趋势一致的、化学上可解释的专家专业化，表明该模型有效地捕获了元素特定的化学特征，以实现精确的原子间建模。这项工作为化学和材料科学中至关重要的原子模拟提供了更强大、可扩展的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 62. [Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus](https://arxiv.org/abs/2603.10457)

**基本信息**

- 🔗 arXiv: [`2603.10457`](https://arxiv.org/abs/2603.10457)
- 👥 作者: Brandon Yee, Wilson Collins, Michael Iofin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10457.pdf)

**💡 相关性分析**

满足标准2：论文的第二部分使用了名为Prometheus的beta-VAE框架（一种无监督机器学习方法）来分析粒子模拟数据，以检测和验证物理相变。这展示了机器学习工具在物理/化学系统分析中的应用，与“化学大模型”主题中利用AI模型进行科学发现的方向相关。

**📖 中文摘要**

本文为中等能量（10-100 MeV）强流带电粒子束中的束-等离子体集体振荡开发了一个理论和计算框架。在第一部分，作者基于Vlasov-Poisson系统建立了动理学场论，推导了三种束分布函数的Lindhard介电函数和随机相位近似（RPA）极化张量。通过介电函数证明了在临界束密度n_c以上存在无阻尼的朗缪尔波模式，并获得了显式的束-等离子体色散关系。等离子体频率由f-求和定则固定，与分布形状无关。空间电荷效应驱动了以sqrt(n-n_c)开始的异常束展宽和在q=2k_F处的Friedel振荡。束-等离子体转变通过重整化群分析属于3D Ising普适类。在第二部分，作者使用在粒子模拟（PIC）束数据上训练的beta-VAE框架Prometheus验证了这些预测，成功检测到集体等离子体振荡的开始。这项工作为理解强流束中的集体现象提供了理论基础，并展示了无监督学习在发现物理相变方面的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; higher dispersion coefficients depend on velocity moments. Space charge effects drive anomalous beam broadening with sqrt(n-n_c) onset and Friedel oscillations at q=2k_F. The beam-plasma transition belongs to the 3D Ising universality class via renormalization group analysis. In Part II, we validate these predictions using Prometheus, a beta-VAE trained on static structure factor data S(q) from particle-in-cell (PIC) beam simulations. Prometheus detects collective plasma oscillation onset in Gaussian and uniform distributions, confirms their absence in the degenerate Fermi gas (n_c -> 0), and resolves the Kohn anomaly at q=2k_F. Dispersion analysis of S(q,omega) from PIC simulations verifies the distribution-independent Omega_p predicted by the f-sum rule. All six validation checks pass. Predicted signatures -- density-tunable plasma resonances at omega_p proportional to sqrt(n), anomalous beam broadening with sqrt(n-n_c) onset, and Friedel oscillations -- are accessible at existing intermediate-energy beam facilities.

</details>

---

## 📊 数据统计
- 累计运行天数：29
- 累计论文数量：2092

## 📝 历史记录

> 暂无历史数据

