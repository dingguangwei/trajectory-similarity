# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import d0_util_3d
from util.algorithm.DTW_BDS_pair import get_DTW_BDS_pair_by_traj

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
    m_fontsize=14

    Q, R, S = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.3', marker='H')

    for i in [0, 1,2, 3, 4,5,6,]:
        ax.text(Q[i, 0] + 0.2, Q[i, 1], Q[i, 2] - 0.9, 'q'+str(i), color='blue', fontsize=m_fontsize)
    for i in range(9):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] - 0.9, 'r'+str(i), color='0.3', fontsize=m_fontsize)

    DTW_BDS_pair, new_Q, DTW_BDS_pair_index = get_DTW_BDS_pair_by_traj()
    for pair in DTW_BDS_pair:
        v1 = R[pair[0]]
        v2 = pair[1]
        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], linestyle='--', linewidth=1.5, color='green')


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