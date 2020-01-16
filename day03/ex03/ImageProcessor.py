from PIL import Image
import numpy as np


class ImageProcessor:
    def load(self, path):
        self.img = Image.open(path)
        self.array = np.array(self.img)
        print(
            "Loading image of dimensions",
            self.array.shape[0], "x", self.array.shape[1])
        self.img.close()
        return self.array

    def display(self, array):
        self.render = Image.fromarray(array)
        self.render.show()
