# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x_list = [i/10. for i in range(0, 11)]
np.random.seed(0)

def get_data():

    # DTW
    # value_DTW = [
    #  [0.1, 0.704], [0.2, 0.696], [0.3, 0.685], [0.4, 0.680], [0.5, 0.673],
    #  [0.6, 0.647], [0.7, 0.64], [0.8, 0.631], [0.9, 0.620], [1.,  0.611]]
    # print(value_DTW)

    value_SDTW = [
     [0.1, 0.894], [0.2, 0.886], [0.3, 0.875], [0.4, 0.860], [0.5, 0.853],
     [0.6, 0.827], [0.7, 0.81], [0.8, 0.791], [0.9, 0.787], [1.,  0.778]]

    value_PTM = [
    [0.1, 0.899], [0.2, 0.895], [0.3, 0.878], [0.4, 0.849], [0.5, 0.830],
    [0.6, 0.807], [0.7, 0.777], [0.8, 0.743], [0.9, 0.701], [1., 0.683]]

    value_STS = [
    [0.1, 0.914], [0.2, 0.909], [0.3, 0.885], [0.4, 0.880], [0.5, 0.878],
    [0.6, 0.860], [0.7, 0.851], [0.8, 0.853], [0.9, 0.848], [1., 0.849]]

    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-7(a).jpg'
    m_title = 'GeoLife'
    return np.array(value_SDTW), np.array(value_PTM), np.array(value_STS), x_list, m_title, path


def get_data_NA():
    # value_DTW = [
    #  [0.1, 0.664],[0.2, 0.659],[0.3, 0.650],[0.4, 0.643],[0.5, 0.640],
    #  [0.6, 0.631],[0.7, 0.627],[0.8, 0.613],[0.9, 0.591],[1.,  0.583]]

    value_SDTW = [
     [0.1, 0.914],[0.2, 0.899],[0.3, 0.885],[0.4, 0.876],[0.5, 0.861],
     [0.6, 0.854],[0.7, 0.847],[0.8, 0.840],[0.9, 0.821],[1.,  0.813]]
    value_PTM = [
     [0.1, 0.896],[0.2, 0.862],[0.3, 0.838],[0.4, 0.829],[0.5, 0.790],
     [0.6, 0.787],[0.7, 0.767],[0.8, 0.733],[0.9, 0.721],[1.,  0.703]]

    value_STS = [
     [0.1, 0.934],[0.2, 0.929],[0.3, 0.913],[0.4, 0.911],[0.5, 0.907],
     [0.6, 0.899],[0.7, 0.890],[0.8, 0.885],[0.9, 0.879],[1.,  0.870]]

    path = 'F:/毕业设计大文件夹/picture/exp/Fig5-7(b).jpg'
    m_title = 'North America Road Network'
    return np.array(value_SDTW), np.array(value_PTM), np.array(value_STS), x_list, m_title, path

if __name__=='__main__':
    fig = plt.figure()
    m_fontsize = 16

    # value_SDTW, value_PTM, value_STS, x_list, m_title, path = get_data()
    value_SDTW, value_PTM, value_STS, x_list, m_title, path = get_data_NA()

    # plt.plot(value_DTW[:, 0], value_DTW[:, 1], color='0.2', linewidth=2, label='DTW', marker='x/m', linestyle=None)
    plt.plot(value_SDTW[:, 0], value_SDTW[:, 1], color='0.6', linewidth=2, label='SDTW', marker='|', linestyle=None)
    plt.plot(value_PTM[:, 0], value_PTM[:, 1], color='0.4', linewidth=2, label='PTM', marker='o', linestyle=None)
    plt.plot(value_STS[:, 0], value_STS[:, 1], color='0.', linewidth=2, label='STS', marker='>', linestyle=None)

    ax = plt.gca()

    plt.legend(ncol=2, fontsize=m_fontsize)
    # plt.xticks([i for i in range(1, 9)], x_list, fontsize=m_fontsize)
    plt.yticks(fontsize=m_fontsize)
    # plt.xlim(0, 4)
    plt.ylim(0.3, 1)
    plt.xlabel('noise rate α', fontsize=m_fontsize)
    plt.ylabel('Precision rate', fontsize=m_fontsize)
    plt.subplots_adjust(top=0.97, bottom=0.15, right=0.99, left=0.12, hspace=0, wspace=0)
    plt.savefig(path)
    plt.show()