from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


imp = ImageProcessor()
arr = imp.load("elon.jpg")
cf = ColorFilter()
cf.to_grayscale(arr, "w")
imp.display(arr)
