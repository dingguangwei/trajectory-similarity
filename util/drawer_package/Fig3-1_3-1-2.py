# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


def get_Data():
    A = [3.2, 2]
    B = [4, 1.2]
    C = [8, 1.2]
    Q = [A, B, C]
    R = [
        [1, 4],
        [1, 3],
        [1,2],
        [2,2],
        [3,2],
        [4, 1],
        [5, 1],
        [8, 1],
        [9, 1],
    ]
    S = [[4.,2.5],  [4.5, 2], [8,2]]

    return np.array(R), np.array(S), np.array(Q)


if __name__ == "__main__":
    fig = plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    m_fontsize = 16

    # 画轨迹
    R, S, Q = get_Data()
    plt.plot(Q[:, 0], Q[:, 1], color='black', linewidth=4, label='Q', marker='H', linestyle='-')
    plt.plot(R[:, 0], R[:, 1], color='0.4', linewidth=4, label='R', marker='*', linestyle=None)
    plt.plot(S[:, 0], S[:, 1], color='0.6', linewidth=4, label='S', marker='|', linestyle=None)

    for i in range(len(Q)):
        plt.text(Q[i][0] - 0.2, Q[i][1] + 0.3, 'q'+str(i), fontsize=m_fontsize, color='black')
    for i in range(len(S)):
        plt.text(S[i][0] - 0.1, S[i][1] + 0.3, 's'+str(i), fontsize=m_fontsize)
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
    plt.xlim(0, 10)
    plt.ylim(0, 4)
    plt.xlabel("x", fontsize=m_fontsize)
    plt.ylabel("y", fontsize=m_fontsize)

    plt.savefig('F:/毕业设计大文件夹/picture/exp/d7-3-1-2.jpg')
    plt.show()
