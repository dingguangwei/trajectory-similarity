# coding=utf-8
# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



def get_data():
    Q = [

    ]
    R = [

    ]
    return np.array(Q), np.array(R)


def draw_2d():
    fig = plt.figure()
    m_fontsize = 16

    Q, R = get_data()
    plt.plot(Q[:, 0], Q[:, 1], color='black')
    plt.plot(R[:, 0], R[:, 1], color='0.4')

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


def draw_3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16

    ax.plot([0, 1], [1, 2], [3, 4], label='a', linestyle='-', linewidth=2, color='0', marker='H')

    ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize)
    ax.set_ylabel('y/m', fontsize=m_fontsize)
    ax.set_zlabel('z/m', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    # ax.set_yticks([])
    ax.set_zticks(np.arange(0, 10, 2), fontsize=m_fontsize)
    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 10)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    ax.view_init(elev=20, azim=20)  # 调整视角
    plt.show()


if __name__ == '__main__':
    draw_2d()