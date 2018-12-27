# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image


m_fontsize = 20


def get_data():
    r0 = [0.1, 0, 0.1]
    r1 = [0, 0.3, 0.3]
    q0 = [0.1, 0.2, 0.1]
    q1 = [0., 0.3, 0.2]
    return r0, r1, q0, q1

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


def cut():
    # 裁剪
    print('裁剪中...')
    path = "F:\\毕业设计大文件夹\\picture\\chapter4\\"
    m_files = ['Fig4-4(a).jpg', 'Fig4-4(b).jpg']

    for m_file in m_files:
        img = Image.open(path + m_file)  # 打开当前路径图像
        # 左，上，右，下
        box1 = (310, 230, 1600, 1350)  # 设置图像裁剪区域
        image1 = img.crop(box1)  # 图像裁剪
        # print(img.size)
        # image1.show()
        # print(image1.size)
        image1.save(path + 'cut_' + m_file)  # 存储当前区域
        print('path = ', path + 'cut_' + m_file)


def draw_a(fig, ax):
    # 轨迹R
    r0, r1, q0, q1 = get_data()
    ax.plot([r0[0], r1[0]], [r0[1], r1[1]], [r0[2], r1[2]], linestyle='-', linewidth=2, color='0.4', marker='*')
    ax.text(r0[0], r0[1] + 0.0, r0[2] - 0.02, r'$r_0$', fontsize=m_fontsize, color='0.4')
    ax.text(r1[0], r1[1] + 0.0, r1[2] - 0.02, r'$r_1$', fontsize=m_fontsize, color='0.4')

    # 断点
    break_point_list = []
    m_step = 0.004
    for z in np.arange(0.1 + m_step, 0.3, m_step):
        x = -(z - 0.1) / 2 + 0.1
        y = 3 * (z - 0.1) / 2
        break_point_list.append([x, y, z])
    print('break_point_list=\n', break_point_list)
    break_point_list = np.array(break_point_list)
    for i in range(len(break_point_list)):
        ax.scatter(break_point_list[i, 0], break_point_list[i, 1], break_point_list[i, 2], marker='.', linewidths=0.5,
                   color='0.4')

    # 轨迹Q（情况一）
    plot([q0, q1], ax=ax, label=None, linestyle='-', linewidth=2, color='black', marker='H')
    ax.text(q0[0], q0[1] - 0.03, q0[2] - 0.03, r'$q_0$', fontsize=m_fontsize, color='black')
    ax.text(q1[0], q1[1] - 0.03, q1[2] - 0.04, r'$q_1$', fontsize=m_fontsize, color='black')

    find_pair_point(ax, r0, q0, q1)
    find_pair_point(ax, r1, q0, q1)
    for i in range(len(break_point_list)):
        find_pair_point(ax, break_point_list[i], q0, q1)
    return "F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-4(a).jpg"


def draw_b(fig, ax):
    # 轨迹R
    r0, r1, q0, q1 = get_data()
    ax.plot([r0[0], r1[0]], [r0[1], r1[1]], [r0[2], r1[2]], linestyle='-', linewidth=2, color='0.4', marker='*')
    ax.text(r0[0], r0[1] + 0.0, r0[2] - 0.02, r'$r_0$', fontsize=m_fontsize, color='0.4')
    ax.text(r1[0], r1[1] + 0.0, r1[2] - 0.02, r'$r_1$', fontsize=m_fontsize, color='0.4')

    # 断点
    break_point_list = []
    m_step = 0.03
    for z in np.arange(0.1 + m_step, 0.3, m_step):
        x = -(z - 0.1) / 2 + 0.1
        y = 3 * (z - 0.1) / 2
        break_point_list.append([x, y, z])
    print('break_point_list=\n', break_point_list)
    break_point_list = np.array(break_point_list)
    for i in range(len(break_point_list)):
        ax.scatter(break_point_list[i, 0], break_point_list[i, 1], break_point_list[i, 2], marker='.', linewidths=2.5,
                   color='0.4')
        ax.text(break_point_list[i, 0], break_point_list[i, 1] - 0.04, break_point_list[i, 2] + 0.015,
                r'$bp_' + str(i) + '$',
                fontsize=m_fontsize, color='0.4')

    #################################################################################
    # 画 break_point_list[2]代表的断点部分
    #################################################################################
    ax.text(break_point_list[2, 0], break_point_list[2, 1] - 0.04, break_point_list[2, 2] + 0.015, r'$bp_' + str(2) + '$', fontsize=m_fontsize, color='0.4')

    nb = [(break_point_list[1] + break_point_list[2]) / 2, (break_point_list[2] + break_point_list[3]) / 2]
    print('nb0=', nb[0])
    print('bp2=', break_point_list[2])
    print('nb1=', nb[1])
    # plot(nb, ax, linewidth=4.)
    ax.text(nb[0][0]+0.02, nb[0][1]+0.01, nb[0][2]-0.03, '$nb_' + str(0) + '$', fontsize=m_fontsize)
    ax.text(nb[1][0], nb[1][1]+0.01, nb[1][2]-0.03, '$nb_' + str(1) + '$', fontsize=m_fontsize)
    for i in range(len(nb)):
        ax.scatter(nb[i][0], nb[i][1], nb[i][2], linewidths=2, color='0')

    # 获取断点
    small_step = 0.004
    small_bp_list = []
    for z in np.arange(nb[0][2] + small_step, nb[1][2], small_step):
        x = -(z - 0.1) / 2 + 0.1
        y = 3 * (z - 0.1) / 2
        small_bp_list.append([x, y, z])
    small_bp_list = np.array(small_bp_list)
    # for i in range(len(small_bp_list)):
    #     ax.scatter(small_bp_list[i, 0], small_bp_list[i, 1], small_bp_list[i, 2], marker='.', linewidths=2.5,
    #                color='0')


    #################################################################################
    # 轨迹Q（情况一）
    #################################################################################
    plot([q0, q1], ax=ax, label=None, linestyle='-', linewidth=2, color='black', marker='H')
    ax.text(q0[0], q0[1] - 0.03, q0[2] - 0.03, r'$q_0$', fontsize=m_fontsize, color='black')
    ax.text(q1[0], q1[1] - 0.03, q1[2] - 0.04, r'$q_1$', fontsize=m_fontsize, color='black')

    find_pair_point(ax, r0, q0, q1)
    find_pair_point(ax, r1, q0, q1)
    for i in range(len(break_point_list)):
        find_pair_point(ax, break_point_list[i], q0, q1)
    # for i in range(len(small_bp_list)):
    #     find_pair_point(ax, small_bp_list[i], q0, q1)
    return "F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-4(b).jpg"

if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # path = draw_a(fig, ax)
    path = draw_b(fig, ax)

    # ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize)
    ax.set_ylabel('y/m', fontsize=m_fontsize)
    ax.set_zlabel('z/m', fontsize=m_fontsize)
    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0.1, 0.34, 0.1))
    ax.set_zlim(0.1, 0.35)
    ax.view_init(elev=20, azim=20)  # 调整视角
    plt.savefig(path, dpi=300)
    plt.show()

    cut()

