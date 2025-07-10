# controller.py

import numpy as np
import cvxpy as cp

def clf_cbf_qp_controller(x, x_ref, env, clf_rate=5.0, cbf_rate=5.0):
    x = np.array(x)
    x_ref = np.array(x_ref)

    # 控制变量
    u = cp.Variable(2)

    # 控制目标（理想方向）
    u_des = -1.5 * (x - x_ref)

    # QP目标函数：最小化 ||u - u_des||^2
    objective = cp.Minimize(cp.sum_squares(u - u_des))

    constraints = []

    # 添加 CLF 约束（使状态靠近参考点）
    V = np.linalg.norm(x - x_ref)**2
    grad_V = 2 * (x - x_ref)
    constraints.append(grad_V @ u + clf_rate * V <= 0)

    # 添加所有 CBF 约束（避开所有障碍）
    for obs in env.obstacles:
        if obs['type'] == 'circle':
            center = obs['center']
            r = obs['radius']
            h = np.linalg.norm(x - center)**2 - r**2
            grad_h = 2 * (x - center)
            constraints.append(grad_h @ u + cbf_rate * h >= 0)

    # 求解 QP
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.OSQP)
        return u.value
    except:
        print("❌ QP failed, fallback to zero velocity.")
        return np.zeros(2)
