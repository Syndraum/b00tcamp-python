from FileLoader import FileLoader
from YoungestFellah import youngestFellah

loader = FileLoader()
data = loader.load("../athlete_events.csv")
youngestFellah(data, 2004)
