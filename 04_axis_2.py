import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)

y1 = 2*x + 1
y2 = x**2 - 4

plt.figure()
plt.plot(x, y1, color='red', linewidth=1., linestyle='--')
plt.plot(x, y2)

plt.xlim((0,3))
plt.ylim((-4,6))
plt.xlabel('X Label')
plt.ylabel('Y Label')

# gca: get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',1))
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',-1))


plt.show()