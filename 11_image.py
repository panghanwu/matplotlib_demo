import matplotlib.pyplot as plt
import numpy as np

pixels = np.arange(16).reshape(4, 4)

plt.figure()
plt.xticks(())
plt.yticks(())

plt.imshow(pixels, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=.8)


plt.show()