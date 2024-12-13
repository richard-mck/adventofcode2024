def split_tuple_between_brackets(values: str) -> list[str]:
    first_bracket = values.index("(")
    second_bracket = values.index(")")
    return values[first_bracket + 1:second_bracket].split(",")

if __name__ == '__main__':
    with open('example.txt') as f:
        data = f.readlines()
    print(data)
    data = data[0].split("mul")
