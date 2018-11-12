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
    return np.array(Q)


def get_vector(v0, v1):
    v0 = np.array(v0)
    v1 = np.array(v1)
    v = v1-v0
    d = np.sqrt(np.sum((v0-v1)**2))
    v = v/d
    d = np.sqrt(v[0]**2+v[1]**2+v[2]**2)
    print('v=', v, '  d=', d)
    return v


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 20

    Q = get_data()
    ax.plot(Q[:,0],Q[:, 1],Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    m_label=[r'$pre(Q(r_i))$', r'$Q(r_i)$', r'$next(Q(r_i))$']
    ax.text(Q[0, 0] - 1.4, Q[0, 1], Q[0, 2]-0.1, m_label[0], color='blue', fontsize=m_fontsize)
    ax.text(Q[1, 0] - 0.8, Q[1, 1], Q[1, 2]-0.4, m_label[1], color='blue', fontsize=m_fontsize)
    ax.text(Q[2, 0] - 0.4, Q[2, 1], Q[2, 2], m_label[2], color='blue', fontsize=m_fontsize)

    v0v1 = get_vector(Q[0], Q[1])
    end1 = v0v1+np.array(Q[1])
    # ax.scatter(end1[0], end1[1], end1[2], r'$end1$', color='blue', fontsize=m_fontsize)
    ax.plot([Q[1, 0], end1[0]],[Q[1, 1], end1[1]],[Q[1, 2], end1[2]], linestyle='-', color='0.4', linewidth='1.5')

    v1v2 = get_vector(Q[1], Q[2])
    end2 = v1v2 + np.array(Q[1])
    ax.plot([Q[1, 0], end2[0]], [Q[1, 1], end2[1]], [Q[1, 2], end2[2]], color='0.4', linewidth='1.5')

    end3 = v1v2+end1
    ax.plot([end1[0], end3[0]], [end1[1], end3[1]], [end1[2], end3[2]], color='0.4', linewidth='1.5')
    ax.plot([end2[0], end3[0]], [end2[1], end3[1]], [end2[2], end3[2]], color='0.4', linewidth='1.5')
    ax.plot([Q[1, 0], end3[0]],[Q[1, 1], end3[1]],[Q[1, 2], end3[2]], linestyle='-', color='0.1', linewidth='1.5')
    ax.text(end3[0],end3[1]-0.6,end3[2]+0.3, r"$Q(r_i)^{'}$", fontsize=m_fontsize, color='0.1')

    print('[end1, end2, end3] = ', end1, end2, end3)
    d_q1_end1 = np.sqrt(np.sum((np.array(Q[1])-end1)**2))
    print('d_q1_end1 = ', d_q1_end1)
    d_q1_end2 = np.sqrt(np.sum((np.array(Q[1]) - end2) ** 2))
    print('d_q1_end2 = ', d_q1_end2)


    # ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)
    # 设置坐标轴刻度
    # ax.set_xticks([])
    # ax.set_yticks([])
    ax.set_zticks(np.arange(0, 3, 1))
    plt.xlim(0, 3)
    plt.ylim(0, 3)
    ax.set_zlim(0, 3)
    ax.view_init(elev=20, azim=300)  # 调整视角
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-4.jpg")
    plt.show()