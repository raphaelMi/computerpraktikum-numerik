import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

import init
import shared


# Called by main module upon init
def setup():
    global plot_visible

    plot_visible = False


# Called in case something should be plotted and no plot window is there
def init_plot(flocks):
    global ax
    global fig
    global plot_visible

    plt.ion()  # Make plot non-blocking, we it can be updated while the simulation runs
    plt.show()
    plt.pause(init.PLOT_PAUSE_TIME)

    fig, ax = plt.subplots(len(flocks))

    plt.subplots_adjust(hspace=1)

    fig.canvas.mpl_connect('close_event', on_close_event)
    fig.canvas.set_window_title(init.PLOT_WINDOW_TITLE)

    plot_visible = True


# Called by main every frame
def update_plot(flocks):
    if not plot_visible:
        init_plot(flocks)

    for i in range(len(flocks)):
        flock = flocks[i]
        axis = ax[i]

        axis.clear()

        # clear() also removes axis descriptions, so we've to add it again
        axis.set_xlabel("Fish")
        axis.set_ylabel("Velocity")
        axis.set_title("Flock " + str(i + 1))

        # Plot a bar diagram
        axis.bar([i for i in range(1, flock.population + 1)],
                 [np.linalg.norm(flock.velocities[i]) for i in range(flock.population)],
                 color=np.asarray(flock.color).astype('float64') * 255 ** -1)

        plt.draw()
        plt.pause(init.PLOT_PAUSE_TIME)


# Called my main when the plot should be closed
def close():
    global plot_visible

    plt.close()
    plot_visible = False


# Callback when the user closed the plot
def on_close_event(arg):
    global plot_visible

    shared.display_plots = False
    plot_visible = False


# Draw a curve of the deviations in velocity
def draw_curves(data):
    # plt.ion()  # Make plot non-blocking, we it can be updated while the simulation runs
    plt.plot(data)
    plt.show()
