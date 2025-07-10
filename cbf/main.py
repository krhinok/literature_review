from environment import Map2D
from path_planner import astar_planner
from controller import clf_cbf_qp_controller
import numpy as np
import matplotlib.pyplot as plt

env = Map2D((100, 100))
env.add_circular_obstacle(center=(50, 50), radius=10)

start = (10, 10)
goal = (90, 90)
path = astar_planner(env, start, goal)

x = np.array(start, dtype=float)
dt = 0.1
trajectory = [x.copy()]

for wp in path:
    for _ in range(10):
        u = clf_cbf_qp_controller(x, wp, env)
        x += dt * u
        trajectory.append(x.copy())

env.plot(path=path, trajectory=trajectory)
