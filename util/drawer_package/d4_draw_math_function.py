# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

m_fontsize=20

def cos_fun(x):
    return np.cos(x)

def draw_cos():
    x = np.linspace(0, np.pi, num=800)
    y = cos_fun(x)
    plt.text(2.5, -1.5, 'y=2*cos(x)-0.7')
    plt.plot(x, y, color='0.5', linewidth=0.8)

    x1 = np.pi / 3
    y1 = cos_fun(x1)
    plt.scatter(x1, y1, linewidths=2, edgecolors='0.5')
    plt.text(x1, y1, '  (π/3, ' + str(round(y1, 2)) + ')')

    x1 = np.pi / 2
    y1 = cos_fun(x1)
    plt.scatter(x1, y1, linewidths=2, edgecolors='0.5')
    plt.text(x1, y1 + 0.1, '  (π/2, ' + str(round(y1, 2)) + ')')


def draw_sigmoid():
    x = np.linspace(-5, 5, 200)
    y = 1/(1+np.power(np.e, -x))
    plt.plot(x, y)
    plt.plot([-5, 5], [1, 1], linewidth=1., linestyle='--')
    plt.text(0.5, 1.5, 'y', fontsize=m_fontsize)
    plt.text(1, 0.5, '$y=1/(1+e^x)$', fontsize=m_fontsize)


def draw_fu_sigmoid():
    miu = 0.3
    x = np.linspace(-5, 5, 200)
    y = 1/(1+np.power(np.e, x))+0.3
    plt.plot(x, y, linewidth=3., color='0')
    plt.plot([-5, 5], [miu, miu], linewidth=1., linestyle='--')
    plt.plot([-5, 5], [1+miu, 1+miu], linewidth=1., linestyle='--')
    plt.text(0.5, 1.6, '$I_{shape}$', fontsize=m_fontsize)
    plt.text(-5, 0.5, '$y=1/(1+e^x)+μ$', fontsize=m_fontsize)
    plt.text(0.3, miu, 'μ', fontsize=m_fontsize)
    plt.text(0.3, 1+miu, '1+μ', fontsize=m_fontsize)


def draw_g_x():
    x0 = np.linspace(0, 5, 500)
    y0 = 1.4-np.power(np.e, -x0)
    x1 = np.linspace(-5, 0, 500)
    y1 = [-0.7 for i in range(500)]
    plt.plot(x0, y0, color='0', linewidth=2.)
    plt.plot(x1, y1, color='0', linewidth=2.)
    plt.text(0.2, -0.74, '-ε', fontsize=14)
    plt.text(-0.4, 0.4, 'μ', fontsize=14)


if __name__=='__main__':
    fig = plt.figure()

    # draw_cos()
    draw_sigmoid()
    # draw_fu_sigmoid()
    # draw_g_x()

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    # plt.xticks(np.arange(-5, 6, 1), fontsize=m_fontsize)
    # plt.yticks(np.arange(0.5, 2, 0.5), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0, 1.6)
    plt.xticks([0])
    plt.yticks([])
    # plt.text(3, -0.15, r'$sim_{shape}$', fontsize=m_fontsize)
    # plt.xlabel(r'$sim_{shape}$', fontsize=m_fontsize)
    plt.text(5, -0.15, 'x', fontsize=m_fontsize)
    # plt.ylabel('y')

    plt.show()




