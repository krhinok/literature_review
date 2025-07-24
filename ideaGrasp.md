通过让用户控制高层决策，同时将低层动作委托给自主机器人，这种方法既保留了用户的代理感，又提升了整体系统性能。

分别使用VR VR+vision VR+vision+LLM
使用LLM可以带来哪些改变，为什么不只使用VR

模块 使用在不同机器人

语言提供约束

VVL-Tele: A MultiModal Teleoperation System for Mobile Manipulation Integrating VR, Vision and Language.

motivation, significance, major challenges, novelty, expected outcomes and impacts

传统遥操作方法通常只使用单一模态作为输入，如使用外骨骼[1，2]，VR[3，4]，RGB cameras [5, 6, 7], wearable gloves [8, 9, 10], language[11, 12]等方法。这些方法都有各自的弊端，例如外骨骼以及VR设配长期佩戴会使操作者疲倦；RGB cameras在有遮挡环境下无法准确获得输入数据；gloves需要根据为操作者定制大小等。总体来说，使用单一模态输入遥操作在特殊场景下存在操作不直观，操作难度大，精度差，成功率低，用户意图较难推断的问题，尤其是对于没有遥操作经验甚至残疾使用者来说。因此，本项目旨在开发一个基于VR，Vision，Language多模态控制的遥操作系统，用来控制Mobile manipulator安全地执行任务。通过多模态融合，我们希望避免上述使用单一模态输入遥操作的问题。
该系统有利于使用者在不同的场景下使用合适的一种或多种方式控制Mobile manipulator，例如在存在遮挡的环境下使用VR+language的方式，在遇到紧急情况直接使用自然语言停止Mobile manipulator的行动，在追求机械臂准确操作时使用VR+Vision的方法等。该系统的提出可以提升人机交互的包容性和效率，降低操作门槛，提高任务成功率。适用于日常生活场景，帮助行动不便者完成日常任务；也适用于灾后救援，危险环境中的操作等场景。同时利用本系统可以采集高质量数据用于模仿学习，为实现机器人全自主操作奠定基础。
本项目的主要挑战为如何融合VR，Vision和language输入的数据，如何防止系统过于庞大和如何确保系统的安全性。
本项目的创新点在于提出了一个融合VR，vision,language多模态输入，应用于Mobile manipulator的遥操作系统，并设计了多模态输入的融合算法，可以用于不同的机器人，例如realman或者tiago++。



[1] Wei, W., Zhou, B., Fan, B. et al. An Adaptive Hand Exoskeleton for Teleoperation System. Chin. J. Mech. Eng. 36, 60 (2023). https://doi.org/10.1186/s10033-023-00882-w
[2] Y. Su, G. Li, Y. Deng, I. Sarakoglou, N. G. Tsagarakis and J. Chen, "The Joint-Space Reconstruction of Human Fingers by using a Highly Under-Actuated Exoskeleton," 2024 IEEE International Conference on Robotics and Automation (ICRA), Yokohama, Japan, 2024, pp. 9645-9651, doi: 10.1109/ICRA57147.2024.10610872.
[3] Open-TeleVision: Teleoperation with Immersive Active Visual Feedback. Xiaolong Wang
[4] A. Iyer, Z. Peng, Y. Dai, I. Guzey, S. Haldar, S. Chintala, and L. Pinto. Open teach: A versatile teleoperation system for robotic manipulation, 2024.
[5] Y. Qin, W. Yang, B. Huang, K. Van Wyk, H. Su, X. Wang, Y.-W. Chao, and D. Fox. Anyteleop:A general vision-based dexterous robot arm-hand teleoperation system. In Robotics: Science and Systems, 2023.
[6] A. Sivakumar, K. Shaw, and D. Pathak. Robotic telekinesis: Learning a robotic hand imitator by watching humans on youtube. arXiv preprint arXiv:2202.10448, 2022.
[7] S. Li, J. Jiang, P. Ruppel, H. Liang, X. Ma, N. Hendrich, F. Sun, and J. Zhang. A mobile robot hand-arm teleoperation system by vision and imu. In 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 10900–10906. IEEE, 2020.
[8] M. Caeiro-Rodr´ıguez, I. Otero-Gonzalez, F. A. Mikic-Fonte, and M. Llamas-Nistal. A system-atic review of commercial smart gloves: Current status and applications. Sensors, 21(8):2667,2021.
[9] H. Liu, Z. Zhang, X. Xie, Y. Zhu, Y. Liu, Y. Wang, and S.-C. Zhu. High-fidelity grasping in virtual reality using a glove-based system. In 2019 international conference on robotics and automation (icra), pages 5180–5186. IEEE, 2019.
[10] H. Liu, X. Xie, M. Millar, M. Edmonds, F. Gao, Y. Zhu, V. J. Santos, B. Rothrock, and S.-C. Zhu. A glove-based system for studying hand-object manipulation via joint pose and force sensing. In 2017 IEEE/RSJ Intern
[11] LILA: Language-Informed Latent Actions
[12] “No, to the Right” – Online Language Corrections for Robotic Manipulation via Shared Autonomy


