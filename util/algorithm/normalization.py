# coding=utf-8
import numpy as np
import os
import sys
import pandas as pd
from util.file_reader import FileReader
from util.algorithm.util import geo_to_xy
from util.print_log import print_rate

def get_I_st(Q, R_list, R_name_list):
    black_list = []
    total_s = 1
    total_t = 1
    for index in range(len(R_list)):
        try:
            if R_name_list[index] in black_list:
                continue
            R = R_list[index]
            for i in range(len(R) - 1):
                v1, v2 = R[i], R[i + 1]
                total_s += np.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)
            total_t += R[-1, 2] - R[0, 2]
            if R[-1, 2] - R[0, 2] < 0:
                print('R.index=', index)
                return index
        except Exception:
            print('Exception: R.index=', index, ' name=', R_name_list[index])
    print('I_st=', total_s/total_t)
    return total_s/total_t


# 将轨迹数据简化至 x,y,timestamp
def data_format():
    path = 'F:\\DataSet\\subGeolife\\timestamp\\'
    reader = FileReader()
    all_trajectory, all_trajectory_id = reader.get_all_trajectory(start_number=0, file_number=5000)
    two_days_count = 0
    for i in range(len(all_trajectory)):
        print_rate('data_format ', i, len(all_trajectory))
        trajectory = np.array(all_trajectory[i])
        file_name = str(all_trajectory_id[i]) + '.txt'
        with open(path + file_name, 'w') as f:
            pre_time_stamp = 0
            for point in trajectory:
                # print(point)
                x, y = geo_to_xy(lon=point[1], lat=point[0])
                time_temp = str(point[3]).split(':')
                time_stamp = int(time_temp[0])*3600+int(time_temp[1])*60+int(time_temp[2])
                if time_stamp>pre_time_stamp:
                    pre_time_stamp = time_stamp
                else:
                    two_days_count+=1
                    break
                f.writelines(str(x)+','+str(y)+','+str(time_stamp)+'\n')
    print('two_days/all = ', two_days_count, ' / ', len(all_trajectory))

def read_data(start_number=0, file_number=20):
    root_path='F:\\DataSet\\subGeolife\\timestamp\\'
    R_list = []
    R_name_list = []
    for root, dirs, files in os.walk(root_path):
        for i in range(start_number, file_number):
            path = root_path+files[i]
            R = np.array(pd.read_csv(path))
            R_list.append(R)
            R_name_list.append(files[i])
    return R_list, R_name_list


# I_st 2.90（前4800条）,5.76（前100条）
def normalization(Q, R_list, I_st=5.76):
    for i in range(len(R_list)):
        for j in range(len(R_list[i])):
            R_list[i][j, 2] *= I_st
    for i in range(len(Q)):
        Q[i, 2] *= I_st
    return Q, R_list

