from util.file_reader import FileReader
from similarity_computation.idc_DTW import dtw
from util.drawer import Drawer


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
        item_distance = dtw(trajectories[0], trajectories[i])
        print("distance[0, ", index_list[i], "]=", item_distance)
        m_drawer.add_reco(
            trajectories[i]["lat"].values,
            trajectories[i]["lon"].values,
            label=str(index_list[i]),
        )
    m_drawer.draw_user_and_reco()


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


if __name__ == "__main__":
    test_2()
