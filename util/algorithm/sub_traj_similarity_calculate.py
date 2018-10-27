# coding=utf-8
import numpy as np
from util.algorithm.util import get_EU_distance, get_L_excitation
import sys


# 参数ε epsilon
def similarity_calculate(d_segment_list, R_segment_length_list, Q_length, Q, R, epsilon):
    min_mean = float('inf')
    R_start_index = 0
    R_end_index = -1
    R_Q_min_distance = float('inf')
    for i in range(len(d_segment_list)):
        for j in range(i, len(d_segment_list)):
            R_segment_length = np.sum(R_segment_length_list[i:j + 1])
            if get_L_excitation(x=R_segment_length, center=Q_length) > epsilon:  # 这里epsilon是一个控制最长或最短允许R长度的参数
                mean_temp = np.average(d_segment_list[i:j + 1])
                if mean_temp<min_mean:
                    R_start_index = i
                    R_end_index = j+1
                    min_mean = mean_temp
    if R_end_index==-1:
        print('[ERROR] similarity_calculate: can not find a sub trajectory cause epsilon is too large')
        sys.exit(0)
    R_Q_min_distance = np.sum(d_segment_list[R_start_index:R_end_index+1])
    return R_start_index, R_end_index, R_Q_min_distance


def get_similar_segment_and_distance(Q, R, d_segment_list, epsilon):
    Q_length = 0
    for i in range(len(Q) - 1):
        Q_length += get_EU_distance(Q[i], Q[i + 1])
    R_segment_length_list = [get_EU_distance(R[i], R[i + 1]) for i in range(len(R) - 1)]

    print('R_segment_length_list=', R_segment_length_list,'\n')

    return similarity_calculate(d_segment_list, R_segment_length_list, Q_length, Q, R, epsilon)


def get_data():
    R = [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 2],
        [0, 1, 3],
        [0, 1, 4],
        [0, 1, 5],
        [0, 1, 6],
        [0, 1, 7]
    ]
    Q = [
        [0, 3, 2],
        [0, 3, 3],
        [0, 3, 4],
        [0, 3, 5]
    ]
    d_segment_list = [10,8,6,6,6,8]
    return Q, R, d_segment_list

if __name__=='__main__':
    Q, R, d_segment_list = get_data()
    res = get_similar_segment_and_distance(Q, R, d_segment_list, 0.1)
    print('[R_start_index, R_end_index, R_Q_min_distance]=', res)










