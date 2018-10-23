# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import d8_PTM_computing

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 14

    Q, R, S = d8_PTM_computing.get_data()

    Q_x = 3
    R_x = 1
    S_x = 5

    plt.scatter(np.ones((1, len(Q))) * Q_x, Q[:, 2], color='blue')
    plt.scatter(np.ones((1, len(R))) * R_x, R[:, 2], color='0.5')
    plt.scatter(np.ones((1, len(S))) * S_x, S[:, 2], color='0.1')

    for i in range(len(Q)):
        plt.text(Q_x+0.2, Q[i, 2], 'q'+str(i), color='blue', fontsize=m_fontsize)
        plt.plot([Q_x, R_x], [Q[i, 2], R[i+3, 2]], color='green', linewidth=1., label='', marker=None,linestyle='--')
        plt.plot([Q_x, S_x], [Q[i, 2], S[i, 2]], color='green', linewidth=1., label='', marker=None,linestyle='--')
    for i in range(len(R)):
        plt.text(R_x+0.2, R[i, 2], 'r' + str(i), color='0.5', fontsize=m_fontsize)
    for i in range(len(S)):
        plt.text(S_x+0.2, S[i, 2], 's' + str(i), color='0.1', fontsize=m_fontsize)

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    # plt.legend(fontsize=m_fontsize)
    # plt.xticks(np.arange(0, 10, 5), fontsize=m_fontsize)
    plt.xticks([0, R_x, Q_x, S_x], [0, 'R', 'Q', 'S'], fontsize=m_fontsize)
    plt.yticks(np.arange(0, 70, 10), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    # plt.xlabel('x', fontsize=m_fontsize)
    plt.ylabel('y / minutes', fontsize=m_fontsize)

    plt.show()