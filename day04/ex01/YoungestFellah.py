class YoungestFellah:
    def __init__(self, data, year):
        return {'f': data.min(level="Age"), 'm': 0}