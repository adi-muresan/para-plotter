import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def plot_parametric(func, t_space, limits=((-100, 100), (-100, 100))):
    """Plots a parametric curve.

    :param func: Parametric function f(t) -> ((x, y), (nx, ny), step_len)
    :param t_space: Generato for parameter space of t in f(f).
    :param limits: Plot limits
    :return:
    """

    plt.style.use('dark_background')

    fig = plt.figure()
    ax = plt.axes(xlim=limits[0], ylim=limits[1])
    plt.axis('equal')
    line, = ax.plot([], [], lw=1)

    # initialization function
    def init():
        # creating an empty plot/frame
        line.set_data([], [])
        return line,

    # lists to store x and y axis points
    xdata, ydata = [], []

    # animation function
    def animate(i):
        # t is a parameter
        t = 0.1 * i

        # x, y values to be plotted
        # x = t * np.sin(t)
        # y = t * np.cos(t)
        (x, y) = func(i)[0]

        # appending new points to x, y axes points list
        xdata.append(x)
        ydata.append(y)
        line.set_data(xdata, ydata)
        return line,

    # plt.axis('equal')
    # plt.axis('off')

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=t_space, interval=2, blit=True)

    plt.show()
