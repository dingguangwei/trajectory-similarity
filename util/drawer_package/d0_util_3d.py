# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def set_text(ax, Q, label_perfix='q', color='blue', fontsize='14'):
    for i in range(len(Q)):
        ax.text(Q[i, 0], Q[i, 1], Q[i, 2], label_perfix+str(i), color=color, fontsize=fontsize)


# 给出一个点，和一条轨迹段的起止点，得到对应点
def find_pair_point(v, start, end, label=None):
    z = v[2]
    min_point = [start[:]]
    min_distance = 10000
    for z in np.arange(min(start[2], end[2]), max(start[2], end[2]), 0.001):
        x = (end[0] - start[0]) / (end[2] - start[2]) * (z - start[2]) + start[0]
        y = (end[1]-start[1])/(end[2]-start[2])*(z-start[2])+start[1]
        if (v[0]-x)**2+(v[1]-y)**2+(v[2]-z)**2 < min_distance**2:
            min_distance = np.sqrt((v[0]-x)**2+(v[1]-y)**2+(v[2]-z)**2)
            min_point = [x, y, z]
    return min_point, min_distance

# 给定一个点，和一条轨迹，得到最短对应点，并画出来
# （没考虑时间递进的关系）
def find_pair_point_in_Traj_and_draw(v, T, label=None, color='green', linestyle='--'):
    min_point, min_distance = [[1000, 1000, 1000], 1000000]
    for i in range(len(T)-1):
        temp_point, temp_distance = find_pair_point(v, T[i], T[i+1])
        if temp_distance<min_distance:
            min_distance = temp_distance
            min_point = temp_point
    plt.plot([v[0], min_point[0]], [v[1], min_point[1]], [v[2], min_point[2]],linestyle=linestyle, linewidth=1, color=color)


