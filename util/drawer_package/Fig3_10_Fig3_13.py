# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image
from d0_util_3d import find_pair_point_in_Traj_and_draw
from util.algorithm.DTW_BDS_pair import get_BDS_point_and_distance

################################################################################################
# --------------------------- util ---------------------------
################################################################################################
m_fontsize = 14
small_fontsize = 11

def get_data():
    Q = [
        [4, 1, 1],
        [4, 4, 4],
        [3, 7.5, 7.5],
        [5.4, 7.5, 8.5]
    ]
    R = [
        [5, 1.5, 1.5],
        [5, 3, 3],
        [5, 4.5, 5],
        [5, 6, 5.5],
        [5, 8, 7],
        [2.5, 8, 8]
    ]
    return np.array(Q), np.array(R)


def draw_line(ax, v1, v2, color='0.5', linewidth=1.):
    ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], linestyle='-.', linewidth=linewidth, color=color)


def get_EU_distance(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    d = np.sqrt(np.sum((v1 - v2) ** 2))
    return d


def get_pair_index_in_DTW(Q, R):
    m = len(Q)
    n = len(R)

    arr = np.zeros(shape=(m + 1, n + 1), dtype=float)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                arr[i, j] = 0
            elif i == 0 or j == 0:
                arr[i, j] = float("inf")
            else:
                d1 = get_EU_distance(Q[i - 1], R[j - 1])
                d2 = min(arr[i - 1, j], arr[i, j - 1], arr[i - 1, j - 1])
                arr[i, j] = d1 + d2
    pair = []
    i, j = m, n
    while i > 0 and j > 0:
        pair.append([i - 1, j - 1])
        post_i, post_j, post_value = i - 1, j - 1, arr[i - 1, j - 1]
        if post_value > arr[i, j - 1]:
            post_i, post_j, post_value = i, j - 1, arr[i, j - 1]
        if post_value > arr[i - 1, j]:
            post_i, post_j, post_value = i - 1, j, arr[i - 1, j]
        i, j = post_i, post_j
    pair.reverse()
    pair = np.array(pair)
    # print("DTW_pair_index=\n", pair, "\n")
    return pair


################################################################################################
# --------------------------- 画图 ---------------------------
################################################################################################


def draw_2d():
    fig = plt.figure()
    Q, R = get_data()
    plt.plot(Q[:, 0], Q[:, 1], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    plt.plot(R[:, 0], R[:, 1], label='R', linestyle='-', linewidth=2, color='.4', marker='*')
    for i in range(len(Q)):
        plt.text(Q[i, 0]+0.2, Q[i, 1]-0.3, '$q_'+str(i)+'$', color='black', fontsize=m_fontsize+4)
    for i in range(len(R)):
        plt.text(R[i, 0] + 0.1, R[i, 1] - 0.4, '$r_' + str(i) + '$', color='.4', fontsize=m_fontsize+4)

    ax = plt.gca()
    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 10, 1), np.arange(0, 100, 10), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 10, 1), np.arange(0, 100, 10), fontsize=m_fontsize)
    plt.xlim(0, 9)
    # plt.ylim(-2, 2)
    plt.xlabel('x/m', fontsize=m_fontsize)
    plt.ylabel('y/m', fontsize=m_fontsize)
    plt.savefig('F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\0-2d.jpg', dpi=500)
    plt.show()


def draw_0(fig, ax):
    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')
    return "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\0.jpg"


def draw_1(fig, ax):
    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # 获取DTW对应点
    DTW_pair = get_pair_index_in_DTW(Q=R, R=Q)
    print(DTW_pair)
    for pair in DTW_pair:
        draw_line(ax, Q[pair[1]], R[pair[0]])

    for i in range(0, len(Q)-1):
        ax.text(Q[i, 0] - 0.7, Q[i, 1]+1, Q[i, 2]-0.8, r'$q_{'+str(i)+'}$', color='black', fontsize=m_fontsize)
    ax.text(Q[-1, 0] + 0.2, Q[-1, 1] , Q[-1, 2] + 0.2, r'$q_{' + str(3) + '}$', color='black', fontsize=m_fontsize)
    for i in range(len(R)-1):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2]+0., r'$r_{' + str(i) + '}$', color='0.4', fontsize=m_fontsize)
    ax.text(R[-1, 0] + 0.2, R[-1, 1], R[-1, 2] + 0., r'$r_{' + str(5) + '}$', color='0.4', fontsize=m_fontsize)
    return "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\1.jpg"

# 寻找r0的对应点
def draw_2(fig, ax):
    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # 获取DTW对应点
    DTW_pair = get_pair_index_in_DTW(Q=R, R=Q)
    print(DTW_pair)
    for i in range(1, len(DTW_pair)):
        pair = DTW_pair[i]
        draw_line(ax, Q[pair[1]], R[pair[0]])

    for i in range(0, len(Q) - 1):
        ax.text(Q[i, 0] - 0.7, Q[i, 1] + 1, Q[i, 2] - 0.8, r'$q_{' + str(i) + '}$', color='black', fontsize=m_fontsize)
    ax.text(Q[-1, 0] + 0.2, Q[-1, 1], Q[-1, 2] + 0.2, r'$q_{' + str(3) + '}$', color='black', fontsize=m_fontsize)
    for i in range(len(R) - 1):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] + 0., r'$r_{' + str(i) + '}$', color='0.4', fontsize=m_fontsize)
    ax.text(R[-1, 0] + 0.2, R[-1, 1], R[-1, 2] + 0., r'$r_{' + str(5) + '}$', color='0.4', fontsize=m_fontsize)

    ###################################################################################################################
    # 寻找r0的对应点
    ###################################################################################################################
    min_point = find_pair_point_in_Traj_and_draw(R[0], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] - 2.6, min_point[1]-0.5, min_point[2], r'$DTW-BDS(r_0)$', color='0.1', fontsize=small_fontsize)
    return "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\2.jpg"

# 寻找r0,r1,r2的对应点
def draw_3(fig, ax):
    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # 获取DTW对应点
    DTW_pair = get_pair_index_in_DTW(Q=R, R=Q)
    print(DTW_pair)
    for i in range(1, len(DTW_pair)):
        pair = DTW_pair[i]
        draw_line(ax, Q[pair[1]], R[pair[0]])

    for i in range(0, len(Q) - 1):
        ax.text(Q[i, 0] - 0.7, Q[i, 1] + 1, Q[i, 2] - 0.8, r'$q_{' + str(i) + '}$', color='black', fontsize=m_fontsize)
    ax.text(Q[-1, 0] + 0.2, Q[-1, 1], Q[-1, 2] + 0.2, r'$q_{' + str(3) + '}$', color='black', fontsize=m_fontsize)
    for i in range(len(R) - 1):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] + 0., r'$r_{' + str(i) + '}$', color='0.4', fontsize=m_fontsize)
    ax.text(R[-1, 0] + 0.2, R[-1, 1], R[-1, 2] + 0., r'$r_{' + str(5) + '}$', color='0.4', fontsize=m_fontsize)

    ###################################################################################################################
    # 寻找r0,r1,r2的对应点
    ###################################################################################################################
    b_x, b_y, b_z = -2.6, -0.5, 0
    min_point = find_pair_point_in_Traj_and_draw(R[0], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] +b_x, min_point[1]+b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[1], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] +b_x, min_point[1]+b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[2], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] +b_x-0.6, min_point[1]+b_y, min_point[2], r'$DTW-BDS(r_2)$', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[3], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] +b_x, min_point[1]+b_y, min_point[2], r'$DTW-BDS(r_3)$', color='0.1', fontsize=small_fontsize)
    return "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\3.jpg"


# 优化r2的对应点
def draw_4(fig, ax):
    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # 获取DTW对应点
    DTW_pair = get_pair_index_in_DTW(Q=R, R=Q)
    print(DTW_pair)
    for i in range(1, len(DTW_pair)):
        pair = DTW_pair[i]
        draw_line(ax, Q[pair[1]], R[pair[0]])

    for i in range(0, len(Q) - 1):
        ax.text(Q[i, 0] - 0.7, Q[i, 1] + 1, Q[i, 2] - 0.8, r'$q_{' + str(i) + '}$', color='black', fontsize=m_fontsize)
    ax.text(Q[-1, 0] + 0.2, Q[-1, 1], Q[-1, 2] + 0.2, r'$q_{' + str(3) + '}$', color='black', fontsize=m_fontsize)
    for i in range(len(R) - 1):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] + 0., r'$r_{' + str(i) + '}$', color='0.4', fontsize=m_fontsize)
    ax.text(R[-1, 0] + 0.2, R[-1, 1], R[-1, 2] + 0., r'$r_{' + str(5) + '}$', color='0.4', fontsize=m_fontsize)

    ###################################################################################################################
    # 优化r2的对应点
    ###################################################################################################################
    b_x, b_y, b_z = -2.6, -0.5, 0
    min_point = find_pair_point_in_Traj_and_draw(R[0], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[1], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[2], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'$DTW-BDS(r_2)$', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[3], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'$DTW-BDS(r_3)$', color='0.1', fontsize=small_fontsize)
    return "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\4.jpg"


# 全部对应点
def draw_5(fig, ax):
    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # 获取DTW对应点
    # DTW_pair = get_pair_index_in_DTW(Q=R, R=Q)
    # print(DTW_pair)
    # for i in range(1, len(DTW_pair)):
    #     pair = DTW_pair[i]
    #     draw_line(ax, Q[pair[1]], R[pair[0]])

    for i in range(0, len(Q) - 1):
        ax.text(Q[i, 0] - 0.7, Q[i, 1] + 1, Q[i, 2] - 0.8, r'$q_{' + str(i) + '}$', color='black', fontsize=m_fontsize)
    ax.text(Q[-1, 0] + 0.2, Q[-1, 1], Q[-1, 2] + 0.2, r'$q_{' + str(3) + '}$', color='black', fontsize=m_fontsize)
    for i in range(len(R) - 1):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] + 0., r'$r_{' + str(i) + '}$', color='0.4', fontsize=m_fontsize)
    ax.text(R[-1, 0] + 0.2, R[-1, 1], R[-1, 2] + 0., r'$r_{' + str(5) + '}$', color='0.4', fontsize=m_fontsize)

    ###################################################################################################################
    # 优化r2的对应点
    ###################################################################################################################
    b_x, b_y, b_z = -2.6, -0.5, 0
    min_point = find_pair_point_in_Traj_and_draw(R[0], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[1], [Q[0], Q[1]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[2], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[3], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] + b_x, min_point[1] + b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[4], [Q[1], Q[2]], color='0.1', ax=ax)
    ax.text(min_point[0] +b_x+0.1, min_point[1] +b_y-0.3, min_point[2]-0.7, r'', color='0.1', fontsize=small_fontsize)

    min_point = find_pair_point_in_Traj_and_draw(R[5], [Q[2], Q[3]], color='0.1', ax=ax)
    ax.text(min_point[0] +b_x-0.6, min_point[1] +b_y, min_point[2], r'', color='0.1', fontsize=small_fontsize)
    return "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\5.jpg"


# BDS
def draw_6(fig, ax):
    Q, R = get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')

    # 获取BDS对应点
    for i in range(len(R)):
        min_point, min_distance = get_BDS_point_and_distance(R[i], Q)
        draw_line(ax, R[i], min_point)


    for i in range(0, len(Q) - 1):
        ax.text(Q[i, 0] - 0.7, Q[i, 1] + 1, Q[i, 2] - 0.8, r'$q_{' + str(i) + '}$', color='black', fontsize=m_fontsize)
    ax.text(Q[-1, 0] + 0.2, Q[-1, 1], Q[-1, 2] + 0.2, r'$q_{' + str(3) + '}$', color='black', fontsize=m_fontsize)
    for i in range(len(R) - 1):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] + 0., r'$r_{' + str(i) + '}$', color='0.4', fontsize=m_fontsize)
    ax.text(R[-1, 0] + 0.2, R[-1, 1], R[-1, 2] + 0., r'$r_{' + str(5) + '}$', color='0.4', fontsize=m_fontsize)

    return "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\6.jpg"

if __name__=='__main__':
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    #
    # # path = draw_0(fig, ax)
    # # path = draw_1(fig, ax)
    # # path = draw_2(fig, ax)
    # #
    # # path = draw_3(fig, ax)
    # # path = draw_4(fig, ax)
    # #
    # # path = draw_5(fig, ax)
    # path = draw_6(fig, ax)
    #
    # # --------------------------------------左     下
    # ax.legend(loc='right', bbox_to_anchor=(0.95, 0.85),ncol=1)  # 显示图例
    #
    # ax.set_xlabel('x/m', fontsize=m_fontsize)
    # ax.set_ylabel('y/m', fontsize=m_fontsize)
    # ax.set_zlabel('z/m', fontsize=m_fontsize)
    # # 设置坐标轴刻度
    # ax.set_xticks([])
    # ax.set_yticks([])
    # ax.set_zticks(np.arange(0, 10, 2))
    # plt.xlim(1, 7)
    # # plt.ylim(0, 2)
    # ax.set_zlim(0, 10)
    # ax.view_init(elev=20, azim=270)  # 调整视角
    # plt.savefig(path, dpi=500)
    # plt.show()
    #
    # # 裁剪
    # print('裁剪中...')
    # path = "F:\\毕业设计大文件夹\\picture\\chapter\\Fig3-10\\"
    # m_files = ['0.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']
    # for m_file in m_files:
    #     img = Image.open(path + m_file)  # 打开当前路径图像
    #     # print(img.size)
    #     # 左，上，右，下
    #     box1 = (750, 400, 2800, 2200)  # 设置图像裁剪区域
    #     image1 = img.crop(box1)  # 图像裁剪
    #     # image1.show()
    #     # print(image1.size)
    #     image1.save(path + 'cut_' + m_file)  # 存储当前区域
    #     print('path = ', path + 'cut_' + m_file)

    #################################################
    # 画2d
    draw_2d()
