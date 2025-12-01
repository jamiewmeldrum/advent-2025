import sys

def main():
    input = None

    with open("input.txt") as f:
        input =  f.read()

    if not input:
        raise Exception("No input read")
    
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

    print(f"The passcode is {zero_count}")
   
main()