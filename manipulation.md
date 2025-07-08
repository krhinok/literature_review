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
