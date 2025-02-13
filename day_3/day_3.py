import re
from common_functions import get_real_data

ENABLE_MULT = "do\(\)"
DISABLE_MULT = "don't\(\)"


def split_tuple_between_brackets(values: str) -> list[str]:
    first_bracket = values.index("(")
    second_bracket = values.index(")")
    return values[first_bracket + 1:second_bracket].split(",")


def get_indices_of_instructions(instructions: str) -> (list[int], list[int]):
    # Get all the active positions
    activate = [pos.start() for pos in re.finditer(ENABLE_MULT, instructions)]
    # We always start with multiplication active
    # activate.insert(0, 0)
    # Get all deactivate positions
    deactivate = [pos.start() for pos in re.finditer(DISABLE_MULT, instructions)]
    return activate, deactivate


if __name__ == '__main__':
    data = get_real_data(False)
    print(data)
    multipliers = []
    for item in data:
        print(item)
        multipliers += item.split("mul")
    print(multipliers)
    # We know all valid multipliers for part 1 sit between brackets and must begin with a bracket
    multipliers = [
        i for i in multipliers
        if "(" in i
           and ")" in i
           and i[0] == "("
    ]
    print(f"Split on mul {multipliers}")
    vals = []
    for item in multipliers:
        nums = split_tuple_between_brackets(item)
        try:
            first = int(nums[0])
            second = int(nums[1])
        except ValueError:
            continue
        print(f"item: {item} nums: {nums}")
        vals.append(int(nums[0]) * int(nums[1]))
    print(vals)
    print(f"Total sum {sum(vals)}")
    # Part 2
    data_2 = get_real_data(False, example_data="example2.txt")
    print(data_2)
    # Find the positions of do and don't
    # For each line, we start with multiplication activated, and only stop it when we reach a stop signal
    # Any commands after the stop signal are ignored until the next start signal or the end of the line
    #
    # do_pos = []
    # dont_pos = []
    vals = []
    for item in data_2:
        do_pos, dont_pos = get_indices_of_instructions(item)
        print(f"Indices {ENABLE_MULT}: {do_pos}, {DISABLE_MULT}: {dont_pos}")
        all_pos = do_pos + dont_pos
        all_pos.sort()
        result_str = ""
        initial_pos = 0
        # Here we should iterate over all positions, grabbing only substrings between active instructions
        for pos in all_pos:
            # Conditions:
            # - between start and -1, grab substring
            # - between stop and -1, skip substring
            if pos == all_pos[-1]:
                if pos in do_pos:
                    result_str += item[pos: -1]
            # - between 0 and start, grab substring or between 0 and stop, grab substring
            if initial_pos == 0 and (pos in do_pos or pos in dont_pos):
                result_str += item[initial_pos:pos]
                initial_pos = pos
                continue
            # - between start and start, grab substring or between start and stop, grab substring
            if initial_pos in do_pos and (pos in do_pos or pos in dont_pos):
                result_str += item[initial_pos:pos]
                initial_pos = pos
                continue
            # - between stop and start, skip substring or between stop and stop, skip substring
            if initial_pos in dont_pos and (pos in do_pos or pos in dont_pos):
                initial_pos = pos
                continue
        print(result_str)
        multipliers = result_str.split("mul")
        print(f"raw mults {multipliers}")
        multipliers = [
            i for i in multipliers
            if "(" in i
               and ")" in i
               and i[0] == "("
        ]
        print(f"Split on mul {multipliers}")
        for val in multipliers:
            nums = split_tuple_between_brackets(val)
            print(f"Split tuple: {nums}")
            try:
                first = int(nums[0])
                second = int(nums[1])
            except ValueError:
                continue
            # print(f"item: {val} nums: {nums}")
            vals.append(int(nums[0]) * int(nums[1]))
    print(vals)
    print(f"Total sum {sum(vals)}")

# Not 119848814
# Not 112592686
# Not 24155524
# Not 86747221
# Correct 83158140
