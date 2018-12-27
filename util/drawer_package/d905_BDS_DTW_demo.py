# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import d0_util_3d


def get_data():
    Q = [
        [1, 1, 1],
        [1, 3, 3],
        [1, 5, 5]
    ]
    R = [
        [3, 1, 1],
        [2, 2, 2],
        [2, 4, 4],
        [3, 5, 5]
    ]
    return np.array(Q), np.array(R)

if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 13

    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker=None)
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.3', marker='H')

    ax.scatter(Q[1, 0], Q[1, 1], Q[1, 2], marker='.', linewidths=3.)

    QQ = np.array([[1, 2, 2], [1, 3, 3],[1, 4, 4]])
    ax.scatter(QQ[0, 0], QQ[0, 1], QQ[0, 2], marker='>', linewidths=3., color='0.3')
    ax.scatter(QQ[2, 0], QQ[2, 1], QQ[2, 2], marker='>', linewidths=3., color='0.3')
    Q_label=['BDS(rj)', 'qi', 'BDS(rk)']
    for i in range(len(QQ)):
        ax.text(QQ[i, 0], QQ[i, 1]-0.2, QQ[i, 2]+0.9, Q_label[i], color='black', fontsize=m_fontsize)
    R_label = ['', 'rj', 'rk']
    for i in [1, 2]:
        ax.text(R[i, 0], R[i, 1], R[i, 2]+0.7, R_label[i], color='0.3', fontsize=m_fontsize)

    ax.plot([QQ[0,0], R[1, 0]], [QQ[0,1], R[1, 1]], [QQ[0,2], R[1, 2]], linestyle='--', linewidth=1.5, color='green')
    ax.plot([QQ[2, 0], R[2, 0]], [QQ[2, 1], R[2, 1]], [QQ[2, 2], R[2, 2]], linestyle='--', linewidth=1.5, color='green')

    ax.plot([QQ[1, 0], 2], [QQ[1, 1], 3], [QQ[1, 2], 3], linestyle='-', linewidth=1.5, color='green')
    ax.text(2, 3, 3, 'R(qi)', fontsize=m_fontsize)

    ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize)
    ax.set_ylabel('y/m', fontsize=m_fontsize)
    ax.set_zlabel('z/m', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    # ax.set_yticks([])
    ax.set_zticks(np.arange(0, 10, 2))

    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 10)

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()