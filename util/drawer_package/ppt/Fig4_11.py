# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from util.algorithm.DTW_BDS_pair import get_DTW_BDS_pair_by_traj


def get_data():
    Q = [
        [1, 1, 1],
        [1, 2, 2],
        [2, 3, 3],
        [2, 4, 4]
    ]
    R = [
        [1, -1, 0],
        [1.5, 0, 0.5],
        [1.5, 1, 1],
        [1.5, 2, 2],
        [2.5, 3, 3],
        [2.5, 4, 4],
        [3, 5, 5],
        [3, 6, 6],
        # [3.8, 3.3, 4],
        # [4.5, 4.6, 5],
    ]
    S = [
        [.5, 2, 2],
        [1.5, 3, 3],
        [1.5, 4.2, 4.5],
        [1.5, 5, 5],
        [1.5, 6, 6],
        [1.5, 7, 7],
        [1.5, 7.2, 8]
    ]
    return np.array(Q), np.array(R), np.array(S)


def plot(point_arr, ax, label=None, linestyle='-', linewidth=1., color='0', marker=None):
    x = []
    y = []
    z = []
    for point in point_arr:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    ax.plot(x, y, z, label=label, linestyle=linestyle, linewidth=linewidth, color=color, marker=marker)


def plot_R(R, ax):
    plot(R[0:3], ax, label='R', linewidth=3., color='0.4', marker='*')
    plot(R[2:6], ax, label='R', linewidth=3., color='0.1', marker='*')
    plot(R[5:8], ax, label='R', linewidth=3., color='0.4', marker='*')


def plot_S(S, ax):
    plot(S[0:4], ax, label='S', linewidth=3., color='0.1', marker='|')
    plot(S[3:], ax, label='S', linewidth=3., color='0.6', marker='|')


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16

    Q, R, S = get_data()

    plot(Q, ax, label='Q', linewidth=3., color='black', marker='H')
    plot_R(R, ax)
    plot_S(S, ax)

    for i in range(len(Q)):
        ax.text(Q[i, 0], Q[i, 1]-0., Q[i, 2], '$q_'+str(i)+'$', fontsize=m_fontsize, color='black')
    for i in range(len(R)):
        ax.text(R[i, 0], R[i, 1]-0.2, R[i, 2], '$r_'+str(i)+'$', fontsize=m_fontsize, color='0.4')
    for i in range(len(S)):
        ax.text(S[i, 0]-0.2, S[i, 1]+0.3, S[i, 2], '$s_'+str(i)+'$', fontsize=m_fontsize, color='0.6')

    DTW_BDS_pair, new_Q, DTW_BDS_pair_index = get_DTW_BDS_pair_by_traj(Q=Q, R=R)
    for i in range(len(R)):
        plot([R[i], DTW_BDS_pair[i][1]], ax, linestyle='--', linewidth=1., color='green')

    DTW_BDS_pair, new_Q, DTW_BDS_pair_index = get_DTW_BDS_pair_by_traj(Q=Q, R=S)
    for i in range(len(S)):
        plot([S[i], DTW_BDS_pair[i][1]], ax, linestyle='--', linewidth=1., color='green')


    # ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize)
    ax.set_ylabel('y/m', fontsize=m_fontsize)
    ax.set_zlabel('z/m', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0, 10, 5))
    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    # ax.set_zlim(0, 10)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    ax.view_init(elev=20, azim=220)  # 调整视角
    plt.savefig("F:\\毕业设计大文件夹\\picture\\ppt图片\\Fig4_11.jpg", dpi=300)
    plt.show()