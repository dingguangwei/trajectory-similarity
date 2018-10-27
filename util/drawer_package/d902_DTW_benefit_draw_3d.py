# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import d0_util_3d
import d902_BDS_weakness_draw


def get_EU_distance_3d(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    d = np.sqrt(np.sum((v1-v2)**2))
    return d


def get_pair_point_in_DTW(Q, R):
    m = len(Q)
    n = len(R)

    arr = np.zeros(shape=(m+1, n+1), dtype=float)
    for i in range(m+1):
        for j in range(n+1):
            if i==0 and j==0:
                arr[i, j]=0
            elif i==0 or j==0:
                arr[i, j]=float('inf')
            else:
                d1 = get_EU_distance_3d(Q[i-1], R[j-1])
                d2 = min(arr[i-1, j], arr[i, j-1], arr[i-1, j-1])
                arr[i, j] = d1+d2
    pair = []
    i, j = m, n
    while i>0 and j>0:
        pair.append([i-1, j-1])
        post_i, post_j, post_value = i-1, j-1, arr[i-1, j-1]
        if post_value>arr[i, j-1]:
            post_i, post_j, post_value = i, j - 1, arr[i, j - 1]
        if post_value>arr[i-1, j]:
            post_i, post_j, post_value = i-1, j, arr[i-1, j]
        i, j = post_i, post_j
    print('pair=\n', pair,'\n')
    return np.array(pair)


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16

    Q, R, S = d902_BDS_weakness_draw.get_data()
    pair = get_pair_point_in_DTW(Q, R)

    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.3', marker='H')

    for i in range(len(pair)):
        v1 = Q[pair[i, 0]]
        v2 = R[pair[i, 1]]
        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]],linestyle='--', linewidth=1.5, color='green', marker=None)

    for i in [0, 1, 3, 4]:
        ax.text(Q[i, 0] + 0.2, Q[i, 1], Q[i, 2] - 0.7, 'q'+str(i), color='blue', fontsize=m_fontsize)
    for i in [0, 2, 3, 5, 6]:
        ax.text(R[i, 0] + 0.4, R[i, 1], R[i, 2] - 0.7, 'r'+str(i), color='0.3', fontsize=m_fontsize)


    ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    # ax.set_yticks([])
    ax.set_zticks(np.arange(0, 10, 2))

    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 10)

    ax.view_init(elev=30, azim=130)  # 调整视角
    plt.show()