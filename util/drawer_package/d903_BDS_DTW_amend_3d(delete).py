# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import d0_util_3d

# r0、r1
def get_data():
    R = [
        [1, 2, 1],
        [1, 3, 2]
    ]
    Q = [
        [3, 1, 1],
        [3, 3.2, 2]
    ]
    return np.array(Q), np.array(R)

# 针对ri
def get_data_ri():
    R = [
        [1, 1, 1],
        [1, 2, 2],
        [1, 3, 3]
    ]
    Q = [
        [3, 1, 1],
        [2.3, 1.7, 1.6],
        [2.3, 2.3, 2.4],
        [3, 3, 3]
    ]
    return np.array(Q), np.array(R)

if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16

    Q, R = get_data_ri()

    ax.plot(Q[:,0],Q[:, 1],Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.3', marker='H')

    for i, j in [[1, 1],[2, 1], [3, 2]]:
        v1 = Q[i]
        v2 = R[j]
        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], linestyle='--', linewidth=1., color='green', marker=None)

    Q_label=[r'$q_{j}$',r'$  q_{j+1} = Q(r_{i-1})$',r'$q_{j+2}$',r'$q_{j+3}$']
    for i in [0, 1,2,3]:
        ax.text(Q[i, 0] + 0., Q[i, 1]+0., Q[i, 2] - 0.7, Q_label[i], color='blue', fontsize=m_fontsize)
    R_label = [r'$r_{i-1}$', r'$r_{i}$', r'$r_{i+1}$']
    for i in [0, 1, 2]:
        ax.text(R[i, 0] + 0., R[i, 1]+0., R[i, 2] - 0.7, R_label[i], color='0.1', fontsize=m_fontsize)

    d0_util_3d.find_pair_point_in_Traj_and_draw(R[0], Q, m_text='', ax=ax, fontsize=14,color='0.1',linestyle='--')
    d0_util_3d.find_pair_point_in_Traj_and_draw(R[1], Q, m_text=r'$ BDS(r_{i})$', ax=ax, fontsize=14, color='0.1', linestyle='--')

    ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_zticks(np.arange(0, 4, 1))

    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 5)

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()