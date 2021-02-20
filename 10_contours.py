import matplotlib.pyplot as plt
import numpy as np

def height(x, y):
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

x_grid, y_grid = np.meshgrid(x, y)

# create figure
plt.figure(figsize=(6,6))
plt.xticks(())
plt.yticks(())

# contourf: filled contour 
plt.contourf(x_grid, y_grid, height(x_grid, y_grid), 8, alpha=.75, cmap='hot')
# plot contour lines
ct_line = plt.contour(x_grid, y_grid, height(x_grid, y_grid), 8, colors='black', linewidths=.7)

# add labels
plt.clabel(ct_line, inline=True, fontsize=10)

plt.show()
