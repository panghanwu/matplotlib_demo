import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)

y1 = 2*x + 1
y2 = x**2 - 4

plt.figure()
plt.plot(x, y1)

plt.figure()
plt.plot(x, y2)

plt.figure(num=6, figsize=(6,6))
plt.plot(x, y1, color='red', linewidth=1., linestyle='--')
plt.plot(x, y2)

plt.show()