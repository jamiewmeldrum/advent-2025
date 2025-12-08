class Circuit:
    def __init__(self):
        self.coordinates = set()


    def add_to_circuit(self, coordinate):
        if coordinate not in self.coordinates:
            self.coordinates.add(coordinate)


    def contains_coordinate(self, coordinate):
        return coordinate in self.coordinates
    

    def merge(self, other):
        new_circuit = Circuit()
        for coordinate in self.coordinates:
            new_circuit.add_to_circuit(coordinate)
        for coordinate in other.coordinates:
            new_circuit.add_to_circuit(coordinate)
        
        return new_circuit