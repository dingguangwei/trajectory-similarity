# coding=utf-8
import numpy as np
from math import radians, cos, sin, asin, sqrt


# 根据经纬度计算欧氏距离，单位为米
# 经度1，维度1，经度2，维度2
def compute_euclidean_distance(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def test():
    lon1, lat1 = 123.433033, 41.661604  # 东北大学
    lon2, lat2 = 116.403955, 39.915121  # 天安门

    distance = compute_euclidean_distance(lon1, lat1, lon2, lat2)
    print("distance=", distance)
