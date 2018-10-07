# coding=utf-8
"""
    using rtree to create trajectory index
"""

from rtree import index

p = index.Property()
idx = index.Index(properties=p)

arr = [30, 30, 40, 40, 35, 35, 45, 45, 62, 62, 80, 80]
for i in range(3):
    print(i, " : ", tuple(arr[4*i:4*i+4]))
    idx.insert(i, tuple(arr[4*i:4*i+4]), obj=i)
idx.insert(4321,(34.3776829412, 26.7375853734, 49.3776829412,41.7375853734),obj=42)

idx.insert(11, (0, 0, 10, 10), 11)
idx.insert(11, (5, 5, 15, 15), 11)
hits1 = idx.intersection((6, 6, 7, 7), objects=True)
for i in hits1:
    print(i.id, ' = ', i.object, ' = ', i.bbox)

# 在id为4321的占位符处插入42并保存，
# print(idx.count((0, 0, 20, 20)))
# 进行判断给定的四个点的范围与已经存在的四点或者多点构成的范围是不是有相交的点
hits = idx.intersection((0, 0, 60, 60), objects=True)
# 找出与（0，0，60，60）有公共区域的所有的区域
# #计算这些点有已经存在的点的交点
# 与它有交点的应该有很多，但我们只要，id为4321处的交点。
for i in hits:
    if i.object == 42:
        print(i.object)
        print(i.bbox)

# 在这些有公共区域的区域内id为4321的区域的范围以及obj
# 对这段代码进行一个简单的注释，进行一个索引属性的设置，在索引列表中添加数据，
print(list(idx.intersection((38, 38, 39, 40), objects='raw')))
# 将所有的与（0，0，60，60）有交集所有区域的bojects进行输出。
