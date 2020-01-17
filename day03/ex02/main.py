from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker

imp = ImageProcessor()
arr = imp.load("../42AI.png")
sb = ScrapBooker()
# arrm = sb.crop(arr, (150, 200), (50, 0))
# arrm = sb.thin(arr, 4, 0)
# arrm = sb.juxtapose(arr, 3, 0)
arrm = sb.mosaic(arr, (3, 2))
imp.display(arrm)
