from FileLoader import FileLoader
from YoungestFellah import *

loader = FileLoader()
data = loader.load("../athlete_events.csv")
# dict = youngestFellah(data, 2004)
# print(dict)
# print(proportionBySport(data, 2004, 'Tennis', 'F'))
# print (howManyMedals(data, 'Kjetil Andr Aamodt'))
sp = SpatioTemporalData(data)
print(sp.where(1896))
