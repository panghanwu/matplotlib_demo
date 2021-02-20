from mpl_toolkits.mplot3d import Axes3D  # 3D-axis module
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)

x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# create figure
fig = plt.figure(figsize=(6,6))
ax = Axes3D(fig)  # plot 3D-axis

# plot on "ax"
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
ax.contourf(x, y, z, zdir='z', offset=-1.5, cmap='rainbow')  # projection
ax.set_zlim(-2, 2)

plt.show()