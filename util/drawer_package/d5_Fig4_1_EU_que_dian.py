# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
from d5_compute_dtw_value import get_QRS

m_fontsize = 17

def plot_line_with_points(point_array, color='0', linewidth=1., label=None, marker=None, linestyle=None):
    plt.plot(point_array[:, 0], point_array[:, 1], color=color, linewidth=linewidth, label=label, marker=marker, linestyle=linestyle)


def draw_DTW_less_point():
    Q, R, S = get_QRS()
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
    Q, R, S = get_QRS(is_less=False)

    # 画轨迹
    plot_line_with_points(Q, color='black', linewidth=1.5, label='Q', marker='*', linestyle='-')
    plot_line_with_points(R, color='blue', linewidth=1.5, label='R', marker='>', linestyle='--')
    plot_line_with_points(S, color='0.5', linewidth=1.5, label='S', marker='H', linestyle='-.')

    # 标注样本点
    m_split = [0, 2, 4, 7, 10, 13, 17]
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

    # draw_DTW_less_point()
    draw_DTW_more_point()

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 19, 5), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 7, 1), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel('x', fontsize=m_fontsize-3)
    plt.ylabel('y', fontsize=m_fontsize-3)

    plt.show()
