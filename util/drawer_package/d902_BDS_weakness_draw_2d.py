# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import d902_BDS_weakness_draw

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    Q, R, S = d902_BDS_weakness_draw.get_data()

    plt.plot(Q[:, 0], Q[:, 1], color='blue', linewidth=2, label='Q', marker='H', linestyle=None)
    plt.plot(R[:, 0], R[:, 1], color='0.5', linewidth=2, label='R', marker='>', linestyle=None)

    for i in range(6):
        plt.text(Q[i, 0]+0.3, Q[i, 1]-0.3, 'q'+str(i), color='blue', fontsize=m_fontsize)
    for i in range(7):
        plt.text(R[i, 0]-0.5, R[i, 1]+0.3, 'r'+str(i), color='0.5', fontsize=m_fontsize)

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 10, 1), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 7, 1), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel('x', fontsize=m_fontsize)
    plt.ylabel('y', fontsize=m_fontsize)

    plt.show()