from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


imp = ImageProcessor()
arr = imp.load("elon.jpg")
cf = ColorFilter()
cf.invert(arr)
imp.display(arr)
