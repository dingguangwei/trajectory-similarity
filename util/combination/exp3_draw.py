# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from util.algorithm.normalization import read_data

if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16

    R_list, R_name_list = read_data(start_number=0, file_number=500)
    for i in [0]:
        R = R_list[i]
        ax.plot(R[:, 0], R[:, 1], R[:, 2], label='R'+str(i), linestyle='-', linewidth=2, color='0.3', marker='H')



    ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # plt.xlim(0, 2)
    # plt.ylim(0, 2)
    # ax.set_zlim(0, 10)

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()