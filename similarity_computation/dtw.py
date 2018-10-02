# coding=utf-8
"""
    Improved distance calculation DTW
"""
import numpy as np
import pandas as pd
from similarity_computation.compute_distance import (
    compute_euclidean_distance,
    compute_manhattan_distance,
)

DTW_CODE = 1
ISDC_DTW_CODE = 2  # 仅改进空间距离
IDC_DTW_CODE = 3  # 改进时空距离


def compute_distance(point_1, point_2, algorithm_code):
    if algorithm_code == DTW_CODE:
        return compute_euclidean_distance(
            point_1[0], point_1[1], point_2[0], point_2[1]
        )
    elif algorithm_code == ISDC_DTW_CODE:
        return compute_manhattan_distance(
            point_1[0], point_1[1], point_2[0], point_2[1]
        )
    else:
        return -1  # TODO


# trajectory_1以DataFrame的形式传入
def compute_trajectory_distance(trajectory_1, trajectory_2, algorithm_code):
    m = len(trajectory_1)
    n = len(trajectory_2)

    # 将DataFrame转换为二维数组
    trajectory_1 = trajectory_1.values
    trajectory_2 = trajectory_2.values

    m_arr = np.zeros(shape=(m + 1, n + 1))
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                m_arr[i, j] = 0
            elif i == 0 or j == 0:
                m_arr[i, j] = float("inf")
            else:
                pre_distance = [m_arr[i - 1, j - 1], m_arr[i - 1, j], m_arr[i, j - 1]]
                m_arr[i, j] = min(pre_distance) + compute_distance(
                    trajectory_1[i - 1], trajectory_2[j - 1], algorithm_code
                )
    return m_arr[m, n]


# 轨迹以DataFrame的形式传入，计算的是经纬度之间的距离，单位为米，下同
def dtw(trajectory_1, trajectory_2):
    return compute_trajectory_distance(trajectory_1, trajectory_2, DTW_CODE)


def isdc_dtw(trajectory_1, trajectory_2):
    return compute_trajectory_distance(trajectory_1, trajectory_2, ISDC_DTW_CODE)


def idc_dtw(trajectory_1, trajectory_2):
    return compute_trajectory_distance(trajectory_1, trajectory_2, IDC_DTW_CODE)


if __name__ == "__main__":
    tra_1 = pd.DataFrame([[1, 0], [2, 0], [3, 0]])
    tra_2 = pd.DataFrame([[1, 1], [2, 1], [3, 1], [4, 1]])
    print("result = ", isdc_dtw(tra_1, tra_2))
