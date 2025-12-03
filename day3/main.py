import sys

def process_battery(battery, digits_required):
    if len(battery) < digits_required:
        raise Exception("Battery string not long enough")
    
    if not battery.isnumeric():
        raise Exception("Battery string must be numeric")
    
    first_part, second_part = battery[:len(battery)-digits_required], battery[len(battery)-digits_required:]

    combination = ""
    for i, current_num in enumerate(second_part):

        biggest_num, position = current_num, None
        
        for j, num in enumerate(reversed(first_part)):
            if num >= biggest_num:
                biggest_num, position = num, j
        
        if position != None:
            first_part = first_part[len(first_part)-position:] + second_part[i]
        else:
            first_part = []

        combination = combination + biggest_num

    return combination


def process_battery_joltage_1(input):  

    passcode = 0
    for battery in input.splitlines():
        passcode += int(process_battery(battery, 2))

    return passcode


def process_battery_joltage_2(input):   
    
    passcode = 0
    for battery in input.splitlines():
        passcode += int(process_battery(battery, 12))

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
    elif method_to_use == 2:
        passcode = process_battery_joltage_2(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()