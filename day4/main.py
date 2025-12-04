import sys
from Grid import Grid

def count_accessible_rolls_of_paper(input):

    rows = input.splitlines()
    width = len(rows[0])
    height = len(rows)
    grid = Grid(width, height)

    for y in range(0, len(rows)):
        row = rows[y]
        for x in range(0, len(row)):
            grid.add_element(x, y, row[x])

    accessible_rolls = 0
    for y in range(0, height):
        for x in range(0, width):

            if grid.get_value(x, y) != "@":
                continue

            if not grid.has_nearest_neighbours_with_value(x, y, 4, "@"):
                accessible_rolls += 1

    return accessible_rolls
        

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
        passcode = count_accessible_rolls_of_paper(input)
    # elif method_to_use == 2:
    #     passcode = process_battery_joltage_2(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()