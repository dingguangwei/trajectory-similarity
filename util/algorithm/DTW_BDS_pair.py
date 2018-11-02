# coding=utf-8
import numpy as np
import sys
from util.algorithm.util import get_EU_distance
from util.algorithm.util import get_BDS_point_and_distance

def get_data():
    R = [
        [1, 2, 0],
        [2, 2, 1],
        [3, 2, 2],
        [3, 3, 3],
        [4, 3, 4],
        [5, 3, 5],
        [5, 2, 6],
        [6, 2, 7],
        [7, 2, 8],
    ]
    Q = [
        [1, 1.5, 1],
        [3, 1.5, 2],
        [4.95, 1.5, 3],
        [4.95, 2.95, 4],
        [3.05, 2.95, 5],
        [3.05, 2, 6],
        [3.05, 0, 7],
    ]
    return np.array(Q), np.array(R)


# 获取pair中的key对应的所有value
def get_pair_index_by_key(pair, key):
    result = []
    for i in range(len(pair)):
        if pair[i, 0] == key:
            result.append(pair[i, 1])
    return result


# 根据时间戳，获取轨迹T中
# 如果point不是采样点，则获取point的下一个采样点
# 如果point是采样点，则返回point
def get_next_point_index(point, T):
    for i in range(len(T)):
        if T[i, 2] >= point[2]:
            return i
    return None


##############################################################################
# 使用DTW算法获取DTW对应点(qi->rj)
def get_pair_index_in_DTW(Q, R):
    m = len(Q)
    n = len(R)

    arr = np.zeros(shape=(m + 1, n + 1), dtype=float)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                arr[i, j] = 0
            elif i == 0 or j == 0:
                arr[i, j] = float("inf")
            else:
                d1 = get_EU_distance(Q[i - 1], R[j - 1])
                d2 = min(arr[i - 1, j], arr[i, j - 1], arr[i - 1, j - 1])
                arr[i, j] = d1 + d2
    pair = []
    i, j = m, n
    while i > 0 and j > 0:
        pair.append([i - 1, j - 1])
        post_i, post_j, post_value = i - 1, j - 1, arr[i - 1, j - 1]
        if post_value > arr[i, j - 1]:
            post_i, post_j, post_value = i, j - 1, arr[i, j - 1]
        if post_value > arr[i - 1, j]:
            post_i, post_j, post_value = i - 1, j, arr[i - 1, j]
        i, j = post_i, post_j
    pair.reverse()
    pair = np.array(pair)
    # print("DTW_pair_index=\n", pair, "\n")
    return pair


##############################################################################
# # 给出一个点，和pair=一条直线段的起止点，得到对应点
# def find_pair_point(v, start, end, label=None):
#     z = v[2]
#     min_point = [start[:]]
#     min_distance = float("inf")
#     for z in np.arange(min(start[2], end[2]), max(start[2], end[2]), 0.001):
#         x = (end[0] - start[0]) / (end[2] - start[2]) * (z - start[2]) + start[0]
#         y = (end[1] - start[1]) / (end[2] - start[2]) * (z - start[2]) + start[1]
#         if (v[0] - x) ** 2 + (v[1] - y) ** 2 + (v[2] - z) ** 2 < min_distance ** 2:
#             min_distance = np.sqrt((v[0] - x) ** 2 + (v[1] - y) ** 2 + (v[2] - z) ** 2)
#             min_point = [x, y, z]
#     return min_point, min_distance
#
#
# # 给定一个点，和一条轨迹段，得到BDS对应点
# def get_pair_point_in_BDS(v, T):
#     if len(T) == 0:
#         print("[error] get_pair_point_in_BDS")
#         sys.exit()
#     min_point, min_distance = [T[0], float("inf")]
#     for i in range(len(T) - 1):
#         temp_point, temp_distance = find_pair_point(v, T[i], T[i + 1])
#         if temp_distance < min_distance:
#             min_distance = temp_distance
#             min_point = temp_point
#     return list(min_point)


################################################################################
# 使用BDS优化DTW_pair
def BDS_optimization(Q, R, DTW_pair):
    m = len(Q)
    n = len(R)
    DTW_BDS_pair = []
    for i in range(n):
        # print('[info] BDS_optimization: i=', i)
        T = []
        if i == 0:
            from_index = 0
            end_index = get_pair_index_by_key(DTW_pair, i)[0]
        elif i != n - 1:
            BDS_pre_i = DTW_BDS_pair[-1][1]
            T.append(BDS_pre_i)
            from_index = get_next_point_index(BDS_pre_i, Q)
            end_index = get_pair_index_by_key(DTW_pair, i + 1)[0]
        else:
            BDS_pre_i = DTW_BDS_pair[-1][1]
            T = [BDS_pre_i]
            from_index = get_next_point_index(BDS_pre_i, Q)
            end_index = m - 1
        # print('对应Q的 from_index=', from_index, 'end_index=', end_index)
        for j in range(from_index, end_index + 1):
            if len(T) > 0 and T[0][2] == Q[j][2]:
                continue
            T.append(Q[j])
        pair_point, pair_distance = get_BDS_point_and_distance(R[i], T)
        DTW_BDS_pair.append([i, pair_point])
    # print("DTW_BDS_pair=\n", DTW_BDS_pair, "\n")
    return DTW_BDS_pair


################################################################################
################################################################################
################################################################################
def get_DTW_BDS_pair_by_traj(Q=None, R=None):
    if Q is None:
        Q, R = get_data()
    # print('Q=\n', Q,'\n')
    # print('R=\n', R,'\n')
    DTW_pair = get_pair_index_in_DTW(R, Q)
    DTW_BDS_pair = BDS_optimization(Q, R, DTW_pair)

    new_Q = []
    DTW_BDS_pair_index = []
    Q_index = 0
    for pair in DTW_BDS_pair:
        v1 = R[pair[0]]
        v2 = pair[1]
        while Q_index < len(Q) and Q[Q_index, 2] < v2[2]:
            if len(new_Q) >= 1 and new_Q[-1][2] < Q[Q_index, 2] or len(new_Q) == 0:
                new_Q.append(Q[Q_index])
            Q_index += 1
        if Q_index < len(Q) and Q[Q_index, 2] == v2[2]:
            Q_index += 1
        if len(new_Q) >= 1 and new_Q[-1][2] < v2[2] or len(new_Q) == 0:
            new_Q.append(v2)
        DTW_BDS_pair_index.append([pair[0], len(new_Q) - 1])
    while Q_index < len(Q):
        new_Q.append(Q[Q_index])
        Q_index += 1
    new_Q = np.array(new_Q)
    # print("new_Q=\n", new_Q, "\n")
    # print("DTW_BDS_pair_index=\n", DTW_BDS_pair_index, "\n")

    return DTW_BDS_pair, new_Q, DTW_BDS_pair_index


if __name__ == "__main__":
    get_DTW_BDS_pair_by_traj()
