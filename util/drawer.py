# coding=utf-8
from conf.config_reader import get_debug_model
import matplotlib.pyplot as plt
import pandas as pd


class Drawer:
    font1 = {"family": "Times New Roman", "weight": "normal", "size": 9}
    font2 = {"family": "Times New Roman", "weight": "normal", "size": 14}
    # min_lon, min_lat = 116.105906, 39.699716
    # max_lon, max_lat = 116.68887, 40.137988
    min_lon, min_lat = 0, 0
    max_lon, max_lat = 9, 9

    user_demand_lon = []
    user_demand_lat = []
    user_color = "black"
    user_label = "userDemand"
    user_line_width = 1.5

    reco_lon_list = []
    reco_lat_list = []
    reco_color = ["yellow", "red", "blue", "green"]
    reco_color_index = 0
    reco_label_list = []
    reco_line_width = 0.9

    # user_demand=pd.DataFrame(), trajectories=[trajectory, trajectory2...]
    def __init__(self, user_demand=None, trajectories=None, trajectories_label=None):
        self.figSize = 8, 9
        plt.subplots(figsize=self.figSize)  # 设定整张图片大小
        if not user_demand is None:
            self.set_user_demand(list(user_demand["lon"]), list(user_demand["lat"]))
        if not trajectories is None:
            for trajectory in trajectories:
                self.add_reco(list(trajectory["lon"]), list(trajectory["lat"]))
        if not trajectories_label is None:
            self.reco_label_list.clear()
            self.reco_label_list = trajectories_label
        if get_debug_model() is True:
            print("reco length", len(self.reco_lon_list))
            print("self.reco_label_list: ", self.reco_label_list)

    def set_user_demand(self, lon, lat):
        self.user_demand_lon = lon
        self.user_demand_lat = lat

    def add_reco(self, lon, lat, label="reco"):
        self.reco_lon_list.append(lon)
        self.reco_lat_list.append(lat)
        self.reco_label_list.append(label)

    def draw(self, lon, lat, color="red", label="label", line_width=0.8):
        plt.plot(
            lon, lat, color=color, label="$" + str(label) + "$", linewidth=line_width
        )

    def get_reco_color(self):
        self.reco_color_index += 1
        self.reco_color_index %= len(self.reco_color)
        return self.reco_color[self.reco_color_index]

    def draw_user_and_reco(self):
        if len(self.user_demand_lon) != 0:
            self.draw(
                self.user_demand_lon,
                self.user_demand_lat,
                color=self.user_color,
                label=self.user_label,
                line_width=self.user_line_width,
            )
            plt.legend(loc="upper right", prop=self.font1, frameon=False)  # 绘制图例，指定图例位置
        for i in range(len(self.reco_lon_list)):
            self.draw(
                self.reco_lon_list[i],
                self.reco_lat_list[i],
                color=self.get_reco_color(),
                label=self.reco_label_list[i],
                line_width=self.reco_line_width,
            )
            plt.legend(loc="upper right", prop=self.font1, frameon=False)  # 绘制图例，指定图例位置
        # plt.xlim(self.min_lon, self.max_lon)
        # plt.ylim(self.min_lat, self.max_lat)
        plt.show()


if __name__ == "__main__":
    drawer = Drawer()
    drawer.set_user_demand([1, 2, 3,], [1, 1.5, 2])
    drawer.add_reco([1, 2.1, 3, 8], [1.1, 1, 1.9, 2], label='CarA')
    drawer.add_reco([1, 2, 3], [2, 2.25, 3], label='CarB')
    drawer.draw_user_and_reco()
