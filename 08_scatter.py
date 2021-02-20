import matplotlib.pyplot as plt
import numpy as np

n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
c = np.arctan2(x, y)  # generate color value

plt.figure(figsize=(6,6))
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(())
plt.yticks(())

plt.scatter(x, y, s=75, c=c, cmap='rainbow', alpha=.5)

plt.show()