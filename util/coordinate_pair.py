import math

class CoordinatePair:
    def __init__(self, first, second):
        pair = [first, second]
        pair.sort()
        self.coordinates = pair

        distance_squared = 0
        if len(first) >= 1 and len(second) >= 1:
            distance_squared += (second[0] - first[0]) ** 2
        if len(first) >= 2 and len(second) >= 2:
            distance_squared += (second[1] - first[1]) ** 2
        if len(first) >= 3 and len(second) >= 3:
            distance_squared += (second[2] - first[2]) ** 2
        self.seperation = math.sqrt(distance_squared)


    def __eq__(self, other):
        if isinstance(other, CoordinatePair):
            return self.coordinates == other.coordinates and self.seperation == other.seperation
        return False
    

    def print(self):
        print(f"First coordinate - {self.coordinates[0]}")
        print(f"Second coordinate - {self.coordinates[1]}")