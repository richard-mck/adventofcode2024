"""Reusable functions for each day"""

def load_input(filename: str) -> list:
    with open(filename, "r") as file:
        contents = file.read().splitlines()
    return contents