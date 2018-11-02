# coding=utf-8
from util.algorithm.normalization import data_format, read_data, get_I_st, normalization
import numpy as np
import time, datetime
from util.algorithm.traj_similarity_query import top_k_similar_query
if __name__=='__main__':
    # 1、
    # data_format()

    # 2、
    R_list, R_name_list = read_data(start_number=0, file_number=500)
    # res = get_I_st(None, R_list, R_name_list)

    Q = R_list[0]
    Q, R_list = normalization(Q, R_list)

    traj_distance_list, index_list = top_k_similar_query(Q, R_list)
    print('traj_distance_list = ', traj_distance_list)
    print('index_list', index_list)