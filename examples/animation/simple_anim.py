"""
===========
Simple Anim
===========

A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimatedLine(object):
    def __init__(self):
        self.fig, ax = plt.subplots()
        self.x = np.arange(0, 2 * np.pi, 0.01)
        self.line, = ax.plot(self.x, np.sin(self.x))

    def animate(self, i):
        self.line.set_ydata(np.sin(self.x + i/10.0))  # update the data
        return self.line,

    def init(self):
        self.line.set_ydata(np.ma.array(self.x, mask=True))
        return self.line,

# l1 = AnimatedLine()
l2 = AnimatedLine()

# ani = animation.FuncAnimation(l1.fig, l1.animate, np.arange(1, 200), init_func=l1.init,
#                               interval=2000, blit=True)

ani2 = animation.FuncAnimation(l2.fig, l2.animate, np.arange(1, 200), init_func=l2.init,
                              interval=20, blit=True)

plt.show()
