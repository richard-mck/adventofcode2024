"""Reusable functions for each day"""

def load_input(filename: str) -> list:
    with open(filename, "r") as file:
        contents = file.read().splitlines()
        #contents = [item.split() for item in contents]
    return contents

def get_real_data(use_real_data: bool, real_data="real_data.txt", example_data="example.txt") -> list[str]:
    """Choose whether to use example data or real data based on a bool, True for real, False for example"""
    if use_real_data:
        return load_input(real_data)
    else:
        return load_input(example_data)

class Tile(object):
    """A single unit within a greater grid"""

    def __init__(self, pos: tuple[int, int], val: str or int):
        self.pos = pos
        self.val = val


class Grid(object):
    """An x/y grid of Tiles or other objects"""

    def __init__(self, raw_data: list[str]):
        self.height = len(raw_data)
        self.width = len(raw_data[0])
        self.grid = {}
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i, j] = raw_data[i][j]

    def inside_grid(self, pos: tuple[int, int]) -> bool:
        (i, j) = pos
        return 0 <= i < self.height and 0 <= j < self.width

    def get_neighbours(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        (i, j) = pos
        all_neighbours = [
            (i, j + 1),  # Right
            (i + 1, j),  # Down
            (i, j - 1),  # Left
            (i - 1, j),  # Up
        ]
        all_neighbours = [k for k in all_neighbours if self.inside_grid(k)]
        return all_neighbours

    def print_grid(self, include_row_nums=False):
        """Given a dictionary grid, print the contents line by line for debugging"""
        for i in range(0, self.height):
            for j in range(0, self.width):
                if include_row_nums and j == 0:
                    print(f"{i}: ", end="")
                if j == self.width - 1:
                    print(self.grid[(i, j)])
                else:
                    print(self.grid[(i, j)], end="")