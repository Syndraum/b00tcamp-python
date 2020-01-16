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
        for line in array:
            for pixel in line:
                for i in range(len(pixel)):
                    j = 256/thresholds
                    while pixel[i] >= j:
                        j += 256/thresholds
                    pixel[i] = j - 256/thresholds
