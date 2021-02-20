import matplotlib.pyplot as plt
import numpy as np

n = 12
x = np.arange(n)
y_upper = (1-x/n) * np.random.uniform(0.5, 1.0, n)
y_downer = (1-x/n) * np.random.uniform(0.5, 1.0, n)

# set axes
plt.xlim(-1, n)
plt.ylim(-1.25, 1.25)
plt.xticks(())
plt.yticks(())

plt.bar(x, +y_upper, facecolor='#9999ff', edgecolor='white')
plt.bar(x, -y_downer, facecolor='#ff9999', edgecolor='white')

# add annotation
for i, j in zip(x, y_upper):
    plt.text(i, j, '{:.2f}'.format(j), ha='center', va='bottom')
    # ha: horizontal alignment, va: vertical alignment

for i, j in zip(x, y_downer):
    plt.text(i, -j-0.02, '{:.2f}'.format(j), ha='center', va='top')


plt.show()
