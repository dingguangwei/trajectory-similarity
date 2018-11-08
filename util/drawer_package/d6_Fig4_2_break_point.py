# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

m_fontsize = 20

def plot(point_arr, ax, label=None, linestyle='-', linewidth=1., color='0', marker=None):
    x = []
    y = []
    z = []
    for point in point_arr:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    ax.plot(x, y, z, label=label, linestyle=linestyle, linewidth=linewidth, color=color, marker=marker)


def find_pair_point(ax, r, qi, qj, color='green'):
    x = qi[0]
    min_point = [qi[0],qi[1],qi[2]]
    min_distance = 100
    for x in np.arange(min(qi[0], qj[0]), max(qi[0], qj[0]), 0.0001):
        y = (qj[1]-qi[1])/(qj[0]-qi[0])*(x-qi[0])+qi[1]
        z = (qj[2]-qi[2])/(qj[0]-qi[0])*(x-qi[0])+qi[2]
        if (r[0]-x)**2+(r[1]-y)**2+(r[2]-z)**2 < min_distance**2:
            min_distance = np.sqrt((r[0]-x)**2+(r[1]-y)**2+(r[2]-z)**2)
            min_point = [x, y, z]
    ax.plot([r[0],min_point[0]], [r[1], min_point[1]], [r[2], min_point[2]], linestyle='--', linewidth=1, color=color)
    # ax.text(min_point[0], min_point[1], min_point[2]+0.01, label, fontsize=fontsize)
    # print('min_point=', min_point)
    return min_point


def draw_a():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 轨迹R
    r0 = [0.1, 0, 0.1]
    r1 = [0, 0.3, 0.3]
    ax.plot([r0[0], r1[0]], [r0[1], r1[1]], [r0[2], r1[2]], linestyle='-', linewidth=1.5, color='0.', marker='s')
    ax.text(r0[0], r0[1] + 0.0, r0[2] - 0.02, r'$r_0$', fontsize=m_fontsize)
    ax.text(r1[0], r1[1] + 0.0, r1[2] - 0.02, r'$r_1$', fontsize=m_fontsize)

    # 断点
    break_point_list = []
    m_step = 0.06
    for z in np.arange(0.1 + m_step, 0.3, m_step):
        x = -(z - 0.1) / 2 + 0.1
        y = 3 * (z - 0.1) / 2
        break_point_list.append([x, y, z])
    print('break_point_list=\n', break_point_list)
    break_point_list = np.array(break_point_list)
    for i in range(len(break_point_list)):
        ax.scatter(break_point_list[i, 0], break_point_list[i, 1], break_point_list[i, 2], marker='.', linewidths=2.5,
                   color='b')
        ax.text(break_point_list[i, 0], break_point_list[i, 1] + 0.0, break_point_list[i, 2] - 0.02, r'$bp_' + str(i)+'$',
                fontsize=m_fontsize)

    # 轨迹Q（情况一）
    q0 = [0.1, 0.2, 0.1]
    q1 = [0., 0.3, 0.2]
    plot([q0, q1], ax=ax, label=None, linestyle='-', linewidth=1.5, color='blue', marker='s')
    ax.text(q0[0], q0[1] - 0.03, q0[2] - 0.03, r'$q_0=Q(r_0)$', fontsize=m_fontsize, color='blue')
    ax.text(q1[0], q1[1] - 0.03, q1[2] - 0.04, r'$q_1=Q(r_1)$', fontsize=m_fontsize, color='blue')

    find_pair_point(ax, r0, q0, q1)
    find_pair_point(ax, r1, q0, q1)
    find_pair_point(ax, break_point_list[0], q0, q1)
    find_pair_point(ax, break_point_list[1], q0, q1)
    find_pair_point(ax, break_point_list[2], q0, q1)

    # ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('z', fontsize=m_fontsize)
    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0.1, 0.34, 0.1))
    ax.set_zlim(0.1, 0.35)
    ax.view_init(elev=20, azim=20)  # 调整视角
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-2(a).jpg")
    plt.show()


def draw_b():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 轨迹R
    r0 = [0.1, 0, 0.1]
    r1 = [0, 0.3, 0.3]
    ax.plot([r0[0], r1[0]], [r0[1], r1[1]], [r0[2], r1[2]], linestyle='-', linewidth=1.5, color='0.', marker='s')
    ax.text(r0[0], r0[1] + 0.02, r0[2] - 0.02, r'$r_0$', fontsize=m_fontsize)
    ax.text(r1[0], r1[1] + 0.02, r1[2] - 0.02, r'$r_1$', fontsize=m_fontsize)

    # 断点
    break_point_list = []
    m_step = 0.06
    for z in np.arange(0.1 + m_step, 0.3, m_step):
        x = -(z - 0.1) / 2 + 0.1
        y = 3 * (z - 0.1) / 2
        break_point_list.append([x, y, z])
    print('break_point_list=\n', break_point_list)
    break_point_list = np.array(break_point_list)
    for i in range(len(break_point_list)):
        ax.scatter(break_point_list[i, 0], break_point_list[i, 1], break_point_list[i, 2], marker='.', linewidths=2.5,
                   color='b')
        ax.text(break_point_list[i, 0], break_point_list[i, 1] + 0.02, break_point_list[i, 2] - 0.02,r'$bp_' + str(i) + '$', fontsize=m_fontsize)

    # 轨迹Q（情况二）
    q0 = [0.1, 0.2, 0.1]
    # plot([q0], ax=ax, label=None, linestyle='-', linewidth=1.5, color='0.5', marker='s')
    ax.scatter(q0[0], q0[1], q0[2], linestyle='-', linewidth=1.5, color='blue', marker='s')
    ax.text(q0[0], q0[1] + 0.02, q0[2] - 0.02, 'q0', fontsize=m_fontsize, color='blue')

    find_pair_point(ax, r0, q0, q0)
    find_pair_point(ax, r1, q0, q0)
    find_pair_point(ax, break_point_list[0], q0, q0)
    find_pair_point(ax, break_point_list[1], q0, q0)
    find_pair_point(ax, break_point_list[2], q0, q0)

    # ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('z', fontsize=m_fontsize)
    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0.1, 0.34, 0.1))
    ax.set_zlim(0.1, 0.35)
    ax.view_init(elev=20, azim=20)  # 调整视角
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-2(b).jpg")
    plt.show()


def draw_c():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 轨迹R
    r0 = [0.1, 0, 0.1]
    r1 = [0, 0.3, 0.3]
    ax.plot([r0[0], r1[0]], [r0[1], r1[1]], [r0[2], r1[2]], linestyle='-', linewidth=1.5, color='0.', marker='s')
    ax.text(r0[0], r0[1] + 0.02, r0[2] - 0.02, r'$r_0$', fontsize=m_fontsize)
    ax.text(r1[0], r1[1] + 0.02, r1[2] - 0.02, r'$r_1$', fontsize=m_fontsize)

    # 断点
    break_point_list = []
    m_step = 0.06
    for z in np.arange(0.1 + m_step, 0.3, m_step):
        x = -(z - 0.1) / 2 + 0.1
        y = 3 * (z - 0.1) / 2
        break_point_list.append([x, y, z])
    print('break_point_list=\n', break_point_list)
    break_point_list = np.array(break_point_list)
    for i in range(len(break_point_list)):
        ax.scatter(break_point_list[i, 0], break_point_list[i, 1], break_point_list[i, 2], marker='.', linewidths=2.5,
                   color='b')
        ax.text(break_point_list[i, 0], break_point_list[i, 1] + 0.02, break_point_list[i, 2] - 0.02,
                r'$bp_' + str(i) + '$',
                fontsize=m_fontsize)

    # 轨迹Q（情况三）
    q = []
    q.append([0.1, 0.2, 0.08])
    q.append([0.1, 0.3, 0.15])
    q.append([0., 0.3, 0.2])
    plot([q[0], q[1], q[2]], ax=ax, label=None, linestyle='-', linewidth=1.5, color='blue', marker='s')
    for i in range(3):
        ax.text(q[i][0], q[i][1] + 0.02, q[i][2] - 0.02, 'q'+str(i), fontsize=m_fontsize, color='blue')

    find_pair_point(ax, r0, q[0], q[1])
    find_pair_point(ax, r1, q[1], q[2] )
    find_pair_point(ax, break_point_list[0], q[0], q[1] )
    find_pair_point(ax, break_point_list[1], q[1], q[2] )
    find_pair_point(ax, break_point_list[2], q[1], q[2] )

    # ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('z', fontsize=m_fontsize)
    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0.1, 0.34, 0.1))
    ax.set_zlim(0.1, 0.35)
    ax.view_init(elev=20, azim=20)  # 调整视角
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-2(c).jpg")
    plt.show()


if __name__=='__main__':
    # draw_a()
    # draw_b()
    draw_c()