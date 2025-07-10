# path_planner.py

import heapq
import numpy as np

def heuristic(a, b):
    """ 欧几里得距离启发式 """
    return np.linalg.norm(np.array(a) - np.array(b))

def get_neighbors(node, map2d):
    """ 获取8邻域可行点 """
    x, y = node
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1),
             (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8方向
    neighbors = []
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < map2d.width and 0 <= ny < map2d.height:
            if not map2d.is_occupied((nx, ny)):
                neighbors.append((nx, ny))
    return neighbors

def astar_planner(map2d, start, goal):
    start = tuple(int(i) for i in start)
    goal = tuple(int(i) for i in goal)

    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, None))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, cost, current, parent = heapq.heappop(open_set)

        if current == goal:
            # 回溯路径
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        if current not in came_from:
            came_from[current] = parent

        for neighbor in get_neighbors(current, map2d):
            tentative_g = g_score[current] + heuristic(current, neighbor)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, tentative_g, neighbor, current))

    print("❌ A* failed: No path found.")
    return []
