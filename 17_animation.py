from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))  # suffix "," means tuple

def action(t):
    # update values of y at t
    line.set_ydata(np.sin(x+t/50))
    return line,

def init():
    # update values of y at t
    line.set_ydata(np.sin(x))
    return line,


anm = animation.FuncAnimation(
    fig = fig, 
    func = action, 
    frames = 500, # total frames
    init_func = init,  # the first frame
    interval = 20,  # per ms
    blit = True  # only update changed pixels
)

plt.show()