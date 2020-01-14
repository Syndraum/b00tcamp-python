class Vector:
    def __init__(self, values):
        self.values = values

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        vector = []
        if isinstance(values, list):
            for number in values:
                if not isinstance(number, float):
                    raise ValueError("Only float values in vector")
            vector = values
        elif isinstance(values, int):
            for i in range(0, values, -1 if 0 > values else 1):
                vector.append(float(i))
        elif isinstance(values, tuple) and len(values) == 2:
            if not isinstance(values[0], int) or not isinstance(values[1], int):
                raise ValueError("No int in tuple")
            for i in range(values[0], values[1], -1 if values[0] > values[1] else 1):
                vector.append(float(i))
        else:
            raise ValueError("Incorrect Value")
        self._values = vector
        self.size = len(vector)

    def __add__(self, other):
        vector = Vector(0)
        for i in range(self.size):
            if isinstance(other, int):
                vector.values.append(self.values[i] + other)
            elif isinstance(other, Vector):
                vector.values.append(self.values[i] + other.values[i])
            vector.size = len(vector.values)
        return vector

    def __radd__(self, add):
        return self.__add__(add)

    def __sub__(self, other):
        vector = Vector(0)
        for i in range(self.size):
            if isinstance(other, int):
                vector.values.append(self.values[i] - other)
            elif isinstance(other, Vector):
                vector.values.append(self.values[i] - other.values[i])
            vector.size = len(vector.values)
        return vector

    def __rsub__(self, add):
        return self.__sub__(add)

    def __mul__(self, other):
        vector = Vector(0)
        for i in range(self.size):
            if isinstance(other, int):
                vector.values.append(self.values[i] * other)
            elif isinstance(other, Vector):
                vector.values.append(self.values[i] * other.values[i])
            vector.size = len(vector.values)
        return vector

    def __rmul__(self, add):
        return self.__mul__(add)

    def __str__(self):
        return "(Vector " + str(self.values) + ") len : " + str(self.size)

    def __repr__(self):
        return {"values": self.name, "size": self.name}
