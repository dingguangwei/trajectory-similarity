# coding=utf-8
import numpy as np
import sys
# from util import get_EU_distance,
from util.algorithm.util import get_EU_distance, reverse_sigmoid, get_BDS_point_and_distance


# 输入：数据轨迹段端点r1、r2，以及对应轨迹段
#   1、Q.length=1。还需要输入Q的前一个点和后一个点，至少输入一个
def get_sim_shape_by_segment(r1, r2, Q, q_pre=None, q_next=None):
    if r1[2]==r2[2]:
        print('[ERROR] get_sim_shape_by_segment: r1与r2时间戳相同！！！待处理...')
        sys.exit(0)
    d_r1_r2 = get_EU_distance(r1, r2)
    sim_shape = 0
    if len(Q)==2:
        vector_a = np.array(r2)-np.array(r1)
        vector_b = np.array(Q[1])-np.array(Q[0])
        d1 = np.dot(vector_a, vector_b)/np.linalg.norm(vector_b)
        d2 = get_EU_distance(Q[0], Q[1])
        sim_shape = min(d1, d2)
        return sim_shape
    elif len(Q)==1:
        vector_a = np.array(r2) - np.array(r1)
        if not q_pre is None and not q_next is None:
            # 取前后两个方向的均值
            vector_pre = np.array(Q[0])-np.array(q_pre)
            vector_next = np.array(q_next)-np.array(Q[0])
            vector_pre = vector_pre/np.linalg.norm(vector_pre)
            vector_next = vector_next/np.linalg.norm(vector_next)
            vector_b = vector_pre+vector_next
        elif q_next is None:
            vector_b = np.array(Q[0])-np.array(q_pre)
        elif q_pre is None:
            vector_b = np.array(q_next) - np.array(Q[0])
        else:
            print('[ERROR] get_sim_shape_by_segment: r1、r2对应同一个点时，如果有pre点和next点，必须要输入')
            sys.exit()
        d1 = np.dot(vector_a, vector_b)/np.linalg.norm(vector_b)
        sim_shape = 0
        if d1<0:
            sim_shape = d1
        return sim_shape
    else:
        new_R = [r1]
        sim_shape=0
        # 轨迹Q中含有元轨迹数据中的样本点
        for i in range(1, len(Q)-1):
            res = get_BDS_point_and_distance(Q[i], [new_R[-1], r2])
            new_point = res[0]
            if new_point[2]>new_R[-1][2]:
                new_R.append(new_point)
        new_R.append(r2)
        for i in range(len(new_R)-1):
            sim_shape += get_sim_shape_by_segment(new_R[i], new_R[i+1], [Q[i], Q[i+1]])
        return sim_shape


# 获取形状影响因子
def get_I_shape(r1, r2, Q, mu, q_pre=None, q_next=None):
    sim_shape = get_sim_shape_by_segment(r1, r2, Q, q_pre=q_pre, q_next=q_next)
    return reverse_sigmoid(sim_shape, mu=mu)


"""
输入：轨迹Q，R，DTW-BDS对应点对pair，形状因素权重mu
输出：R上轨迹段到对应段的形状影响因子
"""
def I_shape_calculate(new_Q, R, DTW_BDS_pair_index, mu):
    I_shape_Traj = []
    for i in range(len(R) - 1):
        start_index = DTW_BDS_pair_index[i][1]
        end_index = DTW_BDS_pair_index[i + 1][1] + 1
        q_pre, q_next = None, None
        if start_index + 1 == end_index:
            if start_index > 0:
                q_pre = new_Q[start_index - 1]
            if end_index < len(new_Q) - 1:
                q_next = new_Q[end_index + 1]
        I_shape = get_I_shape(R[i], R[i + 1], new_Q[start_index:end_index], mu, q_pre=q_pre, q_next=q_next)
        I_shape_Traj.append(I_shape)
    return I_shape_Traj

if __name__=='__main__':
    r1 = np.array([0, 2, 0])
    r2 = np.array([0,2,3])
    Q = [[0, 3, 0], [0, 4, 1], [0, 4, 2], [0, 3, 3]]
    res = get_I_shape(r1, r2, Q, q_pre=[3, 0, 0], q_next=[3, 3, 0])
    print(res)

