# coding=utf-8
import os
import pandas as pd


class file_reader:
    all_file_path = []

    def __init__(self, root_path):
        file_count = 0
        print("scan all file:")
        for root, dirs, files in os.walk(root_path):
            # print('\n', root)
            # print(dirs)
            # print(files)
            if len(files) != 0:
                for m_file in files:
                    if m_file[-4:] == ".plt":
                        self.all_file_path.append(root + "\\" + m_file)
                        file_count += 1
                        if file_count % 5000 == 0:
                            print("file_count: ", file_count)
        print("file_count: ", file_count)

    # 获取单个文件数据中的经纬度和时间戳，以dataFrame格式返回
    def read_file(self, file_path):
        m_data = pd.read_csv(file_path, header=6)
        m_data.columns = ["lat", "lon", "col3", "col4", "col5", "date", "time"]
        result = m_data[["lat", "lon", "date", "time"]]
        return result

    # 将所有轨迹数据存入list，每条数据以一个DataFrame形式存放
    def get_all_trajectory(self):
        all_trajectory = []
        for file_path in self.all_file_path:
            all_trajectory.append(self.read_file(file_path))
        return result

    def get_some_trajectory(self, index_list):
        some_trajectory = []
        for i in index_list:
            if i < len(self.all_file_path):
                some_trajectory.append(self.read_file(self.all_file_path[i]))
        return some_trajectory


if __name__ == "__main__":
    path = "F:\\GeolifeTrajectories1.3\\Data"
    reader = file_reader(root_path=path)
    result = reader.get_some_trajectory([1])
    for item in result:
        print(item)
