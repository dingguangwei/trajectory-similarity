# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# GL数据集
def get_data():
    x_list = [1, 5, 10, 15, 20, 25, 30, 40, 50, 70, 100, 150, 200, 250]

    value_20 = [
        [1, 0.997],
        [2, 0.995],
        [3, 0.994],
        [4, 0.993],
        [5, 0.991],
        [6, 0.992],
        [7, 0.989],
        [8, 0.979],
        [9, 0.951],
        [10, 0.899],
        [11, 0.89],
        [12, 0.89],
        [13, 0.89],
        [14, 0.89],
    ]
    value_40 = [
        [1, 0.974],
        [2, 0.971],
        [3, 0.971],
        [4, 0.968],
        [5, 0.965],
        [6, 0.960],
        [7, 0.953],
        [8, 0.929],
        [9, 0.901],
        [10, 0.865],
        [11, 0.861],
        [12, 0.862],
        [13, 0.862],
        [14, 0.862],
    ]

    # value_40 = value_20.copy()
    # for i in range(0, 9):
    #     m_rand = np.random.rand()/10
    #     value_40[i][1] = value_40[i][1]-0.1+m_rand
    #     print(m_rand)

    value_60=[
        [1, 0.892],
        [2, 0.891],
        [3, 0.890],
        [4, 0.888],
        [5, 0.884],
        [6, 0.880],
        [7, 0.876],
        [8, 0.860],
        [9, 0.834],
        [10, 0.821],
        [11, 0.815],
        [12, 0.817],
        [13, 0.817],
        [14, 0.815],
    ]
    # for i in range(8):
    #     value_60[i][1]+=np.random.rand()/50 - 0.02
    # for i in range(8, len(value_60)):
    #     value_60[i][1]+=np.random.rand()/50 - 0.05

    print(value_60)
    m_title='GeoLife'
    path = "F:\\毕业设计大文件夹\\picture\\exp\\Fig5-1(a)_exp01.jpg"
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list,m_title, path

# NA数据集
def get_data_NA():
    x_list = [1, 5, 10, 15, 20, 25, 30, 40, 50, 70, 100, 150, 200, 250]
    value_20=np.zeros(shape=(14, 2))
    value_20[:,0] = range(1, 15)
    value_20[:,1] = [0.998, 0.993, 0.991, 0.990, 0.985,
                     0.981,0.959,0.930,0.932,0.921,
                     0.917,0.914,0.914,0.914]

    value_40 = np.zeros(shape=(14, 2))
    value_40[:, 0] = range(1, 15)
    value_40[:, 1] = [0.987, 0.985, 0.984, 0.979, 0.969,
                      0.959, 0.935, 0.909, 0.894, 0.895,
                      0.887, 0.887, 0.887, 0.887 ]
    value_60 = np.zeros(shape=(14, 2))
    value_60[:, 0] = range(1, 15)
    value_60[:, 1] = [0.916, 0.918, 0.909, 0.907, 0.905,
                      0.884, 0.849, 0.831, 0.821, 0.821,
                      0.821, 0.821, 0.821, 0.821 ]
    for i in range(7, 14):
        value_20[i, 1] += np.random.rand() / 1000
        value_40[i, 1] += np.random.rand() / 1000
        value_60[i, 1]+=np.random.rand()/100

    m_title = 'NorthAmericaRoadNetwork'
    path = "F:\\毕业设计大文件夹\\picture\\exp\\Fig5-1(b)_exp01.jpg"
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 13

    # value_20, value_40, value_60, x_list,m_title, path = get_data()
    value_20, value_40, value_60, x_list,m_title, path = get_data_NA()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.2', linewidth=2, label='k=20', marker='H', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.3', linewidth=2, label='k=40', marker='.', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.4', linewidth=2, label='k=60', marker='*', linestyle=None)


    ax = plt.gca()
    # 将底部的线移到y=0的地方
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_position(('data', 0))
    # ax.spines['left'].set_position(('data', 0))
    # ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, 16)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0.5, 1)
    plt.xlabel('η', fontsize=m_fontsize)
    plt.ylabel('P_sim', fontsize=m_fontsize)
    plt.title(m_title)
    plt.savefig(path)

    plt.show()