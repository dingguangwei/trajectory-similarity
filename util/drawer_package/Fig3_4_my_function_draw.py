# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import d8_PTM_computing

if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    I_st = 0.92
    m_fontsize=16

    Q, R, S = d8_PTM_computing.get_data()
    ax.plot(Q[:, 0], Q[:, 1], Q[:, 2]*I_st,label='Q', linestyle='-', linewidth=4, color='blue', marker='H')
    ax.plot(R[:, 0], R[:, 1], R[:, 2]*I_st, label='R', linestyle='-', linewidth=4, color='0.4', marker='*')
    ax.plot(S[:, 0], S[:, 1], S[:, 2]*I_st, label='S', linestyle='-', linewidth=4, color='0.6', marker='|')

    for i in range(len(Q)):
        ax.text(Q[i, 0]-1, Q[i, 1]+1, Q[i, 2]*I_st, 'q'+str(i), color='blue', fontsize=m_fontsize)
    for i in range(len(R)):
        ax.text(R[i, 0]-1, R[i, 1], R[i, 2]*I_st-8, 'r'+str(i), color='0.4', fontsize=m_fontsize)
    for i in range(len(S)):
        ax.text(S[i, 0]-1, S[i, 1], S[i, 2]*I_st-8, 's'+str(i), color='0.6', fontsize=m_fontsize)


    ax.legend()  # 显示图例
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    # plt.xlim(0, 2)
    # plt.ylim(0, 2)

    ax.view_init(elev=20, azim=260)  # 调整视角

    plt.show()