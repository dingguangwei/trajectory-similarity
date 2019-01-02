# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


x_list = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 5, 7, 10, 15]
def get_data():
    value_20 = np.zeros(shape=(10, 2))
    value_20[:, 0] = [i for i in range(1, 11)]
    value_20[:, 1] = [0.872, 0.943, 0.985, 0.989, 0.979,
                      0.931, 0.912, 0.907,0.901,0.901]

    value_40 = np.zeros(shape=(10, 2))
    value_40[:, 0] = [i for i in range(1, 11)]
    value_40[:, 1] = [0.852, 0.903, 0.955, 0.971, 0.9686,
                      0.911, 0.90, 0.893, 0.886, 0.886]

    value_60 = np.zeros(shape=(10, 2))
    value_60[:, 0] = [i for i in range(1, 11)]
    value_60[:, 1] = [0.829, 0.863, 0.905, 0.920, 0.9166,
                      0.869, 0.855, 0.854, 0.853, 0.853]
    for i in range(5, len(x_list)-1):
        value_20[i,1]+=0.03
        value_40[i, 1] += 0.03
        value_60[i, 1] += 0.03

    m_title = 'GeoLife'
    path = "F:\\毕业设计大文件夹\\picture\\exp\\Fig5-2(a)_exp02.jpg"
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path


def get_data_NA():
    value_20 = np.zeros(shape=(10, 2))
    value_20[:, 0] = range(1, 11)
    value_20[:, 1] = [0.852, 0.945, 0.983, 0.985, 0.991,
                      0.971, 0.91, 0.889, 0.882, 0.881]

    value_40 = np.zeros(shape=(10, 2))
    value_40[:, 0] = range(1, 11)
    value_40[:, 1] = [0.81, 0.899, 0.954, 0.959, 0.958,
                      0.949, 0.89, 0.8780, 0.868, 0.867]

    value_60 = np.zeros(shape=(10, 2))
    value_60[:, 0] = range(1, 11)
    value_60[:, 1] = [0.766, 0.821, 0.870, 0.887, 0.895,
                      0.884, 0.84, 0.813, 0.801, 0.801]

    for i in range(6, len(x_list)-1):
        value_20[i,1]+=0.03
        value_40[i, 1] += 0.03
        value_60[i, 1] += 0.03

    m_title = 'NorthAmericaRoadNetwork'
    path = "F:\\毕业设计大文件夹\\picture\\exp\\Fig5-2(b)_exp02.jpg"
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list, m_title, path


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    # value_20, value_40, value_60, x_list, m_title, path = get_data()
    value_20, value_40, value_60, x_list, m_title, path = get_data_NA()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.', linewidth=2, label='k=20', marker='|', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.4', linewidth=2, label='k=40', marker='o', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.6', linewidth=2, label='k=60', marker='>', linestyle=None)

    ax = plt.gca()

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, 11)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0.7, 1)
    plt.xlabel('μ', fontsize=m_fontsize)
    plt.ylabel('Precision rate', fontsize=m_fontsize)
    # plt.title(m_title)
    plt.subplots_adjust(top=0.97, bottom=0.15, right=0.99, left=0.15, hspace=0, wspace=0)
    plt.savefig(path)
    plt.show()