# coding=utf-8
import numpy as np


eta_s = 10000
eta_t = 10000
lambda_st = 0.5


def get_Is(v1, v2):
    d = np.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)
    if d > eta_s:
        return 0
    else:
        return np.power(np.e, -d)


def get_It(v1, v2):
    d = np.abs(v1[2] - v2[2])
    if d > eta_t:
        return 0
    else:
        return np.power(np.e, -d)


def S_sim(Q, R):
    if len(Q) == 0 or len(R) == 0:
        return 0
    temp_a = get_Is(Q[0], R[0]) + S_sim(Q[1:], R)
    temp_b = S_sim(Q, R[1:])
    return max(temp_a, temp_b)


def T_sim(Q, R):
    if len(Q) == 0 or len(R) == 0:
        return 0
    temp_a = get_It(Q[0], R[0]) + T_sim(Q[1:], R)
    temp_b = T_sim(Q, R[1:])
    # print('\nT_sim:')
    # print('temp_a:', temp_a)
    # print('temp_b', temp_b)
    return max(temp_a, temp_b)


def ST_sim(Q, R):
    s = S_sim(Q, R)
    t = T_sim(Q, R)
    print('S_sim = ', s)
    print('T_sim = ', t)
    return lambda_st * s + (1 - lambda_st) * t


def get_data():
    Q = [[5, 10, 25], [10, 5, 30], [18, 10, 35]]
    R = [[5, 10.3, 0], [10, 5.3, 5], [18, 10.3, 10], [25,15.5,25],[30,15.5,30],[35,15.5,35]]
    S = [[5, 9, 24], [10, 4.7, 31], [18, 9, 34], [25,15,55],[30,15,60],[35,15,65]]
    return np.array(Q), np.array(R), np.array(S)

if __name__ == "__main__":
    Q, R, S = get_data()

    print('sim(Q,R) = ',ST_sim(Q, R), '\n')
    print('sim(Q,S) = ', ST_sim(Q, S), '\n')

