# coding=utf-8
import os
import sys
import pandas as pd
from conf.config_reader import get_root_path
from util.print_log import print_rate, print_complete, print_error


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
        if not self.__verification_id():
            print_error('FileReader')
            sys.exit()
        print("file_count: ", self.file_count)

    # 验证该数据集使用文件名作为id会不会有重复
    def __verification_id(self):
        id_list = []
        id_set = set()
        for i in range(len(self.all_file_path)):
            file_dir, file_name = os.path.split(self.all_file_path[i])
            id = file_name.split('.')[0]
            if id in id_set:
                print('has the same file name: ', self.all_file_path[i])
                return False
        return True

    @staticmethod
    # 获取单个文件数据中的经纬度和时间戳，以dataFrame格式返回，并返回文件名作为id
    def read_file(file_path):
        m_data = pd.read_csv(file_path, header=6)
        m_data.columns = ["lat", "lon", "col3", "col4", "col5", "date", "time"]
        result_data_frame = m_data[["lat", "lon", "date", "time"]]
        file_dir, file_name = os.path.split(file_path)
        return result_data_frame, int(file_name.split('.')[0])

    # 将所有轨迹数据存入list，每条数据以一个DataFrame形式存放（也可以只读file_number条轨迹）
    def get_all_trajectory(self, file_number=None):
        all_trajectory = []
        all_trajectory_id = []
        print("\nread all files...")
        n = len(self.all_file_path)
        if not file_number is None:
            n = file_number
        for i in range(n):
            print_rate("has_read: ", i, n)
            trajectory, id = FileReader.read_file(self.all_file_path[i])
            all_trajectory.append(trajectory)
            all_trajectory_id.append(id)
        print_complete("read_complete!")
        return all_trajectory, all_trajectory_id

    def get_some_trajectory(self, index_list):
        some_trajectory = []
        some_trajectory_id = []
        for i in index_list:
            if i < len(self.all_file_path):
                trajectory, id = FileReader.read_file(self.all_file_path[i])
                some_trajectory.append(trajectory)
                some_trajectory_id.append(id)
        return some_trajectory, some_trajectory_id


if __name__ == "__main__":
    reader = FileReader()
    result, ids = reader.get_some_trajectory([1])
    for item in result:
        print(item.tail(5))
    print(ids)
