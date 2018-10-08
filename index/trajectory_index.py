# coding=utf-8

from rtree import index
import time
from util.file_reader import FileReader
from util.print_log import print_error
from conf.config_reader import get_debug_model
import pandas as pd


class TrajectoryIndex():
    dict_index = {}
    rtree_index = index.Index(properties=index.Property())

    # 北纬40.182947度（北六环），每15米对应经度变化
    delta_lon = 0.00017657112768522496
    # 每15米对应纬度变化
    delta_lat = 0.00013489824088780959

    def __init__(self, trajectory_list=None, trajectory_id_list=None, index_list=None):
        if trajectory_list is None or trajectory_id_list is None:
            reader = FileReader()
            if not index_list is None:
                trajectory_list, trajectory_id_list = reader.get_some_trajectory(
                    index_list
                )
            else:
                file_number = None
                if get_debug_model():
                    file_number = 200
                trajectory_list, trajectory_id_list = reader.get_all_trajectory(file_number=file_number)

        self.create_dict_index(trajectory_list, trajectory_id_list)
        self.create_rtree_index_by_sample_point()

    def create_dict_index(self, trajectory_list, trajectory_id_list):
        start_time = time.time()
        print("\ncreate_dict_index...")
        for i in range(len(trajectory_list)):
            self.dict_index[trajectory_id_list[i]] = trajectory_list[i]
        end_time = time.time()
        print("create_dict_index complete! Using ", (end_time-start_time), 's')

    def get_trajectory_by_id(self, id):
        return self.dict_index[id]

    def get_trajectory_by_ids(self, id_list):
        trajectory_list = []
        for id in id_list:
            trajectory_list.append(self.dict_index[id])
        return trajectory_list

    # 利用sample_point构造rtree_index
    def create_rtree_index_by_sample_point(self):
        start_time = time.time()
        print("\ncreate_rtree_index_by_sample_point...")
        for id in self.dict_index:
            trajectory = self.get_trajectory_by_id(id)
            for i in range(len(trajectory)):
                lon = trajectory.at[i, "lon"]
                lat = trajectory.at[i, "lat"]
                mbr = (
                    lon - self.delta_lon,
                    lat - self.delta_lat,
                    lon + self.delta_lon,
                    lat + self.delta_lat,
                )
                self.rtree_index.insert(id=id, coordinates=mbr)
        end_time = time.time()
        print("create_rtree_index_by_sample_point complete! Using ", (end_time-start_time), 's')

    def get_intersection_trajectory_ids(self, mbr = None,  min_lon= None, min_lat = None, max_lon = None, max_lat = None):
        if mbr is None:
            if min_lat is None and min_lon is None and max_lat is None and max_lon is None:
                print_error('get_intersection_trajectory_ids: mbr and lat and lon are None!')
            mbr = (min_lon, min_lat, max_lon, max_lat)
        id_set = set()
        hits = self.rtree_index.intersection(coordinates=mbr, objects=True)
        for hit in hits:
            id_set.add(hit.id)
        return id_set


if __name__ == "__main__":
    mbr = (116.291595, 40.00225, 116.326952, 40.024796)
    # mbr = (115, 30, 118, 45)
    index_service = TrajectoryIndex()
    print(index_service.get_intersection_trajectory_ids(mbr=mbr))
