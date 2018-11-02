# coding=utf-8
import numpy as np
from util.algorithm.util import get_EU_distance, get_BDS_point_and_distance

"""
输入：轨迹段的两个端点，以及断点参数eta
输出：[左端点，断点1，断点2，... 右端点]，以及对应权重
"""
def get_break_point(v1, v2, eta=1):
    break_point_list = []
    weight_list = []

    # 当二者时序相等，说明输入错误，因为轨迹中不可能出现时间戳相等的两个点
    if v1[2]==v2[2]:
        print('[ERROR] get_break_point: get v1 and v1 with the same z value, v1=', v1, ' v2=', v2, '\n')
        return break_point_list, weight_list

    k_x = (v2[0]-v1[0])/(v2[2]-v1[2])
    k_y = (v2[1]-v1[1])/(v2[2]-v1[2])
    theta_z = np.arctan(np.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)/(v1[2]-v2[2]))  # 向量v1v2与z轴夹角
    delta_z = eta*np.cos(theta_z)

    break_point_list.append(v1)
    weight_list.append(0.5)
    z = v1[2]+delta_z
    while z < v2[2]:
        x = k_x*(z-v1[2])+v1[0]
        y = k_y*(z-v1[2])+v1[1]
        weight_list.append(1.)
        break_point_list.append([x, y, z])
        z = z+delta_z

    if len(weight_list)>=2:
        # 至少有一个断点
        last_break_point_to_v2_distance = get_EU_distance(break_point_list[-1], v2)
        weight_list[-1] = 0.5*(1+last_break_point_to_v2_distance/eta)
        break_point_list.append(v2)
        weight_list.append(0.5*last_break_point_to_v2_distance/eta)
    else:
        # 一个断点都没有
        v1_to_v2_distance = get_EU_distance(v1, v2)
        weight_list[-1] = 0.5 * v1_to_v2_distance / eta
        break_point_list.append(v2)
        weight_list.append(weight_list[0])

    return break_point_list, weight_list


"""
输入：数据轨迹段的端点r1、r2，以及对应查询轨迹段（起点为r1的BDS对应点，终点为r2的BDS对应点）
输出：r1r2到Q的时空距离
"""
def get_space_time_distance_by_segment(r1, r2, Q, eta):
    if len(Q)==0:
        print('[ERROR] get_space_time_distance_by_segment: Q.length is 0。r1=', r1, ' r2=', r2)
    break_point_list, weight_list = get_break_point(r1, r2, eta=eta)
    # 先计算端点距离
    d_space = weight_list[0]*get_EU_distance(r1, Q[0])+weight_list[-1]*get_EU_distance(r2, Q[-1])
    break_point_pair_point = [[r1, Q[0]]]
    for i in range(1, len(break_point_list)-1):
        BDS_point, distance = get_BDS_point_and_distance(break_point_list[i], Q)
        break_point_pair_point.append([break_point_list[i], BDS_point])
        d_space += weight_list[i]*distance
    break_point_pair_point.append([r2, Q[-1]])
    return d_space, break_point_pair_point


"""
输入：轨迹Q，R，DTW-BDS对应点对pair，断点距离阈值eta
输出：R上轨迹段到对应段的距离，以及断点与对应点
"""
def space_distance_calculate(new_Q, R, DTW_BDS_pair_index, eta):
    d_space_Traj = []
    break_point_pair_point = []
    for i in range(len(R) - 1):
        start_index = DTW_BDS_pair_index[i][1]
        end_index = DTW_BDS_pair_index[i + 1][1] + 1
        res = get_space_time_distance_by_segment(R[i], R[i + 1], new_Q[start_index:end_index], eta=eta)
        d_space_Traj.append(res[0])
        break_point_pair_point.append(res[1])
    return d_space_Traj, break_point_pair_point


if __name__=='__main__':
    v1 = [0, 0, 0]
    v2 = [3, 3, 3]
    break_point_list, weight_list = get_break_point(v1, v2, np.sqrt(3))
    print(break_point_list)
    print(weight_list)
