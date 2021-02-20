import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

x0 = 1
y0 = 2*x0 + 1

plt.figure()

# set axes to (0, 0)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))

# plot
plt.plot(x, y)
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0,x0], [y0,0], 'k--', lw=2.5)

# add annotation
# method 1
plt.annotate(
    r'$2x+1={}$'.format(y0), 
    xy = (x0,y0), 
    xycoords = 'data', 
    xytext = (+30,-30), 
    textcoords ='offset points',
    fontsize = 16,
    arrowprops = dict(
        arrowstyle = '->',
        connectionstyle = 'arc3,rad=.2'
    )
)

# method 2 (by add text)
plt.text(-2.5, 3, r'$\alpha\ is\ the\ first.$', fontdict={'size':16,'color':'red'})

plt.show()