# coding=utf-8
import os
import pandas as pd
from conf.config_reader import get_root_path
from util.util import print_rate, print_complete


class FileReader:
    file_count = 0
    all_file_path = []

    def __init__(self):
        root_path = get_root_path()
        print("root_path=", root_path)
        print("\nscan all file in root_path : ", root_path)
        for root, dirs, files in os.walk(root_path):
            # print('\n', root)
            # print(dirs)
            # print(files)
            if len(files) != 0:
                for m_file in files:
                    if m_file[-4:] == ".plt":
                        self.all_file_path.append(root + "\\" + m_file)
                        self.file_count += 1
        print("file_count: ", self.file_count)

    # 获取单个文件数据中的经纬度和时间戳，以dataFrame格式返回
    def read_file(self, file_path):
        m_data = pd.read_csv(file_path, header=6)
        m_data.columns = ["lat", "lon", "col3", "col4", "col5", "date", "time"]
        result = m_data[["lat", "lon", "date", "time"]]
        return result

    # 将所有轨迹数据存入list，每条数据以一个DataFrame形式存放（也可以只读file_number条轨迹）
    def get_all_trajectory(self, file_number=None):
        all_trajectory = []
        print("\nread all files...")
        n = len(self.all_file_path)
        if not file_number is None:
            n = file_number
        for i in range(n):
            print_rate("has_read: ", i, n)
            all_trajectory.append(self.read_file(self.all_file_path[i]))
        print_complete("read_complete!")
        return all_trajectory

    def get_some_trajectory(self, index_list):
        some_trajectory = []
        for i in index_list:
            if i < len(self.all_file_path):
                some_trajectory.append(self.read_file(self.all_file_path[i]))
        return some_trajectory


if __name__ == "__main__":
    reader = FileReader()
    result = reader.get_some_trajectory([1])
    for item in result:
        print(item)
