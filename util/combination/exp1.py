# coding=utf-8
from util.algorithm.DTW_BDS_pair import get_DTW_BDS_pair_by_traj, get_pair_index_in_DTW
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from util.algorithm.space_calculate import get_space_time_distance_by_segment
from util.algorithm.shape_calculate import get_I_shape
from util.algorithm.similarity_calculate import similar_segment_and_distance
from util.drawer_package import d902_BDS_weakness_draw


def get_data():
    Q = [
        [2.6, 1, 3],
        [3, 2, 4],
        [6, 4, 6.5],
        [8, 3, 8.5],
        [12, 3, 9.5]
    ]

    R = [
        [0, 4, 1],
        [1, 4, 2],
        [2, 4.5, 3],
        [3, 5, 4],
        [4, 4, 5],
        [5, 5, 6],
        [6, 5, 7],
        [8, 4, 8],
        [10, 4, 9],
        [11, 4.4, 10],
        [12, 3.7, 11]
    ]
    return np.array(Q), np.array(R)


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16
    # 1、数据
    # Q, R = get_data()
    Q, R, S = d902_BDS_weakness_draw.get_data()
    print('Q=\n', Q, '\n')
    print('R=\n', R, '\n')
    # 2、画轨迹
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2], label='Q', linestyle='-', linewidth=2, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R', linestyle='-', linewidth=2, color='0.3', marker='H')
    eta = 0.2
    epsilon=0.1

    # 获取DTW_pair
    # DTW_QR_pair = get_pair_index_in_DTW(Q, R)
    # for i in range(len(DTW_QR_pair)):
    #     v1 = Q[DTW_QR_pair[i, 0]]
    #     v2 = R[DTW_QR_pair[i, 1]]
    #     ax.plot([v1[0], v2[0]],[v1[1], v2[1]],[v1[2], v2[2]], linestyle='--', linewidth=1.5, color='green')

    # 3、获取DTW_BDS_pair
    DTW_BDS_pair, new_Q, DTW_BDS_pair_index = get_DTW_BDS_pair_by_traj(Q, R)
    for pair in DTW_BDS_pair:
        v1 = R[pair[0]]
        v2 = pair[1]
        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], linestyle='--', linewidth=1.5, color='green')

    # 4、创建包含对应点的Q的索引

    # 5、计算时空距离
    d_space_Traj = []
    break_point_pair_point = []
    for i in range(len(R)-1):
        start_index = DTW_BDS_pair_index[i][1]
        end_index = DTW_BDS_pair_index[i+1][1]+1
        res = get_space_time_distance_by_segment(R[i], R[i+1], new_Q[start_index:end_index], eta=eta)
        d_space_Traj.append(res[0])
        break_point_pair_point.append(res[1])

    # 5.2、画出断点的对应点
    print('d_space_Traj=', d_space_Traj)
    for break_pairs in break_point_pair_point:
        for i in range(1, len(break_pairs)-1):
            v1 = break_pairs[i][0]
            v2 = break_pairs[i][1]
            ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], linestyle='-', linewidth=1., color='0.65')

    # 6、获取轨迹形状相似性
    I_shape_Traj = []
    for i in range(len(R)-1):
        start_index = DTW_BDS_pair_index[i][1]
        end_index = DTW_BDS_pair_index[i + 1][1]+1
        q_pre, q_next = None, None
        if start_index+1==end_index:
            if start_index>0:
                q_pre = Q[start_index-1]
            if end_index<len(new_Q)-1:
                q_next = Q[end_index+1]
        I_shape = get_I_shape(R[i], R[i+1], new_Q[start_index:end_index], mu=6, q_pre=q_pre, q_next=q_next)
        I_shape_Traj.append(I_shape)
    print('I_shape_Traj=', I_shape_Traj,'\n')

    d_segment_list = np.multiply(I_shape_Traj, d_space_Traj)
    print('d_segment_list=', d_segment_list)

    ####################################################################################
    # 求得所有线段形状影响因子和空间距离后，求最长的相似轨迹段
    ####################################################################################
    res = similar_segment_and_distance(Q, R, d_segment_list, epsilon=epsilon)
    print('[R_start_index, R_end_index, R_Q_min_distance]=', res)

    ####################################################################################
    # 标序号
    # for i in range(len(Q)):
    #     ax.text(Q[i, 0] + 0.2, Q[i, 1], Q[i, 2] - 0.7, 'q' + str(i), color='blue', fontsize=m_fontsize)
    for i in range(len(new_Q)):
        ax.text(new_Q[i, 0] + 0.4, new_Q[i, 1], new_Q[i, 2] - 0.7, 'nq' + str(i), color='blue', fontsize=m_fontsize)
    for i in range(len(R)):
        ax.text(R[i, 0] + 0.2, R[i, 1], R[i, 2] - 0.7, 'r' + str(i), color='0.3', fontsize=m_fontsize)
    ####################################################################################
    # 坐标系
    ####################################################################################
    ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)
    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    # ax.set_zticks(np.arange(0, 10, 2))
    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    ax.set_zlim(0, 10)
    ax.view_init(elev=20, azim=200)  # 调整视角
    plt.show()
