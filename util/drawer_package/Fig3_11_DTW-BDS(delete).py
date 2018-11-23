# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from d0_util_3d import find_pair_point_in_Traj_and_draw

def get_data():
    Q = [
        [4, 6, 0],
        [4, 2.5, 2.5],
        [4, -1, 5]
    ]
    R = [
        [1, 5, 0],
        [1, 3, 2],
        [1, 1, 4]
    ]
    return np.array(Q), np.array(R)


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 14

    Q, R = get_data()

    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0', marker='H')

    ax.plot([Q[0, 0], R[0, 0]], [Q[0, 1], R[0, 1]], [Q[0, 2], R[0, 2]], linestyle='--', linewidth=1, color='0.5')
    ax.plot([Q[1, 0], R[1, 0]], [Q[1, 1], R[1, 1]], [Q[1, 2], R[1, 2]], linestyle='--', linewidth=1, color='0.5')
    # ax.plot([Q[0, 0], R[1, 0]], [Q[0, 1], R[1, 1]], [Q[0, 2], R[1, 2]], linestyle='--', linewidth=1, color='0.5')
    ax.plot([Q[2, 0], R[2, 0]], [Q[2, 1], R[2, 1]], [Q[2, 2], R[2, 2]], linestyle='--', linewidth=1, color='0.5')

    m_label = [r'$q_{0}=DTW(r_0)$',r'$q_{1}=DTW(r_1)$', r'$q_{2}$']
    for i in range(0, len(Q)-1):
        ax.text(Q[i, 0] + 6, Q[i, 1], Q[i, 2] , m_label[i], color='blue', fontsize=m_fontsize)
    ax.text(Q[2, 0]+1.5, Q[2, 1], Q[2, 2], m_label[2], color='blue', fontsize=m_fontsize)
    for i in range(len(R)):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] + 1, r'$r_{'+str(i)+'}$', color='0.3', fontsize=m_fontsize)


    ###################################################################################################################
    # 寻找r0的对应点
    ###################################################################################################################
    min_point = find_pair_point_in_Traj_and_draw(R[0], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0]+6, min_point[1]-1, min_point[2], r'$DTW-DBS(r_0)$', color='0.1', fontsize=m_fontsize)

    ###################################################################################################################
    # 寻找r1的对应点
    ###################################################################################################################
    min_point = find_pair_point_in_Traj_and_draw(R[1], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] + 6, min_point[1] + 1, min_point[2], r'$DTW-DBS(r_1)$', color='0.1', fontsize=m_fontsize)



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

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()