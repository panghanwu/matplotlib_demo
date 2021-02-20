import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)

y1 = 2*x + 1
y2 = x**2 - 4

plt.figure()

l1, = plt.plot(x, y1, color='red', linewidth=1., linestyle='--', label='Line')
l2, = plt.plot(x, y2, label='Curve')

# add legend
plt.legend(handles=[l1,l2,], loc='best')

plt.xlim((0,3))
plt.ylim((-4,6))
plt.xlabel('X Label')
plt.ylabel('Y Label')

plt.show()