# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def get_data_GL():
    name_list = ['lambda=0', 'lambda=0.05', 'lambda=0.1', 'lambda=0.5']
    num_list = [52.4, 57.8, 59.1, 54.6]


    return num_list, name_list


if __name__=='__main__':
    # num_list, name_list = get_data_GL()

    name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
    num_list = [1.5, 0.6, 7.8, 6]
    num_list1 = [1, 2, 3, 1]
    x = list(range(len(name_list)))
    total_width, n = 0.8, 2
    width = total_width / n

    plt.bar(x, num_list, width=width, label='boy', fc='y')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, num_list1, width=width, label='girl', tick_label=name_list, fc='r')
    plt.legend()
    plt.show()