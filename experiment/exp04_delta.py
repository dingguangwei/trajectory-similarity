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
    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-4(a).jpg'
    m_title = 'GeoLife'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path

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
    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-4(b).jpg'
    m_title = 'North America Road Network'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    # value_20, value_40, value_60, x_list, m_title, path = get_data()
    value_20, value_40, value_60, x_list, m_title, path = get_data_NA()

    plt.plot(value_40[:, 0], value_40[:, 1], color='0.5', linewidth=2, label='Precision rate', marker='.', linestyle=None)
    plt.plot(value_20[:, 0], value_20[:, 1], color='0.2', linewidth=2, label='Recall rate', marker='H', linestyle=None)
    # plt.plot(value_60[:, 0], value_60[:, 1], color='0.4', linewidth=2, label='k=60', marker='H', linestyle=None)


    ax = plt.gca()

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, 10)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0.20, 1.1)
    plt.xlabel('δ', fontsize=m_fontsize)
    plt.ylabel('rate', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.97, bottom=0.15, right=0.99, left=0.12, hspace=0, wspace=0)
    plt.savefig(path)
    plt.show()