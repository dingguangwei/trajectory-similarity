# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

label = ['DTW', 'DTW-3d', 'STS']
name_list = ['1km', '5km', '10km']
num_list = []
x = []
def get_data_GL():
    num0 = [0.56,0.683,0.776]
    num_list.append(num0)

    num1 = [0.65,0.848,0.93]
    num_list.append(num1)

    num2 = [0.62,0.785,0.879]
    num_list.append(num2)

    total_width, n = 0.4, len(num_list)
    width = total_width / n
    x.append([0.1, 0.6, 1.1])
    x.append(list(np.array(x[0]) + width))
    x.append(list(np.array(x[1]) + width))
    x.append(list(np.array(x[2]) + width))

    m_title = 'GeoLife'
    path = 'F:/毕业设计大文件夹/picture/exp/exp05_GL.jpg'
    return num_list, x, width, name_list, label, m_title, path


def get_data_NA():
    num0 = [0.64,0.723,0.776]
    num_list.append(num0)

    num1 = [0.75,0.878,0.933]
    num_list.append(num1)

    num2 = [0.694,0.755,0.839]
    num_list.append(num2)

    num3 = [0.962, 0.916, 0.978]
    num_list.append(num3)

    total_width, n = 0.4, len(num_list)
    width = total_width / n
    x.append([0.1, 0.6, 1.1])
    x.append(list(np.array(x[0]) + width))
    x.append(list(np.array(x[1]) + width))
    x.append(list(np.array(x[2]) + width))

    m_title = 'North America Road Network'
    path='F:/毕业设计大文件夹/picture/exp/exp05_NA.jpg'
    return num_list, x, width, name_list, label, m_title, path


if __name__=='__main__':
    num_list, x, width, name_list, label, m_title, path = get_data_GL()
    # num_list, x, width, name_list, label, m_title, path = get_data_NA()

    m_fontsize = 14
    color_list = ['cornflowerblue', 'lightsteelblue', 'lightsalmon', 'rosybrown']
    for i in range(len(num_list)):
        plt.bar(x[i], num_list[i], width, label=label[i], color=color_list[i])

    plt.xticks(x[1], name_list, fontsize=m_fontsize)
    plt.yticks(np.arange(0, 1.1, 0.2), fontsize=m_fontsize)

    plt.ylim((0, 1.5))

    plt.xlabel('L(Q)', fontsize=m_fontsize)
    plt.ylabel('P_mul', fontsize=m_fontsize)

    plt.legend()
    plt.title(m_title, fontsize=m_fontsize)
    plt.savefig(path)
    plt.show()

