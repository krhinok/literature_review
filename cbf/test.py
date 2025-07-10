import numpy as np
import matplotlib.pyplot as plt

# CLF控制器设计
def clf_controller(x, gamma=1.0):
    x1, x2 = x
    V = 0.5 * (x1**2 + x2**2)
    dV_dx = np.array([x1**2, x2])
    
    # 系统动力学 f(x) + g(x)u，其中 f = [x2, 0], g = [0, 1]
    f = np.array([x2, x1])
    g = np.array([0, 1])

    # 使得 dV/dt <= -gamma * V，解 u
    # dV/dt = dV_dx^T (f + g u) = x1*x2 + x2*u
    # 要求 x1*x2 + x2*u <= -gamma * V
    if x2 == 0:
        u = 0
    else:
        u = (-gamma * V - x1 * x2) / x2
    return u

# 模拟系统
def simulate_clf(x0, dt=0.01, T=5.0):
    N = int(T / dt)
    x_traj = [x0]
    for _ in range(N):
        x = x_traj[-1]
        u = clf_controller(x)
        dx1 = x[1]
        dx2 = u
        x_next = x + dt * np.array([dx1, dx2])
        x_traj.append(x_next)
    return np.array(x_traj)

# 初始状态
x0 = np.array([2.0, -1.0])
traj = simulate_clf(x0)

# 绘图
plt.plot(traj[:, 0], traj[:, 1])
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('State Trajectory under CLF Control')
plt.grid(True)
plt.show()
