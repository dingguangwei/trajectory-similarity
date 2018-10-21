# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

m_fontsize = 15

def plot_line_with_points(point_array, color='0', linewidth=1., label=None, marker=None, linestyle=None):
    plt.plot(point_array[:, 0], point_array[:, 1], color=color, linewidth=linewidth, label=label, marker=marker, linestyle=linestyle)


def draw_DTW_less_point():
    Q = np.array([[1,1],[5,1],[18,1]])
    R = np.array([[1,2],[5,2],[18,3]])
    S = np.array([[1, 3], [5, 2], [18, 2]])
    # 画轨迹
    plot_line_with_points(Q, color='black', linewidth=1.5, label='Q', marker='*', linestyle='-')
    plot_line_with_points(R, color='blue', linewidth=1.5, label='R', marker='>', linestyle='--')
    plot_line_with_points(S, color='0.5', linewidth=1.5, label='S', marker='H', linestyle='-.')

    # 标注样本点
    for i in np.arange(0, len(Q), 1):
        m_text = 'q'+str(i)
        plt.text(Q[i,0], Q[i,1]+0.1, m_text, fontsize=m_fontsize)
    for i in np.arange(0, len(R), 1):
        m_text = 'r'+str(i)
        plt.text(R[i,0]-0.5, R[i,1]+0.2, m_text, fontsize=m_fontsize)
    for i in np.arange(0, len(S), 1):
        m_text = 's'+str(i)
        plt.text(S[i,0]+0.2, S[i,1]+0.2, m_text, fontsize=m_fontsize)

    # 画对应点的连线
    for i in np.arange(0, len(Q), 1):
        plot_line_with_points(np.array([Q[i,:], R[i,:]]), color='blue', linewidth=1, linestyle=':')

    for i in np.arange(0, len(Q), 1):
        plot_line_with_points(np.array([Q[i, :], S[i, :]]), color='0.5', linewidth=1, linestyle=':')


def draw_DTW_more_point():
    Q = np.ones(shape=(18, 2))
    Q[:, 0] = np.arange(1, 19, 1)
    print(Q)

    R = np.zeros(shape=(18, 2))
    R[:, 0] = np.arange(1, 19, 1)
    R[0:4, 1] = [2 for i in range(4)]
    for i in np.arange(4, len(R), 1):
        R[i, 1] = (R[i, 0] - 5) / 13 + 2
    print(R)

    S = np.zeros(shape=(18, 2))
    S[:, 0] = np.arange(1, 19, 1)
    for i in np.arange(0, 5, 1):
        S[i, 1] = -(S[i, 0] - 1) / 4 + 3
    S[5:, 1] = [2 for i in range(13)]
    print(S)


    # 画轨迹
    plot_line_with_points(Q, color='black', linewidth=1.5, label='Q', marker='*', linestyle='-')
    plot_line_with_points(R, color='blue', linewidth=1.5, label='R', marker='>', linestyle='--')
    plot_line_with_points(S, color='0.5', linewidth=1.5, label='S', marker='H', linestyle='-.')

    # 标注样本点
    m_split = [0, 4, 10, 15, 17]
    for i in m_split:
        m_text = 'q'+str(i)
        plt.text(Q[i,0], Q[i,1]+0.1, m_text, fontsize=m_fontsize)
    for i in m_split:
        m_text = 'r'+str(i)
        plt.text(R[i,0]-0.1, R[i,1]+0.1, m_text, fontsize=m_fontsize)
    for i in m_split:
        m_text = 's'+str(i)
        plt.text(S[i,0]+0.2, S[i,1]+0.1, m_text, fontsize=m_fontsize)

    # 画对应点的连线
    for i in np.arange(0, len(Q), 1):
        plot_line_with_points(np.array([Q[i,:], R[i,:]]), color='blue', linewidth=1, linestyle=':')

    for i in np.arange(0, len(Q), 1):
        plot_line_with_points(np.array([Q[i, :], S[i, :]]), color='0.5', linewidth=1, linestyle=':')


if __name__=='__main__':
    fig = plt.figure()

    draw_DTW_less_point()
    # draw_DTW_more_point()

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend()
    plt.xticks(np.arange(0, 19, 5), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 7, 1), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel('x', fontsize=m_fontsize)
    plt.ylabel('y', fontsize=m_fontsize)

    plt.show()
