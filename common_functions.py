"""Reusable functions for each day"""


def load_input(filename: str) -> list:
    with open(filename, "r") as file:
        contents = file.read().split("\n")
    if contents[-1] == "":
        return contents[:-1]
    return contents


def get_real_data(use_real_data: bool, real_data="real_data.txt", example_data="example.txt") -> list[str]:
    """Choose whether to use example data or real data based on a bool, True for real, False for example"""
    if use_real_data:
        return load_input(real_data)
    else:
        return load_input(example_data)


def make_dict_grid(row_based_data: list[str]) -> dict[tuple[int, int], str]:
    result = {}
    for i in range(len(row_based_data)):
        for j in range(len(row_based_data[i])):
            result[(i, j)] = row_based_data[i][j]
    return result


def transpose_data(row_based_data: list[str]) -> list[str]:
    """Given a grid of strings, return the same grid transformed into columns instead of rows"""
    result = []
    for i in range(len(row_based_data[0])):
        temp_list = []
        for j in range(len(row_based_data)):
            temp_list.append(row_based_data[j][i])
        result.append("".join(temp_list))
    return result


class Tile(object):
    """A single unit within a greater grid"""

    def __init__(self, pos: tuple[int, int], val: str or int):
        self.pos = pos
        self.val = val

    def __repr__(self):
        return f"Pos: {self.pos} Val: {self.val}"

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return NotImplemented
        return self.pos == other.pos and self.val == other.val


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

    def get_neighbours(self, pos: tuple[int, int], include_diags=False) -> list[tuple[int, int]]:
        (i, j) = pos
        all_neighbours = [
            (i, j + 1),  # Right
            (i + 1, j),  # Down
            (i, j - 1),  # Left
            (i - 1, j),  # Up
        ]
        if include_diags:
            all_neighbours += [
                (i - 1, j + 1),  # Right/Up
                (i + 1, j + 1),  # Right/Down
                (i + 1, j - 1),  # Left/Down
                (i - 1, j - 1),  # Left/Up
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

    def find_val_in_grid(self, value: str) -> tuple[int, int]:
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.grid[(i, j)] == value:
                    return i, j
        print(f"Value not found in grid: {value}")
        return -1, -1
