# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

label = [ 'SDTW', 'PTM', 'STS']
name_list = ['5000', '10000', '15000']
num_list = []
x = []
def get_data_GL():
    # num0 = [0.76,0.733,0.776]  # DTW
    # num_list.append(num0)

    num1 = [0.93,0.848,0.83]  # SDTW
    num_list.append(num1)

    num2 = [0.824,0.805,0.789]  # PTM
    num_list.append(num2)

    num3 = [0.972, 0.926, 0.918]  # STS
    num_list.append(num3)

    total_width, n = 0.4, len(num_list)
    width = total_width / n
    x.append([0.1, 0.6, 1.1])
    x.append(list(np.array(x[0]) + width))
    x.append(list(np.array(x[1]) + width))
    x.append(list(np.array(x[2]) + width))

    m_title = 'GeoLife'
    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-5(a).jpg'
    return num_list, x, width, name_list, label, m_title, path


def get_data_NA():
    # num0 = [0.74,0.723,0.776]
    # num_list.append(num0)

    num1 = [0.917,0.848,0.803]
    num_list.append(num1)

    num2 = [0.843,0.805,0.779]
    num_list.append(num2)

    num3 = [0.942, 0.906, 0.888]
    num_list.append(num3)

    total_width, n = 0.4, len(num_list)
    width = total_width / n
    x.append([0.1, 0.6, 1.1])
    x.append(list(np.array(x[0]) + width))
    x.append(list(np.array(x[1]) + width))
    x.append(list(np.array(x[2]) + width))

    m_title = 'North America Road Network'
    path='F:/毕业设计大文件夹/picture/exp/Fig5-5(b).jpg'
    return num_list, x, width, name_list, label, m_title, path


if __name__=='__main__':
    # num_list, x, width, name_list, label, m_title, path = get_data_GL()
    num_list, x, width, name_list, label, m_title, path = get_data_NA()

    m_fontsize = 14
    color_list = ['cornflowerblue', 'lightsteelblue', 'lightsalmon', 'rosybrown']
    for i in range(len(num_list)):
        plt.bar(x[i], num_list[i], width, label=label[i], color=color_list[i])

    plt.xticks(x[1], name_list, fontsize=m_fontsize)
    plt.yticks(np.arange(0, 1.1, 0.2), fontsize=m_fontsize)

    plt.ylim((0, 1.3))

    plt.xlabel('Number of trajectories', fontsize=m_fontsize)
    plt.ylabel('Precision rate', fontsize=m_fontsize)

    plt.legend(ncol=2,fontsize=m_fontsize)
    # plt.title(m_title, fontsize=m_fontsize)
    plt.subplots_adjust(top=0.97, bottom=0.15, right=0.99, left=0.12, hspace=0, wspace=0)
    plt.savefig(path)
    plt.show()
