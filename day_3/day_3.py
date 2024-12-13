from common_functions import get_real_data

def split_tuple_between_brackets(values: str) -> list[str]:
    first_bracket = values.index("(")
    second_bracket = values.index(")")
    return values[first_bracket + 1:second_bracket].split(",")

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
