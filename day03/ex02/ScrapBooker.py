import numpy as np


class ScrapBooker:
    def crop(slef, array, dimensions, position):
        return array[position[0]:position[0]+dimensions[0], position[1]:position[1]+dimensions[1]]

    def thin(self, array, n, axis):
        return np.delete(array, np.arange(n - 1, array.shape[axis], n), axis)

    def juxtapose(self, array, n, axis):
        return np.concatenate([array] * n, axis)

    def mosaic(self, array, dimensions):
        return np.tile(array, (dimensions[0], dimensions[1], 1))
