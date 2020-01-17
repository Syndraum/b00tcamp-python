import numpy as np


class ColorFilter:
    def invert(self, array):
        for line in array:
            for pixel in line:
                for i in range(len(pixel)):
                    pixel[i] = -(pixel[i] - 256)

    def to_blue(self, array):
        for line in array:
            for pixel in line:
                pixel[0] = 0
                pixel[1] = 0

    def to_green(self, array):
        for line in array:
            for pixel in line:
                pixel[0] = 0
                pixel[2] = 0

    def to_red(self, array):
        for line in array:
            for pixel in line:
                pixel[1] = 0
                pixel[2] = 0

    def celluloid(self, array, thresholds=4):
        lst = np.linspace(0, 256, num=thresholds, endpoint=False)
        print(lst)
        for line in array:
            for pixel in line:
                for i in range(len(pixel)):
                    for seuil in reversed(lst):
                        if seuil < pixel[i]:
                            pixel[i] = seuil
                            break

    def to_grayscale(self, array, fil="mean"):
        if fil is "m" or fil is "mean":
            for line in array:
                for pixel in line:
                    grey = sum(pixel) / array.shape[2]
                    for i in range(len(pixel)):
                        pixel[i] = grey
        elif fil is "w" or fil is "weighted":
            for line in array:
                for pixel in line:
                    grey = np.sum([
                        0.21 * pixel[0],
                        0.72 * pixel[1],
                        0.07 * pixel[2]])
                    for i in range(len(pixel)):
                        pixel[i] = grey
