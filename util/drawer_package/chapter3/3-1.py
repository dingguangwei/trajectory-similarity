# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    Q = [
        [2,1],
        [2,3],
        [9,3]
    ]
    R = [
        [2,5],
        [2,3.3],
        [9,3.3]
    ]
    S = [
        [3,2],
        [8,2]
    ]
    return np.array(Q), np.array(R), np.array(S)


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    Q, R, S = get_data()
    plt.plot(Q[:, 0], Q[:, 1], color='black', linewidth=2, label='Q', marker='H', linestyle='-')
    plt.plot(R[:, 0], R[:, 1], color='0.4', linewidth=2, label='R', marker='*', linestyle=None)
    plt.plot(S[:, 0], S[:, 1], color='0.6', linewidth=2, label='S', marker='|', linestyle=None)

    for i in range(len(Q)):
        if i == 2:
            plt.text(Q[i][0] + 0.3, Q[i][1] - 0.2, 'q' + str(i), fontsize=m_fontsize, color='black')
        else:
            plt.text(Q[i][0] - 0.7, Q[i][1] - 0.2, 'q'+str(i), fontsize=m_fontsize, color='black')
    for i in range(len(S)):
        plt.text(S[i][0] + 0., S[i][1] - 0.5, 's'+str(i), fontsize=m_fontsize)
    for i in range(len(R)):
        if i == 2:
            plt.text(R[i][0] + 0.2, R[i][1] + 0.1, 'r' + str(i), fontsize=m_fontsize)
        else:
            plt.text(R[i][0] - 0.7, R[i][1] + 0.1, 'r'+str(i), fontsize=m_fontsize)

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 11, 2), np.arange(0, 110, 20), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 9, 2), np.arange(0, 110, 20), fontsize=m_fontsize)
    plt.xlim(0, 11)
    # plt.ylim(-2, 2)
    plt.xlabel('x/m', fontsize=m_fontsize)
    plt.ylabel('y/m', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.95, bottom=0.15, right=0.97, left=0.12, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter3_new\\3-1.jpg", dpi=300)
    plt.show()