# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

label = ['DTW', 'SDTW', 'PTM', 'STS']
name_list = [0.39, 0.395, 0.4,0.405,0.41,0.415]
num_list = []
x = []
def get_data_GL():
    num0 = [0.394,0.401,0.413,0.414,0.424,0.427]
    num_list.append(num0)


    total_width, n = 0.4, len(num_list)
    width = total_width / n
    x.append([2,4,6,8,10,12])
    x.append(list(np.array(x[0]) + width))
    x.append(list(np.array(x[1]) + width))
    x.append(list(np.array(x[2]) + width))

    m_title = 'GeoLife'
    path = 'F:/temp/赵影毕设图片/exp01.jpg'
    return num_list, x, width, name_list, label, m_title, path



if __name__=='__main__':
    num_list, x, width, name_list, label, m_title, path = get_data_GL()

    print('name_list=', name_list)


    m_fontsize = 14
    color_list = ['cornflowerblue', 'lightsteelblue', 'lightsalmon', 'rosybrown']
    for i in range(len(num_list)):
        plt.bar(x[i], num_list[i], width, label=label[i], color=color_list[i])

    plt.xticks(x[0], name_list, fontsize=m_fontsize)
    plt.yticks(np.arange(0, 1.1, 0.2), fontsize=m_fontsize)

    plt.ylim((0, 0.6))

    plt.xlabel('Segment Size', fontsize=m_fontsize)
    plt.ylabel('Average hit rate', fontsize=m_fontsize)

    # plt.legend()
    # plt.title(m_title, fontsize=m_fontsize)
    plt.savefig(path)
    plt.show()
