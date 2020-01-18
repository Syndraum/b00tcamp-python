from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


imp = ImageProcessor()
arr = imp.load("sunflower.png")
cf = ColorFilter()
cf.to_grayscale(arr, "m")
imp.display(arr)
