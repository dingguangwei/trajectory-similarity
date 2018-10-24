# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

# 给出一个点，和一条轨迹段的起止点，得到对应点
def find_pair_point(v, start, end, label=None):
    x = v[0]
    min_point = [start[0],start[1]]
    min_distance = 10000
    for x in np.arange(min(start[0], end[0]), max(start[0], end[0]), 0.001):
        y = (end[1]-start[1])/(end[0]-start[0])*(x-start[0])+start[1]
        if (v[0]-x)**2+(v[1]-y)**2 < min_distance**2:
            min_distance = np.sqrt((v[0]-x)**2+(v[1]-y)**2)
            min_point = [x, y]
    return min_point, min_distance

# 给定一个点，和一条轨迹，得到最短对应点，并画出来
# （没考虑时间递进的关系）
def find_pair_point_in_Traj(v, T, label=None, color='green', linestyle='--'):
    min_point, min_distance = [[1000, 1000], 1000000]
    for i in range(len(T)-1):
        temp_point, temp_distance = find_pair_point(v, T[i], T[i+1])
        if temp_distance<min_distance:
            min_distance = temp_distance
            min_point = temp_point
    plt.plot([v[0], min_point[0]], [v[1], min_point[1]], linestyle=linestyle, linewidth=1, color=color)
