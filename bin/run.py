# coding=utf-8
from similarity_computation.dtw import dtw, isdc_dtw, idc_dtw
from util.drawer import Drawer
from similarity_computation.recommend import get_similarity_trajectory
from util.file_reader import FileReader
from conf.config_reader import get_algorithm_code
import numpy as np
import pandas as pd


# 计算相似度并且画出轨迹
def fun_1():
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
def fun_2(user_demand, trajectories):
    drawer = Drawer(user_demand=user_demand, trajectories=trajectories)
    drawer.draw_user_and_reco()

# 计算最相似的轨迹并作图
def fun_3(user_demand, trajectories):
    n = 20

    dtw_distance, dtw_similarity_order = get_similarity_trajectory(
        user_demand=user_demand,
        trajectories=trajectories,
        algorithm_code=get_algorithm_code(),
        n=n,
    )

    print("dtw_similarity_order:", list(dtw_similarity_order))

    similarity_trajectories = []
    for i in dtw_similarity_order:
        similarity_trajectories.append(trajectories[i])

    drawer = Drawer(
        user_demand=user_demand,
        trajectories=similarity_trajectories,
        trajectories_label=list(dtw_similarity_order),
    )
    drawer.draw_user_and_reco()


if __name__ == "__main__":
    user_demand = pd.DataFrame(
        data=[
            [116.401987, 40.000061],
            [116.395448, 39.933315],
            [116.404143, 39.909299],
            [116.396094, 39.909133],
        ],
        columns=["lon", "lat"],
    )
    reader = FileReader()
    trajectories = reader.get_all_trajectory(file_number=550)


    fun_2(user_demand, trajectories[500:550])


# dtw 距离最短的索引
# [16395, 14265, 14710, 14242, 14240, 13724, 11836, 3044, 14545, 12860, 12850, 12846, 3251, 5560, 5874, 5687, 10052, 5476, 329, 5547]
