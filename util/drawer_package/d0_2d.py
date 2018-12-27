# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 10, 1), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 10, 1), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel('x/m', fontsize=m_fontsize)
    plt.ylabel('y/m', fontsize=m_fontsize)

    plt.show()