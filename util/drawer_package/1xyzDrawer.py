# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot(point_arr, ax, label=None, linestyle='-', linewidth=1, color='0', marker=None):
    x = []
    y = []
    z = []
    for point in point_arr:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    ax.plot(x, y, z, label=label, linestyle=linestyle, linewidth=linewidth, color=color, marker=marker)


def find_pair_point(ax, r, qi, qj, label=None):
    x = qi[0]
    min_point = [qi[0],qi[1],qi[2]]
    min_distance = 100
    for x in np.arange(min(qi[0], qj[0]), max(qi[0], qj[0]), 0.0001):
        y = (qj[1]-qi[1])/(qj[0]-qi[0])*(x-qi[0])+qi[1]
        z = (qj[2]-qi[2])/(qj[0]-qi[0])*(x-qi[0])+qi[2]
        if (r[0]-x)**2+(r[1]-y)**2+(r[2]-z)**2 < min_distance**2:
            min_distance = np.sqrt((r[0]-x)**2+(r[1]-y)**2+(r[2]-z)**2)
            min_point = [x, y, z]
    ax.plot([r[0],min_point[0]], [r[1], min_point[1]], [r[2], min_point[2]], linestyle='--', linewidth=1, color='green')
    ax.text(min_point[0], min_point[1], min_point[2]+0.01, label)
    print('min_point=', min_point)


def get_R_and_Q():
    # 对应点情况一
    # R = [
    #     [0.1, 0.2, 0.2],
    #     [0.1, 0.4, 0.3]
    # ]
    # Q = [
    #     [0.4, 0.2, 0.1],
    #     [0.3, 0.3, 0.25],
    #     [0.4, 0.4, 0.4]
    # ]

    # 对应点情况二
    # R = [
    #     [0.1, 0.3, 0.2],
    #     [0.15, 0.4, 0.3]
    # ]
    # Q = [
    #     [0.3, 0.2, 0.1],
    #     [0.4, 0.4, 0.4]
    # ]

    # 对应轨迹段情况一
    # R = [[0.25, 0.3, 0.1],
    #      [0.4, 0.3, 0.2],
    #      [0.55, 0.28, 0.3],
    #      [0.7, 0.3, 0.4]]
    # Q = [[0.1, 0.1, 0.1],
    #      [0.3, 0.2, 0.2],
    #      [0.8, 0.2, 0.3]]

    # 对应点轨迹段情况二
    # R=[
    #     [0.2, 0.1, 0.1],
    #     [0.1, 0.2, 0.2],
    #     [0.1, 0.4, 0.3],
    #     [0.2, 0.5, 0.4]
    # ]
    # Q=[
    #     [0.4, 0.2, 0.1],
    #     [0.3, 0.3, 0.25],
    #     [0.4, 0.4, 0.4]
    # ]

    # 对应轨迹段情况三
    R = [
        [0.2, 0.1, 0.1],
        [0.21, 0.5, 0.4]
    ]
    Q = [
        [0.4, 0.2, 0.1],
        [0.3, 0.25, 0.2],
        [0.3, 0.32, 0.3],
        [0.4, 0.4, 0.4]
    ]

    return R, Q


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4',
               's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_', r'$\clubsuit$']

    R, Q = get_R_and_Q()

    # 画出轨迹R和Q
    plot(R, ax, label='R', linestyle='-', linewidth=2, color='0', marker=markers[2])
    plot(Q, ax, label='Q', linestyle='-', linewidth=2, color='blue', marker=markers[3])
    # 为轨迹样本点进行标注
    for i in range(len(R)):
        m_label = '  r'+str(i)
        ax.text(R[i][0], R[i][1], R[i][2], m_label)
    for i in range(len(Q)):
        m_label = '  q'+str(i)
        ax.text(Q[i][0], Q[i][1], Q[i][2], m_label)

    find_pair_point(ax=ax, r=R[0], qi=Q[1], qj=Q[0], label='   Q(r0)')
    find_pair_point(ax=ax, r=R[1], qi=Q[3], qj=Q[2], label='   Q(r1)')

    # 对应轨迹段情况三(作图讲解d_shape遇到Q(r1)和Q(r2)中间有间隔样本点的情况)
    find_pair_point(ax=ax, r=Q[1], qi=R[0], qj=R[1], label='   R(q1,r0r1)')
    find_pair_point(ax=ax, r=Q[2], qi=R[0], qj=R[1], label='   R(q2,r0r1)')

    ax.legend()  # 显示图例
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_xticks(np.arange(0, 1, 0.1))
    # ax.set_yticks(np.arange(0, 1, 0.1))

    ax.view_init(elev=20, azim=280)  # 调整视角

    # plt.xlim(0, 1)
    # plt.ylim(0, 1)
    plt.show()




################################################################################
# 画3D曲面图
# ax = Axes3D(fig)
# x = np.arange(-4, 4, 0.1)
# y = np.arange(-4, 4, 0.1)
# X, Y = np.meshgrid(x, y)
# R = np.sqrt(X**2+y**2)
# Z = np.sin(R)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
# plt.show()
