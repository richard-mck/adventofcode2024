"""
--- Day 7: Bridge Repair ---

The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?
"""

from itertools import product
from common_functions import get_real_data


def turn_inputs_into_ints(line: str) -> (int, list[int]):
    components = line.split(":")
    total = int(components[0])
    values = [int(i) for i in components[1].split()]
    return total, values


def generate_operators(max_values: int, include_pipe=False) -> list[list[str]]:
    ops = ["+", "*"] if not include_pipe else ["+", "*", "||"]
    result = [list(comb) for comb in product(ops, repeat=max_values)]
    return result


def do_operation(ops: list[str], vals: list[int]):
    # Safety check!
    assert len(ops) == len(vals) - 1

    result = vals[0]
    # Iterate to the end from position 1
    for i, j in enumerate(vals[1:], 1):
        if ops[i - 1] == "+":
            result += vals[i]
        elif ops[i - 1] == "*":
            result *= vals[i]
        elif ops[i - 1] == "||":
            piped = int(str(result) + str(vals[i]))
            print(f"Piping: {result} || {vals[i]} = {piped}")
            result = piped
    return result


if __name__ == "__main__":
    data = get_real_data(False)
    calculate_part_2 = False
    print(data)
    result_vals = []
    for row in data:
        test_val, components = turn_inputs_into_ints(row)
        print(f"Test: {test_val}, comps: {components}")
        operators = generate_operators(len(components) - 1, calculate_part_2)
        print(operators)
        for op in operators:
            print(f"Current op: {op}, seeking: {test_val}")
            if do_operation(op, components) == test_val:
                result_vals.append(test_val)
    # We always have one fewer operators than digits
    # Operators are always evaluated sequentially left to right
    # Can we generate all possible operators for a given sequence?
    # Yes, with itertools!

    # Here we get unique values by using set, then convert to list so we can sum it
    result_vals = sum(list(set(result_vals)))
    print(result_vals)
