# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def get_data():
    Q = [
        [3,0,0],
        [2,1,1],
        [2,3,2]
    ]
    R = [
        [0.5, 1, 0.5],
        [0.5, 1.5, 1.5]
    ]
    return np.array(Q), np.array(R)


def get_vector(v0, v1):
    v0 = np.array(v0)
    v1 = np.array(v1)
    v = v1-v0
    d = np.sqrt(np.sum((v0-v1)**2))
    v = v/d
    d = np.sqrt(v[0]**2+v[1]**2+v[2]**2)
    print('v=', v, '  d=', d)
    return v


# 画一个带箭头的矢量
def draw_vector(ax, A, B):
    # ax.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1],
    #          length_includes_head=True,  # 增加的长度包含箭头部分
    #          head_width=0.05, head_length=0.1, fc='r', ec='b')
    ax.annotate("", xy=(B[0], B[1]), xytext=(A[0], A[1]), arrowprops=dict(arrowstyle="->"), color='0.')


def plot(point_arr, ax, label=None, linestyle='-', linewidth=1., color='0', marker=None):
    x = []
    y = []
    z = []
    for point in point_arr:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    ax.plot(x, y, z, label=label, linestyle=linestyle, linewidth=linewidth, color=color, marker=marker)




if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 25
    small_fontsize = 20

    Q, R = get_data()
    ax.plot(Q[:,0],Q[:, 1],Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # ri & qi
    ax.text(R[0, 0] - 0.3, R[0, 1], R[0, 2] - 0.1, '$r_i$', color='0.4', fontsize=m_fontsize)
    ax.text(R[1, 0] - 0.3, R[1, 1], R[1, 2] - 0.1, '$r_j$', color='0.4', fontsize=m_fontsize)

    m_label=[r'$Q(r_i).pre$', r'$Q(r_i)$', r'$Q(r_i).next$']
    ax.text(Q[0, 0] - 1.4, Q[0, 1], Q[0, 2]-0.1, m_label[0], color='black', fontsize=small_fontsize)
    ax.text(Q[1, 0] + 0.2, Q[1, 1], Q[1, 2]-0.2, m_label[1], color='black', fontsize=small_fontsize)
    ax.text(Q[2, 0] - 0.1, Q[2, 1], Q[2, 2]+0.1, m_label[2], color='black', fontsize=small_fontsize)

    # 对应点连线
    plot([R[0], Q[1]], ax, linestyle='--', linewidth=1, color='green')
    plot([R[1], Q[1]], ax, linestyle='--', linewidth=1, color='green')

    v0v1 = get_vector(Q[0], Q[1])
    end1 = v0v1+np.array(Q[1])
    plot([Q[1], end1], ax, color='0.', linewidth=1.5, linestyle='-')
    # draw_vector(ax, Q[1], end1)

    v1v2 = get_vector(Q[1], Q[2])
    end2 = v1v2 + np.array(Q[1])
    plot([Q[1], end2], ax, color='0.', linewidth=1.5, linestyle='-')

    end3 = v1v2+end1
    plot([end1, end3], ax, linestyle='--', color='0.4', linewidth=1.)
    plot([end2, end3], ax, linestyle='--', color='0.4', linewidth=1.)
    plot([Q[1], end3], ax, linestyle='-', color='0.', linewidth=1.5)
    ax.text(end3[0],end3[1]-0.6,end3[2]+0.3, r"$Q(r_i)^{'}$", fontsize=m_fontsize, color='0.1')

    print('[end1, end2, end3] = ', end1, end2, end3)
    d_q1_end1 = np.sqrt(np.sum((np.array(Q[1])-end1)**2))
    print('d_q1_end1 = ', d_q1_end1)
    d_q1_end2 = np.sqrt(np.sum((np.array(Q[1]) - end2) ** 2))
    print('d_q1_end2 = ', d_q1_end2)


    # ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize-3)
    ax.set_ylabel('y/m', fontsize=m_fontsize-3)
    ax.set_zlabel('z/m', fontsize=m_fontsize-3)
    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0, 3, 1))
    plt.xlim(0, 3)
    plt.ylim(0, 3)
    ax.set_zlim(0, 3)
    ax.view_init(elev=20, azim=300)  # 调整视角
    plt.subplots_adjust(top=1, bottom=0, right=0.95, left=0, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-7.jpg", pad_inches = 0.25)
    plt.show()