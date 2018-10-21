# coding=utf-8
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.array([1]),
                      np.array([1]),
                      np.array([1]))

# Make the direction data for the arrows
u = np.array([1, 0, 0])
v = np.array([0, 1, 0])
w = np.array([0, 0, 1])

ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

plt.show()