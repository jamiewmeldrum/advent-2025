import sys

from util.coordinate_pair import CoordinatePair
from circuit import Circuit

def connect_circuits(input, iterations):

    rows = input.splitlines()

    coordinates = []
    for row in rows:
        entries = row.split(',')
        coordinate = (int(entries[0]), int(entries[1]), int(entries[2]))
        coordinates.append(coordinate)
            
    circuits = []
    for coordinate in coordinates:
        circuit = Circuit()
        circuit.add_to_circuit(coordinate)
        circuits.append(circuit)

    coordinate_pairs = []
    for i in range(0, len(coordinates)):
        for j in range(i+1, len(coordinates)):
            coordinate_pairs.append(CoordinatePair(coordinates[i], coordinates[j]))
    coordinate_pairs.sort(key=lambda x: x.seperation)

    iteration = 0
    coordinate_pairs = iter(coordinate_pairs)
    next_pair = next(coordinate_pairs)
    while iteration < iterations and next_pair:

        matched_circuits = []
        circuits_copy = circuits.copy()
        for circuit in circuits:
            if circuit.contains_coordinate(next_pair.coordinates[0]) or circuit.contains_coordinate(next_pair.coordinates[1]):

                #A bit hacky, but I need the last two coordinates added and I don't really want to rework to track this
                if not circuit.contains_coordinate(next_pair.coordinates[0]):
                    print(next_pair.coordinates[0])
                if not circuit.contains_coordinate(next_pair.coordinates[1]):
                    print(next_pair.coordinates[1])

                circuits_copy.remove(circuit)
                circuit.add_to_circuit(next_pair.coordinates[0])
                circuit.add_to_circuit(next_pair.coordinates[1])
                matched_circuits.append(circuit)

        final_circuit = matched_circuits[0]
        for i in range(1, len(matched_circuits)):
            final_circuit = final_circuit.merge(matched_circuits[i])

        circuits_copy.append(final_circuit)
        circuits = circuits_copy

        iteration += 1
        next_pair = next(coordinate_pairs, None)

    passcode = ""
    lengths = list(map(lambda x: len(x.coordinates), circuits))
    lengths.sort(reverse=True)
    if len(lengths) == 1:
        passcode = lengths[0]
    elif len(lengths) == 2:
        passcode = lengths[0] * lengths[1]
    elif len(lengths) == 3:
        passcode = lengths[0] * lengths[1] * lengths[2]

    return passcode


def main():

    sys_args = sys.argv
    if len(sys_args) != 3:
        print("Usage: python3 main.py <input_file> <iterations>")
        sys.exit(1)

    input_file = sys_args[1]
    iterations = int(sys_args[2])

    input = None
    with open(input_file) as f:
        input =  f.read()

    if not input:
        raise Exception("No input read")
    
    passcode = connect_circuits(input, iterations)

    print(f"The passcode is {passcode}")
   
main()