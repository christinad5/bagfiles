from matplotlib import pyplot as plt
import numpy as np


def lin_acc_plots(filename, title, axis):
    time, x, y, z = np.loadtxt(filename, unpack=True, delimiter=",")

    if axis == 'x':
        plt.title(title, fontsize=25)
        plt.ylabel("Linear Acceleration [m/s^2]", fontsize=20)
        plt.xlabel("Time [s]", fontsize=20)
        plt.plot(time, x)
        plt.show()
    elif axis == 'y':
        plt.title(title, fontsize=25)
        plt.ylabel("Linear Acceleration [m/s^2]", fontsize=20)
        plt.xlabel("Time [s]", fontsize=20)
        plt.plot(time, y)
        plt.show()
    elif axis == 'z':
        plt.title(title, fontsize=25)
        plt.ylabel("Linear Acceleration [m/s^2]", fontsize=20)
        plt.xlabel("Time [s]", fontsize=20)
        plt.plot(time, z)
        plt.show()
    else:
        "Axis not specified correctly"


lin_acc_plots('up_z.csv', 'Z-axis offset in upwards orientation', 'z')