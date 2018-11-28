# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# x_list = [r'$ 10^{-20}$', r'$ 10^{-15}$', r'$ 10^{-10}$', r'$ 10^{-8}$', r'$ 10^{-7}$', r'$ 10^{-6}$', r'$ 10^{-5}$', r'$ 10^{-2}$']

x_list = [0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]
def get_data():

    value_20 = np.zeros((9, 2))
    value_20[:, 0] = [i for i in range(1, 10)]
    value_20[:, 1] = [0.883, 0.904, 0.953, 0.970, 0.989,
                      0.985, 0.946, 0.933, 0.912]
    print(value_20)

    value_40 = np.zeros(shape=(9, 2))
    value_40[:, 0] = range(1, 10)
    value_40[:, 1] = [0.840, 0.866, 0.893, 0.930, 0.949,
                      0.954, 0.928, 0.915, 0.904]

    value_60 = np.zeros(shape=(9, 2))
    value_60[:, 0] = range(1, 10)
    value_60[:, 1] = [0.810, 0.841, 0.873, 0.890, 0.902,
                      0.899, 0.866, 0.854, 0.839]

    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-3(a).jpg'
    m_title = 'GeoLife'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path


def get_data_NA():
    value_20 = np.zeros((9, 2))
    value_20[:, 0] = [i for i in range(1, 10)]
    value_20[:, 1] = [0.916, 0.944, 0.963, 0.980, 0.982,
                      0.975, 0.957, 0.945, 0.930]
    print(value_20)

    value_40 = np.zeros(shape=(9, 2))
    value_40[:, 0] = range(1, 10)
    value_40[:, 1] = [0.837, 0.871, 0.921, 0.940, 0.949,
                      0.929, 0.894, 0.871, 0.861]

    value_60 = np.zeros(shape=(9, 2))
    value_60[:, 0] = range(1, 10)
    value_60[:, 1] = [0.810, 0.851, 0.889, 0.900, 0.902,
                      0.887, 0.865, 0.854, 0.835]

    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-3(b).jpg'
    m_title = 'North America Road Network'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 14

    # value_20, value_40, value_60, x_list, m_title, path = get_data()
    value_20, value_40, value_60, x_list, m_title, path = get_data_NA()

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
    plt.xticks([i for i in range(1, 10)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0.5, 1)
    plt.xlabel('ε', fontsize=m_fontsize)
    plt.ylabel('P_mul', fontsize=m_fontsize)
    plt.title(m_title, fontsize=m_fontsize)
    plt.savefig(path)
    plt.show()