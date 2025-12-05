import sys

from number_range import NumberRange

from itertools import groupby

def count_fresh_ingredients(input):

    rows = input.splitlines()
    sublists = [list(g) for k, g in groupby(rows, key=lambda x: x == '') if not k]

    id_ranges = sublists[0]
    available_ids = sublists[1]

    available_ranges = []
    for id_range in id_ranges:
        start, end = id_range.split("-")
        available_ranges.append(NumberRange(start, end))

    # Nasty - rework to merge ranges and add a binary tree type of thing
    count = set()
    available_ranges.sort(reverse=True, key=lambda x: x.start)
    for available_id in available_ids:
        for available_range in available_ranges:
            if int(available_id) >= available_range.start and int(available_id) <= available_range.end:
                print(f"start = {available_range.start}")
                print(f"end = {available_range.end}")
                print(f"available_id = {available_id}")
                count.add(available_id)

    return len(count)


def count_all_fresh_ingredients(input):

    rows = input.splitlines()
    sublists = [list(g) for k, g in groupby(rows, key=lambda x: x == '') if not k]

    id_ranges = sublists[0]

    available_ranges = []
    for id_range in id_ranges:
        start, end = id_range.split("-")
        available_ranges.append(NumberRange(start, end))
    
    #Merge ranges
    ranges_to_merge = {}
    available_ranges.sort(key=lambda x: x.start)
    available_ranges = iter(available_ranges)

    next_element = next(available_ranges)
    ranges_to_merge = []
    merged_ranges = []
    while (next_element):
        print(next_element.start)
        if not ranges_to_merge:
            print("Nothing")
            ranges_to_merge.append(next_element)
        elif ranges_to_merge[-1].end >= next_element.start:
            print("Append")
            ranges_to_merge.append(next_element)
        else:
            print("Merge")
            merged_ranges.append(NumberRange(ranges_to_merge[0].start, ranges_to_merge[-1].end))
            ranges_to_merge = [next_element]

        next_element = next(available_ranges, None)
        if not next_element:
            merged_ranges.append(NumberRange(ranges_to_merge[0].start, ranges_to_merge[-1].end))       

    count = 0
    for merged_range in merged_ranges:
        print(f"{merged_range.start} - {merged_range.end}")
        count += (1 + merged_range.end - merged_range.start)

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
        passcode = count_fresh_ingredients(input)
    elif method_to_use == 2:
        passcode = count_all_fresh_ingredients(input)
    else:
        raise Exception("Must provide method")

    print(f"The passcode is {passcode}")
   
main()