# 7.27
## Adaptive Articulated Object Manipulation On The Fly with Foundation Model Reasoning and Part Grounding
铰接物体给机器人操纵带来多样挑战，需要自适应探索和动作精炼。现有方法难以跨类别泛化。该论文提出AdaRPG框架，利用基础模型（foundation models）提取物体部件，这些部件具有更高的局部几何相似性，从而提升视觉功能性（affordance）泛化，用于功能性基本技能。框架还借助基础模型推理复杂机制，并基于部件功能性推理生成高级控制代码。模拟和真实世界实验显示，AdaRPG在新型铰接物体类别上具有强大泛化能力

## Experimental Comparison of Whole-Body Control Formulations for Humanoid Robots in Task Acceleration and Task Force Spaces
该论文比较了两种全身控制方法：逆动力学全身控制（Inverse Dynamics Whole-Body Control, ID-WBC）和基于被动性的全身控制（Passivity-Based Whole-Body Control, PB-WBC）。ID-WBC基于任务加速空间制定，而PB-WBC则在任务力空间中融入被动性考虑。尽管两种方法在理想条件下均能实现闭环动态稳定性，但它们对关节摩擦、传感器噪声、未知外部扰动和非完美接触条件的鲁棒性尚不清楚。作者通过人形机器人平台的实验任务（如摆足位置和方向控制、带/不带未知额外重量的蹲起，以及跳跃）进行分析和比较，揭示性能差异，并突出每种控制器的优缺点

## TypeTele: Releasing Dexterity in Teleoperation by Dexterous Manipulation Types
灵巧遥操作对机器人操纵在真实世界数据收集和远程控制至关重要。传统方法依赖于手部重定向来模仿人类手部姿势，但这限制了灵巧手的潜力。为解决此问题，论文提出TypeTele，一个类型引导的灵巧遥操作系统，通过引入灵巧操纵类型，使机器人手能执行非人类运动模式的动作。该系统包括一个可扩展的操纵类型库，以及一个MLLM辅助的类型检索模块，用于根据任务和命令选择合适类型。实验表明，该方法在多样化和复杂任务中提高了成功率和效率

## ReSem3D: Refinable 3D Spatial Constraints via Fine-Grained Semantic Grounding for Generalizable Robotic Manipulation
语义驱动的3D空间约束将高层语义表示与低层动作空间对齐，促进机器人操纵的任务理解和执行统一。现有方法存在限制：（1）约束建模的语义粒度粗糙；（2）缺乏实时闭环规划；（3）在语义多样环境中的鲁棒性不足。为解决这些问题，论文提出ReSem3D框架，利用VFMs和MLLMs进行细粒度视觉 grounding，并动态构建分层3D空间约束，支持实时操纵。框架采用MLLMs中的分层递归推理，与VFMs交互，从自然语言指令和RGB-D观察中分两个阶段构建约束：部件级提取和区域级精炼。这些约束编码为关节空间的实时优化目标，实现对动态扰动的反应行为。模拟和真实世界实验显示，ReSem3D在零样本条件下处理多样操纵任务，具有强大适应性和泛化能力

## High-Resolution Characterization of the Size Exclusion Effect on the Transport of Low-Concentration Mixed-Size Colloids in Porous Media Using a Synthetic DNA-Labeling Method
胶体在地下水中的传输对污染物扩散至关重要，其中尺寸排除效应（Size Exclusion Effect, SEE）是影响胶体命运的关键机制。然而，准确测量低浓度胶体并区分不同粒径的胶体仍面临挑战。本研究将特定DNA片段封装在粒径为0.1、0.2、0.5、1.0、3.0和5.0 μm的胶体中，进行单尺寸或多尺寸胶体的柱状实验，以表征胶体突破曲线并量化SEE。该方法显著增强了检测信号，能够在极低浓度（≤10 mg L⁻¹）下准确检测胶体并精确区分胶体尺寸。此外，通过拟合胶体突破曲线量化SEE的关键参数，即移动胶体不可达的水饱和度（γ）。回归分析显示，γ参数与胶体直径之间呈幂函数相关性，表明SEE随着胶体直径增加而加剧。这些发现突显了DNA标记在高分辨率表征低浓度和混合尺寸胶体颗粒在多孔介质中传输方面的潜力。该研究增强了对胶体传输行为的理解及其环境影响。

# 7.29
## A Fast and Light-weight Non-Iterative Visual Odometry with RGB-D Cameras
提出了一种使用RGB-D相机的视觉里程计（VO）的新方法。视觉里程计从图像序列中估计相机（或机器人）随时间的位置和方向，这对于增强现实（AR）、虚拟现实（VR）和自主导航等应用至关重要。
这种方法称为非迭代深度增强视觉里程计（NIDEVO），其突出特点是非迭代、解耦和轻量级，避免了传统方法（如ORB-SLAM或DSO）对特征提取、匹配和迭代优化求解器的依赖。相反，它利用场景中重叠的平面元素来估计6-DoF（自由度）姿态——将旋转和平移分离以提高效率。它在标准i5 CPU上实现了约71 Hz的实时性能，适用于资源受限的设备。

## Equivariant Volumetric Grasping
提出了一种新型的机器人抓取模型。该模型专注于体积表示的抓取任务，在机器人学中，体积抓取（volumetric grasping）是指基于3D物体体积特征（如点云或体素）来预测抓取姿态的方法。这种方法特别强调“等变性”（equivariance），即模型对输入的特定变换（如垂直轴旋转）保持一致的输出变换，从而提高样本效率和鲁棒性。该论文针对机器人抓取中的挑战，如物体方向多样性和数据需求高的问题，提出了一种高效的解决方案，适用于模拟和真实世界场景。
等变体积抓取的核心概念：在机器人抓取中，物体可能以不同角度出现。如果模型是等变的，当输入（物体3D表示）旋转时，输出（抓取预测）也会相应旋转，而无需重新训练。这减少了训练数据的需要，提高了泛化能力。该论文聚焦于垂直轴90°旋转的等变性，使用三平面体积特征表示来实现。

## METAMORPH – A Metamodeling Approach for Robot Morphology
针对机器人外观在人机交互（HRI）中的关键作用，以及现有分类方法的局限性（如仅依赖宽泛类别：拟人形、拟动物形或技术形，或仅关注拟人特征），提出了一种全面框架MetaMorph。该框架采用元建模方法，从IEEE Robots Guide中的222个机器人数据合成，提供结构化的视觉特征比较方法，帮助探索针对不同任务和情境的最优设计特征。
MetaMorph提供了一个全面的机器人形态分类解决方案，解决现有方法的不足，通过结构化元建模框架提升HRI理解。它支持视觉距离评估和设计特征探索，具有集成到HRI研究中的潜力，并可扩展到辅助技术（如为视障人士描述机器人）。
局限性包括：依赖IEEE Robots Guide数据集，可能未覆盖所有机器人类型或情境；视觉基础忽略功能方面；验证中发现少数缺失概念，需要进一步扩展；未进行大规模用户研究验证实用性。未来工作建议扩展到动态形态、集成AI生成设计，并进行实证HRI实验。

## Human-Agent Joint Learning for Efficient Robot Manipulation Skill Acquisition
通过比例调整人类操作者遥操作与assistive agent的控制比例，提高训练效率。

# 7.30
## A Human-in-the-loop Approach to Robot Action Replanning through LLM Common-Sense Reasoning
焦点在于通过人类参与（Human-in-the-Loop, HITL）框架，利用大型语言模型（LLM）的常识推理来优化机器人动作规划。该方法基于单张RGB视频自动生成的机器人执行计划，通过自然语言输入进行调整，以避免潜在失败并适应用户指定目标。通过人类自然语言干预来提升计划的准确性和适应性。

# 8.1
## A blessing or a burden? Exploring worker perspectives of using a social robot in a church
祝福还是负担？探索工人对在教堂中使用社交机器人的看法

## Improving Generalization Ability of Robotic Imitation Learning by Resolving Causal Confusion in Observations
增强复杂模仿学习算法的泛化能力。本文将IL策略建模为因果模型，使用有向图表示观察和动作之间的交互。

# 8.3
## Multi-layer robotic controller for enhancing the safety of mobile robot navigation in human-centered indoor environments
多层导航系统，旨在增强移动机器人在以人为中心的室内环境中的安全性。该系统专注于提高与机器人共享空间的弱势人群的安全性，同时通过减少对复杂传感器技术和计算资源的依赖来降低运营成本。

## villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models
用于增强视觉-语言-动作（VLA）模型中的潜在动作建模，以应用于机器人操作。它引入了视觉-语言-潜在动作（ViLLA）范式，该范式改进了潜在动作（帧间视觉变化的抽象表示）的学习方式及其在 VLA 预训练中的整合。
At its core, villa-X consists of two main components: the Latent Action Model (LAM) and the Actor (ACT) module.

在其核心，villa-X 由两个主要组件组成：潜在动作模型（LAM）和演员（ACT）模块。
The LAM infers latent actions from pairs of observations using an Inverse Dynamic Model (IDM), a visual Forward Dynamic Model (FDM), and a proprioceptive FDM, which aligns latent tokens with robot states and actions for better grounding. 

LAM 使用逆动态模型（IDM）、视觉前向动态模型（FDM）和本体感受前向动态模型（proprioceptive FDM）从观测对中推断潜在动作，后者将潜在标记与机器人状态和动作对齐，以实现更好的 grounding。
The ACT module, built on a pre-trained Vision-Language Model (VLM), predicts sequences of latent actions and robot actions via a diffusion-based approach, conditioned on visual and language inputs.

ACT 模块基于预训练的视觉-语言模型（VLM），通过基于扩散的方法预测潜在动作和机器人动作序列，受视觉和语言输入的条件约束。
Trained on diverse datasets like Open X-Embodiment, Something-Something V2, and Ego4D, villa-X achieves superior generalization.

在 Open X-Embodiment、Something-Something V2 和 Ego4D 等多样化数据集上训练，villa-X 实现了优越的泛化能力。
