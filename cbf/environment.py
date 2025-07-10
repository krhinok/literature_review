# environment.py

import numpy as np
import matplotlib.pyplot as plt

class Map2D:
    def __init__(self, size=(100, 100), resolution=1.0):
        self.size = size
        self.resolution = resolution
        self.width, self.height = size
        self.obstacles = []

    def add_circular_obstacle(self, center, radius):
        self.obstacles.append({
            'type': 'circle',
            'center': np.array(center),
            'radius': radius
        })

    def is_occupied(self, point):
        """ 判断某个点是否处于任何障碍物内部 """
        p = np.array(point)
        for obs in self.obstacles:
            if obs['type'] == 'circle':
                center = obs['center']
                r = obs['radius']
                if np.linalg.norm(p - center) <= r:
                    return True
        return False

    def plot(self, path=None, trajectory=None):
        fig, ax = plt.subplots(figsize=(6,6))
        # 绘制障碍物
        for obs in self.obstacles:
            if obs['type'] == 'circle':
                circle = plt.Circle(obs['center'], obs['radius'], color='r', alpha=0.3)
                ax.add_patch(circle)

        # 绘制路径
        if path is not None:
            path = np.array(path)
            ax.plot(path[:,0], path[:,1], 'b--', label='Planned Path')

        # 绘制轨迹
        if trajectory is not None:
            trajectory = np.array(trajectory)
            ax.plot(trajectory[:,0], trajectory[:,1], 'g-', linewidth=2, label='Robot Trajectory')

        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.legend()
        plt.title("2D Map with Obstacles")
        plt.show()
