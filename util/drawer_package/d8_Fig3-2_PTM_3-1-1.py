# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import d8_PTM_computing

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 18

    Q, R, S = d8_PTM_computing.get_data()
    plt.plot(Q[:, 0], Q[:, 1], color='blue', linewidth=2, label='Q', marker='H', linestyle=None)
    plt.plot(R[:, 0], R[:, 1], color='0.5', linewidth=2, label='R', marker='*', linestyle=None)
    plt.plot(S[:, 0], S[:, 1], color='0.1', linewidth=2, label='S', marker='.', linestyle=None)

    Q_label = ['q0', 'q1', 'q2']
    plt.text(Q[0][0] - 3, Q[0][1], Q_label[0], fontsize=m_fontsize, color='blue')
    plt.text(Q[1][0] + 0.5, Q[1][1], Q_label[1], fontsize=m_fontsize, color='blue')
    plt.text(Q[2][0] + 0.5, Q[2][1], Q_label[2], fontsize=m_fontsize, color='blue')
    # for i in range(len(Q)):
    #     plt.text(Q[i][0] + 0.5, Q[i][1], Q_label[i], fontsize=m_fontsize, color='blue')

    R_label = ['r0', 'r1', 'r2', 'r3', 'r4', 'r5']
    plt.text(R[0][0], R[0][1] + 1, R_label[0], fontsize=m_fontsize, color='0.5')
    plt.text(R[1][0], R[1][1] + 1, R_label[1], fontsize=m_fontsize, color='0.5')
    plt.text(R[2][0], R[2][1] + 1, R_label[2], fontsize=m_fontsize, color='0.5')
    for i in range(3, len(R)):
        plt.text(R[i][0], R[i][1]+1, R_label[i], fontsize=m_fontsize, color='0.5')

    S_label = ['s0', 's1', 's2', 's3', 's4', 's5']
    plt.text(S[0][0] - 1.4, S[0][1] - 1.5, S_label[0], fontsize=m_fontsize, color='0.1')
    plt.text(S[1][0] - 0.3, S[1][1] - 1.5, S_label[1], fontsize=m_fontsize, color='0.1')
    plt.text(S[2][0] - 0.3, S[2][1] - 1.5, S_label[2], fontsize=m_fontsize, color='0.1')
    for i in range(3, len(S)):
        plt.text(S[i][0]-0.3, S[i][1]-1.5, S_label[i], fontsize=m_fontsize, color='0.1')

    for i in range(len(Q)):
        plt.plot([Q[i, 0], R[i, 0]], [Q[i, 1], R[i, 1]], color='green', linewidth=1., label='', marker=None, linestyle='--')
    for i in range(len(Q)):
        plt.plot([Q[i, 0], S[i, 0]], [Q[i, 1], S[i, 1]], color='green', linewidth=1., label='', marker=None, linestyle='--')

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', -10))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 40, 5), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 21, 5), fontsize=m_fontsize)
    plt.xlim(0, 37)
    plt.ylim(0, 21)
    plt.xlabel('x', fontsize=m_fontsize)
    plt.ylabel('y', fontsize=m_fontsize)

    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-2.jpg")
    plt.show()