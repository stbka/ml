import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

class ImageGen():

    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.initCleanImage()
        self.storage_path = '../data'

    def initCleanImage(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, self.max_x)
        self.ax.set_ylim(0, self.max_y)

    def setStoragePath(self, path):
        self.storage_path = path

    def plot2dArray(self, points, format, alpha=1):
        for p in points:
            self.ax.plot(p[0], p[1], format, alpha=alpha)

    def show(self):
        plt.show()

    def store(self, path, name='img'):
        if not os.path.exists(path):
            os.makedirs(path)
        self.fig.savefig(os.sep.join([path, 'img-{}.png'.format(self.__getTimestamp())]))

    def __getTimestamp(self):
        t = datetime.datetime.now()
        return str((t - datetime.datetime(1970,1,1)).total_seconds()).replace('.', '')

    # scatter
    def __example_1(self):
        n = 1024
        X = np.random.normal(0, 1, n)
        Y = np.random.normal(0, 1, n)
        T = np.arctan2(Y, X)

        plt.axes([0.025, 0.025, 0.95, 0.95])
        plt.scatter(X, Y, s=10, c=T, alpha=.5)

        plt.xlim(-1.5, 1.5)
        plt.xticks(())
        plt.ylim(-1.5, 1.5)
        plt.yticks(())

        plt.show()

    # single point
    def __example_2(self):
        # matplotlib.rcParams['axes.unicode_minus'] = False
        fig, ax = plt.subplots()
        ax.set_xlim(self.v_min, self.v_max)
        ax.set_ylim(self.v_min, self.v_max)
        ax.plot(10, 20, 'r.')
        ax.plot()
        plt.show()