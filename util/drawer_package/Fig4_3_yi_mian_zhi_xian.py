# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot(point_arr, ax, label=None, linestyle='-', linewidth=1., color='0', marker=None):
    x = []
    y = []
    z = []
    for point in point_arr:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    ax.plot(x, y, z, label=label, linestyle=linestyle, linewidth=linewidth, color=color, marker=marker)


# 画一段圆弧
def draw_radian(ax, center_x, center_y, center_z, theta_from=0, r = 1., theta_to=2*np.pi):
    theta = np.linspace(start=theta_from, stop=theta_to, num=800)

    # x = center_x+r*np.cos(theta)
    x = [center_x for i in np.arange(len(theta))]

    y = center_y+r*np.cos(theta)
    # y = [center_y for i in np.arange(len(theta))]

    z = center_z + r*np.sin(theta)
    # z = [center_z for i in np.arange(len(theta))]

    ax.plot(x, y, z, color='0.5', linewidth=0.8)


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize=14
    a=[
        [0, 0, 0],
        [0, 1, 1]
    ]
    b=[
        [1, 0, 0],
        [1, 2, 0]
    ]
    plot(a, ax, label='', linestyle='-', linewidth=2, color='0', marker='H')
    plot(b, ax, label='', linestyle='-', linewidth=2, color='0.5', marker='.')
    ax.text(0, 0.5, 0.7, 'a', fontsize=m_fontsize)
    ax.text(1, 1, -0.2, 'b', fontsize=m_fontsize)
    ax.text(0, 0.6, 0.05, "a'", fontsize=m_fontsize)


    plot([a[0], [0, 1, 0]], ax, label="", linestyle='-', linewidth=2, color='0', marker='2')
    plot([a[0],[0,2,0]], ax, label="", linestyle='--', linewidth=1, color='0.8', marker='2')
    plot([a[0], b[0]], ax, label=None, linestyle='--', linewidth=1, color='green', marker=None)
    plot([[0,2,0], b[1]], ax, label=None, linestyle='--', linewidth=1, color='green', marker=None)
    plot([a[1], [0,1,0]], ax, label=None, linestyle='--', linewidth=1, color='green', marker=None)
    draw_radian(ax=ax, center_x=0, center_y=0, center_z=0, theta_from=0, r=0.2, theta_to=np.pi/4)

    ax.text(0, 0.3, 0.1, 'θ')

    # ax.legend()  # 显示图例
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    plt.xlim(0, 2)
    plt.ylim(0, 2)

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()


