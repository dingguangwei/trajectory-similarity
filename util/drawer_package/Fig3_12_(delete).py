# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from d0_util_3d import find_pair_point_in_Traj_and_draw

def get_data():
    Q = [
        [4, 5, 0],
        [4, 3.7, 1.3],
        [4, -2, 6]
    ]
    R = [
        [1, 5, 0],
        [1, 3, 2],
        [1, 2, 3],
        [1, -1, 5]
    ]
    return np.array(Q), np.array(R)


def draw_line(ax, v1, v2, color='0.5', linewidth=1.):
    ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], linestyle='--', linewidth=linewidth, color=color)


def draw_a():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 14
    small_fontsize = 11

    Q, R = get_data()

    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0', marker='H')

    draw_line(ax, Q[0], R[0], color='0', linewidth=1.5)
    draw_line(ax,Q[1], R[1], color='0', linewidth=1.5)
    draw_line(ax,Q[1], R[2])
    draw_line(ax,Q[2], R[3])

    # m_label = [r'$q_{0}=DTW(r_0)$',r'$q_{1}=DTW(r_1)$', r'$q_{2}$']
    m_label = [r'$q_{0}$', r'$q_{1}$', r'$q_{2}$']
    for i in range(0, len(Q)):
        ax.text(Q[i, 0] - 0.5, Q[i, 1]+1, Q[i, 2], m_label[i], color='blue', fontsize=m_fontsize)
    # ax.text(Q[2, 0]+1.5, Q[2, 1], Q[2, 2], m_label[2], color='blue', fontsize=m_fontsize)
    for i in range(len(R)):
        ax.text(R[i, 0] - 0.5, R[i, 1], R[i, 2], r'$r_{' + str(i) + '}$', color='0.3', fontsize=m_fontsize)

    ax.text(Q[0, 0] + 5, Q[0, 1], Q[0, 2], r'$DTW-DBS(r_0)$', color='0.1', fontsize=small_fontsize)
    ax.text(Q[1, 0] + 5, Q[1, 1], Q[1, 2], r'$DTW-DBS(r_1)$', color='0.1', fontsize=small_fontsize)

    ###################################################################################################################
    # 寻找r2的对应点
    ###################################################################################################################
    min_point = find_pair_point_in_Traj_and_draw(R[2], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] + 5, min_point[1], min_point[2], r'$DTW-DBS(r_2)$', color='0.1', fontsize=small_fontsize)

    ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0, 7, 2))
    plt.xlim(-1, 10)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 7)
    ax.view_init(elev=20, azim=100)  # 调整视角
    plt.show()


def draw_b():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 14
    small_fontsize=11

    Q, R = get_data()

    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0', marker='H')

    draw_line(ax,Q[0], R[0], color='0', linewidth=1.5)
    draw_line(ax,Q[1], R[1])
    draw_line(ax,Q[1], R[2])
    draw_line(ax,Q[2], R[3])

    # m_label = [r'$q_{0}=DTW(r_0)$',r'$q_{1}=DTW(r_1)$', r'$q_{2}$']
    m_label = [r'$q_{0}$', r'$q_{1}$', r'$q_{2}$']
    for i in range(0, len(Q)):
        ax.text(Q[i, 0] + 1.2, Q[i, 1]+0.8, Q[i, 2], m_label[i], color='blue', fontsize=m_fontsize)
    # ax.text(Q[2, 0]+1.5, Q[2, 1], Q[2, 2], m_label[2], color='blue', fontsize=m_fontsize)
    for i in range(len(R)):
        ax.text(R[i, 0] - 0.5, R[i, 1], R[i, 2], r'$r_{' + str(i) + '}$', color='0.3', fontsize=m_fontsize)

    ax.text(Q[0, 0] + 5, Q[0, 1], Q[0, 2], r'$DTW-DBS(r_0)$', color='0.1', fontsize=small_fontsize)
    ###################################################################################################################
    # 寻找r2的对应点
    ###################################################################################################################
    min_point = find_pair_point_in_Traj_and_draw(R[2], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] + 5, min_point[1], min_point[2], r'$DTW-DBS(r_2)$', color='0.1', fontsize=small_fontsize)

    ###################################################################################################################
    # 寻找r1的对应点
    ###################################################################################################################
    min_point = find_pair_point_in_Traj_and_draw(R[1], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] + 5, min_point[1] + 1, min_point[2], r'$DTW-DBS(r_1)$', color='0.1', fontsize=small_fontsize)

    ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0, 7, 2))
    plt.xlim(-1, 10)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 7)
    ax.view_init(elev=20, azim=100)  # 调整视角
    plt.show()

if __name__=='__main__':
    # draw_a()
    draw_b()