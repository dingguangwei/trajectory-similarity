# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


def get_Data():
    A = [4.5, 1.5]
    B = [6, 1.36]
    C = [8, 2]
    Q = [A, B, C]
    R = [
        [1,3],
        [2,2],
        [3,2],
        [4, 2],
        [5, 1],
        [8, 2],
        [9, 3],
        [10, 3]
    ]
    S = [[3,3], [8,3]]

    return np.array(R), np.array(S), np.array(Q)


if __name__ == "__main__":
    fig = plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    m_fontsize = 16

    # 画轨迹
    R, S, Q = get_Data()
    plt.plot(R[:, 0], R[:, 1], color='0.1', linewidth=1.5, label='R', marker='H', linestyle=None)
    plt.plot(S[:, 0], S[:, 1], color='0.4', linewidth=1.5, label='S', marker='H', linestyle=None)
    plt.plot(Q[:, 0], Q[:, 1], color='blue', linewidth=1.5, label='Q', marker='*', linestyle='--')

    #
    # plt.plot([A[0], B[0]], [A[1], B[1]], color='blue', linewidth=1., label='', marker='*', linestyle='--')
    # plt.text(A[0]-0.2, A[1]-0.3, 'A', fontsize=m_fontsize)
    # plt.text(B[0]+0.1, B[1]-0.4, 'B', fontsize=m_fontsize)
    # plt.text(C[0] + 0.1, C[1] + 0.4, 's0', fontsize=m_fontsize)
    # plt.text(D[0] + 0.1, D[1] + 0.4, 's1', fontsize=m_fontsize)

    Q_label = ['A', 'B', 'C']
    for i in range(len(Q)):
        if i == 2:
            plt.text(Q[i][0] + 0.3, Q[i][1], Q_label[i], fontsize=m_fontsize, color='blue')
        else:
            plt.text(Q[i][0] - 0.2, Q[i][1] - 0.5, Q_label[i], fontsize=m_fontsize, color='blue')
    for i in range(len(S)):
        plt.text(S[i][0] - 0.4, S[i][1] - 0.5, 's'+str(i), fontsize=m_fontsize)
    for i in range(len(R)):
        plt.text(R[i][0] - 0.3, R[i][1] - 0.4, 'r'+str(i), fontsize=m_fontsize)


    # plt.text(5 + 0.1, 3 - 0.7, '火车站', fontsize=m_fontsize)
    # plt.text(4 - 0.7, 8 - 0.7, '机场', fontsize=m_fontsize)

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["top"].set_position(("data", 0))
    ax.spines["left"].set_position(("data", 0))
    ax.spines["right"].set_position(("data", 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 12, 1), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 8, 1), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel("x", fontsize=m_fontsize)
    plt.ylabel("y", fontsize=m_fontsize)

    plt.show()
