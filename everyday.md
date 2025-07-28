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
