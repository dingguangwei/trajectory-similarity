# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# GL数据集
def get_data():
    x_list = [50,100,150,200,250,300,350,400]

    value_20 = np.zeros(shape=(len(x_list), 2))
    value_20[:, 0] = list(range(1, len(x_list) + 1))
    value_20[:, 1] = [1,1,1,1,1,1,1,1]

    value_40 = np.zeros(shape=(len(x_list), 2))
    value_40[:, 0] = list(range(1, len(x_list) + 1))
    value_40[:, 1] = [0.926,0.927,0.92,0.927,0.927,0.924,0.925,0.924]

    value_60 = np.zeros(shape=(len(x_list), 2))
    value_60[:, 0] = list(range(1, len(x_list) + 1))
    value_60[:, 1] = [1,1,1,1,1,1,1,1]

    print(value_60)
    m_title='GeoLife'
    path = 'F:/temp/赵影毕设图片/exp12.jpg'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list,m_title, path


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 13

    value_20, value_40, value_60, x_list,m_title, path = get_data()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.1', linewidth=2, label='CCN-NC-Routing', marker='H', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.1', linewidth=2, label='CCN-Shortest', marker='|', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.1', linewidth=2, label='CCN-Flood', marker='>', linestyle=None)


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
    plt.ylim(0.88, 1.02)
    plt.xlabel('Request times', fontsize=m_fontsize)
    plt.ylabel('Average routing success rate', fontsize=m_fontsize)
    # plt.title(m_title)
    plt.savefig(path)

    plt.show()