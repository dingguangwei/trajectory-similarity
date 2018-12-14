# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# x_list = [r'$ 10^{-20}$', r'$ 10^{-15}$', r'$ 10^{-10}$', r'$ 10^{-8}$', r'$ 10^{-7}$', r'$ 10^{-6}$', r'$ 10^{-5}$', r'$ 10^{-2}$']

#        3.6 18 36  72  108 144 km/h
x_list = [1, 5, 10, 20, 30, 40]
def get_data():

    value_20 = np.zeros((len(x_list), 2))
    value_20[:, 0] = [i for i in range(1, len(x_list)+1)]
    value_20[:, 1] = [0.923, 0.980, 0.985, 0.970, 0.835,
                      0.805]
    print(value_20)

    value_40 = np.zeros(shape=(len(x_list), 2))
    value_40[:, 0] = range(1, len(x_list)+1)
    value_40[:, 1] = [0.870, 0.947, 0.953, 0.908, 0.758,
                      0.694]

    value_60 = np.zeros(shape=(len(x_list), 2))
    value_60[:, 0] = range(1, len(x_list)+1)
    value_60[:, 1] = [0.820, 0.885, 0.893, 0.860, 0.638,
                      0.609]

    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-3(a).jpg'
    m_title = 'GeoLife'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path


def get_data_NA():
    value_20 = np.zeros((len(x_list), 2))
    value_20[:, 0] = [i for i in range(1, len(x_list) + 1)]
    value_20[:, 1] = [0.863, 0.904, 0.963, 0.986, 0.965,
                      0.914]
    print(value_20)

    value_40 = np.zeros(shape=(len(x_list), 2))
    value_40[:, 0] = range(1, len(x_list) + 1)
    value_40[:, 1] = [0.820, 0.856, 0.933, 0.960, 0.938,
                      0.874]

    value_60 = np.zeros(shape=(len(x_list), 2))
    value_60[:, 0] = range(1, len(x_list) + 1)
    value_60[:, 1] = [0.760, 0.811, 0.903, 0.92, 0.898,
                      0.819]

    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-3(b).jpg'
    m_title = 'North America Road Network'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    # value_20, value_40, value_60, x_list, m_title, path = get_data()
    value_20, value_40, value_60, x_list, m_title, path = get_data_NA()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.2', linewidth=2, label='k=20', marker='P', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.3', linewidth=2, label='k=40', marker='o', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.4', linewidth=2, label='k=60', marker='>', linestyle=None)


    ax = plt.gca()

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, len(x_list)+1)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0.5, 1)
    plt.xlabel('$I_{st}$', fontsize=m_fontsize+3)
    plt.ylabel('Precision rate', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.97, bottom=0.15, right=0.99, left=0.12, hspace=0, wspace=0)
    plt.savefig(path)
    plt.show()