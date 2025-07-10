# 7.5

一部分聚焦于意图预测 代替执行
进行粗略与精细两种遥操作
通过意图

遥操作的方式

考虑为disabled人群设计

抓取手型 机械臂姿态 学长提到的

## 1. CASPER: Inferring Diverse Intents for Assistive Teleoperation with Vision Language Models
这篇文章主要内容如下：

利用视觉语言模型推断辅助遥操作中的多样意图

### 背景与挑战

* **辅助遥操作** 是指人类与机器人共享控制，用于在非结构化环境中协作。但过去的方法通常只适用于特定场景或任务，泛化能力有限 
### 核心贡献

1. **开放世界感知模块**
   Casper 能识别和理解未知场景与物体，不再仅限于训练中见过的对象 ([catalyzex.com][2])。

2. **基于视觉语言模型（VLMs）的意图推断**
   利用预训练 VLM 嵌含的常识，系统可以实时解读用户的控制动作片段，从而预测更高层次的意图 ([arxiv.org][3])。

3. **技能库支持长程任务**
   通过预设多种操作技能（如抓取、打开、移动等），Casper 可将推断的意图转化为复杂、多步的自主行动 ([arxiv.org][3])。


### 总结

Casper 展示了一种通过视觉语言模型实现“意图认识+技能执行”的全新协作方式，使机器人能更自然地理解并辅助人类，适应更广泛的任务与环境。


[1]: https://chatpaper.com/zh-CN/chatpaper/paper/150450?utm_source=chatgpt.com "Casper: Inferring Diverse Intents for Assistive Teleoperation with Vision Language Models"
[2]: https://www.catalyzex.com/author/Yuke%20Zhu?utm_source=chatgpt.com "Yuke Zhu"
[3]: https://arxiv.org/abs/2506.14727?utm_source=chatgpt.com "Casper: Inferring Diverse Intents for Assistive Teleoperation with Vision Language Models"

code: coming soon


# 7.6
## 2.Intelligent Mode-switching Framework for Teleoperation
提出了一种智能模式切换框架，用于提升远程操作（teleoperation）的效率和可靠性，特别是在通信受限和操作复杂度高的环境中。
传统的远程操作往往依赖操作者在不同操作模式（自动与手动）之间切换，这不仅增加了操作负担，还在通信受限的情况下带来不稳定因素。

用户意图识别（User Intention Recognition）：在操作者端部署算法，实时识别其操作意图。

深度强化学习（Deep Reinforcement Learning, DRL）代理：根据识别出的用户意图，在手动控制与自动操作之间进行无缝切换。

联合考虑通信系统：该框架将通信质量和资源限制纳入决策过程，而非像传统方法那样忽视通信瓶颈。

真实数据集训练：在实际的远程操作测试平台上采集数据，用于训练意图识别和DRL模型

literature review: https://www.themoonlight.io/en/review/intelligent-mode-switching-framework-for-teleoperation

code: no

## 3. Global-Local Interface with Selective Direct and Singularity-Avoiding Motion Mapping for Intuitive Teleoperation
论文提出了一种名为“全局‑局部”（Global‑Local，G‑L）遥操作接口的新框架，旨在融合大范围运动控制与精细操作的优势，提升工业和非结构化环境下的遥操作效率与灵活性

核心概念：G‑L 接口
🔹 全局模块（Global）
负责机器人末端的快速、大范围定位。

可以直观反映整体运动空间与潜在碰撞，侧重效率而非精度。

🔹 局部模块（Local）
专注于细节控制，提升末端的精准与灵巧度（如方向、微动作）。

更强调手部操作的连贯性，适用于细致任务。

G‑L 接口通过把遥控主设备分成这两个模块，使操作者能实现“大动作再细调”的操作风格，覆盖从点对点抓取到精密装配等多样任务 。

code:no

## 4. TelePreview: A User-Friendly Teleoperation System with Virtual Arm Assistance for Enhanced Effectiveness

遥操作（teleoperation）是机器人学习演示（learning from demonstration）中的重要数据采集方式。然而，目前的遥操作系统普遍面临三大难题：

对新手不友好：尤其在控制高自由度机械手时，新手难以理解人手与机器人手之间的动作映射关系。

操作存在安全隐患：错误操作可能导致机器人碰撞或损坏设备。

平台间通用性差：现有系统在不同机器人平台之间迁移困难，缺乏通用性。

🚀 TelePreview 的创新设计
1. 虚拟预览机制（Virtual Arm Preview）
用户操作之前，系统会生成一个虚拟机械臂动画，预测机器人将如何响应当前动作。

用户可以“预演”命令效果，确认无误后再执行实际操作。

该机制极大减少了新手的试错成本，并提升操作安全性。

2. 命令与执行分离（Preview-Then-Act Paradigm）
系统允许在“指令预览”与“实际执行”之间灵活切换，提供更清晰的任务意图表达方式。

3. 低成本实现
TelePreview 系统的总硬件成本不到 $1000 美元，主要包括一台普通电脑、摄像头和简单的传感设备，使其易于复制和部署。

4. 高可用性与跨平台部署
可兼容多种机器人平台（如 UR5、Shadow Hand 等），在多个任务中展现良好效果。

作者提供了开源代码与部署文档，降低学习与使用门槛。

code: coming soom

## 5.Open-TeleVision: Teleoperation with Immersive Active Visual Feedback
提出了一种创新的远程操作系统——Open-TeleVision，专为机器人模仿学习数据采集而设计
1. 主动沉浸式视觉反馈（Immersive Active Visual Feedback）
创新点：与传统远程操作系统主要依赖固定相机或第三人称视角不同，Open-TeleVision 通过主动视觉系统和立体视觉，让操作员以第一人称视角沉浸式地“看到”机器人的环境。

优势：提升操作直觉性，降低操作认知负荷，提高数据质量。

🖐️ 2. 人体动作自然映射至机器人（Embodied Telepresence）
创新点：系统将操作员的手臂和手部动作实时映射到机器人的动作上，使操作者产生“意识转移”到机器人身上的感受。

优势：带来高拟人性控制体验，利于精准、复杂的操作任务。

🤖 3. 适用于多种人形机器人与长时任务
创新点：系统被设计为通用性强，可应用于多个不同平台（两种人形机器人）和多种任务（如罐头分类、插入、折叠、卸载）。

优势：验证了系统在多场景下的实际可部署性和可扩展性。

code:yes

## 6.Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control

上下半身控制解耦

上半身：使用逆运动学（IK）和动作重定向技术，实现精确的手臂操作。

下半身：采用强化学习（RL）训练专注于行走的策略，提升下肢运动的稳健性。

预测运动先验（PMP）模型

利用**条件变分自编码器（CVAE）**对上半身的动作进行建模，生成稳定、可预测的运动表示。

下半身策略在训练时以这些上半身动作为条件，使整体动作更协调、更具鲁棒性。

提升操控精度与稳定性

相比传统使用RL进行全身控制的方法，该方法在需要高自由度操作的任务中表现更好，同时保持行走稳定。

code:yes

## 7. A Single Scale Doesn’t Fit All – Adaptive Motion Scaling for Efficient and Precise Teleoperation
进行缩放
介绍：A Single Scale Doesn’t Fit All – Adaptive Motion Scaling for Efficient and Precise Teleoperation

本研究提出了一种用于遥操作系统的自适应运动缩放方法，旨在提升效率和精度，解决传统固定缩放因子带来的限制问题。遥操作常用于高风险环境如外科手术或危险探索，但固定的运动缩放因子（Motion Scale Factor, MSF）可能导致反复的“clutching”（重新定位控制器）操作以及精度下降，增加操作者的认知负担。

这项研究设计了一个基于用户意图的共享控制器，通过分析操作者的运动轨迹将其划分为粗略（快速、大范围）与精细（缓慢、小范围）动作，并使用模糊C均值（FCM）聚类模型来分类运动尺度。系统会根据分类结果动态调整机器人的运动缩放比例，从而：

在大范围操作时提高效率，减少不必要的重复操作；

在精细任务中增强控制精度。

该系统还包含了模型自适应机制（根据最新轨迹数据更新）和用户反馈机制，使人机双方能够相互适应。

在模拟“钉子转移”（peg transfer）实验中，该方法相比固定缩放系统：

clutching减少38.46%
任务完成时间减少11.96%
NASA-TLX认知负荷评分降低58.01%
这些结果表明，该自适应缩放策略显著提升了遥操作的效率与精度，并有效减轻了操作者的认知负担 (Yoon et al., 2025)。

code：no

## 8. Design of multi-modal feedback channel of human–robot cognitive interface for teleoperation in manufacturing
机器人给人的反馈
论文《**用于制造业遥操作的人-机认知界面的多模态反馈通道设计**》（Zheng 等人，2024）重点研究了如何通过设计更有效的**反馈通道**来提升人机遥操作系统的效率，特别关注从机器人反馈给人类操作员的信息通道，而不是仅关注人对机器的控制输入。

---

### 🌟 主要内容简介：

#### 🔍 研究背景：

在危险或结构复杂的制造环境中，遥操作允许人类远程控制机器人进行作业。然而，现有研究多集中在“指令输入”（人到机器人），\*\*忽视了机器人反馈信息给人的“反馈通道”\*\*设计，这限制了操作效率，并增加了操作员的认知负担。

#### 🧠 研究目标：

本研究旨在从**人类认知的角度**出发，设计一个**多模态反馈通道**（如视觉、听觉、触觉等组合），以增强遥操作时的人机交互效果，提高透明度与理解力。

#### 🛠️ 系统设计：

作者提出了一个**基于多模态反馈的人-机认知接口**，并在一个遥操作的机器人抓取系统中进行了实际开发与应用，主要用于处理易碎产品。

#### 📊 实验与结果：

通过对比实验，研究发现：

* 多模态反馈显著提升了机器人抓取的**准确性与效率**
* 操作员的**认知负荷显著降低**
* 操作员主观评价表明系统使用体验良好

---

### 📘 论文链接：

[点击阅读原文（Zheng 等人，2024）](https://consensus.app/papers/design-of-multimodal-feedback-channel-of-human–robot-zheng-wang/3819ca1db12258ec9a0c287e0c27f26b/?utm_source=chatgpt)

---

### ✅ 总结：

该研究强调：**良好的机器人反馈通道设计对于提高遥操作效率与减轻操作员负担至关重要**。引入多模态反馈能够显著提升人机协作在制造业中的实用性与可靠性。

code:no

## 9. Sketch-MoMa: Teleoperation for Mobile Manipulator via Interpretation of Hand-Drawn Sketches
画画遥操作
《Sketch-MoMa: Teleoperation for Mobile Manipulator via Interpretation of Hand-Drawn Sketches》是一项提出基于手绘草图的移动机械臂远程操作系统的研究。这项工作由Kosei Tanada等人于2024年发表，旨在简化和直观化机器人远程控制操作 (Tanada et al., 2024)。

中文简介：
研究背景与动机：
在日常生活中使用助手机器人时，便捷的远程操作系统非常重要。相比传统的复杂控制界面，2D设备（如平板）上的手绘草图提供了一种直观、人性化的控制方式。然而，以往的方法需要额外的输入方式（如语言、按键）来解释草图的意图，增加了使用复杂度。

核心贡献：
本研究提出“Sketch-MoMa”系统，允许用户直接在观察图像上绘制草图，通过视觉-语言模型（VLM）理解图像中的草图，并将其转化为移动机械臂的低级控制任务。例如，草图可以表示“抓取”、“旋转”、“移动”等操作目标。

方法概述：

利用VLM识别草图所代表的几何形状和语义任务。

将草图信息用于动作规划，生成精确的控制动作。

支持七种典型任务与五种草图形状，具有良好的适应性。

实验验证：

使用14名用户参与对比实验，证明系统相比传统2D接口具有更高的易用性。

系统能够准确指定复杂的细节动作，如抓取方式、旋转角度等。

意义与前景：
“Sketch-MoMa”降低了非专业用户远程操作机器人系统的门槛，展示了草图在自然人机交互中的强大潜力，适合推广于家庭服务机器人等实际场景。

code:no
video:yes

## 10.Vision Language Model-Empowered Contract Theory for AIGC Task Allocation in Teleoperation
这篇文章《**Vision Language Model-Empowered Contract Theory for AIGC Task Allocation in Teleoperation**》提出了一种创新的任务分配框架，用于解决远程操作（teleoperation）中AI生成内容（AIGC）任务的分配问题，结合了视觉语言模型（VLM）和契约理论（contract theory）的方法 [(Zhan et al., 2024)](https://consensus.app/papers/vision-language-modelempowered-contract-theory-for-aigc-zhan-dong/72db4d846857579085fe5c0904a62bc0/?utm_source=chatgpt)。

### 核心内容概述：

1. **问题背景**：

   * 夜间远程操作任务通常需要图像增强，而基于扩散模型的AIGC技术能显著改善图像质量。
   * AIGC模型计算开销大，任务需分配给资源充足的边缘服务器。
   * 不同AIGC任务有不同需求，AIGC模型也因训练数据集规模不同而成本各异，形成信息不对称（边缘服务器无法获知任务难度）。

2. **主要挑战**：

   * 如何在信息不对称的情况下，合理制定差异化定价策略，实现任务和计算资源的高效匹配。
   * 手动评估任务难度成本高、不必要。

3. **提出的解决方案**：

   * **视觉语言模型（VLM）辅助难度评估**：使用VLM自动评估AIGC任务的图像与文本复杂度，精准推断任务难度。
   * **契约理论驱动的任务定价分配机制**：设计激励相容（incentive-compatible）的契约，允许边缘服务器根据任务的隐性需求做出最优策略选择。

4. **实验结果**：

   * 框架在模拟环境中显著提高了效益：远程操作者平均效用提升了10.88%\~12.43%，边缘服务器提升了1.4%\~2.17%。
   * 作者提供了代码和数据开源：[GitHub链接](https://github.com/ZiJun0819/VLM-Contract-Theory)。

### 结论：

该研究展示了如何融合VLM的智能任务分析能力与契约理论的激励设计优势，有效提升远程AIGC任务在边缘计算环境下的分配效率与公平性，是AIGC在工业实际部署中的重要进展。

如需阅读完整论文，可访问原文链接：[(Zhan et al., 2024)](https://consensus.app/papers/vision-language-modelempowered-contract-theory-for-aigc-zhan-dong/72db4d846857579085fe5c0904a62bc0/?utm_source=chatgpt)

## 11.D(R, O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping
**文章介绍：《D(R, O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping》**

这篇论文提出了一种名为 **D(R,O) Grasp** 的新型框架，用于解决机器人在不同手型和物体形状之间通用的灵巧抓取问题。该方法的核心思想是统一表示机器手（Robot, R）与物体（Object, O）之间的交互方式。

### 关键内容：

* **统一表示**：该模型将机器手的结构描述与物体的点云输入结合，预测出既稳定又运动学有效的抓取姿态，具有良好的泛化能力。
* **跨手型适应性**：D(R,O) Grasp 能在多个不同的机器人手型上实现抓取，包括仿真和现实环境，证明其具备跨平台通用性。
* **性能表现**：

  * 在仿真环境中，使用三种不同灵巧机械手测试，平均成功率达到 **87.53%**，预测时间小于1秒。
  * 在真实环境中，使用 LeapHand 机械手也取得了 **89%** 的抓取成功率。
* **优势**：该方法在抓取成功率、多样性和推理速度方面都有显著提升，为应对复杂多变的实际场景提供了一种鲁棒的解决方案。

论文链接：[(Wei et al., 2024)](https://consensus.app/papers/dr-o-grasp-a-unified-representation-of-robot-and-object-wei-xu/a4068f7202185a849d714b9180334890/?utm_source=chatgpt)

code: