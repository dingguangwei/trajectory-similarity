# coding=utf-8
import numpy as np
from util.algorithm.DTW_BDS_pair import get_DTW_BDS_pair_by_traj
from util.algorithm.space_calculate import space_distance_calculate
from util.algorithm.shape_calculate import I_shape_calculate
from util.algorithm.similarity_calculate import similar_segment_and_distance
# from util.print_log import print_rat

# 根据traj_distance_list的大小将index排序
def quick_sort(value_list, index_list, m_start, m_end):
    if m_start>=m_end:
        return
    i, j = m_start, m_end
    mid_value = value_list[i]
    mid_index = index_list[i]
    while i<j:
        while i<j and value_list[j]>=mid_value:
            j-=1
        if i<j and value_list[j]<mid_value:
            value_list[i] = value_list[j]
            index_list[i] = index_list[j]
        while i<j and value_list[i]<=mid_value:
            i+=1
        if i<j and value_list[i]>mid_value:
            value_list[j] = value_list[i]
            index_list[j] = index_list[i]
    value_list[i] = mid_value
    index_list[i] = mid_index
    quick_sort(value_list, index_list, m_start, i-1)
    quick_sort(value_list, index_list, i+1, m_end)


def top_k_similar_query(Q, R_list, k=None, eta=0.2, mu = 0, epsilon = 0.1):
    traj_distance_list = []

    for i in range(len(R_list)):
        print(i, ':')
        R = R_list[i]
        DTW_BDS_pair, new_Q, DTW_BDS_pair_index = get_DTW_BDS_pair_by_traj(Q, R)
        # print('DTW_BDS_pair_index:', DTW_BDS_pair_index, '\n')
        d_space_Traj, break_point_pair_point = space_distance_calculate(new_Q=new_Q, R=R, DTW_BDS_pair_index=DTW_BDS_pair_index, eta=eta)
        # print('d_space_Traj=', d_space_Traj, '\n')
        I_shape_Traj = I_shape_calculate(new_Q=new_Q, R=R, DTW_BDS_pair_index=DTW_BDS_pair_index, mu=mu)
        d_segment_list = np.multiply(I_shape_Traj, d_space_Traj)
        # print('I_shape_Traj=', I_shape_Traj, '\n')

        R_start_index, R_end_index, R_Q_min_distance = similar_segment_and_distance(Q, R, d_segment_list, epsilon=epsilon)
        print('R_start_index, R_end_index, R_Q_min_distance=', R_start_index, R_end_index, R_Q_min_distance, '\n-------------------')

        if not R_Q_min_distance is float('inf'):
            traj_distance_list.append(R_Q_min_distance)
        else:
            traj_distance_list.append(99999999)

    # 将最后的距离进行排序，index表示该距离所在轨迹的索引
    index_list = [i for i in range(len(traj_distance_list)-1)]
    quick_sort(traj_distance_list, index_list, 0, len(index_list)-1)
    return traj_distance_list, index_list