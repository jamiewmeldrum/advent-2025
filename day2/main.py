import sys

def process_passcode_method_1(input):
    
    passcode = 0
    ranges = input.split(",")
    for number_range in ranges:
        start, end = number_range.split("-")
        for value in range(int(start), int(end) + 1):
            value = str(value)
            q, r = divmod(len(value), 2)
            first, second = value[:q + r], value[q + r:]
            if first == second:
                passcode += int(value)

    return passcode


def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

def process_passcode_method_2(input):
    
    passcode = 0
    ranges = input.split(",")
    for number_range in ranges:
        start, end = number_range.split("-")
        for value in range(int(start), int(end) + 1):
            
            str_val = str(value)
            repeating_unit = principal_period(str_val)

            if repeating_unit:
                passcode += value

    return passcode


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
        passcode = process_passcode_method_1(input)
    elif method_to_use == 2:
        passcode = process_passcode_method_2(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()