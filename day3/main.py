import sys

def process_battery_joltage_1(input):   
    
    passcode = 0
    for battery in input.splitlines():
        print(battery)

        first_digit = None
        second_digit = None
        highest_previous_number = None
        for num in reversed(battery):

            if not first_digit:
                first_digit = num
                highest_previous_number = first_digit
            elif first_digit and not second_digit:
                first_digit, second_digit = num, first_digit
                highest_previous_number = max(first_digit, second_digit)
            elif num >= first_digit:
                first_digit = num
                second_digit = highest_previous_number
                if num > highest_previous_number:
                    highest_previous_number = num
        
        passcode += int(str(first_digit) + str(second_digit))

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
        passcode = process_battery_joltage_1(input)
    # elif method_to_use == 2:
    #     passcode = process_passcode_method_2(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()