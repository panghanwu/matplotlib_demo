import matplotlib.pyplot as plt

fig = plt.figure()

x = [1, 2, 3, 4, 5, 6]
y = [1, 6, 2, 5, 3, 4]

# plot main figure
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Title')

# plot insert
left, bottom, width, height = 0.2, 0.58, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, y, 'b')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Insert 1')

# another method for insert
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(x, y, 'g')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
plt.title('Insert 2')

plt.show()