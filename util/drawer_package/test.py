# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def draw(A, B):
    fig = plt.figure()
    ax = fig.add_subplot(111)


    ax.arrow(A[0], A[1], B[0]-A[0], B[1]-A[1],
                 length_includes_head=True,# 增加的长度包含箭头部分
                 head_width=0.05, head_length=0.1, fc='r', ec='b')
    ax.annotate("", xy=(B[0], B[1]), xytext=(A[0], A[1]),arrowprops=dict(arrowstyle="->"))
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.show()

if __name__ == '__main__':
    A, B = [0, 0], [1, 1]

    draw(A, B)


