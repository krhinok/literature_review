import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 初始化参数
dt = 0.1
T = 100

# 初始位置 & 目标
x = np.array([0.0, 0.0])
goal = np.array([5.0, 5.0])

# 圆形障碍物中心和半径
obs_center = np.array([2.5, 2.5])
obs_radius = 2.0
alpha = 5.0

# 记录轨迹
x_hist = []

for t in range(T):
    # 控制目标（PD tracking）
    # 原来的 to_goal
    to_goal = goal - x
    dir_goal = to_goal / np.linalg.norm(to_goal)

    # 添加绕障引导
    dir_obs = x - obs_center
    dist = np.linalg.norm(dir_obs)

    if dist < 2.0:
        dir_orth = np.array([-dir_obs[1], dir_obs[0]])  # 向左绕障
        dir_orth = dir_orth / np.linalg.norm(dir_orth)
        u_des = 1.2 * dir_goal + 0.8 * dir_orth
    else:
        u_des = 1.5 * dir_goal


    # 控制障碍函数 h(x) = ||x - obs_center||^2 - r^2 >= 0
    delta = x - obs_center
    h = delta @ delta - obs_radius**2

    # 计算 Lf h = 0，Lg h = 2(x - x_obs)
    Lg_h = 2 * delta

    # QP cost: minimize ||u - u_des||^2
    def cost(u):
        return np.sum((u - u_des)**2)

    # CBF 约束: Lg h · u + alpha * h >= 0
    def cbf_constraint(u):
        return Lg_h @ u + alpha * h

    constraints = ({
        'type': 'ineq',
        'fun': cbf_constraint
    })

    res = minimize(cost, x0=[0.0, 0.0], constraints=constraints)
    u_safe = res.x

    # 状态更新
    x = x + dt * u_safe
    x_hist.append(x.copy())

# 可视化
x_hist = np.array(x_hist)
theta = np.linspace(0, 2*np.pi, 100)
circle_x = obs_center[0] + obs_radius * np.cos(theta)
circle_y = obs_center[1] + obs_radius * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x_hist[:, 0], x_hist[:, 1], label="Robot Trajectory")
plt.plot(goal[0], goal[1], 'go', label="Goal")
plt.plot(circle_x, circle_y, 'r--', label="Obstacle")
plt.plot(obs_center[0], obs_center[1], 'ro')
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.title("2D CBF-Based Obstacle Avoidance")
plt.show()
