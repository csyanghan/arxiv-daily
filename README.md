# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-16 12:57:26

## 📅 2026-03-16 (今日最新)

**相关论文数：49**

### 1. [Generalist Large Language Models for Molecular Property Prediction: Distilling Knowledge from Specialist Models](https://arxiv.org/abs/2603.12344)

**基本信息**

- 🔗 arXiv: [`2603.12344`](https://arxiv.org/abs/2603.12344)
- 👥 作者: Khiem Le, Sreejata Dey, Marcos Martínez Galindo 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12344.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，专注于提升大型语言模型在化学信息学核心任务——分子性质预测上的性能，并提出了专门的知识蒸馏方法。

**📖 中文摘要**

本文提出了一种名为TreeKD的新颖知识蒸馏方法，旨在提升大型语言模型（LLMs）在分子性质预测（MPP）任务中的性能。MPP是药物发现中的核心任务。该方法的核心思想是将基于功能基团特征训练的专家决策树（如随机森林）所学习到的预测规则，转化为自然语言描述，从而为LLMs提供规则增强的上下文学习。这使得LLMs能够利用仅从SMILES字符串中难以提取的结构化洞察。此外，论文还引入了一种受装袋法启发的测试时缩放技术“规则一致性”，通过集成来自随机森林的不同规则进行预测。在TDC基准测试的22个ADMET性质上的实验表明，TreeKD显著提升了LLM的性能，缩小了其与最先进专家模型之间的差距，推动了面向分子性质预测的实用通用模型的发展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular Property Prediction (MPP) is a central task in drug discovery. While Large Language Models (LLMs) show promise as generalist models for MPP, their current performance remains below the threshold for practical adoption. We propose TreeKD, a novel knowledge distillation method that transfers complementary knowledge from tree-based specialist models into LLMs. Our approach trains specialist decision trees on functional group features, then verbalizes their learned predictive rules as natural language to enable rule-augmented context learning. This enables LLMs to leverage structural insights that are difficult to extract from SMILES strings alone. We further introduce rule-consistency, a test-time scaling technique inspired by bagging that ensembles predictions across diverse rules from a Random Forest. Experiments on 22 ADMET properties from the TDC benchmark demonstrate that TreeKD substantially improves LLM performance, narrowing the gap with SOTA specialist models and advancing toward practical generalist models for molecular property prediction.

</details>

---

### 2. [Budget-Sensitive Discovery Scoring: A Formally Verified Framework for Evaluating AI-Guided Scientific Selection](https://arxiv.org/abs/2603.12349)

**基本信息**

- 🔗 arXiv: [`2603.12349`](https://arxiv.org/abs/2603.12349)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12349.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接评估大型语言模型（作为“化学大模型”的一种）在药物发现（化学信息学核心应用）候选物筛选任务中的价值，是围绕该主题的实证研究。

**📖 中文摘要**

本文提出了预算敏感发现评分（BSDS）和发现质量评分（DQS），这是一个经过形式化验证的框架，用于评估在预算约束下由AI引导的科学候选物选择策略。作为一个案例研究，该框架被应用于回答一个关键问题：在药物发现候选物选择中，大型语言模型（LLMs）能否为现有的机器学习流程增加边际价值？研究评估了39种提议方法（包括11种机制变体、14种零样本LLM配置和14种少样本LLM配置），使用MoleculeNet HIV数据集上的SMILES表示。研究发现，简单的基于随机森林的贪婪ML提议器取得了最佳DQS，在所有零样本和少样本评估中，没有一种LLM配置能够超越这个经过训练的基线分类器。这表明，在现有的训练好的分类器之上，LLMs没有提供额外的价值。该框架适用于任何在预算约束和不对称错误成本下选择候选对象的场景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific discovery increasingly relies on AI systems to select candidates for expensive experimental validation, yet no principled, budget-aware evaluation framework exists for comparing selection strategies -- a gap intensified by large language models (LLMs), which generate plausible scientific proposals without reliable downstream evaluation. We introduce the Budget-Sensitive Discovery Score (BSDS), a formally verified metric -- 20 theorems machine-checked by the Lean 4 proof assistant -- that jointly penalizes false discoveries (lambda-weighted FDR) and excessive abstention (gamma-weighted coverage gap) at each budget level. Its budget-averaged form, the Discovery Quality Score (DQS), provides a single summary statistic that no proposer can inflate by performing well at a cherry-picked budget. As a case study, we apply BSDS/DQS to: do LLMs add marginal value to an existing ML pipeline for drug discovery candidate selection? We evaluate 39 proposers -- 11 mechanistic variants, 14 zero-shot LLM configurations, and 14 few-shot LLM configurations -- using SMILES representations on MoleculeNet HIV (41,127 compounds, 3.5% active, 1,000 bootstrap replicates) under both random and scaffold splits. Three findings emerge. First, the simple RF-based Greedy-ML proposer achieves the best DQS (-0.046), outperforming all MLP variants and LLM configurations. Second, no LLM surpasses the Greedy-ML baseline under zero-shot or few-shot evaluation on HIV or Tox21, establishing that LLMs provide no marginal value over an existing trained classifier. Third, the proposer hierarchy generalizes across five MoleculeNet benchmarks spanning 0.18%-46.2% prevalence, a non-drug AV safety domain, and a 9x7 grid of penalty parameters (tau >= 0.636, mean tau = 0.863). The framework applies to any setting where candidates are selected under budget constraints and asymmetric error costs.

</details>

---

### 3. [Shattering the Shortcut: A Topology-Regularized Benchmark for Multi-hop Medical Reasoning in LLMs](https://arxiv.org/abs/2603.12458)

**基本信息**

- 🔗 arXiv: [`2603.12458`](https://arxiv.org/abs/2603.12458)
- 👥 作者: Xing Zi, Xinying Zhou, Jinghao Xiao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12458.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕评估和改进大型语言模型（“化学大模型”在医学领域的延伸）在复杂化学/生物医学推理任务（多跳诊断）中的能力，并构建了专门的基准数据集。

**📖 中文摘要**

本文介绍了ShatterMed-QA，一个用于严格评估大型语言模型（LLMs）在临床多跳推理中深度诊断能力的双语基准。该基准包含10,558个多跳临床问题，旨在解决LLMs在真实世界临床设置中面临的“捷径学习”问题。论文通过一种新颖的k-Shattering算法构建了一个拓扑正则化的医学知识图谱，通过剪枝通用的中心节点来显式地切断逻辑捷径。通过应用隐式桥接实体掩码和拓扑驱动的硬负采样来合成评估案例，迫使模型在不依赖表面消除的情况下导航生物学上合理的干扰项。对21个LLM的全面评估揭示了它们在多跳任务上的性能大幅下降。关键的是，通过检索增强生成（RAG）恢复被掩码的证据会触发近乎普遍的性能恢复，这验证了该基准在诊断当前医学AI根本性推理缺陷方面的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) achieve expert-level performance on standard medical benchmarks through single-hop factual recall, they severely struggle with the complex, multi-hop diagnostic reasoning required in real-world clinical settings. A primary obstacle is "shortcut learning", where models exploit highly connected, generic hub nodes (e.g., "inflammation") in knowledge graphs to bypass authentic micro-pathological cascades. To address this, we introduce ShatterMed-QA, a bilingual benchmark of 10,558 multi-hop clinical questions designed to rigorously evaluate deep diagnostic reasoning. Our framework constructs a topology-regularized medical Knowledge Graph using a novel $k$-Shattering algorithm, which physically prunes generic hubs to explicitly sever logical shortcuts. We synthesize the evaluation vignettes by applying implicit bridge entity masking and topology-driven hard negative sampling, forcing models to navigate biologically plausible distractors without relying on superficial elimination. Comprehensive evaluations of 21 LLMs reveal massive performance degradation on our multi-hop tasks, particularly among domain-specific models. Crucially, restoring the masked evidence via Retrieval-Augmented Generation (RAG) triggers near-universal performance recovery, validating ShatterMed-QA's structural fidelity and proving its efficacy in diagnosing the fundamental reasoning deficits of current medical AI. Explore the dataset, interactive examples, and full leaderboards at our project website: this https URL

</details>

---

### 4. [Modal Logical Neural Networks for Financial AI](https://arxiv.org/abs/2603.12487)

**基本信息**

- 🔗 arXiv: [`2603.12487`](https://arxiv.org/abs/2603.12487)
- 👥 作者: Antonin Sulc
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12487.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕“化学大模型”的广义概念——大型语言模型/基础模型在特定领域（金融）的应用与增强，并提出了专门的神经符号架构（MLNNs）来提升其推理和合规能力。

**📖 中文摘要**

本文探讨了在金融AI中采用模态逻辑神经网络（MLNNs）作为连接深度学习与符号逻辑的桥梁。MLNNs将克里普克语义集成到神经架构中，实现对必要性、可能性、时间和知识的可微推理。论文将MLNNs视为金融领域的可微“逻辑层”，通过将核心组件（必要性神经元和可学习可达性）映射到监管护栏、市场压力测试和合谋检测等场景，展示了MLNN风格的约束如何促进交易代理的合规性、帮助恢复用于市场监控的潜在信任网络、鼓励在压力情景下的鲁棒性，以及区分统计信念与已验证知识以帮助减轻机器人顾问的幻觉。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The financial industry faces a critical dichotomy in AI adoption: deep learning often delivers strong empirical performance, while symbolic logic offers interpretability and rule adherence expected in regulated settings. We use Modal Logical Neural Networks (MLNNs) as a bridge between these worlds, integrating Kripke semantics into neural architectures to enable differentiable reasoning about necessity, possibility, time, and knowledge. We illustrate MLNNs as a differentiable ``Logic Layer'' for finance by mapping core components, Necessity Neurons ($\Box$) and Learnable Accessibility ($A_\theta$), to regulatory guardrails, market stress testing, and collusion detection. Four case studies show how MLNN-style constraints can promote compliance in trading agents, help recover latent trust networks for market surveillance, encourage robustness under stress scenarios, and distinguish statistical belief from verified knowledge to help mitigate robo-advisory hallucinations.

</details>

---

### 5. [TRACE: Temporal Rule-Anchored Chain-of-Evidence on Knowledge Graphs for Interpretable Stock Movement Prediction](https://arxiv.org/abs/2603.12500)

**基本信息**

- 🔗 arXiv: [`2603.12500`](https://arxiv.org/abs/2603.12500)
- 👥 作者: Qianggang Ding, Haochen Shi, Luis Castejón Lozano 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12500.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用大型语言模型（作为“大模型”的一种）进行复杂领域（金融）的推理和预测，并设计了集成LLM的端到端管道，属于大模型在特定科学计算领域的应用。

**📖 中文摘要**

本文提出了一种用于可解释股票走势预测的时序规则锚定证据链（TRACE）方法，该方法在知识图谱上统一了符号关系先验、动态图探索和LLM引导的决策制定。该方法执行受规则引导的多跳探索，将候选推理链锚定在同时期的新闻中，并将完全接地的证据聚合成可审计的涨/跌判断及人类可读的路径。在标准普尔500基准测试中，该方法在预测准确率、精确率、召回率和F1分数上均超越了强基线模型。性能提升源于（i）规则引导的探索将搜索集中在有经济意义的模式上，而非任意游走；（ii）文本接地的整合选择性地聚合高置信度、完全接地的假设，而非均匀池化弱信号。这些选择在提供可忠实审计的解释的同时，带来了预测性能的提升。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a Temporal Rule-Anchored Chain-of-Evidence (TRACE) on knowledge graphs for interpretable stock movement prediction that unifies symbolic relational priors, dynamic graph exploration, and LLM-guided decision making in a single end-to-end pipeline. The approach performs rule-guided multi-hop exploration restricted to admissible relation sequences, grounds candidate reasoning chains in contemporaneous news, and aggregates fully grounded evidence into auditable \texttt{UP}/\texttt{DOWN} verdicts with human-readable paths connecting text and structure. On an S\&P~500 benchmark, the method achieves 55.1\% accuracy, 55.7\% precision, 71.5\% recall, and 60.8\% F1, surpassing strong baselines and improving recall and F1 over the best graph baseline under identical evaluation. The gains stem from (i) rule-guided exploration that focuses search on economically meaningful motifs rather than arbitrary walks, and (ii) text-grounded consolidation that selectively aggregates high-confidence, fully grounded hypotheses instead of uniformly pooling weak signals. Together, these choices yield higher sensitivity without sacrificing selectivity, delivering predictive lift with faithful, auditably interpretable explanations.

</details>

---

### 6. [Using a Human-AI Teaming Approach to Create and Curate Scientific Datasets with the SCILIRE System](https://arxiv.org/abs/2603.12638)

**基本信息**

- 🔗 arXiv: [`2603.12638`](https://arxiv.org/abs/2603.12638)
- 👥 作者: Necva Bölücü, Jessica Irons, Changhyun Lee 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12638.pdf)

**💡 相关性分析**

满足标准2：论文提出的SCILIRE系统是一个用于从科学文献中创建和整理数据集的通用框架。这为“化学大模型”和“质谱结构推理”领域提供了潜在的数据资源或工具，可用于构建专门的化学或质谱数据集。

**📖 中文摘要**

本文介绍了SCILIRE系统，这是一个基于人机协同原则、用于从科学文献中创建数据集的系统。面对科学文献的快速增长，手动提取结构化知识变得不切实际。SCILIRE的设计围绕以人为中心的工作流程，支持研究人员审查和纠正AI输出，并将这种交互作为反馈信号来改进未来基于LLM的推理。该系统通过迭代工作流程促进高效的数据集创建和整理。评估结合了内在基准测试结果和跨多个领域的真实案例研究，结果表明SCILIRE提高了提取的保真度并促进了高效的数据集创建。虽然论文主题更通用，但其核心是构建一个用于科学数据提取和整理的AI系统，这为化学信息学等领域（如从文献中提取质谱数据或分子结构信息）提供了潜在的数据集、资源或工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of scientific literature has made manual extraction of structured knowledge increasingly impractical. To address this challenge, we introduce SCILIRE, a system for creating datasets from scientific literature. SCILIRE has been designed around Human-AI teaming principles centred on workflows for verifying and curating data. It facilitates an iterative workflow in which researchers can review and correct AI outputs. Furthermore, this interaction is used as a feedback signal to improve future LLM-based inference. We evaluate our design using a combination of intrinsic benchmarking outcomes together with real-world case studies across multiple domains. The results demonstrate that SCILIRE improves extraction fidelity and facilitates efficient dataset creation.

</details>

---

### 7. [Continual Learning in Large Language Models: Methods, Challenges, and Opportunities](https://arxiv.org/abs/2603.12658)

**基本信息**

- 🔗 arXiv: [`2603.12658`](https://arxiv.org/abs/2603.12658)
- 👥 作者: Hongyang Chen, Zhongwu Sun, Hongfei Ye 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12658.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于大型语言模型持续学习的综述，它包含了重要的相关讨论。虽然不专门针对化学，但其讨论的方法、挑战和机遇直接适用于构建和更新“化学大模型”，使其能够持续学习新的化学知识和推理技能，这与关注主题高度相关。

**📖 中文摘要**

本文对大型语言模型中的持续学习方法进行了全面的综述。持续学习使LLM能够动态适应不断发展的知识和顺序任务，同时缓解灾难性遗忘。本综述围绕三个核心训练阶段（持续预训练、持续微调和持续指令调优）构建，在经典的基于排练、正则化和架构的方法分类基础上，根据其独特的遗忘缓解机制进一步细分每个类别，并对传统CL方法在LLM中的适应性和关键改进进行了严格的比较分析。综述涵盖了基本的评估指标以及用于评估CL性能的新兴基准。虽然这是一篇综述论文，并非专门针对化学信息学，但它系统地回顾和讨论了使大模型（包括潜在的化学大模型）能够持续学习和适应新知识（如新的分子结构或质谱解析规则）的关键方法、挑战和机遇。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continual learning (CL) has emerged as a pivotal paradigm to enable large language models (LLMs) to dynamically adapt to evolving knowledge and sequential tasks while mitigating catastrophic forgetting-a critical limitation of the static pre-training paradigm inherent to modern LLMs. This survey presents a comprehensive overview of CL methodologies tailored for LLMs, structured around three core training stages: continual pre-training, continual fine-tuning, and continual this http URL the canonical taxonomy of rehearsal-, regularization-, and architecture-based methods, we further subdivide each category by its distinct forgetting mitigation mechanisms and conduct a rigorous comparative analysis of the adaptability and critical improvements of traditional CL methods for LLMs. In doing so, we explicitly highlight core distinctions between LLM CL and traditional machine learning, particularly with respect to scale, parameter efficiency, and emergent capabilities. Our analysis covers essential evaluation metrics, including forgetting rates and knowledge transfer efficiency, along with emerging benchmarks for assessing CL performance. This survey reveals that while current methods demonstrate promising results in specific domains, fundamental challenges persist in achieving seamless knowledge integration across diverse tasks and temporal scales. This systematic review contributes to the growing body of knowledge on LLM adaptation, providing researchers and practitioners with a structured framework for understanding current achievements and future opportunities in lifelong learning for language models.

</details>

---

### 8. [RetroReasoner: A Reasoning LLM for Strategic Retrosynthesis Prediction](https://arxiv.org/abs/2603.12666)

**基本信息**

- 🔗 arXiv: [`2603.12666`](https://arxiv.org/abs/2603.12666)
- 👥 作者: Hanbum Ko, Chanhui Lee, Ye Rin Kim 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12666.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于逆合成预测的化学大语言模型（RetroReasoner），这直接属于“化学大模型”和“质谱结构推理”的范畴，因为它涉及使用LLM进行分子结构推理和反应路径规划。

**📖 中文摘要**

本文提出了RetroReasoner，一个用于逆合成预测的推理大语言模型。该模型旨在模拟化学家的战略思维，通过预测给定产物分子的反应物来解决有机合成的核心任务。传统方法耗时且依赖专家经验，而现有分子大模型要么缺乏战略推理，要么只进行通用的产物分析。RetroReasoner通过结合监督微调和强化学习来克服这些限制。在监督微调阶段，作者引入了SyntheticRetro框架，生成结构化的断键理由和反应物预测。在强化学习阶段，模型使用往返准确性作为奖励（将预测的反应物通过正向合成模型，若生成的产物与原始输入匹配则给予奖励）。实验结果表明，RetroReasoner不仅性能优于现有基线，还能生成更广泛的可行反应物方案，特别是在处理更具挑战性的反应实例时。该工作直接围绕“化学大模型”和“质谱结构推理”的相关主题，展示了LLM在化学信息学中用于复杂结构推理任务的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrosynthesis prediction is a core task in organic synthesis that aims to predict reactants for a given product molecule. Traditionally, chemists select a plausible bond disconnection and derive corresponding reactants, which is time-consuming and requires substantial expertise. While recent advancements in molecular large language models (LLMs) have made progress, many methods either predict reactants without strategic reasoning or conduct only a generic product analysis, rather than reason explicitly about bond-disconnection strategies that logically lead to the choice of specific reactants. To overcome these limitations, we propose RetroReasoner, a retrosynthetic reasoning model that leverages chemists' strategic thinking. RetroReasoner is trained using both supervised fine-tuning (SFT) and reinforcement learning (RL). For SFT, we introduce SyntheticRetro, a framework that generates structured disconnection rationales alongside reactant predictions. In the case of RL, we apply a round-trip accuracy as reward, where predicted reactants are passed through a forward synthesis model, and predictions are rewarded when the forward-predicted product matches the original input product. Experimental results show that RetroReasoner not only outperforms prior baselines but also generates a broader range of feasible reactant proposals, particularly in handling more challenging reaction instances.

</details>

---

### 9. [RXNRECer Enables Fine-grained Enzymatic Function Annotation through Active Learning and Protein Language Models](https://arxiv.org/abs/2603.12694)

**基本信息**

- 🔗 arXiv: [`2603.12694`](https://arxiv.org/abs/2603.12694)
- 👥 作者: Zhenkun Shi, Jun Zhu, Dehang Wang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12694.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用蛋白质语言模型（一种化学大模型）来直接预测酶催化反应，这直接围绕“化学大模型”这一主题。

**📖 中文摘要**

本文提出了RXNRECer，一个基于Transformer的集成框架，用于直接预测酶催化反应，而无需依赖酶学委员会（EC）编号。该框架整合了蛋白质语言建模和主动学习，以捕获高级序列语义和细粒度的转化模式。它通过利用蛋白质语言模型（一种化学大模型）来理解和预测酶的功能，直接与“化学大模型”主题相关。该方法绕过了传统基于EC编号的间接策略，提高了预测准确性，并为蛋白质组范围内的反应注释提供了可扩展的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A key challenge in enzyme annotation is identifying the biochemical reactions catalyzed by proteins. Most existing methods rely on Enzyme Commission (EC) numbers as intermediaries: they first predict an EC number and then retrieve the associated reactions. This indirect strategy introduces ambiguity due to the complex many-to-many mappings among proteins, EC numbers, and reactions, and is further complicated by frequent updates to EC numbers and inconsistencies across databases. To address these challenges, we present RXNRECer, a transformer-based ensemble framework that directly predicts enzyme-catalyzed reactions without relying on EC numbers. It integrates protein language modeling and active learning to capture both high-level sequence semantics and fine-grained transformation patterns. Evaluations on curated cross-validation and temporal test sets demonstrate consistent improvements over six EC-based baselines, with gains of 16.54% in F1 score and 15.43% in accuracy. Beyond accuracy gains, the framework offers clear advantages for downstream applications, including scalable proteome-wide reaction annotation, enhanced specificity in refining generic reaction schemas, systematic annotation of previously uncurated proteins, and reliable identification of enzyme promiscuity. By incorporating large language models, it also provides interpretable rationales for predictions. These capabilities make RXNRECer a robust and versatile solution for EC-free, fine-grained enzyme function prediction, with potential applications across multiple areas of enzyme research and industrial applications.

</details>

---

### 10. [SciDesignBench: Benchmarking and Improving Language Models for Scientific Inverse Design](https://arxiv.org/abs/2603.12724)

**基本信息**

- 🔗 arXiv: [`2603.12724`](https://arxiv.org/abs/2603.12724)
- 👥 作者: David van Dijk, Ivan Vrkic
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12724.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和改进语言模型（作为化学大模型的一种形式）在科学逆向设计任务中的能力，这直接围绕“化学大模型”主题。

**📖 中文摘要**

本文介绍了SciDesignBench，一个包含14个科学领域、520个基于模拟器任务的基准测试，用于评估语言模型在科学逆向设计（即给定目标结果寻找实现设计）中的能力。该基准测试涵盖了从单次设计到长时域反馈优化等多种设置。论文还引入了RLSF（基于模拟器反馈的训练方法），通过微调模型来提升性能。这项工作将基于模拟器的逆向设计定位为科学推理的基准，并展示了如何利用大语言模型（化学大模型的一种应用）来解决化学、材料等领域的复杂设计问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many of the most important problems in science and engineering are inverse problems: given a desired outcome, find a design that achieves it. Evaluating whether a candidate meets the spec is often routine; a binding energy can be computed, a reactor yield simulated, a pharmacokinetic profile predicted. But searching a combinatorial design space for inputs that satisfy those targets is fundamentally harder. We introduce SciDesignBench, a benchmark of 520 simulator-grounded tasks across 14 scientific domains and five settings spanning single-shot design, short-horizon feedback, long-horizon refinement, and seed-design optimization. On the 10-domain shared-core subset, the best zero-shot model reaches only 29.0% success despite substantially higher parse rates. Simulator feedback helps, but the leaderboard changes with horizon: Sonnet 4.5 is strongest in one-turn de novo design, whereas Opus 4.6 is strongest after 20 turns of simulator-grounded refinement. Providing a starting seed design reshuffles the leaderboard again, demonstrating that constrained modification requires a fundamentally different capability from unconstrained de novo generation. We then introduce RLSF, a simulator-feedback training recipe. An RLSF-tuned 8B model raises single-turn success rates by 8-17 percentage points across three domains. Together, these results position simulator-grounded inverse design as both a benchmark for scientific reasoning and a practical substrate for amortizing expensive test-time compute into model weights.

</details>

---

### 11. [MoKus: Leveraging Cross-Modal Knowledge Transfer for Knowledge-Aware Concept Customization](https://arxiv.org/abs/2603.12743)

**基本信息**

- 🔗 arXiv: [`2603.12743`](https://arxiv.org/abs/2603.12743)
- 👥 作者: Chenyang Zhu, Hongxiang Li, Xiu Li 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12743.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用大型语言模型进行跨模态知识编辑和概念定制的框架，这本质上是在探索和扩展大模型（包括潜在的化学大模型）在结构化知识表示与操作方面的能力。

**📖 中文摘要**

本文提出了MoKus框架，用于解决“知识感知概念定制”这一新任务，旨在将多样化的文本知识绑定到目标视觉概念上。该框架的核心观察是跨模态知识转移，即修改文本模态中的知识会自然转移到视觉模态的生成过程中。MoKus包含视觉概念学习和文本知识更新两个阶段，利用大型语言模型（LLM）作为知识源和处理器。虽然主要应用在图像生成，但其核心机制——利用大模型进行跨模态知识编辑和绑定——与构建和理解复杂化学结构（如分子）的“化学大模型”在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept customization typically binds rare tokens to a target concept. Unfortunately, these approaches often suffer from unstable performance as the pretraining data seldom contains these rare tokens. Meanwhile, these rare tokens fail to convey the inherent knowledge of the target concept. Consequently, we introduce Knowledge-aware Concept Customization, a novel task aiming at binding diverse textual knowledge to target visual concepts. This task requires the model to identify the knowledge within the text prompt to perform high-fidelity customized generation. Meanwhile, the model should efficiently bind all the textual knowledge to the target concept. Therefore, we propose MoKus, a novel framework for knowledge-aware concept customization. Our framework relies on a key observation: cross-modal knowledge transfer, where modifying knowledge within the text modality naturally transfers to the visual modality during generation. Inspired by this observation, MoKus contains two stages: (1) In visual concept learning, we first learn the anchor representation to store the visual information of the target concept. (2) In textual knowledge updating, we update the answer for the knowledge queries to the anchor representation, enabling high-fidelity customized generation. To further comprehensively evaluate our proposed MoKus on the new task, we introduce the first benchmark for knowledge-aware concept customization: KnowCusBench. Extensive evaluations have demonstrated that MoKus outperforms state-of-the-art methods. Moreover, the cross-model knowledge transfer allows MoKus to be easily extended to other knowledge-aware applications like virtual concept creation and concept erasure. We also demonstrate the capability of our method to achieve improvements on world knowledge benchmarks.

</details>

---

### 12. [A Multi-task Large Reasoning Model for Molecular Science](https://arxiv.org/abs/2603.12808)

**基本信息**

- 🔗 arXiv: [`2603.12808`](https://arxiv.org/abs/2603.12808)
- 👥 作者: Pengfei Liu, Shuang Ge, Jun Tao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12808.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个专门用于分子科学的多任务大推理模型，这直接属于“化学大模型”范畴，并涉及分子结构推理。

**📖 中文摘要**

本文介绍了一个用于分子科学的多任务大推理模型，旨在通过结构化推理和反思来模拟分子科学家的认知过程。该模型整合了多专家模块以提供广泛的分子专业知识，并采用由分子知识增强的强化学习链式思维框架，实现结构化和反思性推理。系统评估表明，该模型在10个分子任务上平均性能提升50.3%，超越了20多个最先进的基线模型。这项工作验证了嵌入显式推理机制可以实现高效学习，使较小规模的模型在效能和可解释性上超越大规模模型。该框架通过中枢神经系统药物候选物设计的案例研究，展示了其桥接数据驱动和知识集成方法进行智能分子设计的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advancements in artificial intelligence for molecular science are necessitating a paradigm shift from purely data-driven predictions to knowledge-guided computational reasoning. Existing molecular models are predominantly proprietary, lacking general molecular intelligence and generalizability. This underscores the necessity for computational methods that can effectively integrate scientific logic with deep learning architectures. Here we introduce a multi-task large reasoning model designed to emulate the cognitive processes of molecular scientists through structured reasoning and reflection. Our approach incorporates multi-specialist modules to provide versatile molecular expertise and a chain-of-thought (CoT) framework enhanced by reinforcement learning infused with molecular knowledge, enabling structured and reflective reasoning. Systematic evaluations across 10 molecular tasks and 47 metrics demonstrate that our model achieves an average 50.3% improvement over the base architecture, outperforming over 20 state-of-the-art baselines, including ultra-large-parameter foundation models, despite using significantly fewer training data and computational resources. This validates that embedding explicit reasoning mechanisms enables high-efficiency learning, allowing smaller-scale models to surpass massive counterparts in both efficacy and interpretability. The practical utility of this computational framework was validated through a case study on the design of central nervous system (CNS) drug candidates, illustrating its capacity to bridge data-driven and knowledge-integrated approaches for intelligent molecular design.

</details>

---

### 13. [Multimodal Protein Language Models for Enzyme Kinetic Parameters: From Substrate Recognition to Conformational Adaptation](https://arxiv.org/abs/2603.12845)

**基本信息**

- 🔗 arXiv: [`2603.12845`](https://arxiv.org/abs/2603.12845)
- 👥 作者: Fei Wang, Xinye Zheng, Kun Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12845.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于蛋白质语言模型（化学大模型）的多模态框架，用于预测酶动力学参数，这直接涉及利用大模型进行化学结构（酶和底物）的功能与相互作用推理。

**📖 中文摘要**

本文针对酶动力学参数预测问题，提出了酶反应桥接适配器框架。该框架将动力学预测重新表述为一个分阶段的多模态条件建模问题，通过微调将跨模态信息注入蛋白质语言模型（PLMs）中，同时保留其生化先验。ERBA分两个阶段进行条件化：分子识别交叉注意力首先注入底物信息以捕获特异性；几何感知混合专家然后整合活性位点结构并将样本路由到口袋专用专家以反映诱导契合。这项工作利用蛋白质语言模型（一种化学大模型）作为基础，通过多模态融合来提升对酶-底物相互作用和构象变化的建模能力，从而更准确地预测催化效率参数。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting enzyme kinetic parameters quantifies how efficiently an enzyme catalyzes a specific substrate under defined biochemical conditions. Canonical parameters such as the turnover number ($k_\text{cat}$), Michaelis constant ($K_\text{m}$), and inhibition constant ($K_\text{i}$) depend jointly on the enzyme sequence, the substrate chemistry, and the conformational adaptation of the active site during binding. Many learning pipelines simplify this process to a static compatibility problem between the enzyme and substrate, fusing their representations through shallow operations and regressing a single value. Such formulations overlook the staged nature of catalysis, which involves both substrate recognition and conformational adaptation. In this regard, we reformulate kinetic prediction as a staged multimodal conditional modeling problem and introduce the Enzyme-Reaction Bridging Adapter (ERBA), which injects cross-modal information via fine-tuning into Protein Language Models (PLMs) while preserving their biochemical priors. ERBA performs conditioning in two stages: Molecular Recognition Cross-Attention (MRCA) first injects substrate information into the enzyme representation to capture specificity; Geometry-aware Mixture-of-Experts (G-MoE) then integrates active-site structure and routes samples to pocket-specialized experts to reflect induced fit. To maintain semantic fidelity, Enzyme-Substrate Distribution Alignment (ESDA) enforces distributional consistency within the PLM manifold in a reproducing kernel Hilbert space. Experiments across three kinetic endpoints and multiple PLM backbones, ERBA delivers consistent gains and stronger out-of-distribution performance compared with sequence-only and shallow-fusion baselines, offering a biologically grounded route to scalable kinetic prediction and a foundation for adding cofactors, mutations, and time-resolved structural cues.

</details>

---

### 14. [Enhanced Drug-drug Interaction Prediction Using Adaptive Knowledge Integration](https://arxiv.org/abs/2603.12885)

**基本信息**

- 🔗 arXiv: [`2603.12885`](https://arxiv.org/abs/2603.12885)
- 👥 作者: Pengfei Liu, Jun Tao, Zhixiang Ren
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12885.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用大型语言模型（作为化学大模型的一种应用）并通过强化学习整合化学领域先验知识，以改进药物-药物相互作用预测的框架。

**📖 中文摘要**

本文提出了一种知识增强框架，用于药物-药物相互作用事件预测。该框架利用强化学习技术，自适应地将先验药物知识注入大型语言模型（LLM）中，以促进自适应知识提取和合成，从而高效优化策略空间，提升LLM在DDIE预测中的准确性。通过小样本学习，该方法相比基线取得了显著改进。这项工作为DDIE预测建立了一个有效的科学知识学习框架，展示了利用大语言模型（作为化学领域大模型的一种应用）整合专业知识以解决复杂生化预测问题的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drug-drug interaction event (DDIE) prediction is crucial for preventing adverse reactions and ensuring optimal therapeutic outcomes. However, existing methods often face challenges with imbalanced datasets, complex interaction mechanisms, and poor generalization to unknown drug combinations. To address these challenges, we propose a knowledge augmentation framework that adaptively infuses prior drug knowledge into a large language model (LLM). This framework utilizes reinforcement learning techniques to facilitate adaptive knowledge extraction and synthesis, thereby efficiently optimizing the strategy space to enhance the accuracy of LLMs for DDIE predictions. As a result of few-shot learning, we achieved a notable improvement compared to the baseline. This approach establishes an effective framework for scientific knowledge learning for DDIE predictions.

</details>

---

### 15. [DS$^2$-Instruct: Domain-Specific Data Synthesis for Large Language Models Instruction Tuning](https://arxiv.org/abs/2603.12932)

**基本信息**

- 🔗 arXiv: [`2603.12932`](https://arxiv.org/abs/2603.12932)
- 👥 作者: Ruiyao Xu, Noelle I. Samia, Han Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12932.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于大语言模型指令微调的领域特定数据合成框架。这直接与“化学大模型”主题相关，因为该框架可以应用于生成化学领域的指令数据，从而支持化学领域大模型的训练和优化。

**📖 中文摘要**

本文提出DS²-Instruct，一个用于大语言模型指令微调的零样本领域特定数据合成框架。该框架旨在解决现有数据合成方法在捕获领域特定术语和推理模式方面的不足。它首先生成任务相关的关键词以确保全面的领域覆盖，然后结合布鲁姆分类法的不同认知层次创建多样化的指令，最后通过自一致性验证来确保数据质量。作者将该框架应用于数学、金融和逻辑推理等七个具有挑战性的领域生成数据集。综合评估表明，使用生成数据微调的模型相比现有数据生成方法有显著提升。这项工作直接关联“化学大模型”主题，因为它提供了一种为特定领域（如化学）高效生成高质量指令数据的方法论，这对于训练和微调化学领域的专业大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adapting Large Language Models (LLMs) to specialized domains requires high-quality instruction tuning datasets, which are expensive to create through human annotation. Existing data synthesis methods focus on general-purpose tasks and fail to capture domain-specific terminology and reasoning patterns. To address this, we introduce DS$^2$-Instruct, a zero-shot framework that generates domain-specific instruction datasets without human supervision. Our approach first generates task-informed keywords to ensure comprehensive domain coverage. It then creates diverse instructions by pairing these keywords with different cognitive levels from Bloom's Taxonomy. Finally, it uses self-consistency validation to ensure data quality. We apply this framework to generate datasets across seven challenging domains, such as mathematics, finance, and logical reasoning. Comprehensive evaluation demonstrates that models fine-tuned on our generated data achieve substantial improvements over existing data generation methods.

</details>

---

### 16. [Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization](https://arxiv.org/abs/2603.12933)

**基本信息**

- 🔗 arXiv: [`2603.12933`](https://arxiv.org/abs/2603.12933)
- 👥 作者: Xudong Wang, Chaoning Zhang, Jiaquan Zhang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12933.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大语言模型驱动的多智能体系统的路由优化框架。这直接关联“化学大模型”主题，因为类似的系统架构和路由策略可以应用于构建和管理由多个专业化化学模型组成的协作系统。

**📖 中文摘要**

本文提出AMRO-S，一个用于多智能体大语言模型系统的高效且可解释的路由框架。该框架将多智能体系统路由建模为一个语义条件路径选择问题，通过三个关键机制提升路由性能：使用监督微调的小语言模型进行意图推断；将路由记忆分解为任务特定的信息素专家以减少跨任务干扰；采用质量门控的异步更新机制来解耦推理和学习。在五个公共基准和高并发压力测试上的广泛实验表明，AMRO-S在质量-成本权衡上持续优于强基线路由方法。这项工作与“化学大模型”主题相关，因为它探讨了如何高效管理和路由异构的大语言模型智能体池，这种架构和优化思路可以应用于构建由多个专业化模型（例如，用于分子性质预测、反应推理、文献分析等）组成的化学大模型系统，以实现更高效、可控的复杂化学任务处理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Model (LLM)-driven Multi-Agent Systems (MAS) have demonstrated strong capability in complex reasoning and tool use, and heterogeneous agent pools further broaden the quality--cost trade-off space. Despite these advances, real-world deployment is often constrained by high inference cost, latency, and limited transparency, which hinders scalable and efficient routing. Existing routing strategies typically rely on expensive LLM-based selectors or static policies, and offer limited controllability for semantic-aware routing under dynamic loads and mixed intents, often resulting in unstable performance and inefficient resource utilization. To address these limitations, we propose AMRO-S, an efficient and interpretable routing framework for Multi-Agent Systems (MAS). AMRO-S models MAS routing as a semantic-conditioned path selection problem, enhancing routing performance through three key mechanisms: First, it leverages a supervised fine-tuned (SFT) small language model for intent inference, providing a low-overhead semantic interface for each query; second, it decomposes routing memory into task-specific pheromone specialists, reducing cross-task interference and optimizing path selection under mixed workloads; finally, it employs a quality-gated asynchronous update mechanism to decouple inference from learning, optimizing routing without increasing latency. Extensive experiments on five public benchmarks and high-concurrency stress tests demonstrate that AMRO-S consistently improves the quality--cost trade-off over strong routing baselines, while providing traceable routing evidence through structured pheromone patterns.

</details>

---

### 17. [Delta1 with LLM: symbolic and neural integration for credible and explainable reasoning](https://arxiv.org/abs/2603.12953)

**基本信息**

- 🔗 arXiv: [`2603.12953`](https://arxiv.org/abs/2603.12953)
- 👥 作者: Yang Xu, Jun Liu, Shuwei Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12953.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是集成形式化定理生成与大语言模型以构建可解释的神经符号推理系统。这为“化学大模型”和“质谱结构推理”领域提供了构建可解释、可靠推理模型的重要方法论参考。

**📖 中文摘要**

本文介绍了一个端到端的可解释性构建流程，该流程将基于全三角标准矛盾的自动定理生成器Delta1与大语言模型集成。Delta1以多项式时间确定性地构造最小不可满足子句集和完备定理，确保构造的可靠性和最小性。大语言模型层将每个定理和证明轨迹用连贯的自然语言解释和可操作的见解进行表述。在医疗保健、合规和监管领域的实证研究表明，Delta1与大语言模型的结合实现了可解释、可审计且与领域对齐的推理。这项工作推进了逻辑、语言和学习的融合，将构造性定理生成定位为神经符号可解释AI的原则性基础。虽然论文本身不直接处理化学或质谱数据，但其核心方法论——将形式化逻辑推理与大语言模型的自然语言生成能力结合以构建可解释的AI系统——为“化学大模型”和“质谱结构推理”领域提供了重要的技术思路。例如，可以设想将类似的神经符号框架应用于化学知识推理或质谱解析规则的生成与解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neuro-symbolic reasoning increasingly demands frameworks that unite the formal rigor of logic with the interpretability of large language models (LLMs). We introduce an end to end explainability by construction pipeline integrating the Automated Theorem Generator Delta1 based on the full triangular standard contradiction (FTSC) with LLMs. Delta1 deterministically constructs minimal unsatisfiable clause sets and complete theorems in polynomial time, ensuring both soundness and minimality by construction. The LLM layer verbalizes each theorem and proof trace into coherent natural language explanations and actionable insights. Empirical studies across health care, compliance, and regulatory domains show that Delta1 and LLM enables interpretable, auditable, and domain aligned reasoning. This work advances the convergence of logic, language, and learning, positioning constructive theorem generation as a principled foundation for neuro-symbolic explainable AI.

</details>

---

### 18. [Is Human Annotation Necessary? Iterative MBR Distillation for Error Span Detection in Machine Translation](https://arxiv.org/abs/2603.12983)

**基本信息**

- 🔗 arXiv: [`2603.12983`](https://arxiv.org/abs/2603.12983)
- 👥 作者: Boxuan Lyu, Haiyue Song, Zhi Qu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12983.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大语言模型通过迭代MBR蒸馏生成训练数据，以提升机器翻译错误检测模型的性能。这种方法论与利用“化学大模型”生成数据或优化化学领域任务模型（如分子属性预测、反应条件优化）的思路高度相关。

**📖 中文摘要**

本文提出了一种基于最小贝叶斯风险解码的自进化框架，名为“迭代MBR蒸馏用于错误跨度检测”，旨在消除机器翻译评估中错误跨度检测任务对人类标注的依赖。该框架利用现成的大语言模型生成伪标签。在WMT指标共享任务数据集上的实验表明，仅在这些自生成的伪标签上训练的模型，在系统和跨度级别上均优于未适应的基础模型和使用人类标注训练的监督基线，同时在句子级别保持竞争力。这项工作与“化学大模型”主题相关，因为它展示了一种利用大语言模型自动生成高质量训练数据（伪标签）以改进特定任务模型性能的方法。这种“自进化”或“自蒸馏”范式可以迁移到化学领域，例如，利用化学大模型为未标注的分子性质数据或反应结果生成伪标签，从而训练更高效的子模型或进行模型迭代优化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Error Span Detection (ESD) is a crucial subtask in Machine Translation (MT) evaluation, aiming to identify the location and severity of translation errors. While fine-tuning models on human-annotated data improves ESD performance, acquiring such data is expensive and prone to inconsistencies among annotators. To address this, we propose a novel self-evolution framework based on Minimum Bayes Risk (MBR) decoding, named Iterative MBR Distillation for ESD, which eliminates the reliance on human annotations by leveraging an off-the-shelf LLM to generate this http URL experiments on the WMT Metrics Shared Task datasets demonstrate that models trained solely on these self-generated pseudo-labels outperform both unadapted base model and supervised baselines trained on human annotations at the system and span levels, while maintaining competitive sentence-level performance.

</details>

---

### 19. [Mending the Holes: Mitigating Reward Hacking in Reinforcement Learning for Multilingual Translation](https://arxiv.org/abs/2603.13045)

**基本信息**

- 🔗 arXiv: [`2603.13045`](https://arxiv.org/abs/2603.13045)
- 👥 作者: Yifeng Liu, Siqi Ouyang, Yatish Hosmane Revanasiddappa 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13045.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大语言模型翻译任务提出一种数据高效的强化学习方法。该方法论（特别是关于缓解奖励漏洞的部分）对于训练和优化“化学大模型”（例如，用于分子设计、反应预测）具有重要的参考价值。

**📖 中文摘要**

本文介绍了WALAR，一种仅使用单语文本的强化训练方法，旨在提升大语言模型在大量低资源语言上的翻译能力，同时保持其在高资源语言上的性能。该方法的关键见解基于对现有基于源语言的多语言质量估计模型失败模式（或“漏洞”）的观察。使用这些质量估计模型进行强化学习往往会放大此类漏洞。作者开发了包括词对齐和语言对齐在内的技术来缓解WALAR奖励中的这些漏洞。作者使用WALAR持续训练了一个支持101种语言翻译的大语言模型。实验表明，新模型在Flores-101数据集的1400个语言方向上大幅超越了最强的开源多语言大语言模型之一LLaMAX。这项工作与“化学大模型”主题相关，因为它提出了一种针对大语言模型的、数据高效的强化学习训练方法，并解决了奖励模型中的漏洞问题。这种训练和优化策略可以应用于化学领域，例如，训练化学大模型在数据稀缺的特定分子性质预测或反应类型上表现更好，或者设计更鲁棒的奖励函数来指导分子生成或合成路线规划。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated remarkable capability in machine translation on high-resource language pairs, yet their performance on low-resource translation still lags behind. Existing post-training methods rely heavily on high-quality parallel data, which are often scarce or unavailable for low-resource languages. In this paper, we introduce WALAR, a reinforcement training method using only monolingual text to elevate LLMs' translation capabilities on massive low-resource languages while retaining their performance on high-resource languages. Our key insight is based on the observation of failure modes (or "holes") in existing source-based multilingual quality estimation (QE) models. Reinforcement learning (RL) using these QE models tends to amplify such holes, resulting in poorer multilingual LLMs. We develop techniques including word alignment and language alignment to mitigate such holes in WALAR's reward for RL training. We continually trained an LLM supporting translation of 101 languages using WALAR. The experiments show that our new model outperforms LLaMAX, one of the strongest open-source multilingual LLMs by a large margin on 1400 language directions on Flores-101 dataset.

</details>

---

### 20. [Causal Cellular Context Transfer Learning (C3TL): An Efficient Architecture for Prediction of Unseen Perturbation Effects](https://arxiv.org/abs/2603.13051)

**基本信息**

- 🔗 arXiv: [`2603.13051`](https://arxiv.org/abs/2603.13051)
- 👥 作者: Michael Scholkemper, Sach Mukherjee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13051.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是预测化学扰动对细胞状态的效应，这直接属于计算化学和药物发现的范畴，与“化学大模型”主题高度相关。同时，其提出的轻量级、数据高效的建模框架对构建“质谱结构推理”模型具有方法论上的参考价值。

**📖 中文摘要**

本文提出了C3TL，一个轻量级框架，用于预测化学和遗传扰动对定量细胞状态的影响。该框架利用生物干预的结构化性质和特定的归纳偏差/不变性，通过利用可获得的关于扰动效应的信息来泛化到新的上下文，并且仅需要广泛可用的批量分子数据。与需要大量计算资源和广泛数据集的最先进基础模型相比，该方法在预测新上下文中的扰动效应方面表现出竞争力，但需要更简单的数据、更小的模型规模和更少的时间。通过专注于鲁棒的批量信号和高效的架构，作者表明，无需专有硬件或非常大的模型，也能准确预测扰动效应。这项工作直接与“化学大模型”和“质谱结构推理”主题相关。预测化学扰动（即小分子药物）的细胞效应是药物发现和化学生物学的核心。该框架提供了一种高效、可扩展的方法来构建此类预测模型。此外，其方法论（利用结构化先验、轻量级架构）可以启发构建用于质谱数据解析（即从质谱信号推理分子结构）的类似高效模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting the effects of chemical and genetic perturbations on quantitative cell states is a central challenge in computational biology, molecular medicine and drug discovery. Recent work has leveraged large-scale single-cell data and massive foundation models to address this task. However, such computational resources and extensive datasets are not always accessible in academic or clinical settings, hence limiting utility. Here we propose a lightweight framework for perturbation effect prediction that exploits the structured nature of biological interventions and specific inductive biases/invariances. Our approach leverages available information concerning perturbation effects to allow generalization to novel contexts and requires only widely-available bulk molecular data. Extensive testing, comparing predictions of context-specific perturbation effects against real, large-scale interventional experiments, demonstrates accurate prediction in new contexts. The proposed approach is competitive with SOTA foundation models but requires simpler data, much smaller model sizes and less time. Focusing on robust bulk signals and efficient architectures, we show that accurate prediction of perturbation effects is possible without proprietary hardware or very large models, hence opening up ways to leverage causal learning approaches in biomedicine generally.

</details>

---

### 21. [GeoChemAD: Benchmarking Unsupervised Geochemical Anomaly Detection for Mineral Exploration](https://arxiv.org/abs/2603.13068)

**基本信息**

- 🔗 arXiv: [`2603.13068`](https://arxiv.org/abs/2603.13068)
- 👥 作者: Yihao Ding, Yiran Zhang, Chris Gonzalez 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13068.pdf)

**💡 相关性分析**

满足标准2：论文提供了GeoChemAD，一个开源的多区域地球化学异常检测基准数据集，以及GeoChemFormer模型框架。这些资源可用于化学数据分析和模式识别的研究，与“化学大模型”和“质谱结构推理”领域的数据处理和分析需求相关。

**📖 中文摘要**

本文介绍了GeoChemAD，一个用于矿物勘探中地球化学异常检测的开源基准数据集。该数据集编译自政府主导的地质调查，涵盖多个区域、采样来源和目标元素，包含代表不同空间尺度和采样条件的八个子集。为了建立强基线，作者复现并基准测试了一系列无监督异常检测方法。此外，作者提出了GeoChemFormer，一个基于Transformer的框架，利用自监督预训练来学习空间样本的目标元素感知地球化学表示。大量实验表明，GeoChemFormer在所有八个子集上始终实现优异且稳健的性能，在异常检测准确性和泛化能力方面均优于现有的无监督方法。所提出的数据集和框架为这一方向的可重复研究和未来发展奠定了基础。这项工作与“化学大模型”和“质谱结构推理”主题相关。地球化学数据本质上是多维的化学元素浓度数据，其异常检测可以视为一种特殊的化学数据模式识别问题。GeoChemAD数据集作为一个公开的多区域、多元素化学数据集，可用于训练和评估化学领域的数据分析模型。GeoChemFormer框架展示了一种针对化学数据（元素浓度）进行表示学习和异常检测的有效方法，其技术思路（如自监督预训练、Transformer架构）可以迁移到其他化学数据分析任务，包括质谱数据的解析和结构推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Geochemical anomaly detection plays a critical role in mineral exploration as deviations from regional geochemical baselines may indicate mineralization. Existing studies suffer from two key limitations: (1) single region scenarios which limit model generalizability; (2) proprietary datasets, which makes result reproduction unattainable. In this work, we introduce \textbf{GeoChemAD}, an open-source benchmark dataset compiled from government-led geological surveys, covering multiple regions, sampling sources, and target elements. The dataset comprises eight subsets representing diverse spatial scales and sampling conditions. To establish strong baselines, we reproduce and benchmark a range of unsupervised anomaly detection methods, including statistical models, generative and transformer-based approaches. Furthermore, we propose \textbf{GeoChemFormer}, a transformer-based framework that leverages self-supervised pretraining to learn target-element-aware geochemical representations for spatial samples. Extensive experiments demonstrate that GeoChemFormer consistently achieves superior and robust performance across all eight subsets, outperforming existing unsupervised methods in both anomaly detection accuracy and generalization capability. The proposed dataset and framework provide a foundation for reproducible research and future development in this direction.

</details>

---

### 22. [SldprtNet: A Large-Scale Multimodal Dataset for CAD Generation in Language-Driven 3D Design](https://arxiv.org/abs/2603.13098)

**基本信息**

- 🔗 arXiv: [`2603.13098`](https://arxiv.org/abs/2603.13098)
- 👥 作者: Ruogu Li, Sikai Li, Yao Mu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13098.pdf)

**💡 相关性分析**

满足标准2：论文提供了SldprtNet，一个大规模、多模态的3D CAD模型数据集，以及配套的参数化编码/解码工具。这种类型的数据资源和数据处理方法可以启发和应用于构建化学领域的3D分子结构数据集，对于训练涉及分子几何的“化学大模型”具有重要价值。

**📖 中文摘要**

本文介绍了SldprtNet，一个包含超过24.2万个工业零件的大规模多模态数据集，专为语义驱动的CAD建模、几何深度学习以及用于3D设计的多模态模型的训练和微调而设计。数据集提供.step和.sldprt两种格式的3D模型。为了支持参数化建模并促进数据集可扩展性，作者开发了支持工具（编码器和解码器），支持13种CAD命令，并实现3D模型与结构化文本表示之间的无损转换。此外，每个样本都配有一张由3D模型七个不同视角渲染图合并而成的复合图像。通过将此图像与编码器输出的参数化文本结合，作者使用轻量级多模态语言模型Qwen2.5-VL-7B生成每个零件外观和功能的自然语言描述。这些描述与参数化建模脚本、渲染图像和3D模型文件完全对齐，构成了SldprtNet。为了评估其有效性，作者在数据集子集上微调了基线模型，比较了图像加文本输入与纯文本输入。结果证实了多模态数据集对于CAD生成的必要性和价值。这项工作与“化学大模型”主题相关，因为它提供了一个大规模、多模态的3D几何数据集和配套工具。在化学领域，分子的3D结构（构象）至关重要。类似的数据集构建思路（将3D结构、参数化表示、多视角渲染和文本描述对齐）可以应用于创建大规模的分子3D几何数据集，用于训练能够理解和生成分子3D结构的化学大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce SldprtNet, a large-scale dataset comprising over 242,000 industrial parts, designed for semantic-driven CAD modeling, geometric deep learning, and the training and fine-tuning of multimodal models for 3D design. The dataset provides 3D models in both .step and .sldprt formats to support diverse training and testing. To enable parametric modeling and facilitate dataset scalability, we developed supporting tools, an encoder and a decoder, which support 13 types of CAD commands and enable lossless transformation between 3D models and a structured text representation. Additionally, each sample is paired with a composite image created by merging seven rendered views from different viewpoints of the 3D model, effectively reducing input token length and accelerating inference. By combining this image with the parameterized text output from the encoder, we employ the lightweight multimodal language model Qwen2.5-VL-7B to generate a natural language description of each part's appearance and functionality. To ensure accuracy, we manually verified and aligned the generated descriptions, rendered images, and 3D models. These descriptions, along with the parameterized modeling scripts, rendered images, and 3D model files, are fully aligned to construct SldprtNet. To assess its effectiveness, we fine-tuned baseline models on a dataset subset, comparing image-plus-text inputs with text-only inputs. Results confirm the necessity and value of multimodal datasets for CAD generation. It features carefully selected real-world industrial parts, supporting tools for scalable dataset expansion, diverse modalities, and ensured diversity in model complexity and geometric features, making it a comprehensive multimodal dataset built for semantic-driven CAD modeling and cross-modal learning.

</details>

---

### 23. [The DIME Architecture: A Unified Operational Algorithm for Neural Representation, Dynamics, Control and Integration](https://arxiv.org/abs/2603.12286)

**基本信息**

- 🔗 arXiv: [`2603.12286`](https://arxiv.org/abs/2603.12286)
- 👥 作者: Ionel Cristian Vladu, Nicu Bizdoaca, Ionica Pirici 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12286.pdf)

**💡 相关性分析**

满足标准3：论文是一篇理论性综述/展望文章，提出了一个统一的计算神经架构框架（DIME）。虽然其直接领域是神经科学和认知架构，但文中明确提到该框架“也可能为人工智能和机器人学提供信息”，这包括了对构建具有复杂推理、记忆和决策能力的AI系统（如“化学大模型”或科学AI代理）的展望和启发。它提供了从神经科学角度对智能系统关键组件的深入讨论。

**📖 中文摘要**

本文介绍了DIME（检测-整合-标记-执行）神经架构，该架构在一个共同的操作周期内组织感知、记忆、估值和意识访问。该框架包括四个相互作用的部分：印迹（支持多种激活轨迹的分布式循环神经结构）、执行线程（实现神经过程的时空轨迹）、标记系统（调节增益、可塑性和轨迹选择的神经调节和边缘机制）以及超印迹（与操作性意识访问相关的大规模整合状态）。该框架与来自海马索引、循环皮层处理、重放现象、大规模网络整合和神经调节调节的经验证据一致。在抽象计算层面表述的DIME也可能为人工智能和机器人学提供信息，通过提供一个统一的机制，使表征、估值和时间序列从中浮现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern neuroscience has accumulated extensive evidence on perception, memory, prediction, valuation, and consciousness, yet still lacks an explicit operational architecture capable of integrating these phenomena within a unified computational framework. Existing theories address specific aspects of neural function: predictive coding and active inference emphasize hierarchical inference and prediction error minimization; engram theories explain memory through distributed cell assemblies; neuromodulatory accounts focus on value-dependent regulation of plasticity and behaviour; and global workspace or large-scale network models investigate mechanisms underlying conscious access. Despite their explanatory power, these approaches remain only partially integrated at the architectural level. This work introduces DIME (Detect-Integrate-Mark-Execute), a neural architecture organizing perception, memory, valuation, and conscious access within a common operational cycle. The framework includes four interacting components: engrams, distributed recurrent neural structures supporting multiple activation trajectories; execution threads, spatiotemporal trajectories implementing neural processes; marker systems, neuromodulatory and limbic mechanisms regulating gain, plasticity, and trajectory selection; and hyperengrams, large-scale integrative states associated with operational conscious access. The framework is consistent with empirical evidence from hippocampal indexing, recurrent cortical processing, replay phenomena, large-scale network integration, and neuromodulatory regulation. Formulated at an abstract computational level, DIME may also inform artificial intelligence and robotics by providing an architectural template in which representation, valuation, and temporal sequencing emerge from a unified mechanism. An extended theoretical exposition is available in a companion monograph on Zenodo.

</details>

---

### 24. [Optimal Experimental Design for Reliable Learning of History-Dependent Constitutive Laws](https://arxiv.org/abs/2603.12365)

**基本信息**

- 🔗 arXiv: [`2603.12365`](https://arxiv.org/abs/2603.12365)
- 👥 作者: Kaushik Bhattacharya, Lianghao Cao, Andrew Stuart
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12365.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个贝叶斯最优实验设计（BOED）框架，专门用于从数据中学习历史相关的本构模型参数。该框架作为一种强大的实验设计和数据收集策略工具，可以广泛应用于化学和材料科学中，用于指导哪些实验或模拟最能有效减少模型参数的不确定性，从而加速材料发现或化学过程优化，这与“化学大模型”高效获取训练数据的需求相关。

**📖 中文摘要**

本文提出了一个贝叶斯最优实验设计框架，用于量化、解释和最大化实验设计在可靠学习历史相关本构模型方面的效用。在该框架中，设计效用被定义为参数不确定性的预期减少或预期信息增益。这使得能够使用模拟数据进行硅上设计优化，并降低可靠参数识别所需的物理实验成本。我们引入了两种近似方法，使该框架适用于具有昂贵正向模型和高维数据的先进材料测试：(i) 预期信息增益的高斯近似，以及 (ii) 费雪信息矩阵的代理近似。前者实现了高效的设计优化和解释，而后者通过分摊重复效用评估的成本，将这种方法扩展到批量设计优化。我们对粘弹性固体单轴试验的数值研究表明，优化的试样几何形状和加载路径产生的图像和力数据，相对于随机设计，显著改善了参数可识别性，特别是对于与记忆效应相关的参数。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

History-dependent constitutive models serve as macroscopic closures for the aggregated effects of micromechanics. Their parameters are typically learned from experimental data. With a limited experimental budget, eliciting the full range of responses needed to characterize the constitutive relation can be difficult. As a result, the data can be well explained by a range of parameter choices, leading to parameter estimates that are uncertain or unreliable. To address this issue, we propose a Bayesian optimal experimental design framework to quantify, interpret, and maximize the utility of experimental designs for reliable learning of history-dependent constitutive models. In this framework, the design utility is defined as the expected reduction in parametric uncertainty or the expected information gain. This enables in silico design optimization using simulated data and reduces the cost of physical experiments for reliable parameter identification. We introduce two approximations that make this framework practical for advanced material testing with expensive forward models and high-dimensional data: (i) a Gaussian approximation of the expected information gain, and (ii) a surrogate approximation of the Fisher information matrix. The former enables efficient design optimization and interpretation, while the latter extends this approach to batched design optimization by amortizing the cost of repeated utility evaluations. Our numerical studies of uniaxial tests for viscoelastic solids show that optimized specimen geometries and loading paths yield image and force data that significantly improve parameter identifiability relative to random designs, especially for parameters associated with memory effects.

</details>

---

### 25. [Sampling through iterated approximation: Gradient-free and multi-fidelity Bayesian inference via transport](https://arxiv.org/abs/2603.12448)

**基本信息**

- 🔗 arXiv: [`2603.12448`](https://arxiv.org/abs/2603.12448)
- 👥 作者: Daniel Sharp, Bart van Bloemen Waanders, Youssef Marzouk
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12448.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种通用的、适用于计算密集型模型的贝叶斯推断和采样框架。该框架（包括测度传输代理模型、多保真度建模和重要性加权）作为一种强大的计算工具，可以应用于化学信息学中涉及昂贵量子化学计算或分子动力学模拟的逆问题，例如力场参数推断、分子性质预测的不确定性量化等，为相关主题提供了方法论资源。

**📖 中文摘要**

本文开发了一种用于贝叶斯推断问题的迭代框架，适用于后验分布可能涉及计算密集型模型、难以处理的梯度、显著的后验集中度和明显非高斯性的情况。我们的方法整合了：(i) 结合几何退火与多保真度建模的广义退火方案；(ii) 用于中间退火目标和最终目标分布的、无需评估目标密度梯度即可变分学习的表达性测度传输代理模型；(iii) 结合多种求积规则的重要性加权方案，该方案在构建连续的后验近似时回收并重新加权昂贵的模型评估。我们的方案既产生了用于计算后验期望的求积规则，也产生了基于传输的后验近似，从中我们可以轻松生成独立的蒙特卡洛样本。我们在涉及偏微分方程的低维但强非高斯贝叶斯反问题上展示了该方法的效率和准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop an iterative framework for Bayesian inference problems where the posterior distribution may involve computationally intensive models, intractable gradients, significant posterior concentration, and pronounced non-Gaussianity. Our approach integrates: (i) a generalized annealing scheme that combines geometric tempering with multi-fidelity modeling; (ii) expressive measure transport surrogates for the intermediate annealed and final target distributions, learned variationally without evaluating gradients of the target density; and, (iii) an importance-weighting scheme to combine multiple quadrature rules, which recycles and reweighs expensive model evaluations as successive posterior approximations are built. Our scheme produces both a quadrature rule for computing posterior expectations and a transport-based approximation of the posterior from which we can easily generate independent Monte Carlo samples. We demonstrate the efficiency and accuracy of our approach on low-dimensional but strongly non-Gaussian Bayesian inverse problems involving partial differential equations.

</details>

---

### 26. [Physics-Guided Inverse Design of Optical Waveforms for Nonlinear Electromagnetic Dynamics](https://arxiv.org/abs/2603.12503)

**基本信息**

- 🔗 arXiv: [`2603.12503`](https://arxiv.org/abs/2603.12503)
- 👥 作者: Hao Zhang, Jack Hirschman, Randy Lemons 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12503.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是物理引导的逆向设计，虽然应用场景是光学和加速器物理，但其方法论——结合物理模拟训练代理模型并进行梯度优化——与化学信息学中用于分子设计、反应优化或材料发现的“化学大模型”和逆向设计框架在理念和技术路径上高度相关。

**📖 中文摘要**

本文提出了一个物理引导的深度学习框架，用于光学时域波形的逆向设计。该框架通过训练一个轻量级代理模型，实现了基于梯度的光学轮廓合成，以补偿驱动粒子-场系统中的非线性场畸变。作为一个代表性应用，该方法被用于生成先进光子和粒子源中使用的电子束。学习到的光学波形在模拟中，相对于传统高斯操作，将外在发射度增长抑制了52%以上，相对于理论上的平顶极限也改善了约9%。作者进一步通过使用可编程脉冲整形平台合成预测波形，并演示了实验可行性；将测量得到的光学轮廓纳入束线模拟，可使外在发射度贡献降低31%。这项工作为光学控制场的物理引导逆向设计建立了一种通用方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Structured optical waveforms are emerging as powerful control fields for the next generation of complex photonic and electromagnetic systems, where the temporal structure of light can determine the ultimate performance of scientific instruments. However, identifying optimal optical drive fields in strongly nonlinear regimes remains challenging because the mapping between optical inputs and system response is high-dimensional and typically accessible only through computationally expensive simulations. Here, we present a physics-guided deep learning framework for the inverse design of optical temporal waveforms. By training a light-weighted surrogate model on simulations, the method enables gradient-based synthesis of optical profiles that compensate nonlinear field distortions in driven particle-field systems. As a representative application, we apply the approach to the generation of electron beams used in advanced photon and particle sources. The learned optical waveform actively suppresses extrinsic emittance growth by more than 52% compared with conventional Gaussian operation and by approximately 9% relative to the theoretical flattop limit in simulation. We further demonstrate experimental feasibility by synthesizing the predicted waveform using a programmable pulse-shaping platform; incorporating the measured optical profile into beamline simulations yields a 31% reduction in the extrinsic emittance contribution. Beyond accelerator applications, this work establishes a general way for physics-guided inverse design of optical control fields, enabling structured light to approach fundamental performance limits in nonlinear photonic and high-frequency electromagnetic systems.

</details>

---

### 27. [Accelerating materials discovery using foundation model based In-context active learning](https://arxiv.org/abs/2603.12567)

**基本信息**

- 🔗 arXiv: [`2603.12567`](https://arxiv.org/abs/2603.12567)
- 👥 作者: Jeffrey Hu, Rongzhi Dong, Ying Feng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12567.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用预训练的基础模型（TabPFN）来加速材料发现中的主动学习。这直接涉及“化学大模型”在材料科学领域的应用，即利用强大的AI模型来指导实验设计和加速新材料发现。

**📖 中文摘要**

本文提出了一种基于基础模型的上下文主动学习（ICAL）方法，用于加速材料发现。该方法用TabPFN（一种在数百万合成任务上预训练的基于Transformer的基础模型）替代了传统主动学习中的高斯过程或随机森林代理模型。TabPFN通过单次前向传播执行原则性的贝叶斯推断，无需针对特定数据集重新训练，就能在小数据机制（这正是大多数材料数据集的特点）下提供校准良好的预测不确定性。在涵盖铜合金硬度、导电性、块体金属玻璃形成能力以及晶体晶格热导率等10个材料数据集的基准测试中，TabPFN在8个数据集上胜出，相对于高斯过程平均节省了52%的额外实验/评估，相对于随机森林节省了29.77%。交叉验证分析证实，TabPFN的优势源于其卓越的不确定性校准能力。这项工作表明，预训练的基础模型可以作为加速基于主动学习的材料发现的高度有效的代理模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Active learning (AL) has emerged as a powerful paradigm for accelerating materials discovery by iteratively steering experiments toward the most promising candidates, reducing costly synthesis-and-characterization cycles. However, current AL relies predominantly on Gaussian Process (GP) and Random Forest (RF) surrogates with complementary limitations: GP underfits complex composition--property landscapes due to rigid kernel assumptions, while RF produces unreliable uncertainty estimates in small-data regimes, precisely where most materials datasets reside (with < 500 samples). Here we propose foudaiton model based In-Context Active Learning (ICAL), replacing conventional surrogates with TabPFN, a transformer-based foundation model pre-trained on millions of synthetic tasks to meta-learn a universal prior over tabular data. TabPFN performs principled Bayesian inference in a single forward pass without dataset-specific retraining, delivering well-calibrated predictive uncertainty where GP and RF fail most severely. Benchmarked against GP and RF across 10 materials datasets spanning copper alloy hardness and electrical conductivity, bulk metallic glass-forming ability, and crystal lattice thermal conductivity, TabPFN wins on 8 out of 10 datasets, achieving a mean saving of 52\% in extra experiments/evaluations relative to GP and 29.77% relative to RF. Cross-validation analysis confirms that TabPFN's advantage stems from superior uncertainty calibration,achieving the lowest Negative Log-Likelihood and Area Under the Sparsification Error curve among all surrogates. Our work demonstrates that a pre-trained foundation model can serve as a highly effective surrogate for accelerating active learning-based materials discovery.

</details>

---

### 28. [VecMol: Vector-Field Representations for 3D Molecule Generation](https://arxiv.org/abs/2603.12734)

**基本信息**

- 🔗 arXiv: [`2603.12734`](https://arxiv.org/abs/2603.12734)
- 👥 作者: Yuchen Hua, Xingang Peng, Jianzhu Ma 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12734.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是三维分子生成，这是化学信息学和化学大模型（特别是用于分子生成和表示的模型）的核心主题之一。VecMol提出了一种全新的、基于连续向量场的分子表示和生成范式。

**📖 中文摘要**

本文提出了VecMol，一个用于三维分子生成的范式转换框架。与现有将分子表示为3D图并共同生成离散原子类型和连续原子坐标的方法不同，VecMol将3D分子重新构想为欧几里得空间上的连续向量场。在该表示中，向量指向附近的原子并隐式编码分子结构。该向量场由神经场参数化，并使用潜在扩散模型生成，从而避免了显式的图生成，并将结构学习与离散原子实例化解耦。作者在QM9和GEOM-Drugs基准上验证了这种新颖方法的可行性。VecMol代表了一种基于向量场的3D分子表示新方向，为分子生成提供了新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative modeling of three-dimensional (3D) molecules is a fundamental yet challenging problem in drug discovery and materials science. Existing approaches typically represent molecules as 3D graphs and co-generate discrete atom types with continuous atomic coordinates, leading to intrinsic learning difficulties such as heterogeneous modality entanglement and geometry-chemistry coherence constraints. We propose VecMol, a paradigm-shifting framework that reimagines molecular representation by modeling 3D molecules as continuous vector fields over Euclidean space, where vectors point toward nearby atoms and implicitly encode molecular structure. The vector field is parameterized by a neural field and generated using a latent diffusion model, avoiding explicit graph generation and decoupling structure learning from discrete atom instantiation. Experiments on the QM9 and GEOM-Drugs benchmarks validate the feasibility of this novel approach, suggesting vector-field-based representations as a promising new direction for 3D molecular generation.

</details>

---

### 29. [From Experiments to Expertise: Scientific Knowledge Consolidation for AI-Driven Computational Research](https://arxiv.org/abs/2603.13191)

**基本信息**

- 🔗 arXiv: [`2603.13191`](https://arxiv.org/abs/2603.13191)
- 👥 作者: Haonan Huang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13191.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个AI驱动的计算研究平台，该平台通过整合和积累科学知识来指导后续计算，这直接涉及构建能够进行复杂科学推理和规划的“化学大模型”或更广义的科学AI模型。

**📖 中文摘要**

本文介绍了QMatSuite，一个用于AI驱动计算材料科学研究的开源平台。该平台的核心创新在于解决了当前AI驱动计算科学中普遍存在的“知识丢弃”问题。传统范式将每次计算执行视为孤立事件，而QMatSuite通过让AI代理记录具有完整溯源的研究发现、在新计算前检索知识，并在专门的反思会话中纠正错误发现并将观察结果合成为跨化合物的模式，实现了知识的渐进式积累。在六步量子力学模拟工作流的基准测试中，积累的知识将推理开销减少了67%，并将准确度从与文献的47%偏差提高到3%偏差。当将学习到的知识迁移到一种不熟悉的材料时，实现了1%的偏差且零流程失败。这项工作展示了如何通过系统性的知识整合，使AI代理从单纯的执行者转变为能够积累和运用领域知识的研究者，这对于开发能够进行自主科学发现的AI系统至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While large language models (LLMs) have transformed AI agents into proficient executors of computational materials science, performing a hundred simulations does not make a researcher. What distinguishes research from routine execution is the progressive accumulation of knowledge -- learning which approaches fail, recognizing patterns across systems, and applying understanding to new problems. However, the prevailing paradigm in AI-driven computational science treats each execution in isolation, largely discarding hard-won insights between runs. Here we present QMatSuite, an open-source platform closing this gap. Agents record findings with full provenance, retrieve knowledge before new calculations, and in dedicated reflection sessions correct erroneous findings and synthesize observations into cross-compound patterns. In benchmarks on a six-step quantum-mechanical simulation workflow, accumulated knowledge reduces reasoning overhead by 67% and improves accuracy from 47% to 3% deviation from literature -- and when transferred to an unfamiliar material, achieves 1% deviation with zero pipeline failures.

</details>

---

### 30. [Denoising Diffusion Variational Inference: Diffusion Models as Expressive Variational Posteriors](https://arxiv.org/abs/2401.02739)

**基本信息**

- 🔗 arXiv: [`2401.02739`](https://arxiv.org/abs/2401.02739)
- 👥 作者: Wasu Top Piriyakulkij, Yingheng Wang, Volodymyr Kuleshov
- 📄 PDF: [下载](https://arxiv.org/pdf/2401.02739.pdf)

**💡 相关性分析**

满足标准2：论文提出了DDVI，一种将扩散模型用作灵活变分后验的推断方法。扩散模型是当前生成式AI的核心组件之一。这项工作提供了一种强大的、基于扩散模型的概率推断工具，可以应用于化学信息学中涉及不确定性和复杂后验分布的问题，例如分子生成模型的训练、贝叶斯优化或不确定性量化，为相关主题提供了方法论资源。

**📖 中文摘要**

本文提出了去噪扩散变分推断（DDVI），这是一种用于潜变量模型的黑盒变分推断算法，它依赖扩散模型作为灵活的近似后验。具体来说，我们的方法引入了一类富有表现力的、基于扩散的变分后验，这些后验在潜空间中进行迭代细化；我们使用一种受唤醒-睡眠算法启发的新型正则化证据下界（ELBO）来训练这些后验。我们的方法易于实现（它拟合了ELBO的正则化扩展），与黑盒变分推断兼容，并且优于基于标准化流或对抗网络的替代类别的近似后验。我们发现，DDVI在常见基准测试以及一项生物学激励任务（从人类基因组推断潜在祖先）中，改进了深度潜变量模型中的推断和学习，在千人基因组数据集上它优于强基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose denoising diffusion variational inference (DDVI), a black-box variational inference algorithm for latent variable models which relies on diffusion models as flexible approximate posteriors. Specifically, our method introduces an expressive class of diffusion-based variational posteriors that perform iterative refinement in latent space; we train these posteriors with a novel regularized evidence lower bound (ELBO) on the marginal likelihood inspired by the wake-sleep algorithm. Our method is easy to implement (it fits a regularized extension of the ELBO), is compatible with black-box variational inference, and outperforms alternative classes of approximate posteriors based on normalizing flows or adversarial networks. We find that DDVI improves inference and learning in deep latent variable models across common benchmarks as well as on a motivating task in biology -- inferring latent ancestry from human genomes -- where it outperforms strong baselines on the Thousand Genomes dataset.

</details>

---

### 31. [A DNN Biophysics Model with Topological and Electrostatic Features](https://arxiv.org/abs/2409.03658)

**基本信息**

- 🔗 arXiv: [`2409.03658`](https://arxiv.org/abs/2409.03658)
- 👥 作者: Elyssa Sliheet, Md Abu Talha, Weihua Geng
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.03658.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于预测蛋白质性质的深度神经网络模型。虽然标题未直接提及化学大模型或质谱，但其核心方法——使用DNN结合多尺度拓扑和静电特征来预测分子（蛋白质）的物理化学性质（库仑能、溶剂化能）——与化学信息学中利用机器学习模型进行分子性质预测和结构-性质关系研究的主题高度相关。这可以视为一种针对生物大分子的专用化学模型。

**📖 中文摘要**

本文提出了一种基于深度神经网络（DNN）的生物物理模型，用于预测蛋白质性质（如库仑能或溶剂化能）。该模型的核心是使用多尺度、统一的拓扑和静电特征。拓扑特征通过对重原子或碳原子使用元素特异性持续同调（ESPH）生成。静电特征则使用一种新颖的笛卡尔树码生成，以增强模型预测。这些特征对于不同大小的蛋白质具有统一的数量，因此可以利用广泛可用的蛋白质结构数据库进行训练。该模型在超过17,000个蛋白质上训练，用于预测库仑能，取得了MSE约为0.024、MAPE为0.073和R²为0.976的优异结果。该特征生成算法有潜力作为通用工具，辅助基于机器学习的蛋白质性质和功能预测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this project, we present a deep neural network (DNN)-based biophysics model that uses multi-scale and uniform topological and electrostatic features to predict protein properties, such as Coulomb energies or solvation energies. The topological features are generated using element-specific persistent homology (ESPH) on a selection of heavy atoms or carbon atoms. The electrostatic features are generated using a novel Cartesian treecode, which adds underlying electrostatic interactions to further improve the model prediction. These features are uniform in number for proteins of varying sizes; therefore, the widely available protein structure databases can be used to train the network. These features are also multi-scale, allowing users to balance resolution and computational cost. The optimal model trained on more than 17,000 proteins for predicting Coulomb energy achieves MSE of approximately 0.024, MAPE of 0.073 and $R^2$ of 0.976. Meanwhile, the optimal model trained on more than 4,000 proteins for predicting solvation energy achieves MSE of approximately 0.064, MAPE of 0.081, and $R^2$ of 0.926, showing the efficiency and fidelity of these features in representing the protein structure and force field. The feature generation algorithms also have the potential to serve as general tools for assisting machine learning based prediction of protein properties and functions.

</details>

---

### 32. [Unsupervised anomaly detection in MeV ultrafast electron diffraction](https://arxiv.org/abs/2505.13702)

**基本信息**

- 🔗 arXiv: [`2505.13702`](https://arxiv.org/abs/2505.13702)
- 👥 作者: Mariana A. Fazio, Manel Martinez-Ramon, Salvador Sosa Güitron 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13702.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于处理和分析质谱相关技术（超快电子衍射，MUED）产生的大型数据集的工具和方法。具体来说，它开发了一种无监督的异常检测算法，用于识别和过滤质谱/衍射数据中的噪声和异常样本。这为质谱数据分析提供了有价值的资源和方法，有助于提高后续结构推理等分析的可靠性。

**📖 中文摘要**

本文针对MeV超快电子衍射（MUED）实验中的异常衍射图案检测问题，提出了一种完全无监督的方法。MUED是一种用于研究材料动态结构演化的泵浦-探测技术，其衍射图案信噪比较低，通常需要对数千次拍摄进行平均。然而，电子束的逐次不稳定性会扭曲单个图案，引入不确定性。为了提高MUED的准确性，需要从大型数据集中检测并移除这些异常图案。本文开发了一种基于卷积自编码器的方法，通过计算衍射图案的重构均方误差，并基于该误差的统计分析，为用户提供图案为正常的概率估计。该方法仅使用100个衍射图案进行训练，并在1521个图案上进行测试，实现了0.2%至0.4%的误报率。该方法也可应用于其他因仪器不稳定性而产生故障图像的大型数据集的衍射技术中。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

MeV ultrafast electron diffraction (MUED) is a pump-probe technique used to study the dynamic structural evolution of materials. An ultrashort laser pulse triggers structural changes, which are then probed by an ultrashort relativistic electron beam. To overcome low signal-to-noise ratios, diffraction patterns are averaged over thousands of shots. However, shot-to-shot instabilities in the electron beam can distort individual patterns, introducing uncertainty. Improving MUED accuracy requires detecting and removing these anomalous patterns from large datasets. In this work, we developed a fully unsupervised methodology for the detection of anomalous diffraction patterns. Using a convolutional autoencoder, we calculate the reconstruction mean squared error of the diffraction patterns. Based on the statistical analysis of this error, we provide the user an estimation of the probability that the pattern is normal, which also allows a posterior visual inspection of the images that are difficult to classify. This method has been trained with only 100 diffraction patterns and tested on 1521 patterns, resulting in a false positive rate between 0.2\% and 0.4\%, with a training time of 10 seconds per image and a test time of about 1 second per image. The proposed methodology can also be applied to other diffraction techniques in which large datasets are collected that include faulty images due to instrumental instabilities.

</details>

---

### 33. [ASTGI: Adaptive Spatio-Temporal Graph Interactions for Irregular Multivariate Time Series Forecasting](https://arxiv.org/abs/2509.23313)

**基本信息**

- 🔗 arXiv: [`2509.23313`](https://arxiv.org/abs/2509.23313)
- 👥 作者: Xvyuan Liu, Xiangfei Qiu, Hanyin Cheng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.23313.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于处理不规则多元时间序列（IMTS）的深度学习框架。虽然应用领域包括医疗和金融，但其处理时序数据、构建动态图模型以及进行预测的方法论，与化学信息学和质谱分析中处理时序质谱信号、构建分子结构关系图以及进行谱图解析或结构推理的任务在方法论上高度相似。该框架为处理复杂的、非均匀采样的序列数据（如质谱扫描序列）提供了潜在的技术思路。

**📖 中文摘要**

本文提出了自适应时空图交互（ASTGI）框架，用于解决不规则多元时间序列（IMTS）预测中的核心挑战。IMTS在医疗和金融等关键领域普遍存在，其异步采样和不规则间隔给现有方法带来两大难题：1）如何在不引入失真的情况下准确表示不规则时间序列的原始信息；2）如何有效捕捉观测点之间复杂的动态依赖关系。ASTGI框架首先通过时空点表示模块将每个离散观测编码为可学习嵌入空间中的一个点。其次，通过邻域自适应图构建模块，为嵌入空间中的每个点自适应地构建因果图。随后，时空动态传播模块基于点之间的相对时空位置生成消息并计算交互权重，在这些自适应因果图上迭代更新信息。最后，基于查询点的预测模块通过聚合新查询点的邻域信息进行最终预测。在多个基准数据集上的广泛实验表明，ASTGI优于各种最先进的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Irregular multivariate time series (IMTS) are prevalent in critical domains like healthcare and finance, where accurate forecasting is vital for proactive decision-making. However, the asynchronous sampling and irregular intervals inherent to IMTS pose two core challenges for existing methods: (1) how to accurately represent the raw information of irregular time series without introducing data distortion, and (2) how to effectively capture the complex dynamic dependencies between observation points. To address these challenges, we propose the Adaptive Spatio-Temporal Graph Interaction (ASTGI) framework. Specifically, the framework first employs a Spatio-Temporal Point Representation module to encode each discrete observation as a point within a learnable spatio-temporal embedding space. Second, a Neighborhood-Adaptive Graph Construction module adaptively builds a causal graph for each point in the embedding space via nearest neighbor search. Subsequently, a Spatio-Temporal Dynamic Propagation module iteratively updates information on these adaptive causal graphs by generating messages and computing interaction weights based on the relative spatio-temporal positions between points. Finally, a Query Point-based Prediction module generates the final forecast by aggregating neighborhood information for a new query point and performing forecasting. Extensive experiments on multiple benchmark datasets demonstrate that ASTGI outperforms various state-of-the-art methods.

</details>

---

### 34. [Uni-Parser Technical Report](https://arxiv.org/abs/2512.15098)

**基本信息**

- 🔗 arXiv: [`2512.15098`](https://arxiv.org/abs/2512.15098)
- 👥 作者: Xi Fang, Haoyi Tao, Shuwen Yang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.15098.pdf)

**💡 相关性分析**

满足标准2：论文提出的Uni-Parser是一个强大的文档解析工具，能够专门提取化学结构、反应方案等化学信息学关键数据。这为构建用于训练化学大模型（如AI4Science模型）的大规模、高质量数据集提供了核心的数据资源和技术工具。

**📖 中文摘要**

本文介绍了Uni-Parser，一个面向科学文献和专利的工业级文档解析引擎。其核心是一个模块化、松散耦合的多专家架构，能够跨文本、方程、表格、图形和化学结构等多种模态保持细粒度的跨模态对齐。该系统针对大规模云部署进行了优化，在8个NVIDIA RTX 4090D GPU上处理速率高达每秒20个PDF页面。这种可扩展性支持广泛的下游应用，包括文献检索、摘要生成，以及化学结构、反应方案和生物活性数据等关键科学信息的提取。对于化学信息学领域，该工具为构建用于训练下一代化学大模型（AI4Science模型）的大规模语料库提供了高效、精确的数据解析基础，直接服务于化学大模型的数据准备和知识发现流程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This technical report introduces Uni-Parser, an industrial-grade document parsing engine tailored for scientific literature and patents, delivering high throughput, robust accuracy, and cost efficiency. Unlike pipeline-based document parsing methods, Uni-Parser employs a modular, loosely coupled multi-expert architecture that preserves fine-grained cross-modal alignments across text, equations, tables, figures, and chemical structures, while remaining easily extensible to emerging modalities. The system incorporates adaptive GPU load balancing, distributed inference, dynamic module orchestration, and configurable modes that support either holistic or modality-specific parsing. Optimized for large-scale cloud deployment, Uni-Parser achieves a processing rate of up to 20 PDF pages per second on 8 x NVIDIA RTX 4090D GPUs, enabling cost-efficient inference across billions of pages. This level of scalability facilitates a broad spectrum of downstream applications, ranging from literature retrieval and summarization to the extraction of chemical structures, reaction schemes, and bioactivity data, as well as the curation of large-scale corpora for training next-generation large language models and AI4Science models.

</details>

---

### 35. [Development of Ontological Knowledge Bases by Leveraging Large Language Models](https://arxiv.org/abs/2601.10436)

**基本信息**

- 🔗 arXiv: [`2601.10436`](https://arxiv.org/abs/2601.10436)
- 👥 作者: Le Ngoc Luyen, Marie-Hélène Abel, Philippe Gouspillou
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.10436.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发基于LLM的本体知识库构建方法。在化学信息学背景下，该方法可直接应用于构建化学领域本体，这是化学大模型进行知识表示、推理和整合的核心组成部分，因此与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一种利用大型语言模型（LLMs）自动化和增强本体知识库（OKBs）开发的结构化、迭代方法。该方法优化了知识获取，自动化了本体构件的生成，并支持持续的优化循环。通过一个专注于车辆销售领域用户上下文配置文件本体的详细案例研究，展示了该方法如何显著加速本体构建过程、提高本体一致性、有效缓解偏差并增强本体工程过程的透明度。这项工作强调了将LLMs集成到本体开发中以改善知识管理系统可扩展性、集成能力和整体效率的变革潜力。对于化学信息学，该方法为自动化构建化学领域本体（如化合物、反应、性质的本体）提供了可行的技术路径，这些结构化知识是化学大模型进行可靠推理和知识整合的重要基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ontological Knowledge Bases (OKBs) play a vital role in structuring domain-specific knowledge and serve as a foundation for effective knowledge management systems. However, their traditional manual development poses significant challenges related to scalability, consistency, and adaptability. Recent advancements in Generative AI, particularly Large Language Models (LLMs), offer promising solutions for automating and enhancing OKB development. This paper introduces a structured, iterative methodology leveraging LLMs to optimize knowledge acquisition, automate ontology artifact generation, and enable continuous refinement cycles. We demonstrate this approach through a detailed case study focused on developing a user context profile ontology within the vehicle sales domain. Key contributions include significantly accelerated ontology construction processes, improved ontological consistency, effective bias mitigation, and enhanced transparency in the ontology engineering process. Our findings highlight the transformative potential of integrating LLMs into ontology development, notably improving scalability, integration capabilities, and overall efficiency in knowledge management systems.

</details>

---

### 36. [LLM-driven Multimodal Recommendation](https://arxiv.org/abs/2602.05474)

**基本信息**

- 🔗 arXiv: [`2602.05474`](https://arxiv.org/abs/2602.05474)
- 👥 作者: Yicheng Di
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.05474.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发基于LLM的多模态推荐系统框架（LMMRec），重点是利用LLM理解异构文本信息以进行深层动机建模。该框架的理念和技术（LLM用于语义解析和特征提取）可直接迁移至化学信息学领域，用于处理化学文献、专利等文本，辅助化合物发现、反应条件推荐等任务，因此与“化学大模型”的应用主题相关。

**📖 中文摘要**

本文提出了LMMRec框架，一个基于大型语言模型（LLM）驱动的多模态推荐系统。该研究探索了动机建模在推荐系统中的作用，旨在超越传统的表面交互信号，挖掘影响用户决策过程的深层心理因素。论文特别指出，现有研究通常将动机简化为从行为数据中隐式学习的潜在变量，这限制了捕捉用户动机中固有的语义丰富性的能力。像评论文本这样通常携带明确动机线索的异构信息在当前动机建模框架中仍未得到充分探索。LMMRec框架通过利用LLM的强大语义理解能力，旨在更好地建模和利用这些异构的、富含语义的信息（如文本评论）来提升推荐的解释性和说服力。虽然论文聚焦于通用推荐，但其核心思想——利用LLM解析和理解复杂、异构的领域文本（如科学文献、产品描述、用户评论）以提取深层语义特征——与化学信息学中利用大模型处理化学文献、专利文本以进行化合物性质预测、反应推荐等任务高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As a paradigm that delves into the deep seated drivers of user behavior, motivation-based recommendation systems have emerged as a prominent research direction in the field of personalized information retrieval. Unlike traditional approaches that primarily rely on surface level interaction signals, these systems aim to uncover the intrinsic psychological factors that shape users' decision-making processes and content preferences. By modeling motivation, recommender systems can better interpret not only what users choose, but why they make such choices, thereby enhancing both the interpretability and the persuasive power of recommendations. However, existing studies often simplify motivation as a latent variable learned implicitly from behavioral data, which limits their ability to capture the semantic richness inherent in user motivations. In particular, heterogeneous information such as review texts which often carry explicit motivational cues remains underexplored in current motivation modeling frameworks. Extensive experiments conducted on three real world datasets demonstrate the effectiveness of the proposed LMMRec framework.

</details>

---

### 37. [On the Geometric Coherence of Global Aggregation in Federated Graph Neural Networks](https://arxiv.org/abs/2602.15510)

**基本信息**

- 🔗 arXiv: [`2602.15510`](https://arxiv.org/abs/2602.15510)
- 👥 作者: Chethana Prasad Kabgere, Shylaja SS
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.15510.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕图神经网络（GNN）在异构联邦学习环境中的行为，而GNN是构建化学大模型（用于分子表示、性质预测等）的核心架构之一。论文探讨的GNN消息传递机制的几何相干性问题，直接关系到如何训练出在分布式化学数据上表现稳健的大规模模型。

**📖 中文摘要**

本文研究了联邦图神经网络（GNN）中全局聚合的几何相干性问题。作者指出，在跨域联邦GNN设置中，客户端图具有异构的结构和传播特性，标准的参数聚合机制可能导致全局模型在关系转换空间中产生破坏性干扰，从而损害全局消息传递的相干性。为了解决这个问题，作者提出了GGRS（全局几何参考结构）框架，该框架基于几何容许性准则在聚合前调节客户端更新，以保持关系变换的方向一致性和传播子空间的多样性。这项工作与化学信息学中构建用于分子属性预测或结构推理的图神经网络模型高度相关，因为它深入探讨了在分布式、异构数据环境下如何保持GNN核心的消息传递机制的几何一致性，这对于构建鲁棒的、可泛化的化学大模型（尤其是基于图的模型）具有重要的方法论意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Federated Learning (FL) enables distributed training across multiple clients without centralized data sharing, while Graph Neural Networks (GNNs) model relational data through message passing. In federated GNN settings, client graphs often exhibit heterogeneous structural and propagation characteristics. When standard aggregation mechanisms are applied to such heterogeneous updates, the global model may converge numerically while exhibiting degraded relational behavior. Our work identifies a geometric failure mode of global aggregation in Cross- Domain Federated GNNs. Although GNN parameters are numerically represented as vectors, they encode relational transformations that govern the direction, strength, and sensitivity of information flow across graph neighborhoods. Aggregating updates originating from incompatible propagation regimes can therefore introduce destructive interference in this transformation space. This leads to loss of coherence in global message passing. Importantly, this degradation is not necessarily reflected in conventional metrics such as loss or accuracy. To address this issue, we propose GGRS (Global Geometric Reference Structure), a server-side framework that regulates client updates prior to aggregation based on geometric admissibility criteria. GGRS preserves directional consistency of relational transformations as well as maintains diversity of admissible propagation subspaces. It also stabilizes sensitivity to neighborhood interactions, without accessing client data or graph topology. Experiments on heterogeneous GNN-native, Amazon Co-purchase datasets demonstrate that GGRS preserves global message-passing coherence across training rounds by highlighting the necessity of geometry-aware regulation in federated graph learning.

</details>

---

### 38. [Which Data Matter? Embedding-Based Data Selection for Speech Recognition](https://arxiv.org/abs/2603.05819)

**基本信息**

- 🔗 arXiv: [`2603.05819`](https://arxiv.org/abs/2603.05819)
- 👥 作者: Zakaria Aldeneh, Skyler Seto, Maureen de Seyssel 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05819.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于多模态嵌入的数据选择框架，可用于从大规模异构数据集中筛选出与目标领域最相关的子集。这种方法论可以直接迁移到化学信息学和质谱分析领域，用于构建高质量的数据集以训练化学大模型或质谱结构推理模型。

**📖 中文摘要**

本文研究了基于嵌入的数据选择方法，用于为特定领域的自动语音识别（ASR）系统优化训练数据。作者提出通过表征说话人属性、语音内容和语义含义的互补嵌入来表示语音样本，并分析沿着这些轴进行数据选择时的相关性和多样性如何影响下游ASR性能。实验表明，在100k小时的野外训练数据中，战略性地选择5%的子集进行训练，可以在目标领域上获得比使用全部数据训练的模型更好的性能（相对WER降低高达36.8%）。这项工作虽然聚焦于语音识别，但其核心方法论——利用多模态嵌入进行数据筛选以优化领域特定模型的性能——与化学信息学和质谱分析中面临的问题高度相似。例如，在构建用于质谱结构推理的模型时，如何从海量、异构的质谱数据中选择高质量、有代表性的训练子集是一个关键挑战。本文提出的嵌入驱动数据选择框架为化学领域类似问题的解决提供了直接参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern ASR systems are typically trained on large-scale pseudo-labeled, in-the-wild data spanning multiple domains. While such heterogeneous data benefit generalist models designed for broad deployment, they pose challenges for specialist models targeting specific domains: specialist models lack the capacity to learn from all available data, and one must pay closer attention to addressing the mismatch between training and test conditions. In this work, we study targeted data selection as a strategy to address these challenges, selecting relevant subsets from 100k hours of in-the-wild training data to optimize performance on target domains. We represent speech samples using embeddings that capture complementary characteristic--speaker attributes, phonetic content, and semantic meaning--and analyze how relevance and diversity along these axes when performing data selection affect downstream ASR performance. Our experiments with CTC-based Conformer models show that training on a strategically selected 5% subset can exceed the performance of models trained on the full dataset by up to 36.8% relative WER reduction on target domains.

</details>

---

### 39. [Distributional Regression with Tabular Foundation Models: Evaluating Probabilistic Predictions via Proper Scoring Rules](https://arxiv.org/abs/2603.08206)

**基本信息**

- 🔗 arXiv: [`2603.08206`](https://arxiv.org/abs/2603.08206)
- 👥 作者: Jonas Landsgesell, Pascal Knoll
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08206.pdf)

**💡 相关性分析**

满足标准2：论文倡导并提供了用于评估预测分布质量的严格评分规则（CRPS, CRLS等），这些工具和评估理念对于构建和评估化学大模型（特别是进行回归预测的模型）至关重要，有助于提升模型预测的可靠性和不确定性量化能力。

**📖 中文摘要**

本文指出，像TabPFN和TabICL这样的表格基础模型已经能够产生完整的预测分布，但现有的评估基准（如TabArena, TALENT）仍然几乎完全依赖点估计指标（如RMSE, R²）。这种不匹配导致模型优化目标与真实分布质量评估脱节。作者提出用严格评分规则（如CRPS, CRLS, Interval Score）来补充标准点估计指标，以全面评估预测分布的质量。他们进一步证明，不同的严格评分规则会导致不同的模型排名和训练时的归纳偏差。通过使用预训练期间未见过的评分规则对TabPFNv2.5进行微调，可以在相应指标上获得持续改进。这项工作与化学信息学中基于机器学习模型的预测任务高度相关。在化学领域，许多预测任务（如分子性质预测、反应产率预测）本质上是回归问题，并且预测的不确定性（即分布）对于决策（如实验设计）至关重要。本文倡导的分布评估理念和提供的严格评分规则，为评估和优化化学大模型（尤其是处理表格化分子描述符或光谱数据的模型）的预测可靠性提供了重要的方法论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tabular foundation models such as TabPFN and TabICL already produce full predictive distributions, yet the benchmarks used to evaluate them (TabArena, TALENT, and others) still rely almost exclusively on point-estimate metrics (RMSE, $R^2$). This mismatch implicitly rewards models that elicit a good conditional mean while ignoring the quality of the predicted distribution. We make two contributions. First, we propose supplementing standard point metrics with proper scoring rules (CRPS, CRLS, and the Interval Score) and provide a head-to-head comparison of realTabPFNv2.5 and TabICLv2 with regards to some proper scoring rules across 20 OpenML regression datasets. Second, we show analytically and empirically that different proper scoring rules induce different model rankings and different inductive biases during training, even though each rule is individually minimized by the true distribution. Fine-tuning realTabPFNv2.5 with scoring rules not seen during pretraining (CRLS, $\beta=1.8$ energy score) yields consistent improvements on the corresponding metrics, confirming that the training loss shapes the model beyond what propriety alone guarantees. Together, these findings argue for (i) reporting distributional metrics in tabular regression benchmarks and (ii) making the training objective of foundation models adaptable (via fine-tuning or task-token conditioning) to the scoring rule relevant to the downstream decision problem.

</details>

---

### 40. [TubeMLLM: A Foundation Model for Topology Knowledge Exploration in Vessel-like Anatomy](https://arxiv.org/abs/2603.09217)

**基本信息**

- 🔗 arXiv: [`2603.09217`](https://arxiv.org/abs/2603.09217)
- 👥 作者: Yaoyu Liu, Minghui Zhang, Xin You 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09217.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个能够理解和推理复杂拓扑结构（管状解剖）的多模态大语言模型（MLLM）。这种对结构化、拓扑化信息的处理能力与化学信息学中处理分子图结构、进行质谱谱图推理等任务在本质上高度相关，为化学大模型的设计提供了新颖的思路和方法论参考。

**📖 中文摘要**

本文提出了TubeMLLM，一个用于医学管状解剖结构（如血管）拓扑知识探索的统一基础模型。该模型通过将拓扑先验（以自然语言提示形式）与视觉表征在多模态大语言模型（MLLM）的共享注意力架构中对齐，显著增强了拓扑感知能力。作者构建了TubeMData多模态基准，包含全面的以拓扑为中心的任务，并采用自适应损失加权策略在训练中强调拓扑关键区域。实验在15个不同数据集上进行，证明该模型在分布外泛化、零样本跨模态迁移（例如从眼底彩照到X射线血管造影）以及对图像退化（模糊、噪声等）的鲁棒性方面均达到先进水平。这项工作与化学信息学中分子结构（本质上是图或拓扑结构）的分析高度相关。虽然应用领域不同，但TubeMLLM的核心创新——将拓扑先验和结构化理解融入多模态大模型以提升对复杂结构的感知和推理能力——为化学大模型的研究提供了重要启示。例如，可以借鉴其思路，开发能够理解和推理分子图拓扑结构（如官能团连接、环系）的化学基础模型，用于分子性质预测或逆合成分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modeling medical vessel-like anatomy is challenging due to its intricate topology and sensitivity to dataset shifts. Consequently, task-specific models often suffer from topological inconsistencies, including artificial disconnections and spurious merges. Motivated by the promise of multimodal large language models (MLLMs) for zero-shot generalization, we propose TubeMLLM, a unified foundation model that couples structured understanding with controllable generation for medical vessel-like anatomy. By integrating topological priors through explicit natural language prompting and aligning them with visual representations in a shared-attention architecture, TubeMLLM significantly enhances topology-aware perception. Furthermore, we construct TubeMData, a pionner multimodal benchmark comprising comprehensive topology-centric tasks, and introduce an adaptive loss weighting strategy to emphasize topology-critical regions during training. Extensive experiments on fifteen diverse datasets demonstrate our superiority. Quantitatively, TubeMLLM achieves state-of-the-art out-of-distribution performance, substantially reducing global topological discrepancies on color fundus photography (decreasing the $\beta_{0}$ number error from 37.42 to 8.58 compared to baselines). Notably, TubeMLLM exhibits exceptional zero-shot cross-modality transferring ability on unseen X-ray angiography, achieving a Dice score of 67.50% while significantly reducing the $\beta_{0}$ error to 1.21. TubeMLLM also maintains robustness against degradations such as blur, noise, and low resolution. Furthermore, in topology-aware understanding tasks, the model achieves 97.38% accuracy in evaluating mask topological quality, significantly outperforming standard vision-language baselines.

</details>

---

### 41. [ForgeDreamer: Industrial Text-to-3D Generation with Multi-Expert LoRA and Cross-View Hypergraph](https://arxiv.org/abs/2603.09266)

**基本信息**

- 🔗 arXiv: [`2603.09266`](https://arxiv.org/abs/2603.09266)
- 👥 作者: Junhao Cai, Deyu Zeng, Junhao Pang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09266.pdf)

**💡 相关性分析**

满足标准1：论文提出的多专家LoRA集成机制旨在解决大模型在跨领域应用时的知识干扰和泛化问题。这种先进的模型适应与集成技术对于构建能够覆盖化学多个子领域（如合成化学、计算化学、分析化学）的通用化学大模型具有重要的参考价值。

**📖 中文摘要**

本文提出了ForgeDreamer框架，旨在解决当前文本到3D生成方法在工业应用中的两大关键限制：领域适应挑战和几何推理缺陷。针对领域适应，作者提出了多专家LoRA集成机制，将多个特定类别的LoRA模型整合为统一表示，以实现优异的跨类别泛化并消除知识干扰。针对几何推理，作者开发了跨视图超图几何增强方法，同时捕获跨多个视角的结构依赖性。这些组件协同工作，在自定义工业数据集上的实验证明了其在语义泛化和几何保真度方面的优越性。这项工作与“化学大模型”主题相关，主要体现在其先进的模型适应和集成技术。在化学领域，一个通用的化学大模型可能需要适应众多不同的子领域（如有机合成、材料设计、药物发现），每个子领域都有其特定的数据分布和知识体系。ForgeDreamer中解决跨类别知识干扰和实现有效知识整合的多专家LoRA集成机制，为构建能够灵活适应化学多个子领域的、可扩展的大模型提供了有价值的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current text-to-3D generation methods excel in natural scenes but struggle with industrial applications due to two critical limitations: domain adaptation challenges where conventional LoRA fusion causes knowledge interference across categories, and geometric reasoning deficiencies where pairwise consistency constraints fail to capture higher-order structural dependencies essential for precision manufacturing. We propose a novel framework named ForgeDreamer addressing both challenges through two key innovations. First, we introduce a Multi-Expert LoRA Ensemble mechanism that consolidates multiple category-specific LoRA models into a unified representation, achieving superior cross-category generalization while eliminating knowledge interference. Second, building on enhanced semantic understanding, we develop a Cross-View Hypergraph Geometric Enhancement approach that captures structural dependencies spanning multiple viewpoints simultaneously. These components work synergistically improved semantic understanding, enables more effective geometric reasoning, while hypergraph modeling ensures manufacturing-level consistency. Extensive experiments on a custom industrial dataset demonstrate superior semantic generalization and enhanced geometric fidelity compared to state-of-the-art approaches. Our code and data are provided in the supplementary material attached in the appendix for review purposes.

</details>

---

### 42. [Context Engineering: From Prompts to Corporate Multi-Agent Architecture](https://arxiv.org/abs/2603.09619)

**基本信息**

- 🔗 arXiv: [`2603.09619`](https://arxiv.org/abs/2603.09619)
- 👥 作者: Vera V. Vishnyakova
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09619.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题“语境工程”（Context Engineering）直接关系到如何为AI智能体（包括化学领域的AI智能体）构建有效的决策环境。这对于部署化学大模型作为自主智能体进行科学研究（如逆合成规划、实验自动化）至关重要，提供了构建可靠化学AI系统的工程学框架。

**📖 中文摘要**

本文提出了“语境工程”（Context Engineering, CE）作为一个独立的学科，专注于设计、构建和管理AI智能体进行决策的整个信息环境。作者认为，随着AI系统从无状态的聊天机器人演变为自主的多步骤智能体，仅关注单个查询设计的“提示工程”（PE）已显不足。CE关注的是智能体的“操作系统”，并提出了语境质量的五个标准：相关性、充分性、隔离性、经济性和可追溯性。在此基础上，文章进一步提出了“意图工程”（IE）和“规范工程”（SE），共同构成了智能体工程的累积金字塔成熟度模型。这项工作与“化学大模型”主题高度相关，尤其是当化学大模型被部署为自主智能体用于实验设计、文献挖掘或数据分析时。如何为这些化学智能体设计和构建一个稳定、可靠、高效的决策语境（包括相关的化学数据库、工具API、安全协议、领域知识等），是确保其有效、安全运行的关键。本文提供的框架和原则为系统化地解决这一问题提供了重要的理论指导和实践思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As artificial intelligence (AI) systems evolve from stateless chatbots to autonomous multi-step agents, prompt engineering (PE), the discipline of crafting individual queries, proves necessary but insufficient. This paper introduces context engineering (CE) as a standalone discipline concerned with designing, structuring, and managing the entire informational environment in which an AI agent makes decisions. Drawing on vendor architectures (Google ADK, Anthropic, LangChain), current academic work (ACE framework, Google DeepMind's intelligent delegation), enterprise research (Deloitte, 2026; KPMG, 2026), and the author's experience building a multi-agent system, the paper proposes five context quality criteria: relevance, sufficiency, isolation, economy, and provenance, and frames context as the agent's operating system. Two higher-order disciplines follow. Intent engineering (IE) encodes organizational goals, values, and trade-off hierarchies into agent infrastructure. Specification engineering (SE) creates a machine-readable corpus of corporate policies and standards enabling autonomous operation of multi-agent systems at scale. Together these four disciplines form a cumulative pyramid maturity model of agent engineering, in which each level subsumes the previous one as a necessary foundation. Enterprise data reveals a gap: while 75% of enterprises plan agentic AI deployment within two years (Deloitte, 2026), deployment has surged and retreated as organizations confront scaling complexity (KPMG, 2026). The Klarna case illustrates a dual deficit, contextual and intentional. Whoever controls the agent's context controls its behavior; whoever controls its intent controls its strategy; whoever controls its specifications controls its scale.

</details>

---

### 43. [From Imitation to Intuition: Intrinsic Reasoning for Open-Instance Video Classification](https://arxiv.org/abs/2603.10300)

**基本信息**

- 🔗 arXiv: [`2603.10300`](https://arxiv.org/abs/2603.10300)
- 👥 作者: Ke Zhang, Xiangchen Zhao, Yunjie Tian 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10300.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个框架，以增强视觉语言模型（VLM）的内在推理能力，并将其应用于复杂分类任务。这种专注于提升大模型推理能力（而非仅表征能力）的研究，对于开发能够进行复杂逻辑推理的化学大模型（例如，从质谱数据推理出候选分子结构）具有直接的启发和借鉴意义。

**📖 中文摘要**

本文提出了DeepIntuit框架，旨在解决开放实例视频分类的挑战。该框架通过将视觉语言模型（VLM）的推理能力（直觉）从简单的特征模仿演进到内在推理，来应对现实世界中类内变化巨大且复杂的情况。框架包含冷启动监督对齐以初始化推理能力，使用组相对策略优化（GRPO）通过强化学习增强推理连贯性，并引入一个直觉校准阶段，在VLM生成的内在推理轨迹上训练分类器，以确保稳定的知识迁移。这项工作与“化学大模型”和“质谱结构推理”主题相关，主要体现在其利用和增强大模型内在推理能力的方法上。在化学领域，许多任务（如从质谱推断分子结构、预测复杂反应路径）需要深度的符号推理和逻辑演绎，而不仅仅是模式匹配。DeepIntuit框架中提出的通过强化学习优化推理过程、并将推理轨迹用于训练下游任务的方法，为开发具有更强推理能力的化学大模型（特别是用于结构解析等复杂任务）提供了创新的技术路线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Conventional video classification models, acting as effective imitators, excel in scenarios with homogeneous data distributions. However, real-world applications often present an open-instance challenge, where intra-class variations are vast and complex, beyond existing benchmarks. While traditional video encoder models struggle to fit these diverse distributions, vision-language models (VLMs) offer superior generalization but have not fully leveraged their reasoning capabilities (intuition) for such tasks. In this paper, we bridge this gap with an intrinsic reasoning framework that evolves open-instance video classification from imitation to intuition. Our approach, namely DeepIntuit, begins with a cold-start supervised alignment to initialize reasoning capability, followed by refinement using Group Relative Policy Optimization (GRPO) to enhance reasoning coherence through reinforcement learning. Crucially, to translate this reasoning into accurate classification, DeepIntuit then introduces an intuitive calibration stage. In this stage, a classifier is trained on this intrinsic reasoning traces generated by the refined VLM, ensuring stable knowledge transfer without distribution mismatch. Extensive experiments demonstrate that for open-instance video classification, DeepIntuit benefits significantly from transcending simple feature imitation and evolving toward intrinsic reasoning. Our project is available at this https URL .

</details>

---

### 44. [Linear-Scaling Tensor Train Sketching](https://arxiv.org/abs/2603.11009)

**基本信息**

- 🔗 arXiv: [`2603.11009`](https://arxiv.org/abs/2603.11009)
- 👥 作者: Paul Cazeaux, Mi-Song Dupuy, Rodrigo Figueroa Justiniano
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11009.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种高效的张量火车（TT）格式草图算法（TTStack），用于高维数据的压缩和近似。这种处理高维数据的强大数学工具对于化学信息学至关重要，因为化学数据（如分子描述符、光谱、量子化学计算输出）通常是高维的，该工具可用于构建高效的数据处理管道，服务于化学大模型的训练和应用。

**📖 中文摘要**

本文引入了TTStack草图，一种为张量火车（TT）格式量身定制的结构化随机投影，它统一了现有的TT自适应草图算子。作者证明了TTStack满足 oblivious subspace embedding (OSE) 性质，其参数仅线性依赖于张量阶数d和子空间维度r，与此前指数级依赖于d的构造相比有显著改进。作为直接推论，作者为QB分解和随机化TT舍入推导了准最优误差界。这项工作与“化学大模型”主题相关，主要体现在其高效处理高维数据的技术上。在计算化学和化学信息学中，许多问题（如电子结构计算、分子动力学模拟、高通量筛选数据）会产生高维张量。TT格式是一种重要的张量网络，用于压缩和高效处理这类高维数据。本文提出的TTStack草图及其理论保证，为在化学大模型的训练或推理中，高效处理和分析高维化学数据（例如，将高维分子描述符或光谱数据压缩为低维TT表示）提供了强大的数学工具和算法基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the TTStack sketch, a structured random projection tailored to the tensor train (TT) format that unifies existing TT-adapted sketching operators. By varying two integer parameters $P$ and $R$, TTStack interpolates between the Khatri-Rao sketch ($R=1$) and the Gaussian TT sketch ($P=1$). We prove that TTStack satisfies an oblivious subspace embedding (OSE) property with parameters $R = \mathcal{O}(d(r+\log 1/\delta))$ and $P = \mathcal{O}(\varepsilon^{-2})$, and an oblivious subspace injection (OSI) property under the condition $R = \mathcal{O}(d)$ and $P = \mathcal{O}(\varepsilon^{-2}(r + \log r/\delta))$. Both guarantees depend only linearly on the tensor order $d$ and on the subspace dimension $r$, in contrast to prior constructions that suffer from exponential scaling in $d$. As direct consequences, we derive quasi-optimal error bounds for the QB factorization and randomized TT rounding. The theoretical results are supported by numerical experiments on synthetic tensors, Hadamard products, and a quantum chemistry application.

</details>

---

### 45. [H2LooP Spark Preview: Continual Pretraining of Large Language Models for Low-Level Embedded Systems Code](https://arxiv.org/abs/2603.11139)

**基本信息**

- 🔗 arXiv: [`2603.11139`](https://arxiv.org/abs/2603.11139)
- 👥 作者: Amit Singh, Vedant Nipane, Pulkit Agrawal 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11139.pdf)

**💡 相关性分析**

满足标准2：论文展示了一个完整的领域特定持续预训练（CPT）流程，包括领域语料构建、高效微调（LoRA）和性能评估。这种方法论和实证结果对于在化学领域构建和优化领域大模型（例如，专门用于质谱解析或合成路线设计的模型）具有直接的参考价值，提供了如何利用领域数据提升大模型专业能力的技术蓝图。

**📖 中文摘要**

本文介绍了H2LooP Spark Preview，一个针对嵌入式系统低层代码领域的持续预训练（CPT）流程。该工作将完全开放的语言模型OLMo-3-7B，使用BF16 LoRA在嵌入式系统领域的数据上进行适配。训练语料库通过层次化的数据手册到代码映射方法构建，覆盖了117个制造商的100B令牌原始嵌入式系统数据。持续预训练带来了显著的性能提升，在13个嵌入式领域的生成式代码补全基准测试中，所得的7B模型在8个类别上的令牌准确率超过了Claude Opus 4.6和Qwen3-Coder-30B。这项工作与“化学大模型”主题相关，主要体现在其领域特定持续预训练的方法论上。在化学领域，构建一个通用的化学大模型后，通常需要针对特定的子领域（如有机合成、材料科学、分析化学）进行进一步的适配，以提升其在专业任务上的性能。本文展示的通过精心构建领域语料库、使用高效参数微调技术（如高秩LoRA）进行持续预训练，并显著提升模型在专业领域能力的完整流程，为化学大模型的领域适配提供了可复现的范例和有力的实证支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) demonstrate strong code generation abilities in general-purpose programming languages but remain limited in specialized domains such as low-level embedded systems programming. This domain involves hardware register manipulation, vendor-specific SDKs, real-time operating system APIs, and hardware abstraction layers that are underrepresented in standard pretraining corpora. We introduce H2LooP Spark Preview, a continual pretraining (CPT) pipeline that adapts the OLMo-3-7B-a fully open language model to the embedded systems domain using BF16 LoRA with rank-stabilized scaling on 8 NVIDIA H100 GPUs. Our training corpus is constructed from repository-datasheet pairs covering 100B tokens of raw embedded systems data across 117 manufacturers, processed using the hierarchical datasheet-to-code mapping approach proposed in SpecMap (Nipane et al., 2026). The resulting curated dataset split contains 23.5B tokens across 13 embedded domains. Continual pretraining with high-rank LoRA (r=512) yields substantial gains, reducing in-domain perplexity by 70.4% and held-out repository perplexity by 66.1%. On generative code completion benchmarks spanning 13 embedded domains, our 7B model outperforms Claude Opus 4.6 and Qwen3-Coder-30B on 8 categories in token accuracy, showing that targeted continual pretraining enables smaller open-weight models to rival frontier systems on specialized technical tasks. We release the production training checkpoint on Huggingface as an open-source artifact.

</details>

---

### 46. [XSkill: Continual Learning from Experience and Skills in Multimodal Agents](https://arxiv.org/abs/2603.12056)

**基本信息**

- 🔗 arXiv: [`2603.12056`](https://arxiv.org/abs/2603.12056)
- 👥 作者: Guanyu Jiang, Zhaochen Su, Xiaoye Qu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12056.pdf)

**💡 相关性分析**

满足标准1：论文的核心是提出一个框架，使多模态AI智能体能够通过持续学习从交互历史中积累和复用“经验”与“技能”。这种使智能体具备持续学习和知识积累能力的研究，对于开发能够在化学研究环境中长期工作、不断从成功和失败中学习的化学AI助手或实验自动化平台具有重要的指导意义。

**📖 中文摘要**

本文提出了XSkill，一个用于多模态智能体中从经验和技能进行持续学习的双流框架。XSkill从视觉观察中提取和检索可重用的知识：经验（提供工具选择和决策的行动级指导）和技能（提供规划和工具使用的任务级指导）。在积累阶段，XSkill通过视觉基础总结和跨路径批判，从多路径轨迹中提炼和巩固经验和技能。在推理阶段，它根据当前视觉上下文检索并适配这些知识，并将使用历史反馈回积累阶段以形成持续学习循环。在五个不同领域的基准测试中，XSkill持续且显著地优于仅使用工具和基于学习的方法。这项工作与“化学大模型”主题高度相关，尤其是当化学大模型被部署为自主智能体进行实验或数据分析时。化学研究过程本身涉及大量可重复使用的“经验”（如特定反应条件的优化历史）和“技能”（如标准分析操作流程或数据解读模式）。XSkill框架为化学AI智能体提供了一种系统化的方法，使其能够从历史交互中自动学习、积累和复用这些宝贵的领域知识，从而实现能力的持续增长和任务的更高效完成，这对于构建具有长期学习和适应能力的化学研究助手至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal agents can now tackle complex reasoning tasks with diverse tools, yet they still suffer from inefficient tool use and inflexible orchestration in open-ended settings. A central challenge is enabling such agents to continually improve without parameter updates by learning from past trajectories. We identify two complementary forms of reusable knowledge essential for this goal: experiences, providing concise action-level guidance for tool selection and decision making, and skills, providing structured task-level guidance for planning and tool use. To this end, we propose XSkill, a dual-stream framework for continual learning from experience and skills in multimodal agents. XSkill grounds both knowledge extraction and retrieval in visual observations. During accumulation, XSkill distills and consolidates experiences and skills from multi-path rollouts via visually grounded summarization and cross-rollout critique. During inference, it retrieves and adapts this knowledge to the current visual context and feeds usage history back into accumulation to form a continual learning loop. Evaluated on five benchmarks across diverse domains with four backbone models, XSkill consistently and substantially outperforms both tool-only and learning-based baselines. Further analysis reveals that the two knowledge streams play complementary roles in influencing the reasoning behaviors of agents and show superior zero-shot generalization.

</details>

---

### 47. [Aligning Large Language Model Agents with Rational and Moral Preferences: A Supervised Fine-Tuning Approach](https://arxiv.org/abs/2507.20796)

**基本信息**

- 🔗 arXiv: [`2507.20796`](https://arxiv.org/abs/2507.20796)
- 👥 作者: Wei Lu, Amit Dhanda, Daniel L. Chen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.20796.pdf)

**💡 相关性分析**

满足标准1：论文的核心是研究如何通过监督微调将AI智能体的行为与明确的经济或道德偏好对齐。这种AI对齐技术对于确保化学大模型在自主决策时（如实验设计、工艺优化）符合科学伦理、安全规范和可持续发展目标具有关键意义，提供了将领域价值观嵌入模型行为的具体方法。

**📖 中文摘要**

本文研究了大型语言模型（LLM）智能体在战略环境中的经济行为，并发现现成的LLM智能体在经典经济博弈中表现出系统性偏离收益敏感行为。作者引入了一种监督微调方法，使智能体行为与明确的经济偏好（如纯粹自利的“经济人”或包含康德普遍化原则的“道德人”）保持一致。通过在一个小的、理论驱动的合成数据集上进行微调，可以诱导出战略行为的持久且可解释的转变。在道德困境和重复双寡头定价的应用中，与不同偏好结构对齐的智能体产生了系统不同的均衡结果和定价动态。这项工作与“化学大模型”主题相关，主要体现在其AI对齐（AI Alignment）的方法论上。当化学大模型被用于自动化决策时（例如，在绿色化学原则下选择合成路线，或在成本与收率之间进行权衡），其行为需要与人类设定的目标、价值观或约束条件对齐。本文提出的基于明确效用规范（通过理论生成最优策略）进行对齐微调的方法，为将化学领域的专业知识、伦理准则（如绿色化学12原则）或安全约束注入化学大模型的行为中，提供了一种严谨且可解释的技术途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As large language models (LLMs) increasingly act as autonomous agents in markets and organizations, their behavior in strategic environments becomes economically consequential. We document that off-the-shelf LLM agents exhibit systematic deviations from payoff-sensitive behavior in canonical economic games, including excessive cooperation and limited responsiveness to incentives. We introduce a supervised fine-tuning approach that aligns agent behavior with explicit economic preferences. Specifically, we generate optimal strategies under two stylized utility specifications, homo economicus, which maximizes self-interest, and homo moralis, which incorporates Kantian universalizability, and use these utility-implied reasoning and strategies to guide fine-tuning. Fine-tuning on a small, theory-driven synthetic dataset induces persistent and interpretable shifts in strategic behavior. In applications to moral dilemmas and repeated duopoly pricing, agents aligned to different preference structures produce systematically distinct equilibrium outcomes and pricing dynamics. These results frame AI alignment in multi-agent settings as an objective-design problem and illustrate how economic theory can guide the design of strategically coherent AI agents.

</details>

---

### 48. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等20人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种名为LatentChem的新方法，旨在改进化学大语言模型的推理机制。

**📖 中文摘要**

本文介绍了LatentChem，一种用于化学推理的潜在推理接口。该工作直接针对“化学大模型”这一核心主题，旨在解决当前化学大语言模型（LLMs）依赖显式自然语言思维链（CoT）进行推理的局限性。作者指出，化学推理本质上是连续和结构化的，将其强制转化为离散的语言标记会导致表征失配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中进行多步推理，而仅输出最终的语言结果。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变不仅是风格上的，更是计算优势上的。在多个化学推理基准测试中，LatentChem相比基于CoT的基线模型取得了显著优势（在ChemCoTBench上获得59.88%的非平局胜率），同时平均减少了10.84倍的推理开销。这项工作为化学大模型提供了一种新的、更高效的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average reduction in reasoning overhead. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 49. [Proof-Carrying Materials: Falsifiable Safety Certificates for Machine-Learned Interatomic Potentials](https://arxiv.org/abs/2603.12183)

**基本信息**

- 🔗 arXiv: [`2603.12183`](https://arxiv.org/abs/2603.12183)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12183.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（机器学习模型的可靠性审计与安全认证）与构建可靠、稳健的“化学大模型”这一主题直接相关，为化学信息学中的模型可信度问题提供了重要思路。

**📖 中文摘要**

本文提出了“材料证明携带”（Proof-Carrying Materials, PCM）框架，旨在为机器学习原子间势（MLIPs）提供可证伪的安全性证书。虽然论文主要关注材料科学中MLIPs的可靠性验证，但其核心方法论——通过对抗性测试、置信区间构建和形式化验证来审计和保证机器学习模型在科学计算中的安全性——与构建可靠、可解释的“化学大模型”高度相关。论文中审计了CHGNet、TensorNet和MACE等先进的MLIPs，揭示了不同模型架构特有的盲点，并训练了一个风险模型来预测未见材料的失败情况。这种系统性的模型评估、漏洞发现和可靠性保证框架，对于开发用于化学信息学（如分子性质预测、反应预测）的稳健大模型具有重要的借鉴意义。它提供了一种确保模型在复杂化学空间中进行高通量筛选时可靠性的方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learned interatomic potentials (MLIPs) are deployed for high-throughput materials screening without formal reliability guarantees. We show that a single MLIP used as a stability filter misses 93% of density functional theory (DFT)-stable materials (recall 0.07) on a 25,000-material benchmark. Proof-Carrying Materials (PCM) closes this gap through three stages: adversarial falsification across compositional space, bootstrap envelope refinement with 95% confidence intervals, and Lean 4 formal certification. Auditing CHGNet, TensorNet and MACE reveals architecture-specific blind spots with near-zero pairwise error correlations (r <= 0.13; n = 5,000), confirmed by independent Quantum ESPRESSO validation (20/20 converged; median DFT/CHGNet force ratio 12x). A risk model trained on PCM-discovered features predicts failures on unseen materials (AUC-ROC = 0.938 +/- 0.004) and transfers across architectures (cross-MLIP AUC-ROC ~ 0.70; feature importance r = 0.877). In a thermoelectric screening case study, PCM-audited protocols discover 62 additional stable materials missed by single-MLIP screening - a 25% improvement in discovery yield.

</details>

---

## 📊 数据统计
- 累计运行天数：33
- 累计论文数量：2301

## 📝 历史记录

> 暂无历史数据

