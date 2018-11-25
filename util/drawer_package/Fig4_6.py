# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


m_fontsize = 20

def get_data(s='a'):
    if s == 'a':
        Q = [[0, 0],[5, 0]]
        R_x = 4.5
        R = [[0, 0], [R_x, np.sqrt(25-R_x**2)]]
        S_x = 2
        S = [[0, 0], [S_x, np.sqrt(25-S_x**2)]]
        return np.array(Q), np.array(R), np.array(S)
    elif s=='b':
        Q = [[0, 0], [4, 0]]
        R = [[0,0],[2,2]]
        S = [[0,0],[4,4]]
        return np.array(Q), np.array(R), np.array(S)


def plot(plt, v1, v2, color='0.', linewidth=2., linestyle='-'):
    plt.plot([v1[0], v2[0]], [v1[1], v2[1]], color=color, linewidth=linewidth, linestyle=linestyle)


def draw_a():
    fig = plt.figure()


    Q, R, S = get_data()
    plot(plt, Q[0], Q[1])
    plot(plt, R[0], R[1])
    plot(plt, S[0], S[1])

    plt.text(Q[0, 0] - 0.3, Q[0, 0] - 0.3, 'O', fontsize=m_fontsize, color='0')
    plt.text(S[1, 0], S[1, 1] + 0.1, 'A', fontsize=m_fontsize, color='0')
    plt.text(R[1, 0], R[1, 1] + 0.1, 'B', fontsize=m_fontsize, color='0')
    plt.text(1.9, 0-0.6, "$A^{\'}$", fontsize=m_fontsize, color='0')
    plt.text(4.4, 0-0.6, "$B^{\'}$", fontsize=m_fontsize, color='0')

    # 辅助线
    plot(plt, [2, 0], S[1], color='green', linewidth=1, linestyle='--')
    plot(plt, [4.5, 0], R[1], color='green', linewidth=1, linestyle='--')

    theta = np.linspace(0, np.pi / 2, 800)
    x, y = np.cos(theta) * 5, np.sin(theta) * 5
    plt.plot(x, y, color='green', linewidth=1, linestyle='--')
    plt.axis('scaled')

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    # plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(1, 7, 1), ['', '', '', '', '5', ], fontsize=m_fontsize)
    plt.yticks(np.arange(1, 7, 1), ['', '', '', '', '5', ], fontsize=m_fontsize)
    plt.xlim(0, 5.5)
    plt.ylim(0, 5.5)
    # plt.xlabel('x', fontsize=m_fontsize)
    plt.ylabel('y', fontsize=m_fontsize)
    path = "F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-6(a).jpg"
    plt.savefig(path, dpi=300)
    # plt.show()

    print('裁剪中...')
    img = Image.open(path)  # 打开当前路径图像
    # 左，上，右，下
    box1 = (210, 150, 1600, 1430)  # 设置图像裁剪区域
    image1 = img.crop(box1)  # 图像裁剪
    image1.save(path)  # 存储当前区域
    print('path = ', path)


def draw_b():
    fig = plt.figure()


    Q, R, S = get_data(s='b')
    plot(plt, Q[0], Q[1])
    plot(plt, R[0], R[1])
    plot(plt, S[0], S[1])

    plt.text(Q[0, 0] - 0.3, Q[0, 0] - 0.3, 'O', fontsize=m_fontsize, color='0')
    plt.text(S[1, 0]-0.2, S[1, 1] + 0.2, 'B', fontsize=m_fontsize, color='0')
    plt.text(R[1, 0]-0.2, R[1, 1] + 0.2, 'A', fontsize=m_fontsize, color='0')

    plt.text(3.9, 0-0.5, "$B^{\'}$", fontsize=m_fontsize, color='0')
    plt.text(1.9, 0-0.5, "$A^{\'}$", fontsize=m_fontsize, color='0')

    # 辅助线
    plot(plt, [4, 0], S[1], color='green', linewidth=1, linestyle='--')
    plot(plt, [2, 0], R[1], color='green', linewidth=1, linestyle='--')

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))
    # plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(1, 7, 1), ['', '', '', '', '', ], fontsize=m_fontsize)
    plt.yticks(np.arange(1, 7, 1), ['', '', '', '', '', ], fontsize=m_fontsize)
    plt.xlim(0, 4.5)
    plt.ylim(0, 4.5)
    # plt.xlabel('x', fontsize=m_fontsize)
    plt.ylabel('y', fontsize=m_fontsize)
    path = "F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-6(b).jpg"
    plt.savefig(path, dpi=300)
    # plt.show()

    print('裁剪中...')
    img = Image.open(path)  # 打开当前路径图像
    # 左，上，右，下
    box1 = (70, 150, 1750, 1430)  # 设置图像裁剪区域
    image1 = img.crop(box1)  # 图像裁剪
    image1.save(path)  # 存储当前区域
    print('path = ', path)


if __name__=='__main__':
    # draw_a()
    draw_b()