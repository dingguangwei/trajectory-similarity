# coding=utf-8
import numpy as np


def get_EU_distance(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    d = np.sqrt(np.sum((v1 - v2) ** 2))
    return d


def reverse_sigmoid(x, mu=0):
    y = 1/(1+np.power(np.e, x))+mu
    return y


"""
输入：一个点，一条轨迹
输出：BDS对应点坐标，距离
"""
def get_BDS_point_and_distance(v, T):
    if len(T)==0:
        print('[error] get_BDS_point: T.length is 0')
        return None
    elif len(T)==1:
        d = get_EU_distance(v, T[0])
        return T[0], d
    else:
        min_point = []
        min_distance = float('inf')
        for i in range(len(T)-1):
            v1 = T[i]
            v2 = T[i+1]
            # 使用立体几何求解最近点
            a = v1[0]-v2[0]
            b = v1[1]-v2[1]
            c = v1[2]-v2[2]
            m_molecule = (v[0]-v1[0])*a+(v[1]-v1[1])*b+(v[2]-v1[2])*c
            m_denominator = a*a+b*b+c*c
            if m_denominator==0:
                print('[error] get_BDS_point: 计算有错误，点和直线没有交点 v=', v, '\nT=', T, '\n')
            t = m_molecule/m_denominator

            x = v1[0]+a*t
            y = v1[1]+b*t
            z = v1[2]+c*t
            point = [x, y, z]
            # 对垂足在线段外情况的处理
            if point[2]<v1[2]:
                point = v1
            elif point[2]>v2[2]:
                point = v2
            distance = get_EU_distance(v, point)

            if distance<min_distance:
                min_point = point
                min_distance = distance
    return min_point, min_distance


"""
输入：x，对称轴central
输出：子轨迹长度x获得的激励程度
目的：保证子轨迹段长度接近查询轨迹长度
"""
def get_L_excitation(x, center):
    if x>=center:
        return np.power(np.e, center-x)
    else:
        return np.power(np.e, x-center)


# 输入：经度lon，纬度lat
# 输出：坐标
def geo_to_xy(lon, lat):
    R=6371393.0
    L = R * np.pi * 2
    W=L
    H=L/2
    mill=2.3
    x = lon * np.pi / 180
    y = lat * np.pi / 180
    y=1.25 * np.log( np.tan( 0.25 * np.pi + 0.4 * y ) )
    x = ( W / 2 ) + ( W / (2 * np.pi) ) * x
    y = ( H / 2 ) - ( H / ( 2 * mill ) ) * y
    return x, y

if __name__=='__main__':
    # v = [0,0,0]
    # T = [[0,1,0],[0,0,1]]
    # min_point, min_distance = get_BDS_point_and_distance(v, T)
    # print(min_point, min_distance)

    print(reverse_sigmoid(0))
    print(reverse_sigmoid(100))
