# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from util.drawer_package import d0_util_3d

def get_data():
    R = [
        [1, 2, 0],
        [2, 2, 1],
        [3, 2, 2],
        [3, 3, 3],
        [4, 3, 4],
        [5, 3, 5],
        [5, 2, 6],
        [6, 2, 7],
        [7, 2, 8]
    ]
    Q = [
        [1, 1.5, 1],
        [3, 1.5, 2],
        [4.95, 1.5, 3],
        [4.95, 2.95, 4],
        [3.05, 2.95, 5],
        [3.05, 2, 6],
        [3.05, 0, 7]
    ]
    S = [
        [0, ]
    ]

    return np.array(Q), np.array(R), np.array(S)

if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize='14'

    Q, R, S = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=4, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=4, color='0.4', marker='H')

    for i in [0, 1, 3, 4]:
        ax.text(Q[i, 0] + 0.2, Q[i, 1], Q[i, 2] - 0.7, 'q'+str(i), color='blue', fontsize=m_fontsize)
    for i in [0, 2, 3, 5]:
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] - 1, 'r'+str(i), color='0.4', fontsize=m_fontsize)

    for i in range(3):
        d0_util_3d.find_pair_point_in_Traj_and_draw(R[i], Q[:3], label=None, color='green', linestyle='--')
    for i in range(3, 7):
        d0_util_3d.find_pair_point_in_Traj_and_draw(R[i], Q[2:], label=None, color='green', linestyle='--')
    for i in range(7, len(R)):
        d0_util_3d.find_pair_point_in_Traj_and_draw(R[i], Q, label=None, color='green', linestyle='--')


    # ax.plot([0,1],[1, 2],[3, 4], label='a', linestyle='-', linewidth=2, color='0', marker='H')


    ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)

    # 设置坐标轴刻度
    # ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0, 10, 2))

    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 10)

    ax.view_init(elev=10, azim=120)  # 调整视角

    plt.show()