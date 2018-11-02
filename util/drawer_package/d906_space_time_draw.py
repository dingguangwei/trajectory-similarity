# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import d0_util_3d


if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 16


    # ax.plot([0,1],[1, 2],[3, 4], label='a', linestyle='-', linewidth=2, color='0', marker='H')

    # ax.legend()  # 显示图例
    ax.set_xlabel('x', fontsize=m_fontsize)
    ax.set_ylabel('y', fontsize=m_fontsize)
    ax.set_zlabel('Z', fontsize=m_fontsize)

    # 设置坐标轴刻度
    ax.set_xticks(np.arange(0, 101, 100))
    ax.set_yticks(np.arange(0, 101, 100))
    ax.set_zticks(np.arange(0, 6, 5))

    plt.xlim(0, 110)
    plt.ylim(0, 110)
    ax.set_zlim(0, 6)

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()