import sys

from calculation import Calculation

def do_maths_homework(input):

    rows = input.splitlines()
    rows = list(reversed(rows))

    calculations = []
    for row in rows:
        #NOT GUARENTEED TO BE 4 chars!
        entries = [(row[i:i+4]) for i in range(0, len(row), 4)]     


        for i in range(0, len(entries)):
            if len(calculations) == len(entries):
                calculations[i].add_number(entries[i])
            else:
                calculations.append(Calculation(entries[i].strip()))

    count = 0
    for calculation in calculations: 
        #Small extra step to ensure the calculation numbers are flipped before beinf computed       
        count += calculation.compute()

    return count


def do_maths_homework_flipped(input):

    rows = input.splitlines()
    rows = list(reversed(rows))

    calculations = []
    for row in rows:
        entries = [(row[i:i+4]) for i in range(0, len(row), 4)]     
        for i in range(0, len(entries)):
            if len(calculations) == len(entries):
                calculations[i].add_number(entries[i])
            else:
                calculations.append(Calculation(entries[i].strip()))

    count = 0
    for calculation in calculations: 
        #Small extra step to ensure the calculation numbers are flipped before beinf computed       
        count += calculation.flip_and_compute()

    return count

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
        passcode = do_maths_homework(input)
    elif method_to_use == 2:
        passcode = do_maths_homework_flipped(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()