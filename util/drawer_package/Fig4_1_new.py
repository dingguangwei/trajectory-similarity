# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

m_fontsize = 17


def plot_line_with_points(point_array, color='0', linewidth=1., label=None, marker=None, linestyle=None):
    plt.plot(point_array[:, 0], point_array[:, 1], color=color, linewidth=linewidth, label=label, marker=marker, linestyle=linestyle)


def get_QRS(is_less=True, is_print=True):
    if is_less:
        Q = np.array([[1, 1, 0], [3, 1, 2], [5, 1, 4], [18, 1, 17]])
        R = np.array([[1, 2, 0], [3, 2, 2], [5, 2, 4], [18, 3, 17]])
        S = np.array([[1, 3, 0], [3, 2.5, 2], [5, 2, 4], [18, 2, 17]])
    else:
        Q = np.ones(shape=(18, 3))
        Q[:, 0] = np.arange(1, 19, 1)
        Q[:, 2] = Q[:, 0]-1
        # print(Q)

        R = np.zeros(shape=(18, 3))
        R[:, 0] = np.arange(1, 19, 1)
        R[0:4, 1] = [2 for i in range(4)]
        for i in np.arange(4, len(R), 1):
            R[i, 1] = (R[i, 0] - 5) / 13 + 2
        R[:, 2] = R[:, 0] - 1
        # print(R)

        S = np.zeros(shape=(18, 3))
        S[:, 0] = np.arange(1, 19, 1)
        for i in np.arange(0, 5, 1):
            S[i, 1] = -(S[i, 0] - 1) / 4 + 3
        S[5:, 1] = [2 for i in range(13)]
        S[:, 2] = S[:, 0] - 1

    if is_print:
        print('Q=\n', Q)
        print('R=\n', R)
        print('S=\n', S)
    return Q, R, S


def draw_DTW_less_point():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16

    Q, R, S = get_QRS()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')
    ax.plot(S[:, 0], S[:, 1], S[:, 2], label='S', linestyle='-', linewidth=2, color='0.6', marker='|')

    for i in range(len(Q)):
        ax.text(Q[i,0], Q[i, 1], Q[i, 2], '$q_'+str(i)+'$', fontsize=m_fontsize, color='0.')
        ax.text(R[i,0], R[i, 1]-0.1, R[i, 2], '$r_'+str(i)+'$', fontsize=m_fontsize, color='0.4')
        ax.text(S[i,0], S[i, 1]+0.5, S[i, 2], '$s_'+str(i)+'$', fontsize=m_fontsize, color='0.6')
        ax.plot([Q[i,0], R[i,0]], [Q[i,1], R[i,1]], [Q[i,2], R[i,2]], linestyle='--', linewidth=1, color='0')
        ax.plot([Q[i, 0], S[i, 0]], [Q[i, 1], S[i, 1]], [Q[i, 2], S[i, 2]], linestyle='--', linewidth=1, color='0.5')

    ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize)
    ax.set_ylabel('y/m', fontsize=m_fontsize)
    ax.set_zlabel('z/m', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    # ax.set_yticks([])
    ax.set_zticks(np.arange(5, 16, 10))
    # plt.xlim(0, 2)
    plt.ylim(0, 5)
    ax.set_zlim(0, 20)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    ax.view_init(elev=20, azim=170)  # 调整视角
    plt.show()


def draw_DTW_more_point():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16

    Q, R, S = get_QRS(is_less=False)
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='black', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.4', marker='*')
    ax.plot(S[:, 0], S[:, 1], S[:, 2], label='S', linestyle='-', linewidth=2, color='0.6', marker='|')

    m_list = [0, 2, 4, 7, 10, 13, 17]
    for i in m_list:
        ax.text(Q[i, 0], Q[i, 1], Q[i, 2], '$q_{' + str(i) + '}$', fontsize=m_fontsize, color='0.')

    for i in m_list:
        if i<5:
            R_bias = -0.1
        else:
            R_bias = 0.5
        ax.text(R[i, 0], R[i, 1] +R_bias, R[i, 2], '$r_{' + str(i) + '}$', fontsize=m_fontsize, color='0.4')
    for i in m_list:
        if i<5:
            S_bias = 0.5
        else:
            S_bias = -0.1
        ax.text(S[i, 0], S[i, 1] + S_bias, S[i, 2], '$s_{' + str(i) + '}$', fontsize=m_fontsize, color='0.6')

    for i in range(len(Q)):
        ax.plot([Q[i,0], R[i,0]], [Q[i,1], R[i,1]], [Q[i,2], R[i,2]], linestyle='--', linewidth=1, color='0')
        ax.plot([Q[i, 0], S[i, 0]], [Q[i, 1], S[i, 1]], [Q[i, 2], S[i, 2]], linestyle='--', linewidth=1, color='0.5')

    ax.legend()  # 显示图例
    ax.set_xlabel('x/m', fontsize=m_fontsize)
    ax.set_ylabel('y/m', fontsize=m_fontsize)
    ax.set_zlabel('z/m', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    # ax.set_yticks([])
    ax.set_zticks(np.arange(5, 16, 10))
    # plt.xlim(0, 2)
    plt.ylim(0, 5)
    ax.set_zlim(0, 20)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    ax.view_init(elev=20, azim=170)  # 调整视角
    plt.show()



if __name__=='__main__':
    # draw_DTW_less_point()
    draw_DTW_more_point()