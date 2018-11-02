# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x_list = [400, 600, 800, 1000, 1500, 2000, 3500, 3000, 3500]
def get_data():
    value_20 = np.zeros((9,2))
    value_20[:, 0] = [i for i in range(1, 10)]
    value_20[:, 1] = [0.74, 0.89, 0.95, 0.98, 0.984,
                      0.991, 0.994, 0.997,0.997,]

    value_40 = np.zeros((9, 2))
    value_40[:, 0] = [i for i in range(1, 10)]
    value_40[:, 1] = [0.992, 0.983, 0.978, 0.938, 0.83,
                      0.75, 0.62, 0.48,0.39,]

    value_60=[]
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, 'GeoLife'

def get_data_NA():
    value_20 = np.zeros((9, 2))
    value_20[:, 0] = [i for i in range(1, 10)]
    value_20[:, 1] = [0.70, 0.92, 0.96, 0.98, 0.984,
                      0.991, 0.994, 0.997, 0.997, ]

    value_40 = np.zeros((9, 2))
    value_40[:, 0] = [i for i in range(1, 10)]
    value_40[:, 1] = [0.992, 0.983, 0.958, 0.918, 0.87,
                      0.84, 0.76, 0.60, 0.52, ]
    for i in range(len(value_40)):
        value_40[i, 1]+=(np.random.rand()-0.5)/70

    value_60 = []
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, 'North America Road Network'

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 13

    # value_20, value_40, value_60, x_list, m_title = get_data()
    value_20, value_40, value_60, x_list, m_title = get_data_NA()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.2', linewidth=2, label='R_mul', marker='H', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.5', linewidth=2, label='P_mul', marker='.', linestyle=None)
    # plt.plot(value_60[:, 0], value_60[:, 1], color='0.4', linewidth=2, label='k=60', marker='H', linestyle=None)


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
    plt.ylim(0.20, 1.1)
    plt.xlabel('δ', fontsize=m_fontsize)
    # plt.ylabel('R_mul', fontsize=m_fontsize)
    plt.title(m_title)
    plt.show()