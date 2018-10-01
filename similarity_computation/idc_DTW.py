"""
    Improved distance calculation DTW
"""
# coding=utf-8
import numpy as np
from similarity_computation.compute_distance import compute_euclidean_distance


def compute_distance(point_1, point_2):
    # print("\npoint: ", point_1[0], point_1[1], point_2[0], point_2[1])
    # print(
    #     "distance: ",
    #     compute_euclidean_distance(point_1[0], point_1[1], point_2[0], point_2[1]),
    # )
    return compute_euclidean_distance(point_1[0], point_1[1], point_2[0], point_2[1])


# trajectory_1以DataFrame的形式传入
def dtw(trajectory_1, trajectory_2):
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
                    trajectory_1[i - 1], trajectory_2[j - 1]
                )
    return m_arr[m, n]


if __name__ == "__main__":
    trajectory_1 = [[1, 0], [2, 0], [3, 0]]
    trajectory_2 = [[1, 1], [2, 1], [3, 1], [4, 1]]
    print("result = ", dtw(trajectory_1, trajectory_2))
