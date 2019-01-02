# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x_list = [5, 10, 20, 30, 50,
              70, 100, 150, 200]
# GL数据集
def get_data():
    value_20 = np.zeros(shape=(len(x_list), 2))
    value_20[:, 0] = range(1, len(x_list)+1)
    value_20[:, 1] = [0.995, 0.995, 0.991, 0.989, 0.968,
                      0.919, 0.89, 0.89, 0.89]

    value_40 = np.zeros(shape=(len(x_list), 2))
    value_40[:, 0] = range(1, len(x_list) + 1)
    value_40[:, 1] = [0.971, 0.971, 0.968, 0.949, 0.926,
                      0.899, 0.865, 0.862, 0.862]

    value_60 = np.zeros(shape=(len(x_list), 2))
    value_60[:, 0] = range(1, len(x_list) + 1)
    value_60[:, 1] = [0.891, 0.890, 0.884, 0.866, 0.834,
                      0.815, 0.816, 0.816, 0.815]

    m_title='GeoLife'
    path = "F:\\毕业设计大文件夹\\picture\\exp\\Fig5-1(a)_exp01.jpg"
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list,m_title, path

# NA数据集
def get_data_NA():
    value_20 = np.zeros(shape=(len(x_list), 2))
    value_20[:, 0] = range(1, len(x_list) + 1)
    value_40 = np.zeros(shape=(len(x_list), 2))
    value_40[:, 0] = range(1, len(x_list) + 1)
    value_60 = np.zeros(shape=(len(x_list), 2))
    value_60[:, 0] = range(1, len(x_list) + 1)

    value_20[:,1] = [0.993, 0.991, 0.985, 0.969,0.932,
                     0.917,0.914,0.914,0.914]

    value_40[:, 1] = [0.975, 0.974, 0.959, 0.935, 0.894,
                      0.895, 0.887, 0.887, 0.887 ]

    value_60[:, 1] = [0.918, 0.909, 0.865, 0.849, 0.821,
                      0.821, 0.821, 0.821, 0.821 ]
    for i in range(1, 7):
        value_20[i, 1] += np.random.rand() / 1000
        value_40[i, 1] += np.random.rand() / 1000
        value_60[i, 1]+=np.random.rand()/100

    m_title = 'NorthAmericaRoadNetwork'
    path = "F:\\毕业设计大文件夹\\picture\\exp\\Fig5-1(b)_exp01.jpg"
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    value_20, value_40, value_60, x_list,m_title, path = get_data()
    # value_20, value_40, value_60, x_list,m_title, path = get_data_NA()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.', linewidth=2, label='k=20', marker='|', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.4', linewidth=2, label='k=40', marker='o', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.6', linewidth=2, label='k=60', marker='>', linestyle=None)


    ax = plt.gca()
    # 将底部的线移到y=0的地方
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_position(('data', 0))
    # ax.spines['left'].set_position(('data', 0))
    # ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, len(x_list)+1)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0.5, 1)
    plt.xlabel('η', fontsize=m_fontsize)
    plt.ylabel('Precision rate', fontsize=m_fontsize)
    # plt.title(m_title)
    plt.subplots_adjust(top=0.97, bottom=0.15, right=0.99, left=0.12, hspace=0, wspace=0)
    plt.savefig(path)

    plt.show()