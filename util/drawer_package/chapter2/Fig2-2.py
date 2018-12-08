# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    Q = [
        [1, 1],
        [2, 2],
        [2.5, 2.5],
        [3, 3],
        [5, 3],
        [7, 3],
    ]
    R = [
        [0.8, 1.8],
        [1.3, 2.3],
        [1.8, 2.8],
        [2.2, 3.2],
        [3, 4],
        [3.5, 4],
        [5, 4],
        [6.5, 4],
        [7, 4],
    ]
    return np.array(Q), np.array(R)


def draw_line( v1, v2, color='0.5', linewidth=1.):
    plt.plot([v1[0], v2[0]], [v1[1], v2[1]], linestyle='-.', linewidth=linewidth, color=color)


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 20

    Q, R = get_data()
    plt.plot(Q[:, 0], Q[:, 1], color='blue', linewidth=4, label='Q', marker='H', linestyle='-')
    plt.plot(R[:, 0], R[:, 1], color='0.4', linewidth=4, label='R', marker='*', linestyle=None)

    for i in range(len(Q)):
        plt.text(Q[i][0] - 0.2, Q[i][1] - 0.5, 'q'+str(i), fontsize=m_fontsize, color='blue')
    for i in range(len(R)):
        plt.text(R[i][0] - 0.3, R[i][1] + 0.3, 'r'+str(i), fontsize=m_fontsize, color='0.4')

    draw_line(Q[0], R[0], linewidth=2.)
    draw_line(Q[1], R[1], linewidth=2.)
    draw_line(Q[1], R[2], linewidth=2.)
    draw_line(Q[2], R[3], linewidth=2.)
    draw_line(Q[3], R[4], linewidth=2.)
    draw_line(Q[3], R[5], linewidth=2.)
    draw_line(Q[4], R[6], linewidth=2.)
    draw_line(Q[5], R[7], linewidth=2.)
    draw_line(Q[5], R[8], linewidth=2.)

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 10, 1), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 10, 1), fontsize=m_fontsize)
    plt.xlim(0, 8)
    plt.ylim(0, 7)
    plt.xlabel('x', fontsize=m_fontsize)
    plt.ylabel('y', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.95, bottom=0.15, right=0.97, left=0.12, hspace=0, wspace=0)
    plt.savefig('F:/毕业设计大文件夹/picture/chapter2/2-2.jpg')
    plt.show()