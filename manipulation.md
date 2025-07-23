
训练数据来源：遥操作数据
遥操作只是为了提供数据？
辅助遥操作抓取：在移动机器人进行遥操作抓取时，不同物体应当抓取不同的位置，避免例如液体洒落等问题。在抓取物体时

## 1.AhaRobot: A Low-Cost Open-Source Bimanual Mobile Manipulator for Embodied AI
本文提出 AhaRobot，一种低成本、开源、双臂移动操作机器人系统，旨在推动具身人工智能（Embodied AI）研究在真实环境中的应用。AhaRobot系统的成本仅为1000美元（不含计算模块），约为现有主流移动操作平台的 1/15。
 模仿学习任务
使用ACT算法对三个任务（如拾取盒子、插笔、收集玩具）进行模仿学习，平均成功率高，最高达到 100%。为了解决移动底座控制中的困难，作者采用位置控制替代速度控制，提升了学习稳定性。

code:yes

## 2.BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities
在现实家庭环境中，移动操作机器人面临诸多挑战，如操控变形物体、在狭窄空间中操作、以及跨越长距离移动并完成精细任务。现有的机器人基准测试表明，成功执行这些任务主要依赖于三个关键的全身控制能力：

双臂协调：需要两个机械臂协同工作；

稳定而精准的导航能力：机器人必须能平稳地在家中移动；

广泛的末端执行器可达性：机械臂能够灵活地伸展、到达复杂位置。

为了解决因系统复杂性带来的感知和运动控制学习难题，研究人员提出了一个完整解决方案——BEHAVIOR Robot Suite（BRS），其主要特点包括：

🧠 一体化硬件平台：基于具备双臂、轮式底盘和4自由度躯干的移动机器人；

🎮 低成本全身遥操作界面：用于收集人类演示数据，训练机器人；

🤖 全身视觉运动控制策略的学习算法：让机器人能够模仿人类完成日常任务。

视觉感知依赖度高 算力需要

code:yes

## 3.Beyond Task and Motion Planning: Hierarchical Robot Planning with General-Purpose Policies
核心创新：TASP + CIP
1. TASP方法简介
为了解决上述挑战，作者提出了 Task and Skill Planning（TASP） 框架，一种分层规划方法，结合了：

高层的符号规划器（symbolic planner）；

低层的运动规划与技能控制；

以及通用技能的封装与可组合性处理。

2. Composable Interaction Primitives（CIPs）
论文核心机制是 CIP，即可组合交互原语，每一个CIP代表一个“技能+上下运动规划”的三段结构：

Head plan：运动到技能的起始条件；

Skill policy：执行一个非运动技能（如擦白板）；

Tail plan：从技能结束后运动回空闲状态。

通过这种“夹心式”设计，TASP 能够将非运动技能整合进传统TAMP框架中，使得不具可组合性的预训练技能可以被连接在一起使用。

code: no

## 4. Bilevel Learning for Bilevel Planning

神经符号双层学习框架，称为 IVNTR

研究动机：传统的双层规划（bilevel planning）方法依赖于手工设计或过于简单的谓词（predicates），难以扩展到连续或高维状态空间中。这限制了机器人从演示中学习并泛化到新任务的能力。

方法贡献：作者提出了 IVNTR，这是首个能从示范中直接学习神经谓词的双层规划方法。它采用神经-符号的混合学习机制，交替进行：

符号学习：学习谓词的“效果”；

神经学习：学习谓词的“函数”。

这两者互相指导，从而实现更强的抽象能力和任务泛化。

实验结果：在六个不同的机器人任务环境中，IVNTR 在未见任务中的平均成功率为 77%，而其他方法通常低于 35%。此外，它还成功应用于真实的移动操控机器人上，能泛化到新的物体、新状态和更长的任务序列。

code :yes

## 5. DexWild: Dexterous Human Interactions for In-the-Wild Robot Policies

**DexWild: 用于自然环境中机器人策略的灵巧人类交互** 是一项前沿研究，旨在通过从“自然环境”（in-the-wild）中收集的人类交互数据，训练出能够适应真实世界任务的机器人灵巧操作策略。DexWild 的核心思想是：利用未经精心设计或实验室控制的真实人类操作视频和交互数据，作为学习机器人手部操作技能的基础，从而提升其在现实生活场景中的泛化能力和灵活性。

### 背景与意义

传统的机器人灵巧操作策略往往依赖于：

* 在实验室中精心采集的演示数据；
* 昂贵的遥操作设备；
* 高度控制的模拟环境。

这些方法限制了机器人在现实世界中面对复杂、不确定任务时的适应性。而 DexWild 提出，从日常生活中捕捉到的人类操作行为中直接学习，可以打破这种限制。

### 技术关键点

* **无标签人类视频数据学习**：DexWild 利用如 YouTube、生活记录等自然环境下的视频，通过计算机视觉提取手部姿态和物体交互信息。
* **策略训练与泛化**：将提取到的人类操作先验（如手部姿态、物体抓握方式）作为强化学习的引导，提升学习效率和策略泛化能力。
* **高自由度灵巧手控制**：采用具备30自由度的机器人手（如Shadow Hand），使其模仿人类完成多样化的抓握与操控任务。

### 类似相关研究

DexWild 的研究理念与以下成果密切相关：

* [DexVIP](https://consensus.app/papers/dexvip-learning-dexterous-grasping-with-human-hand-pose-mandikal-grauman/618236dbc6b75a5db43d96a0cfe66caf/?utm_source=chatgpt)：从 YouTube 视频中提取人类手部抓握先验，用于训练机器人抓握策略；
* [DexCap](https://consensus.app/papers/dexcap-scalable-and-portable-mocap-data-collection-system-wang-shi/d75d77ace6d25fd09e98d632c2e221a1/?utm_source=chatgpt)：构建可扩展的运动捕捉系统，从自然环境中获取高质量人类手部动作数据；
* [DexMV](https://consensus.app/papers/dexmv-imitation-learning-for-dexterous-manipulation-from/c1b82accb89f54e59d91a86d3c5f8834/?utm_source=chatgpt)：通过从视频中提取的3D手部与物体姿态，实现机器人灵巧操作的模仿学习。

### 总结

DexWild 所代表的研究方向，标志着机器人从“实验室学习”迈向“现实世界学习”的重要转变。通过大规模、人类自然行为数据驱动的学习策略，DexWild 有望赋予机器人更强的操作能力与环境适应性，是迈向通用机器人操作智能的重要一步。

code:yes

84544361654+1

## 6. EMMOE: A Comprehensive Benchmark for Embodied Mobile Manipulation in Open Environments
面向“开放环境下具身移动操作”（Embodied Mobile Manipulation）的综合性评测基准 EMMO

面向“开放环境下具身移动操作”（Embodied Mobile Manipulation）的综合性评测基准 EMMOE，旨在推动自然语言驱动的家庭服务机器人发展。现有挑战包括：

缺乏统一的长时序复杂任务评测基准；

评估方法单一；

大语言模型（LLM）与机器人轨迹数据之间存在不兼容问题。

为此，作者构建了：

EMMOE Benchmark：统一融合高层规划与底层操作任务；

EMMOE-100 数据集：包含100个复杂任务，支持失败重试、任务属性标注、过程注释、以及用于训练LLM的子数据集（SFT 与 DPO）；

HOMIEBOT 智能体系统：结合LLM规划、轻量级导航与操作模型、多种错误检测机制，完成任务执行与反馈循环。

code:yes

## 7.Evaluating Real-World Robot Manipulation Policies in Simulation
在实际中对机器人操作策略进行评估成本过高，这篇文章提出了一种可以通过仿真来代替现实进行评估的方法

这篇论文提出了一个名为 SIMPLER 的方法体系：

通过构建通用仿真环境，模拟真实机器人平台的典型任务；

缩小“仿真-现实差距”，特别是视觉和控制精度方面的差距；

验证仿真与真实评估结果高度相关，即可以用仿真结果近似替代真实实验；

所有工具和流程都开源，便于他人使用和扩展。

code:yes

## 8.FRESHR-GSI: A Generalized Safety Model and Evaluation Framework for Mobile Robots in Multi-Human Environments

机器人与人的安全检测

该论文提出了一个通用的、可扩展的安全评估框架，名为 FRESHR-GSI（Generalized Safety Index），专门用于评估移动机器人在多人环境下的人类安全。与传统集中于工业机械臂的安全指标不同，该框架面向 移动机器人与多个行人动态共处的开放空间。

框架整合了以下关键参数来实时计算安全性指数：

人与机器人的相对距离

人的移动速度

人体面向的朝向信息

此外，该系统通过集成 RGB-D 摄像头与深度学习的人体检测算法，实现对周围环境中人的动态感知，并生成细粒度的安全指数（GSI）。

code：no

## 9.HEATS: A Hierarchical Framework for Efficient Autonomous Target Search with Mobile Manipulators
复杂未知环境中进行目标搜索任务的能力

code:coming soon

## 10.Hi-Dyna Graph: Hierarchical Dynamic Scene Graph for Robotic Autonomy in Human-Centric Environments

复杂场景环境构建

**Hi-Dyna Graph：面向人类中心环境下机器人自主性的分层动态场景图**


### 简介

在现实世界中，机器人需要在动态、复杂且以人为中心的环境中自主运行，例如室内办公室、商场或家庭等场景。**Hi-Dyna Graph**（Hierarchical Dynamic Scene Graph，分层动态场景图）是一种新型的场景表示方法，旨在帮助机器人构建对环境更深入的理解，从而实现更加智能、自主的感知、规划和交互。

Hi-Dyna Graph 的核心思想是将环境建模为一个**不断更新的图结构**，图中的节点代表场景中的对象（如人、桌子、房间等），边表示它们之间的语义关系（如“在……里面”、“靠近”等）。这种结构是**分层的**，可以支持从低层物体识别到高层空间语义推理，同时支持动态更新，适应环境中人的移动、物体的变动等实时变化。

### 相关研究支撑

1. \*\*3D动态场景图（3D Dynamic Scene Graphs）\*\*提出了一种将场景表示为包含人、物体和空间关系的图结构的方法，可支持机器人进行空间理解和任务规划 [(Rosinol 等, 2020)](https://consensus.app/papers/3d-dynamic-scene-graphs-actionable-spatial-perception/17b3f56e3a84578e8ef7b669169cb5bb/?utm_source=chatgpt)。

2. **OrionNav 系统**利用大语言模型（LLM）与分层场景图结合，实现了机器人在未知动态环境中的实时自主导航，支持自然语言任务输入和多步规划 [(Devarakonda 等, 2024)](https://consensus.app/papers/orionnav-online-planning-for-robot-autonomy-with-devarakonda-goswami/2a5876b391ed50268eb837ec6311dee5/?utm_source=chatgpt)。

3. \*\*约束式动态实体建模（Constraint-Based Dynamic Entities）\*\*使用分层3D场景图将动态物体（如人）纳入SLAM系统，提高了机器人对动态环境中物体和自身定位的准确性 [(Giberna 等, 2025)](https://consensus.app/papers/constraintbased-modeling-of-dynamic-entities-in-3d-scene-giberna-shaheer/01fffe7174f95c848aab05f4a618923e/?utm_source=chatgpt)。

4. **xFLIE架构**利用分层语义图进行任务规划和环境探索，使机器人能够在未知环境中基于语义信息进行感知和路径规划 [(Viswanathan 等, 2024)](https://consensus.app/papers/xflie-leveraging-actionable-hierarchical-scene-viswanathan-saucedo/040c18caabff54ac8395c387754d9fea/?utm_source=chatgpt)。

---

### 总结

Hi-Dyna Graph 的设计思想正在引领机器人场景理解的发展方向。通过**分层建模、动态更新和语义推理**，它为机器人在复杂人类环境中的自主行为提供了强大的支持，是实现高水平智能机器人的关键工具之一。

code: not yet

## 11. HOMER: Learning In-the-Wild Mobile Manipulation via Hybrid Imitation and Whole-Body Control
该论文提出了一种面向**移动操作任务（mobile manipulation）**的模仿学习系统框架 HOMER，主要用于处理现实家庭环境中的复杂任务。HOMER 结合了：

混合动作策略（Hybrid Action Modes）：结合了用于长距离移动的绝对位姿预测和用于精细操作的相对动作预测；

基于运动学的全身控制器（Whole-Body Controller, WBC）：将高层次的末端执行器动作转化为移动底盘与机械臂的协调动作；

模仿学习（Imitation Learning, IL）：仅用 20 条演示就能实现出色的策略学习。

该系统部署在一个具有全向轮和 7 自由度机械臂的机器人平台上，并在实际家庭环境中执行任务（如开柜门、扫垃圾、整理枕头），在六项任务中取得 79.17% 的平均成功率，领先基线方法 29.17%。

code: yes

## 12. Immersive Teleoperation Framework for Locomanipulation Tasks
这篇论文《Immersive Teleoperation Framework for Locomanipulation Tasks》由伦敦大学学院（UCL）的研究团队于2025年4月21日发布，提出了一种新型的虚拟现实（VR）远程操作框架，旨在提升机器人在移动和操作任务中的精确性和沉浸感。([paperreading.club][1])

---

### 🧠 主要内容

该框架结合了移动平台和机械臂，采用高斯点阵（Gaussian Splatting）技术，在VR环境中构建高保真、三维的场景表示，使操作者能够像与真实机器人互动一样进行导航和操作。([paperreading.club][1])

系统分为两个阶段：([emergentmind.com][2])

1. **导航阶段**：操作者使用传统控制界面（如操纵杆）和2D摄像头视图进行机器人底盘的定位。([paperreading.club][1])

2. **操作阶段**：当机器人到达目标位置后，系统切换到VR界面，操作者通过“抓取”和“拖动”虚拟机械臂模型来进行精细操作。([themoonlight.io][3])

该方法通过高斯点阵渲染技术，提供更深的空间一致性，允许操作者自由调整视角，特别有助于处理被遮挡的任务。([paperreading.club][1])

---

### 💡 创新点

* **高斯点阵渲染**：不同于传统的结构光或点云重建方法，该技术通过将场景表示为一组3D高斯分布，实现了更高效、实时的渲染，特别适用于动态环境中的远程操作。([quantumzeitgeist.com][4])

* **双阶段操作流程**：结合传统控制和沉浸式VR交互，提升了任务的精确性和效率。

* **用户研究验证**：通过用户研究，系统在任务完成时间、精确度、响应性和情境意识等方面表现优于传统方法。([paperreading.club][1])

---

### ⚠️ 存在的问题

* **延迟和带宽限制**：高质量的VR渲染和实时数据传输可能受到网络延迟和带宽的限制，影响操作体验。

* **环境复杂性**：在极端复杂或动态变化的环境中，系统的表现和鲁棒性仍需进一步验证。

* **操作者适应性**：长时间使用VR设备可能导致操作者疲劳，影响操作效率。

* **硬件成本**：高质量的传感器和VR设备增加了系统的整体成本和部署复杂度。

* **自动化程度**：目前系统主要依赖人工操作，缺乏智能辅助决策和自动化功能。

---

### 🔗 获取论文全文

您可以通过以下链接访问论文全文：

* [arXiv预印本](https://arxiv.org/abs/2504.15229)

* [ResearchGate页面](https://www.researchgate.net/publication/390991491_Immersive_Teleoperation_Framework_for_Locomanipulation_Tasks)


[1]: https://paperreading.club/page?id=301107&utm_source=chatgpt.com "Immersive Teleoperation Framework for ... - Paper Reading"
[2]: https://www.emergentmind.com/papers/2504.15229?utm_source=chatgpt.com "Immersive Teleoperation for Locomanipulation - Emergent Mind"
[3]: https://www.themoonlight.io/en/review/immersive-teleoperation-framework-for-locomanipulation-tasks?utm_source=chatgpt.com "[Literature Review] Immersive Teleoperation Framework for ..."
[4]: https://quantumzeitgeist.com/virtual-reality-transforms-teleoperation-with-gaussian-splatting/?utm_source=chatgpt.com "Virtual Reality Transforms Teleoperation With Gaussian Splatting"

## 13. Implicit Communication in Human-Robot Collaborative Transport
论文《Implicit Communication in Human-Robot Collaborative Transport》的核心创新点主要集中在**如何通过动作中的隐含信号提升人与机器人协同搬运任务中的协调效率和自然交互感**。以下是其主要内容创新点总结：

### 1. **动作中的隐性信号作为沟通媒介**

* 创新地提出机器人可以通过其操作对象（被共同搬运的物体）的状态变化来**隐式传达意图**，从而与人类协同搬运，无需口头或显式指令。
* 这种“物体状态即信号”的方法，允许人与机器人在没有语言交流的情况下实现流畅配合 [(Yang & Mavrogiannis, 2025)](https://consensus.app/papers/implicit-communication-in-humanrobot-collaborative-yang-mavrogiannis/60e7d81acf67575eaad40c3eff0e265d/?utm_source=chatgpt)。

### 2. **基于推理机制的策略推断**

* 设计了一种**概率推理机制**，可以从人机联合动作的观测数据中**推断出目标路径的协同策略**。
* 该机制为机器人建立了对人类意图的理解模型，使机器人能在不明确知道目的地的情况下选择合适的行动方向。

### 3. **引入不确定性最小化成本函数**

* 提出一种新颖的成本函数，代表人类对运输策略的不确定性，机器人通过模型预测控制器（MPC）在最小化不确定性的同时**优化任务效率**。

### 4. **实证验证：机器人表现更流畅、更高效**

* 在移动机械臂 Hello Robot Stretch 上部署该框架，并通过24人参与的实验发现：相比不具备沟通机制的对照组，机器人显著提升了任务效率，**更被认为是“流畅”、“可信赖”的协作伙伴** [(Yang & Mavrogiannis, 2025)](https://consensus.app/papers/implicit-communication-in-humanrobot-collaborative-yang-mavrogiannis/60e7d81acf67575eaad40c3eff0e265d/?utm_source=chatgpt)。

### 总结

该研究的最大创新在于将**隐性动作信号编码**作为人与机器人之间的沟通方式，并结合推理模型和优化控制方法，实现了无需显式交流的高效协同搬运系统。

code:yes


## 14 Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation
论文《Instruction-Augmented Long-Horizon Planning: Embedding Grounding Mechanisms in Embodied Mobile Manipulation》的核心创新点在于**将自然语言指令与长期规划能力结合，通过多层次的语义与感知机制，实现机器人在复杂环境中自主完成长时间、多步骤的移动操控任务**。根据相关研究成果，该方向的主要内容创新可总结如下：

---

### 核心创新点总结：

1. **指令增强的长期规划（Instruction-Augmented Long-Horizon Planning）**
   利用大语言模型（LLM）将自然语言指令分解为结构化子任务或策略目标，然后通过符号规划、图结构或动作库完成可执行动作计划。此方式增强了机器人理解与执行复杂任务的泛化能力。
   相关研究支持：使用LLM生成子目标并与视觉语言模型协作可实现复杂的双臂移动操控任务 [(Li et al., 2024)](https://consensus.app/papers/instructionfollowing-longhorizon-manipulation-by-li-liu/e2458faa55b9537cb44f828c74313982/?utm_source=chatgpt)。

2. **嵌入式语义锚定机制（Embedded Grounding Mechanisms）**
   通过引入动作和感知的语义锚定机制，使机器人能够在执行过程中检测偏差并纠正。动作库、感知库以及动态状态图用于桥接高层语言规划与低层物理执行。
   相关研究支持：构建行为感知库，并基于LLM进行动态任务修正 [(Wang et al., 2024)](https://consensus.app/papers/autonomous-behavior-planning-for-humanoid-wang-laurenzi/4441a169365957ceb68cca7d0b503859/?utm_source=chatgpt)。

3. **跨场景与跨域的技能迁移能力**
   采用层级语义技能分解（如SemGro框架），区分通用短期技能与特定领域的长时任务，并利用语言模型在新环境中进行语义迁移和适配。
   相关研究支持：通过语义技能分解提高在300个跨域任务中的迁移成功率 [(Shin et al., 2024)](https://consensus.app/papers/semantic-skill-grounding-for-embodied-shin-kim/b59fdee460a0501eba3a4f6116b9a4d2/?utm_source=chatgpt)。

4. **融合语言模型与符号规划**
   将自然语言任务分解、视觉理解、动作执行以模块化结构集成，使得系统具备强泛化能力、对未知目标具有适应性。该方法支持从自由文本到动作序列的完整转换。
   相关研究支持：语言模型生成目标状态，符号规划器完成任务执行 [(Li et al., 2024)](https://consensus.app/papers/instructionfollowing-longhorizon-manipulation-by-li-liu/e2458faa55b9537cb44f828c74313982/?utm_source=chatgpt)。

---

### 总结：

本研究的主要创新在于：**将自然语言指令嵌入至长期移动操控规划体系中，并通过语义锚定机制提高跨场景、跨技能的泛化能力与稳定执行性能**。该方法展示了大语言模型在复杂机器人任务中的规划能力，并在现实与仿真环境中均有有效验证。
