# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# GL数据集
def get_data():
    x_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    value_20 = [
        [1, 0.76],
        [2, 0.64],
        [3, 0.54],
        [4, 0.42],
        [5, 0.34],
        [6, 0.20],
        [7, 0.08],
    ]
    value_40 = [
        [1, 0.92],
        [2, 0.79],
        [3, 0.64],
        [4, 0.58],
        [5, 0.54],
        [6, 0.35],
        [7, 0.24],
    ]


    value_60=[
        [1, 0.84],
        [2, 0.72],
        [3, 0.60],
        [4, 0.5],
        [5, 0.40],
        [6, 0.29],
        [7, 0.16],
    ]

    print(value_60)
    m_title='GeoLife'
    path = 'F:/temp/赵影毕设图片/exp03.jpg'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list,m_title, path


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 13

    value_20, value_40, value_60, x_list,m_title, path = get_data()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.1', linewidth=2, label='ICN-NC-Routing', marker='H', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.1', linewidth=2, label='ICN-NC-Shortest', marker='|', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.1', linewidth=2, label='ICN-NC-Flood', marker='>', linestyle=None)


    ax = plt.gca()
    # 将底部的线移到y=0的地方
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_position(('data', 0))
    # ax.spines['left'].set_position(('data', 0))
    # ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, 8)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0., 1)
    plt.xlabel('Relative Cache Size', fontsize=m_fontsize)
    plt.ylabel('Average Serve Load', fontsize=m_fontsize)
    # plt.title(m_title)
    plt.savefig(path)

    plt.show()