import math

class CoordinatePair:
    def __init__(self, first, second):
        pair = [first, second]
        pair.sort()
        self.coordinates = pair
        self.seperation = math.sqrt((second[0] - first[0]) ** 2 + (second[1] - first[1]) ** 2 + (second[2] - first[2]) ** 2 )

    def __eq__(self, other):
        if isinstance(other, CoordinatePair):
            return self.coordinates == other.coordinates and self.seperation == other.seperation
        return False