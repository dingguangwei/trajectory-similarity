# coding=utf-8
from util.file_reader import FileReader
from similarity_computation.dtw import dtw, isdc_dtw, idc_dtw
from util.drawer import Drawer
import numpy as np


# 计算相似度并且画出轨迹
def test_1():
    index_list = [0, 6, 7, 8, 9, 10]
    reader = FileReader()
    trajectories = reader.get_some_trajectory(index_list=index_list)

    m_drawer = Drawer()
    m_drawer.set_user_demand(
        trajectories[0]["lat"].values, trajectories[0]["lon"].values
    )

    for i in range(1, len(index_list)):
        item_distance = isdc_dtw(trajectories[0], trajectories[i])
        print("distance[0, ", index_list[i], "]=", item_distance)
        m_drawer.add_reco(
            trajectories[i]["lat"].values,
            trajectories[i]["lon"].values,
            label=str(index_list[i]),
        )
    m_drawer.draw_user_and_reco()


# 画轨迹
def test_2():
    index_list = range(1100, 1150)
    reader = FileReader()
    trajectories = reader.get_some_trajectory(index_list=index_list)

    m_drawer = Drawer()
    m_drawer.set_user_demand(
        trajectories[0]["lat"].values, trajectories[0]["lon"].values
    )

    for i in range(1, len(index_list)):
        m_drawer.add_reco(
            trajectories[i]["lat"].values,
            trajectories[i]["lon"].values,
            label=str(index_list[i]),
        )
    m_drawer.draw_user_and_reco()


def test_3():
    user_demand = np.array(
        [
            [116.401987, 40.000061],
            [116.395448, 39.933315],
            [116.404143, 39.909299],
            [116.396094, 39.909133],
        ]
    )
    user_demand_x = user_demand[:, 0]
    user_demand_y = user_demand[:, 1]


if __name__ == "__main__":
    test_2()
