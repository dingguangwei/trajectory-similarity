# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# GL数据集
def get_data():
    x_list = [100, 150, 200, 250, 300, 350,400,450 ]

    value_20 = [
        [1, 180],
        [2, 190],
        [3, 170],
        [4, 160],
        [5, 150],
        [6, 170],
        [7, 160],
        [8, 180],
    ]
    value_40 = [
        [1, 310],
        [2, 300],
        [3, 320],
        [4, 330],
        [5, 290],
        [6, 300],
        [7, 320],
        [8, 317],
    ]
    value_60=[
        [1, 270],
        [2, 250],
        [3, 280],
        [4, 260],
        [5, 240],
        [6, 250],
        [7, 230],
        [8, 260],
    ]

    print(value_60)
    m_title='GeoLife'
    path = 'F:/temp/赵影毕设图片/exp04.jpg'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list,m_title, path


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 13

    value_20, value_40, value_60, x_list,m_title, path = get_data()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.1', linewidth=2, label='ICN-NC-Routing', marker='H', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.1', linewidth=2, label='ICN-Shortest', marker='|', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.1', linewidth=2, label='ICN-Flood', marker='>', linestyle=None)


    ax = plt.gca()
    # 将底部的线移到y=0的地方
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_position(('data', 0))
    # ax.spines['left'].set_position(('data', 0))
    # ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, 9)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(100, 430)
    plt.xlabel('Request Times', fontsize=m_fontsize)
    plt.ylabel('Access Cost(ms)', fontsize=m_fontsize)
    # plt.title(m_title)
    plt.savefig(path)

    plt.show()