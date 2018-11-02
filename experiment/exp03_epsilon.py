# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x_list = [r'$ 10^{-20}$', r'$ 10^{-15}$', r'$ 10^{-10}$', r'$ 10^{-8}$', r'$ 10^{-7}$', r'$ 10^{-6}$', r'$ 10^{-5}$', r'$ 10^{-2}$']

def get_data():

    value_20 = np.zeros((8,2))
    value_20[:, 0] = [i for i in range(1, 9)]
    value_20[:, 1] = [0.883, 0.904, 0.933, 0.950, 0.969,
                      0.984, 0.988, 0.98]
    print(value_20)

    value_40 = np.zeros(shape=(8, 2))
    value_40[:, 0] = range(1, 9)
    value_40[:, 1] = [0.840, 0.866, 0.893, 0.930, 0.949,
                      0.954, 0.958, 0.958]

    value_60 = np.zeros(shape=(8, 2))
    value_60[:, 0] = range(1, 9)
    value_60[:, 1] = [0.830, 0.851, 0.863, 0.890, 0.902,
                      0.909, 0.910, 0.907]

    path = 'F:/毕业设计大文件夹/picture/exp/exp03_GeoLife.jpg'
    m_title = 'GeoLife'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path


def get_data_NA():
    value_20 = np.zeros((8, 2))
    value_20[:, 0] = [i for i in range(1, 9)]
    value_20[:, 1] = [0.876, 0.924, 0.963, 0.980, 0.982,
                      0.985, 0.987, 0.984]
    print(value_20)

    value_40 = np.zeros(shape=(8, 2))
    value_40[:, 0] = range(1, 9)
    value_40[:, 1] = [0.860, 0.891, 0.93, 0.940, 0.949,
                      0.954, 0.958, 0.958]

    value_60 = np.zeros(shape=(8, 2))
    value_60[:, 0] = range(1, 9)
    value_60[:, 1] = [0.810, 0.871, 0.893, 0.900, 0.902,
                      0.909, 0.910, 0.907]

    path = 'F:/毕业设计大文件夹/picture/exp/exp03_NorthAmericaRoadNetwork.jpg'
    m_title = 'North America Road Network'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 14

    value_20, value_40, value_60, x_list, m_title, path = get_data()
    # value_20, value_40, value_60, x_list, m_title, path = get_data_NA()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.2', linewidth=2, label='k=20', marker='P', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.3', linewidth=2, label='k=40', marker='o', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.4', linewidth=2, label='k=60', marker='>', linestyle=None)


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
    plt.ylim(0.5, 1)
    plt.xlabel('ε', fontsize=m_fontsize)
    plt.ylabel('P_mul', fontsize=m_fontsize)
    plt.title(m_title, fontsize=m_fontsize)
    plt.savefig(path)
    plt.show()