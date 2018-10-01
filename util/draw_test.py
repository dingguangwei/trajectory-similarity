# coding=utf-8
import matplotlib.pyplot as plt

y0 = [1, 2, 3]
y1 = [6, 5, 6]
y2 = [7, 8, 9]
y3 = [10, 11, 12]
y4 = [13, 14, 15]


font1 = {"family": "Times New Roman", "weight": "normal", "size": 9}
font2 = {"family": "Times New Roman", "weight": "normal", "size": 14}

figsize = 8, 9
plt.subplots(figsize=figsize)  # 设定整张图片大小

# ax1 = plt.subplot(1, 4, 2)
# ax1.yaxis.set_major_locator(MultipleLocator(15))  # 设定y轴刻度间距
# 第一条线
x = range(0, len(y0))
print(len(x))
print(y0)
plt.plot(x, y0, color="black", label="$DT$", linewidth=0.8)  # 绘制，指定颜色、标签、线宽，标签采用latex格式
# plt.ylim(-90, -20)  # 设定y轴范围
hl = plt.legend(loc="upper right", prop=font1, frameon=False)  # 绘制图例，指定图例位置
# set(hl,'Box','off');

# 第二条曲线
x = range(0, len(y1))
plt.plot(x, y1, color="yellow", label="$M_1$", linewidth=0.8)
plt.legend(loc="upper right", prop=font1, frameon=False)  # 绘制图例，指定图例位置
plt.xticks([])  # 去掉x坐标轴刻度
# plt.xlim(0, 580)  # 设定x轴范围
#
# ax2 = plt.subplot(4, 1, 2)
# ax2.yaxis.set_major_locator(MultipleLocator(15))
# x = range(0, len(y0))
# plt.plot(x, y0, color="black", label="$DT$", linewidth=0.8)
# plt.ylim(-90, -20)
# hl = plt.legend(loc="upper right", prop=font1, frameon=False)
# # set(hl,'Box','off');
# x = range(0, len(y2))
# plt.plot(x, y2, color="red", label="$M_2$", linewidth=0.8)
# plt.legend(loc="upper right", prop=font1, frameon=False)
# plt.ylabel("strength/dBm", font2)
# plt.xticks([])
# plt.xlim(0, 580)
#
# ax3 = plt.subplot(4, 1, 3)
# ax3.yaxis.set_major_locator(MultipleLocator(15))
# x = range(0, len(y0))
# plt.plot(x, y0, color="black", label="$DT$", linewidth=0.8)
# hl = plt.legend(loc="upper right", prop=font1, frameon=False)
# # set(hl,'Box','off');
# plt.ylim(-90, -20)
# x = range(0, len(y3))
# plt.plot(x, y3, color="red", label="$M_3$", linewidth=0.8)
# plt.legend(loc="upper right", prop=font1, frameon=False)
# plt.xticks([])
# plt.xlim(0, 580)
#
# ax4 = plt.subplot(4, 1, 4)
# ax4.yaxis.set_major_locator(MultipleLocator(15))
# ax4.xaxis.set_major_locator(MultipleLocator(50))
# x = range(0, len(y0))
# plt.plot(x, y0, color="black", label="$DT$", linewidth=0.8)
# plt.ylim(-90, -20)
# hl = plt.legend(loc="upper right", prop=font1, frameon=False)
# # set(hl,'Box','off');
# x = range(0, len(y4))
# plt.plot(x, y4, color="red", label="$M_4$", linewidth=0.8)
# plt.legend(loc="upper right", prop=font1, frameon=False)
# plt.xlabel("index of grids in path", font2)
# plt.xlim(0, 580)

# plt.savefig("1.png", dpi=600))

plt.show()
