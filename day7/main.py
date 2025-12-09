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

    grid.print()

    return beam_splitters - grid.count_char("^") 


def process_and_count_routes_many_worlds_recursive(input):

    rows = input.splitlines()
    width = len(rows[0])
    height = len(rows)
    grid = Grid(width, height)

    #Raw grid
    for y in range(0, height):
        row = rows[y]
        for x in range(0, width):
            grid.add_element(x, y, row[x])

    #Processed Grid
    grids = construct_grids(width, height, 0, 0, grid)
    for grid in grids:
        grid.print()
        print()

    return len(grids)

def construct_grids(width, height, start_width, start_height, grid):
    grids = []

    grid.print()
    print()
    
    for y in range(start_height, height):
        row = grid.get_row(y)

        if y == start_height:
            x_range_start = start_width
        else:
            x_range_start = 0

        for x in range(x_range_start, width):
            if grid.get_value(x, y-1) == "S" or grid.get_value(x, y-1) == "|":
                if row[x] == "^":
                    grid.add_element(x, y, ".")

                    new_grid_left = grid.copy()
                    new_grid_left.add_element(x-1, y, "|")

                    grids += construct_grids(width, height, x + 1, y, new_grid_left)

                    new_grid_right = grid.copy()                    
                    new_grid_right.add_element(x+1, y, "|")

                    grids += construct_grids(width, height, x + 1, y, new_grid_right)
                else:
                    grid.add_element(x, y, "|")
            elif grid.get_value(x, y) == "|":
                continue
            else:
                grid.add_element(x, y, row[x])
    
    if not grids:
        grids.append(grid)
    return grids


def process_and_count_routes_many_worlds_using_count(input):

    rows = input.splitlines()
    width = len(rows[0])
    height = len(rows)
    grid = Grid(width, height)

    #Raw grid
    for y in range(0, height):
        row = rows[y]
        for x in range(0, width):
            if row[x] == ".":
                grid.add_element(x, y, 0)
            else:
                grid.add_element(x, y, row[x])

    #Processed Grid
    for y in range(0, height):
        row = grid.get_row(y)
        for x in range(0, width):
            cell_above = grid.get_value(x, y-1)
            if cell_above:
                
                cell_above_value = cell_above
                if cell_above == "S":
                    cell_above_value = 1

                if grid.get_value(x, y) == "^":                    
                    grid.add_element(x-1, y, cell_above_value + grid.get_value(x-1, y))
                    grid.add_element(x+1, y, cell_above_value + grid.get_value(x+1, y))
                elif isinstance(cell_above_value, int):
                    grid.add_element(x, y, cell_above_value + grid.get_value(x, y))

    return sum(grid.get_row(height-1))


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
    elif method_to_use == 2:
        passcode = process_and_count_routes_many_worlds_recursive(input)
    elif method_to_use == 3:
        passcode = process_and_count_routes_many_worlds_using_count(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()