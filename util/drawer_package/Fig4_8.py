# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D

m_fontsize = 16
def plot(point_arr, ax, label=None, linestyle='-', linewidth=1, color='0', marker=None):
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


def get_R_and_Q(s='a'):
    # 对应点情况一
    # R = [
    #     [0.1, 0.2, 0.2],
    #     [0.1, 0.4, 0.3]
    # ]
    # Q = [
    #     [0.4, 0.2, 0.1],
    #     [0.3, 0.3, 0.25],
    #     [0.4, 0.4, 0.4]
    # ]

    # 对应点情况二
    # R = [
    #     [0.1, 0.3, 0.2],
    #     [0.15, 0.4, 0.3]
    # ]
    # Q = [
    #     [0.3, 0.2, 0.1],
    #     [0.4, 0.4, 0.4]
    # ]

    #对应轨迹段情况一
    if s=='a':
        R = [[0.4, 0.3, 0.2],
             [0.6, 0.28, 0.3],
             [0.7, 0.3, 0.4]]
        Q = [[0.3, 0.2, 0.2],
             [0.8, 0.2, 0.3]]
        return np.array(R), np.array(Q)

    # 对应点轨迹段情况二
    elif s=='b':
        R=[[0.1, 0.2, 0.2],
            [0.1, 0.4, 0.3],
            [0.2, 0.5, 0.4]
        ]
        Q=[
            [0.4, 0.2, 0.1],
            [0.3, 0.3, 0.25],
            [0.4, 0.4, 0.4]
        ]
        return np.array(R), np.array(Q)

    # 对应轨迹段情况三
    else:
        R = [
            [0.2, 0.1, 0.1],
            [0.21, 0.5, 0.4]
        ]
        Q = [
            [0.4, 0.2, 0.1],
            [0.3, 0.25, 0.2],
            [0.3, 0.32, 0.3],
            [0.4, 0.4, 0.4]
        ]
        return np.array(R), np.array(Q)


def draw():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    R, Q = get_R_and_Q('c')

    # 画出轨迹R和Q
    plot(Q, ax, label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    plot(R, ax, label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # 为轨迹样本点进行标注
    for i in range(len(R)):
        m_label = r'$r_' + str(i) + '$'
        ax.text(R[i][0] - 0.03, R[i][1] - 0.01, R[i][2] + 0.02, m_label, fontsize=m_fontsize, color='0.4')
    for i in range(len(Q)):
        m_label = r'$q_' + str(i) + '$'
        ax.text(Q[i][0] + 0.01, Q[i][1], Q[i][2] + 0.005, m_label, fontsize=m_fontsize, color='black')

    ################################################################################################
    # 寻找对应点
    ################################################################################################
    # 寻找R0对应点
    min_point = find_pair_point(ax=ax, r=R[0], qi=Q[0], qj=Q[1])
    ax.scatter(min_point[0], min_point[1], min_point[2], marker='*', linewidths=2., color='0.4')
    ax.text(min_point[0]+0.01, min_point[1], min_point[2] + 0.01, r'$Q(r_0)$', fontsize=m_fontsize, color='0.4')

    # 寻找R1对应点
    min_point = find_pair_point(ax=ax, r=R[1], qi=Q[2], qj=Q[3])
    ax.scatter(min_point[0], min_point[1], min_point[2], marker='*', linewidths=2., color='0.4')
    ax.text(min_point[0]+0.01, min_point[1], min_point[2] - 0.01, r'$Q(r_1)$', fontsize=m_fontsize, color='0.4')

    # 寻找q1对应点
    min_point = find_pair_point(ax=ax, r=Q[1], qi=R[0], qj=R[1])
    ax.scatter(min_point[0], min_point[1], min_point[2], marker='*', linewidths=2., color='0.4')
    ax.text(min_point[0] - 0.06, min_point[1], min_point[2] - 0.01, r'$R(q_1)$', fontsize=m_fontsize, color='0.4')

    # 寻找q2对应点
    min_point = find_pair_point(ax=ax, r=Q[2], qi=R[0], qj=R[1])
    ax.scatter(min_point[0], min_point[1], min_point[2], marker='*', linewidths=2., color='0.4')
    ax.text(min_point[0] - 0.06, min_point[1], min_point[2] - 0.01, r'$R(q_2)$', fontsize=m_fontsize, color='0.4')


    ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize-3)
    ax.set_ylabel('y/m', fontsize=m_fontsize-3)
    ax.set_zlabel('z/m', fontsize=m_fontsize-3)

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks(np.arange(0.2, 0.5, 0.1))
    ax.view_init(elev=20, azim=240)  # 调整视角
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter4\\Fig4-8.jpg", dpi=500)
    plt.show()

if __name__=='__main__':
    draw()

    # 裁剪
    print('裁剪中...')
    path = "F:\\毕业设计大文件夹\\picture\\chapter4\\"
    m_files = ['Fig4-8.jpg']
    for m_file in m_files:
        img = Image.open(path + m_file)  # 打开当前路径图像
        # print(img.size)
        # 左，上，右，下
        box1 = (530, 230, 2900, 2150)  # 设置图像裁剪区域
        image1 = img.crop(box1)  # 图像裁剪
        # image1.show()
        # print(image1.size)
        image1.save(path + 'cut_' + m_file)  # 存储当前区域
        print('path = ', path + 'cut_' + m_file)


