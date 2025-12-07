import sys

from Grid import Grid

def process_and_count_routes(input):

    rows = input.splitlines()
    width = len(rows[0])
    height = len(rows)
    grid = Grid(width, height)

    #Raw grid
    for y in range(0, height):
        row = rows[y]
        for x in range(0, width):
            grid.add_element(x, y, row[x])

    beam_splitters = grid.count_char("^")

    #Processed Grid
    for y in range(0, height):
        row = rows[y]
        for x in range(0, width):
            if grid.get_value(x, y-1) == "S" or grid.get_value(x, y-1) == "|":
                if row[x] == "^":
                    grid.add_element(x-1, y, "|")
                    grid.add_element(x+1, y, "|")
                    grid.add_element(x, y, ".")
                else:
                    grid.add_element(x, y, "|")
            elif grid.get_value(x, y) == "|":
                continue
            else:
                grid.add_element(x, y, row[x])

    return beam_splitters - grid.count_char("^") 


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
        passcode = process_and_count_routes(input)
    # elif method_to_use == 2:
    #     passcode = do_maths_homework_flipped(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()