# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# GL数据集
def get_data():
    x_list = [10, 50, 100, 150, 200, 250, 300, 350,400,450 ]

    value_20 = [
        [1, 0.99],
        [2, 0.48],
        [3, 0.34],
        [4, 0.14],
        [5, 0.22],
        [6, 0.18],
        [7, 0.19],
        [8, 0.22],
        [9, 0.16],
        [10, 0.14],
    ]
    value_40 = [
        [1, 1],
        [2, 0.62],
        [3, 0.38],
        [4, 0.30],
        [5, 0.40],
        [6, 0.22],
        [7, 0.20],
        [8, 0.21],
        [9, 0.18],
        [10, 0.20],
    ]


    value_60=[
        [1, 1],
        [2, 0.54],
        [3, 0.40],
        [4, 0.18],
        [5, 0.38],
        [6, 0.12],
        [7, 0.10],
        [8, 0.12],
        [9, 0.14],
        [10, 0.12],
    ]

    print(value_60)
    m_title='GeoLife'
    path = 'F:/temp/赵影毕设图片/exp02.jpg'
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
    plt.xticks([i for i in range(1, 11)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0., 1)
    plt.xlabel('Requests Times', fontsize=m_fontsize)
    plt.ylabel('Server Load', fontsize=m_fontsize)
    # plt.title(m_title)
    plt.savefig(path)

    plt.show()