# coding=utf-8
import matplotlib.pyplot as plt


class Drawer:
    font1 = {"family": "Times New Roman", "weight": "normal", "size": 9}
    font2 = {"family": "Times New Roman", "weight": "normal", "size": 14}

    user_demand_x = []
    user_demand_y = []
    user_color = "black"
    user_label = "userDemand"
    user_line_width = 1.5

    reco_x_list = []
    reco_y_list = []
    reco_color = ["yellow", "red", "blue", "green"]
    reco_color_index = 0
    reco_label_list = []
    reco_line_width = 0.9

    def __init__(self):
        self.figSize = 8, 9
        plt.subplots(figsize=self.figSize)  # 设定整张图片大小

    def set_user_demand(self, x, y):
        self.user_demand_x = x
        self.user_demand_y = y

    def add_reco(self, x, y, label="reco"):
        self.reco_x_list.append(x)
        self.reco_y_list.append(y)
        self.reco_label_list.append(label)

    def draw(self, x, y, color="red", label="label", line_width=0.8):
        plt.plot(x, y, color=color, label="$" + label + "$", linewidth=line_width)

    def get_reco_color(self):
        self.reco_color_index += 1
        self.reco_color_index %= len(self.reco_color)
        return self.reco_color[self.reco_color_index]

    def draw_user_and_reco(self):
        if len(self.user_demand_x) != 0:
            self.draw(
                self.user_demand_x,
                self.user_demand_y,
                color=self.user_color,
                label=self.user_label,
                line_width=self.user_line_width,
            )
            plt.legend(loc="upper right", prop=self.font1, frameon=False)  # 绘制图例，指定图例位置
        for i in range(len(self.reco_x_list)):
            self.draw(
                self.reco_x_list[i],
                self.reco_y_list[i],
                color=self.get_reco_color(),
                label=self.reco_label_list[i],
                line_width=self.reco_line_width,
            )
            plt.legend(loc="upper right", prop=self.font1, frameon=False)  # 绘制图例，指定图例位置
        plt.show()


if __name__ == "__main__":
    drawer = Drawer()
    drawer.set_user_demand([1, 2, 3, 4], [16, 3, 7, 1])
    drawer.add_reco([1, 2, 3, 4], [6, 8, 2, 8])
    drawer.add_reco([4, 5, 6, 7], [3, 5, 7, 2])
    drawer.draw_user_and_reco()