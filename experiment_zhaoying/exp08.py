# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# GL数据集
def get_data():
    x_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5]

    value_20 = np.zeros(shape=(len(x_list), 2))
    value_20[:, 0] = list(range(1, len(x_list) + 1))
    value_20[:, 1] = [170,420,560,760,820,860]

    value_40 = np.zeros(shape=(len(x_list), 2))
    value_40[:, 0] = list(range(1, len(x_list) + 1))
    value_40[:, 1] = [310,540,740,960,1020,1080]

    value_60 = np.zeros(shape=(len(x_list), 2))
    value_60[:, 0] = list(range(1, len(x_list) + 1))
    value_60[:, 1] = [255,500,680,900,950,1020]

    print(value_60)
    m_title='GeoLife'
    path = 'F:/temp/赵影毕设图片/exp08.jpg'
    return np.array(value_20), np.array(value_40), np.array(value_60), x_list,m_title, path


if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 13

    value_20, value_40, value_60, x_list,m_title, path = get_data()

    plt.plot(value_20[:, 0], value_20[:, 1], color='0.1', linewidth=2, label='ICN-NC-Routing', marker='H', linestyle=None)
    plt.plot(value_40[:, 0], value_40[:, 1], color='0.1', linewidth=2, label='ICN-Shortest', marker='|', linestyle=None)
    plt.plot(value_60[:, 0], value_60[:, 1], color='0.1', linewidth=2, label='ICN-Flood', marker='>', linestyle=None)


    ax = plt.gca()
    # 将底部的线移到y=0的地方
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_position(('data', 0))
    # ax.spines['left'].set_position(('data', 0))
    # ax.spines['right'].set_position(('data', 0))

    plt.legend(fontsize=m_fontsize)
    plt.xticks([i for i in range(1, 7)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    # plt.ylim(0., 1)
    plt.xlabel('Probability of Link Failure', fontsize=m_fontsize)
    plt.ylabel('Average Access Cost(ms)', fontsize=m_fontsize)
    # plt.title(m_title)
    plt.savefig(path)

    plt.show()