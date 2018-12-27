# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import d8_PTM_computing


def get_data():
    Q, R, S = d8_PTM_computing.get_data()

    Q_x = 1.5
    R_x = 0.5
    S_x = 2.5

    Q2 = np.ones(shape=(len(Q),2))
    R2 = np.ones(shape=(len(R),2))
    S2 = np.ones(shape=(len(S), 2))
    for i in range(len(Q)):
        Q2[i,0] = Q[i,2]*60
        Q2[i, 1] = 2
    for i in range(len(R)):
        R2[i,0]=R[i,2]*60
        R2[i, 1] = 3
    for i in range(len(S)):
        S2[i,0] = S[i,2]*60

    return Q2, R2, S2



if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    Q, R, S = get_data()

    plt.scatter(Q[:, 0], Q[:, 1], color='black')
    plt.scatter(R[:, 0], R[:, 1], color='0.4')
    plt.scatter(S[:, 0], S[:, 1], color='0.6')

    for i in range(len(Q)):
        plt.text(Q[i, 0], Q[i, 1]+0.1, 'q'+str(i), color='black', fontsize=m_fontsize)
        plt.plot([Q[i, 0], R[i+3, 0]], [Q[i, 1], R[i+3, 1]], color='green', linewidth=1., label='', marker=None,linestyle='--')
        plt.plot([Q[i, 0], S[i, 0]], [Q[i, 1], S[i, 1]], color='green', linewidth=1., label='', marker=None,linestyle='--')
        if i < len(Q)-1:
            plt.plot([Q[i,0], Q[i+1,0]], [Q[i,1], Q[i+1,1]], color='black', linewidth=4., label='Q', marker=None, linestyle='-')
    for i in range(len(R)):
        plt.text(R[i, 0], R[i, 1]+0.1, 'r' + str(i), color='0.4', fontsize=m_fontsize)
        if i < len(R)-1:
            plt.plot([R[i,0], R[i+1,0]], [R[i,1], R[i+1,1]], color='0.4', linewidth=4., label='R', marker=None, linestyle='-')
    for i in range(len(S)):
        plt.text(S[i, 0], S[i, 1]-0.35, 's' + str(i), color='0.6', fontsize=m_fontsize)
        if i < len(S)-1:
            plt.plot([S[i,0], S[i+1,0]], [S[i,1], S[i+1,1]], color='0.6', linewidth=4., label='S', marker=None, linestyle='-')

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_position(('data', 0))
    # ax.spines['left'].set_position(('data', 0))
    # ax.spines['right'].set_position(('data', 0))

    # plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 4001, 1000), fontsize=m_fontsize)
    plt.yticks([0, 1, 2, 3, 4], [0, 'S', 'Q', 'R', ''], fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel('x / second', fontsize=m_fontsize)
    # plt.ylabel('', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.7, bottom=0.15, right=0.97, left=0.07, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-3_time.jpg")
    plt.show()