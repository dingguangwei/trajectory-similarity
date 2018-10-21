# coding=utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import d1_xyzDrawer

if __name__=='__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    m_fontsize = 12

    # 轨迹R
    r0 = [0.1,0,0.1]
    r1 = [0,0.3,0.3]
    d1_xyzDrawer.plot([r0, r1], ax=ax, label=None, linestyle='-', linewidth=1.5, color='0.', marker='s')
    ax.text(r0[0], r0[1]+0.02, r0[2]-0.02, 'r0', fontsize=m_fontsize)
    ax.text(r1[0], r1[1]+0.02, r1[2]-0.02, 'r1', fontsize=m_fontsize)

    # 断点
    break_point_list = []
    m_step = 0.06
    for z in np.arange(0.1+m_step, 0.3, m_step):
        x = -(z-0.1)/2+0.1
        y = 3*(z-0.1)/2
        break_point_list.append([x, y, z])
    print('break_point_list=\n',break_point_list)
    break_point_list = np.array(break_point_list)
    for i in range(len(break_point_list)):
        ax.scatter(break_point_list[i, 0], break_point_list[i, 1], break_point_list[i, 2], marker='.', linewidths=2.5, color='b')
        ax.text(break_point_list[i, 0], break_point_list[i, 1]+0.02, break_point_list[i, 2]-0.02, 'bp'+str(i), fontsize=m_fontsize)

    # 轨迹Q（情况一）
    # q0 = [0.1, 0.2, 0.1]
    # q1 = [0., 0.3, 0.2]
    # d1_xyzDrawer.plot([q0, q1], ax=ax, label=None, linestyle='-', linewidth=1.5, color='0.5', marker='s')
    # ax.text(q0[0], q0[1] + 0.02, q0[2] - 0.02, 'q0', fontsize=m_fontsize)
    # ax.text(q1[0], q1[1] + 0.02, q1[2] - 0.02, 'q1', fontsize=m_fontsize)
    #
    # d1_xyzDrawer.find_pair_point(ax, r0, q0, q1, label='Q(r0)')
    # d1_xyzDrawer.find_pair_point(ax, r1, q0, q1, label='Q(r1)')
    # d1_xyzDrawer.find_pair_point(ax, break_point_list[0], q0, q1, label='          Q(bp0)')
    # d1_xyzDrawer.find_pair_point(ax, break_point_list[1], q0, q1, label='Q(bp1)')
    # d1_xyzDrawer.find_pair_point(ax, break_point_list[2], q0, q1, label='          Q(bp2)')

    # 轨迹Q（情况二）
    # q0 = [0.1, 0.2, 0.1]
    # d1_xyzDrawer.plot([q0], ax=ax, label=None, linestyle='-', linewidth=1.5, color='0.5', marker='s')
    # ax.text(q0[0], q0[1] + 0.02, q0[2] - 0.02, 'q0', fontsize=m_fontsize)
    #
    # d1_xyzDrawer.find_pair_point(ax, r0, q0, q0, label='Q(r0)')
    # d1_xyzDrawer.find_pair_point(ax, r1, q0, q0, label='')
    # d1_xyzDrawer.find_pair_point(ax, break_point_list[0], q0, q0, label='')
    # d1_xyzDrawer.find_pair_point(ax, break_point_list[1], q0, q0, label='')
    # d1_xyzDrawer.find_pair_point(ax, break_point_list[2], q0, q0, label='')

    # 轨迹Q（情况三）
    q = []
    q.append([0.1, 0.2, 0.08])
    q.append([0.1, 0.3, 0.15])
    q.append([0., 0.3, 0.2])
    d1_xyzDrawer.plot([q[0], q[1], q[2]], ax=ax, label=None, linestyle='-', linewidth=1.5, color='0.5', marker='s')
    for i in range(3):
        ax.text(q[i][0], q[i][1] + 0.02, q[i][2] - 0.02, 'q'+str(i), fontsize=m_fontsize)

    d1_xyzDrawer.find_pair_point(ax, r0, q[0], q[1], label='')
    d1_xyzDrawer.find_pair_point(ax, r1, q[1], q[2], label='')
    d1_xyzDrawer.find_pair_point(ax, break_point_list[0], q[0], q[1], label='')
    d1_xyzDrawer.find_pair_point(ax, break_point_list[1], q[1], q[2], label='')
    d1_xyzDrawer.find_pair_point(ax, break_point_list[2], q[1], q[2], label='')


    # ax.legend()  # 显示图例
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # 设置坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])
    # plt.xlim(0, 2)
    # plt.ylim(0, 2)

    ax.view_init(elev=20, azim=20)  # 调整视角

    plt.show()