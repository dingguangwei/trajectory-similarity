# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


def find_pair_point(v, start, end, label=None):
    x = v[0]
    min_point = [start[0],start[1]]
    min_distance = 10000
    for x in np.arange(min(start[0], end[0]), max(start[0], end[0]), 0.001):
        y = (end[1]-start[1])/(end[0]-start[0])*(x-start[0])+start[1]
        if (v[0]-x)**2+(v[1]-y)**2 < min_distance**2:
            min_distance = np.sqrt((v[0]-x)**2+(v[1]-y)**2)
            min_point = [x, y]
    return min_point, min_distance

def find_pair_point_in_Traj(v, T, label=None, color='green', linestyle='--'):
    min_point, min_distance = [[1000, 1000], 1000000]
    for i in range(len(T)-1):
        temp_point, temp_distance = find_pair_point(v, T[i], T[i+1])
        if temp_distance<min_distance:
            min_distance = temp_distance
            min_point = temp_point
    plt.plot([v[0], min_point[0]], [v[1], min_point[1]], linestyle=linestyle, linewidth=1, color=color)


def get_y(x, start, end):
    y = (x-start[0])*(end[1]-start[1])/(end[0]-start[0])+start[1]
    return y

def get_data():
    Q = [[0.8, 0.9],
         [1.8, get_y(1.8, [0.8, 0.9], [2.6, 1.9])],
         [2.6, 1.9],
         [3.4, get_y(3.4, [2.6, 1.9], [5.6, 0.9])],
         [3.9, get_y(3.9, [2.6, 1.9], [5.6, 0.9])],
         [4.4, get_y(4.4, [2.6, 1.9], [5.6, 0.9])],
         [5.6, 0.9],
         [7.1, 2.8],
         ]
    R = [[0.4, 1.9],
         [2.3, 2.8],
         [4.5, get_y(4.5, [2.3, 2.8],[5.4, 1.8])],
         [5.4, 1.8],
         [5.6, get_y(5.6, [5.4, 1.8],[6.7, 3.6])],
         [5.9, get_y(5.9, [5.4, 1.8],[6.7, 3.6])],
         [6.3, get_y(6.3, [5.4, 1.8],[6.7, 3.6])],
         [6.7, 3.6]]
    return np.array(Q), np.array(R)

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    Q, R = get_data()
    plt.plot(Q[:, 0], Q[:, 1], color='black', linewidth=2, label='Q', marker='H', linestyle=None)
    plt.plot(R[:, 0], R[:, 1], color='0.5', linewidth=2, label='R', marker='*', linestyle=None)

    for i in range(len(Q)):
        plt.text(Q[i][0] + 0.2, Q[i][1], 'q'+str(i), fontsize=m_fontsize, color='black')
    for i in range(len(R)):
        plt.text(R[i][0] + 0.2, R[i][1], 'r'+str(i), fontsize=m_fontsize, color='0.5')

    # 下面只允许运行一段：
    # for i in range(len(Q)):
    #     plt.plot([Q[i,0], R[i, 0]], [Q[i, 1], R[i, 1]], color='green', linewidth=1.0, linestyle='--')

    for i in range(len(Q)):
        find_pair_point_in_Traj(Q[i], R)
    for i in range(len(R)):
        find_pair_point_in_Traj(R[i], Q, color='red', linestyle='-.')


    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 10, 1), np.arange(0, 100, 10), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 5, 1), np.arange(0, 50, 10), fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(-2, 2)
    plt.xlabel('x/m', fontsize=m_fontsize)
    plt.ylabel('y/m', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.95, bottom=0.15, right=0.97, left=0.12, hspace=0, wspace=0)
    plt.savefig("F:\\毕业设计大文件夹\\picture\\chapter\\3-4.jpg", dpi=300)
    plt.show()