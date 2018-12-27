# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# 给出一个点，和一条轨迹段的起止点，得到对应点
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

# 给定一个点，和一条轨迹，得到最短对应点，并画出来
# （没考虑时间递进的关系）
def find_pair_point_in_Traj(v, T, label=None, color='0.4', linestyle='--'):
    min_point, min_distance = [[1000, 1000], 1000000]
    for i in range(len(T)-1):
        temp_point, temp_distance = find_pair_point(v, T[i], T[i+1])
        if temp_distance<min_distance:
            min_distance = temp_distance
            min_point = temp_point
    plt.plot([v[0], min_point[0]], [v[1], min_point[1]], linestyle=linestyle, linewidth=2, color=color)


def get_data():
    Q = [
        [1, 1],
        [1.5, 1.5],
        [2, 2],
        [2.5, 2.5],
        [3, 3],
        [5, 3],
        [7, 3],
    ]
    R = [
        [0.8, 1.8],
        [2, 3],
        [3, 4],
        [4, 4],
        [5, 4],
        [6, 4],
        [7, 4],
    ]
    return np.array(Q), np.array(R)


def draw_line( v1, v2, color='0.4', linewidth=1.):
    plt.plot([v1[0], v2[0]], [v1[1], v2[1]], linestyle='-.', linewidth=linewidth, color=color)


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 20

    Q, R = get_data()
    plt.plot(Q[:, 0], Q[:, 1], color='black', linewidth=2, label='Q', marker='H', linestyle='-')
    plt.plot(R[:, 0], R[:, 1], color='0.6', linewidth=2, label='R', marker='*', linestyle=None)

    for i in range(len(Q)):
        plt.text(Q[i][0] - 0.2, Q[i][1] - 0.5, 'q'+str(i), fontsize=m_fontsize, color='black')
    for i in range(len(R)):
        plt.text(R[i][0] - 0.3, R[i][1] + 0.3, 'r'+str(i), fontsize=m_fontsize, color='0.4')

    for i in range(len(Q)):
        find_pair_point_in_Traj(Q[i], R)
    for i in range(len(R)):
        find_pair_point_in_Traj(R[i], Q)

    ax = plt.gca()
    # 将底部的线移到y=0的地方
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks(np.arange(0, 10, 1), np.arange(0, 100, 10), fontsize=m_fontsize)
    plt.yticks(np.arange(0, 10, 1), np.arange(0, 100, 10), fontsize=m_fontsize)
    plt.xlim(0, 8)
    plt.ylim(0, 7)
    plt.xlabel('x/m', fontsize=m_fontsize)
    plt.ylabel('y/m', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.95, bottom=0.15, right=0.97, left=0.12, hspace=0, wspace=0)
    plt.savefig('F:/毕业设计大文件夹/picture/chapter2/2-12.jpg')
    plt.show()