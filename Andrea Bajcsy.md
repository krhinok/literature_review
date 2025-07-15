## Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions
code: yes

通过操纵杆输入一个“向前”的指令，传统控制器可能会输出一个高维动作：
预测：joint_1 = 0.3 rad/s, joint_2 = -0.2 rad/s, ..., joint_7 = 0.1 rad/s
但 conformalized 控制器会告诉你：
预测：joint_1 ∈ [0.2, 0.4] rad/s (90%置信区间)
预测：joint_2 ∈ [-0.3, -0.1] rad/s (90%置信区间)

Prior works on dimensionality reduction have shown increasingly sophisticated methods for designing or learning a mapping from the user’s input to the robot’s high-DOF control action [39, 24, 40, 19].

早期的维度简化研究提出了越来越复杂的方法，用于从用户输入中设计或学习出到机器人高自由度动作的映射关系 [39, 24, 40, 19]。

Alternatively, the shared control paradigm combines low-DoF human input with autonomous robot policies in order to make teleoperation of the robot more fluent [7, 6].

另一种方法是“共享控制”模式，它结合了低自由度的人类输入与机器人的自动策略，从而使遥操作更流畅 [7, 6]。

Other works considers the inverse approach of developing high-dimensional interfaces to control high-DoF robots [35].

还有研究反过来尝试开发高维人机接口，直接控制高自由度机器人 [35]。

## Adapting by Analogy: OOD Generalization of Visuomotor Policies via Functional Correspondence
OOD-ID
我们方法的一个关键部分是利用专家的人类知识——以文本描述的形式——来交互式地学习与当前任务相关的高级功能对应关系。
![alt text](<屏幕截图 2025-07-15 061321.png>)

code:no

Future work should study the autonomous identification of correspondence features (e.g., via another foundation model).

## Generalizing Safety Beyond Collision-Avoidance via Latent-Space Reachability Analysis
