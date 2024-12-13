from common_functions import get_real_data, Grid

XMAS = "XMAS"

if __name__ == '__main__':
    data = get_real_data(False)
    print(data)
    grid = Grid(data)
    grid.print_grid(True)
    # For every point in the grid, we need to check if xmas is present horizontal, vertical, diagonal, written backwards, or even overlapping other words
    # The easiest way to do this would be a sweep around the compass points (including half intervals) for each point on the grid
    # At the edges we can discard any directions that take us off the grid
    # And we can discard any searches that take us off the grid generally