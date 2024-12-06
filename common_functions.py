"""Reusable functions for each day"""

def load_input(filename: str) -> list:
    with open(filename, "r") as file:
        contents = file.read().splitlines()
        contents = [item.split() for item in contents]
    return contents

def get_real_data(use_real_data: bool, real_data="real_data.txt", example_data="example.txt") -> list[str]:
    """Choose whether to use example data or real data based on a bool, True for real, False for example"""
    if use_real_data:
        return load_input(real_data)
    else:
        return load_input(example_data)