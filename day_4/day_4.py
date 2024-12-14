import pprint
from common_functions import get_real_data, transpose_data

XMAS = "XMAS"
SAMX = "SAMX"

def rotate_list_45_degrees(m: int, n: int, data: list[str]) -> list:
    counter = 0
    rotated_data = []
    while counter < 2 * n - 1:
        row = []
        for i in range(m):
            for j in range(n):
                if i + j == counter:
                    row.append(data[i][j])
        row.reverse()
        rotated_data.append("".join(row))
        counter += 1
    return rotated_data

if __name__ == '__main__':
    data = get_real_data(False)
    print(data)
    grid = Grid(data)
    grid.print_grid(True)
    # For every point in the grid, we need to check if xmas is present horizontal, vertical, diagonal, written backwards, or even overlapping other words
    # The easiest way to do this would be a sweep around the compass points (including half intervals) for each point on the grid
    # At the edges we can discard any directions that take us off the grid
    # And we can discard any searches that take us off the grid generally