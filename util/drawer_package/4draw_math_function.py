# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np


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
    x = np.linspace(-10, 10, 200)
    y = 1/(1+np.power(np.e, -x))
    plt.plot(x, y)


if __name__=='__main__':
    fig = plt.figure()

    # draw_cos()
    draw_sigmoid()

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.xticks(np.arange(-10, 11, 5))
    plt.yticks(np.arange(0, 1.1, 0.5))
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()




