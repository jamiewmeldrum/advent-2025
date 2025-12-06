import sys

def do_maths_homework(input):

    rows = input.splitlines()
    rows = list(reversed(rows))

    calculations = []
    for row in rows:
        #print(calculations)
        #print(row)
        entries = row.split(" ")
        entries = list(filter(None, entries))
        #print(entries)
        for i in range(0, len(entries)):
            if len(calculations) == len(entries):
                if calculations[i][1]:
                    if calculations[i][0] == "+":
                        calculations[i][1] += int(entries[i])
                    elif calculations[i][0] == "*":
                        calculations[i][1] *= int(entries[i])
                else:
                    calculations[i][1] = int(entries[i])
            else:
                calculations.append([entries[i], 0])

    count = 0
    for calculation in calculations:
        
        count += calculation[1]

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
    # elif method_to_use == 2:
    #     passcode = count_all_fresh_ingredients(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()