import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)

y1 = 2*x + 1
y2 = x**2 - 4

plt.figure()
plt.plot(x, y1, color='red', linewidth=1., linestyle='--')
plt.plot(x, y2)

plt.xlim((0,2))
plt.ylim((-4,6))
plt.xlabel('X Label')
plt.ylabel('Y Label')

# ticks
x_ticks = np.linspace(-2, 3, 11)
plt.xticks(x_ticks)
plt.yticks(
    [-1., 1.5, 4., 5.5],
    ['Low' ,'Normal', 'High', r'$So\ high$']  # r'$str$': latex math
)


plt.show()