# coding=utf-8
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# 画箭头
def draw(A, B):
    fig = plt.figure()
    ax = fig.add_subplot(111)


    ax.arrow(A[0], A[1], B[0]-A[0], B[1]-A[1],
                 length_includes_head=True,# 增加的长度包含箭头部分
                 head_width=0.05, head_length=0.1, fc='r', ec='b', linewidth=1, color='0.')
    ax.annotate("", xy=(B[0], B[1]), xytext=(A[0], A[1]),arrowprops=dict(arrowstyle="->"), color='0.')
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.show()


def draw_b():
    import matplotlib.pyplot as plt
    fig = plt.figure()  # figsize=(10,6)
    ax = fig.add_subplot(111)
    ax.set_xlim([1, 6]);
    ax.set_ylim([1, 9]);
    ax.text(2, 8, r"$ \mu \alpha \tau \pi \lambda \omega \tau \
        lambda \iota \beta $", color='r', fontsize=20);
    ax.text(2, 6, r"$ \lim_{x \rightarrow 0} \frac{1}{x} $", fontsize=20);
    ax.text(2, 4, r"$ a \ \leq \ b \ \leq \ c \ \Rightarrow \ a \
        \leq \ c$", fontsize=20);
    ax.text(2, 2, r"$ \sum_{i=1}^{\infty}\ x_i^2$", fontsize=20);
    ax.text(4, 8, r"$ \sin(0) = \cos(\frac{\pi}{2})$", fontsize=20);
    ax.text(4, 6, r"$ \sqrt[3]{x} = \sqrt{y}$", fontsize=20);
    ax.text(4, 4, r"$ \neg (a \wedge b) \Leftrightarrow \neg a \
        \vee \neg b$");
    ax.text(4, 2, r"$ \int_a^b f(x)dx$", fontsize=20);
    plt.show()

if __name__ == '__main__':
    A, B = [0, 0,], [1, 1,]
    draw(A, B)

    # draw_b()


