# coding=utf-8
import numpy as np


def compute_distance(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    result = np.sqrt((x1-x2)**2+(y1-y2)**2)
    # print(point1, ', ', point2, ' = ', result)
    return result


def dtw(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    m_arr = np.zeros(shape=(m + 1, n + 1))
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                m_arr[i, j] = 0
            elif i == 0 or j == 0:
                m_arr[i, j] = float("inf")
            else:
                pre_distance = [m_arr[i - 1, j - 1], m_arr[i - 1, j], m_arr[i, j - 1]]
                m_arr[i, j] = min(pre_distance) + compute_distance(arr1[i-1], arr2[j-1])
    print('m_arr=\n', m_arr)


def get_QRS(is_less=True, is_print=False):
    if is_less:
        Q = np.array([[1, 1], [5, 1], [18, 1]])
        R = np.array([[1, 2], [5, 2], [18, 3]])
        S = np.array([[1, 3], [5, 2], [18, 2]])
    else:
        Q = np.ones(shape=(18, 2))
        Q[:, 0] = np.arange(1, 19, 1)
        # print(Q)

        R = np.zeros(shape=(18, 2))
        R[:, 0] = np.arange(1, 19, 1)
        R[0:4, 1] = [2 for i in range(4)]
        for i in np.arange(4, len(R), 1):
            R[i, 1] = (R[i, 0] - 5) / 13 + 2
        # print(R)

        S = np.zeros(shape=(18, 2))
        S[:, 0] = np.arange(1, 19, 1)
        for i in np.arange(0, 5, 1):
            S[i, 1] = -(S[i, 0] - 1) / 4 + 3
        S[5:, 1] = [2 for i in range(13)]
    if is_print:
        print('Q=\n', Q)
        print('R=\n', R)
        print('S=\n', S)
    return Q, R, S

if __name__=='__main__':
    Q, R, S = get_QRS(is_less=True)

    # print(S.shape)
    dtw(Q, R)
    dtw(Q, S)


