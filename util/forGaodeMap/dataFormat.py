# coding=utf-8
"""
一个单独运行的脚本
目的：将plt文件转化为jsp方便读取的json格式
"""
import pandas as pd
import os
import json


# 获取单个文件数据中的经纬度和时间戳，以dataFrame格式返回
def read_file(file_path):
    m_data = pd.read_csv(file_path, header=6)
    m_data.columns = ["lat", "lon", "col3", "col4", "col5", "date", "time"]
    result = m_data[["lat", "lon", "date", "time"]]
    return result


# 将一个DataFrame格式 (columns=['lat', 'lon']) 的数据转化为json数据 {"lat":lats, "lon": lons}
def data_convert(data):
    lats = list(data['lat'])
    lons = list(data['lon'])
    json_data = {"lat":lats, "lon": lons}
    return json_data


# 将plt文件转化为json文件存储
def plt_to_json(file_path, new_file_dir='F:\\json', new_file_name=None):
    file_dir, file_name = os.path.split(file_path)
    print('[plt] file_dir, file_name: ', file_dir, file_name)
    if not os.path.exists(new_file_dir):
        os.mkdir(new_file_dir)
    if new_file_name is None:
        new_file_path = os.path.join(new_file_dir, file_name.split('.')[0]) + '.json'
    else:
        new_file_path = os.path.join(new_file_dir, new_file_name)
    print('[json] new_file_path: ', new_file_path)

    data = read_file(file_path)
    json_data = data_convert(data)

    with open(new_file_path, 'w') as f:
        f.write(json.dumps(json_data))


if __name__ == '__main__':
    plt_to_json('F:\\GeolifeTrajectories1.3\\Data\\000\\Trajectory\\20081024020959.plt')

