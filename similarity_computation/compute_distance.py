# coding=utf-8
import numpy as np

# 计算欧氏距离
def compute_euclidean_distance(x_1, y_1, x_2, y_2):
    return np.sqrt(pow(x_1 - x_2, 2) + pow(y_1 - y_2, 2))
