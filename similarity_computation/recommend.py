# coding=utf-8
import heapq
from similarity_computation.dtw import compute_trajectory_distance
from similarity_computation.dtw import DTW_CODE, ISDC_DTW_CODE, IDC_DTW_CODE
from util.print_log import print_complete, print_rate

"""
user_demand = pd.DataFrame()
trajectories = [trajectory1, trajectory2 ... ]
trajectory1 = pd.DataFrame()
n: 返回距离最小的n个数
"""


def get_similarity_trajectory(user_demand, trajectories, algorithm_code, n):
    print("\ncalculate_similarity_trajectory:")
    if algorithm_code == DTW_CODE:
        print("DTW:")
    elif algorithm_code == ISDC_DTW_CODE:
        print("ISDC_DTW")
    else:
        print("IDC_DTW")
    distance = []
    trajectories_count = len(trajectories)
    for i in range(trajectories_count):
        print_rate("has_calculate_count: ", i, trajectories_count)
        distance.append(
            compute_trajectory_distance(user_demand, trajectories[i], algorithm_code)
        )
    print("calculate_complete!")
    # 得到最小距离及其索引
    similarity_map = map(distance.index, heapq.nsmallest(n=n, iterable=distance))
    similarity_order = list(similarity_map)
    return distance, similarity_order
