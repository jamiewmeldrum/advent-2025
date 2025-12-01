import sys

def count_when_landing_on_zero(input):
    zero_count = 0
    position = 50
    for entry in input.splitlines():
        if entry[0] == "L":
            position -= int(entry[1:])
        elif entry[0] == "R":
            position += int(entry[1:])
        else:
            raise Exception("Unexpected movement instruction")
        
        position = position % 100
        
        if position == 0:
            zero_count += 1
    return zero_count

def count_when_passing_zero(input):
    zero_count = 0
    position = 50
    for entry in input.splitlines():
        initial_position = position
        if entry[0] == "L":
            position -= int(entry[1:])
        elif entry[0] == "R":
            position += int(entry[1:])
        else:
            raise Exception("Unexpected movement instruction")
        
        #This counts the number of times we have passed multiples of +ive 100 or -ive 101
        adjust = abs(position // 100)

        #If we started on 0 and went down, we need to avoid double counting
        if initial_position == 0 and position // 100 < 0:
            adjust -= 1

        #If we landed on multiples of -ive 100 exactly then we need to make sure it gets counted
        if position <= 0 and position % 100 == 0:
            adjust += 1

        zero_count +=adjust

        position = position % 100        

    return zero_count

def count_when_passing_zero_mk2(input):
    zero_count = 0
    position = 50
    for entry in input.splitlines():
        initial_position = position
        if entry[0] == "L":
            position -= int(entry[1:])
        elif entry[0] == "R":
            position += int(entry[1:])
        else:
            raise Exception("Unexpected movement instruction")
        
        if initial_position == 0 and position < 0:
            zero_count -= 1
        
        while (position < 0):
            zero_count += 1
            position += 100

        if position == 0:
            zero_count += 1

        while (position >= 100):
            zero_count += 1
            position -= 100     

    return zero_count

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
    
    zero_count = 0
    if method_to_use == 1:
        zero_count = count_when_landing_on_zero(input)
    elif method_to_use == 2:
        zero_count = count_when_passing_zero(input)
    elif method_to_use == 3:
        zero_count = count_when_passing_zero_mk2(input)
    else:
        raise Exception("Must provide count method")

    print(f"The passcode is {zero_count}")
   
main()