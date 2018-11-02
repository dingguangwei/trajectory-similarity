# coding=utf-8

import numpy as np
from util.algorithm.normalization import read_data
from util.algorithm.traj_similarity_query import quick_sort

def analyse(m_list, str=''):
    print('---------------------')
    print(str+':')
    print('min=', np.min(m_list))
    print('max=', np.max(m_list))
    print('avg=', np.average(m_list))
    print(np.argmax(m_list))
    print(m_list[0:5])

def fun(s_list):
    s_list[0]=-1

if __name__=='__main__':
    # R_list, R_name_list = read_data(start_number=0, file_number=5)
    #
    # R_length = []
    # R_time = []
    # for i in range(len(R_list)):
    #     R = R_list[i]
    #     d, time = 0, 0
    #     for j in range(len(R)-1):
    #         v1 = R[j]
    #         v2 = R[j+1]
    #         d+=np.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)
    #     R_length.append(d)
    #     R_time.append(R[-1, 2]-R[0, 2])
    #
    # analyse(R_length, 'R_length')
    # analyse(R_time, 'R_time')
    value_list = [4,2,1,5,3]
    index_list = [1,2,3,4,5]
    quick_sort(value_list, index_list, 0, len(value_list)-1)
    print(value_list)
    print(index_list)



