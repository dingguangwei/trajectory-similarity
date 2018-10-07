# coding=utf-8

from rtree import index
from util.file_reader import FileReader
import pandas as pd


class IndexService:
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
                trajectory_list, trajectory_id_list = reader.get_all_trajectory(
                    file_number=200
                )
        self.create_dict_index(trajectory_list, trajectory_id_list)
        self.create_rtree_index_by_sample_point()

    def create_dict_index(self, trajectory_list, trajectory_id_list):
        print("\ncreate_dict_index...")
        for i in range(len(trajectory_list)):
            self.dict_index[trajectory_id_list[i]] = trajectory_list[i]
        print("create_dict_index complete!")

    def get_trajectory_by_id(self, id):
        return self.dict_index[id]

    def get_trajectory_by_ids(self, id_list):
        trajectory_list = []
        for id in id_list:
            trajectory_list.append(self.dict_index[id])
        return trajectory_list

    # 利用sample_point构造rtree_index
    def create_rtree_index_by_sample_point(self):
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
        print("create_rtree_index_by_sample_point complete!")

    def get_intersection_trajectory_ids(self, mbr):
        id_set = set()
        hits = self.rtree_index.intersection(coordinates=mbr, objects=True)
        for hit in hits:
            id_set.add(hit.id)
        return id_set


if __name__ == "__main__":
    mbr = (116.424867, 39.907368, 116.442366, 39.914563)
    # mbr = (115, 30, 118, 45)
    index_service = IndexService()
    print(index_service.get_intersection_trajectory_ids(mbr))
