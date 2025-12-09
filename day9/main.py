import sys

from util.coordinate_pair import CoordinatePair

def calculate_rectangular_area(coordinate_pairs):
    return abs((coordinate_pairs.coordinates[1][0] - coordinate_pairs.coordinates[0][0]) + 1) * abs((coordinate_pairs.coordinates[1][1] - coordinate_pairs.coordinates[0][1] + 1))


def find_biggest_rectangle(input):

    rows = input.splitlines()

    coordinates = []
    for row in rows:
        entries = row.split(',')
        coordinate = (int(entries[0]), int(entries[1]))
        coordinates.append(coordinate)


    coordinate_pairs = []
    for i in range(0, len(coordinates)):
        for j in range(i+1, len(coordinates)):
            coordinate_pair = CoordinatePair(coordinates[i], coordinates[j])
            coordinate_pairs.append(coordinate_pair)

    areas = []
    for coordinate_pair in coordinate_pairs:
        areas.append(calculate_rectangular_area(coordinate_pair))

    areas.sort()

    return areas[-1]

def main():

    sys_args = sys.argv
    if len(sys_args) != 3:
        print("Usage: python3 main.py <input_file> <method_to_use>")
        sys.exit(1)

    input_file = sys_args[1]
    method_to_use = int(sys_args[2])

    input = None
    with open(input_file) as f:
        input =  f.read()

    if not input:
        raise Exception("No input read")
    
    passcode = 0
    if method_to_use == 1:
        passcode = find_biggest_rectangle(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()