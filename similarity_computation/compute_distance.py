# coding=utf-8
import numpy as np
from math import radians, cos, sin, asin, sqrt


# 根据经纬度计算欧氏距离，单位为米
# 经度1，维度1，经度2，维度2
def compute_euclidean_distance(lon1, lat1, lon2, lat2):
    # 将角度转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    print('lon1, lat1, lon2, lat2 = ', lon1, lat1, lon2, lat2 )

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为千米
    return c * r * 1000


# 根据经纬度计算曼哈顿距离
def compute_manhattan_distance(lon1, lat1, lon2, lat2):
    # 将角度转化为弧度
    lon1_rad, lat1_rad, lon2_rad, lat2_rad = map(radians, [lon1, lat1, lon2, lat2])
    print('lon1_rad, lat1_rad, lon2_rad, lat2_rad = ', lon1_rad, lat1_rad, lon2_rad, lat2_rad)

    # 1、计算纬线间经线长度
    standard_lat_distance = 111194.92664455873  # 1纬度之间经线长度
    d_lat = np.abs(lat1-lat2) * standard_lat_distance

    # 2、计算经线间纬线长度。上下纬度两条不等长，取中间经度均值
    d_lon = np.abs(lon1-lon2) * cos((lat1_rad+lat2_rad)/2) * standard_lat_distance

    print('d_lat, d_lon = ', d_lat, d_lon)
    return d_lat+d_lon


"""
测试
"""
def fun_1():
    # lon1, lat1 = 123.433033, 41.661604  # 东北大学
    # lon2, lat2 = 116.403955, 39.915121  # 天安门
    # lon1, lat1 = 0, 2
    # lon2, lat2 = 0, 1
    lon1, lat1 = 116.847542, 40.419675  # 密云区，东北角
    lon2, lat2 = 116.093253, 39.704022  # 房山区，西南角

    lon1, lat1 = 116.847542, 39.704022  # 东南角
    lon2, lat2 = 116.093253, 39.704022  # 西南角

    euclidean_distance = compute_euclidean_distance(lon1, lat1, lon2, lat2)
    manhattan_distance = compute_manhattan_distance(lon1, lat1, lon2, lat2)
    print(euclidean_distance, manhattan_distance)


if __name__ == '__main__':
    fun_1()


# 一纬度间经线的长度为111194.92664455873

########################################################################
# lon1, lat1 = 116.847542, 40.419675  # 密云区，东北角
# lon2, lat2 = 116.093253, 40.419675  # 西北角
# 63853.72182270603 m
#
# lon1, lat1 = 116.847542, 39.704022  # 东南角
# lon2, lat2 = 116.093253, 39.704022  # 西南角
# 64527.982365072705 m
#
# 结论：北京东北和西南上下纬线长度差674.26m
########################################################################
