# coding=utf-8
import numpy as np
import d8_PTM_computing

I_st = 0.3

# mms: meter multiply distance
def get_mms_distance(v1, v2):
    d_space = np.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)
    d_time = np.abs(v1[2]-v2[2])
    # if d_space<15 or d_time <1:
    #     return 1
    print('[',v1, ' & ', v2, '] d_space=', d_space, '  d_time=', d_time, '\t res=',d_space*(d_time), '\n')
    return d_space*(d_time)


def get_st_distance(v1, v2):
    z = I_st*(v1[2] - v2[2])
    distance = np.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2+z**2)
    # print('distance=',distance, '\n')
    return distance


# 返回两条轨迹中的对应点对，未写完
def get_pair_point(Q, R):
    return None


if __name__=='__main__':
    Q, R, S = d8_PTM_computing.get_data()

    d_QR = 0
    d_QS = 0

    for i in range(len(Q)):
        d_QR += get_st_distance(Q[i], R[i])

    # for i in range(len(Q)):
    #     d_QR += get_st_distance(Q[i], R[i+3])

    for i in range(len(Q)):
        d_QS += get_st_distance(Q[i], S[i])

    print('d_QR=', d_QR, '\n')
    print('d_QS=', d_QS, '\n')
