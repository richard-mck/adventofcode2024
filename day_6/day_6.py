"""
--- Day 6: Guard Gallivant ---

The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
"""

from common_functions import get_real_data, Grid, Tile

DIRECTION = {
    "^": (-1, 0),
    ">": (0, 1),
    "V": (1, 0),
    "<": (0, -1),
}
SYMBOLS = {
    (-1, 0): "^",
    (0, 1): ">",
    (1, 0): "V",
    (0, -1): "<",
}


def calculate_next_position(direction: str, pos: tuple[int, int]) -> tuple[int, int]:
    return pos[0] + DIRECTION[direction][0], pos[1] + DIRECTION[direction][1]


def get_next_dir(symbol: str) -> str:
    return SYMBOLS[DIRECTION[symbol][1], DIRECTION[symbol][0] * -1]


def explore_map(map_grid: Grid, pos: tuple[int, int], direction: str) -> (Grid, list[Tile]):
    visited_positions = []
    while map_grid.inside_grid(pos) and Tile(pos, direction) not in visited_positions:
        next_pos = calculate_next_position(map_grid.grid[pos], pos)
        if not map_grid.inside_grid(next_pos):
            map_grid.grid[pos] = "X"
            visited_positions.append(Tile(pos, direction))
            return map_grid, visited_positions
        if guard_map.grid[next_pos] != "#":
            map_grid.grid[pos] = "X"
            visited_positions.append(Tile(pos, direction))
            pos = next_pos
            guard_map.grid[next_pos] = direction
        elif guard_map.grid[next_pos] == "#":
            next_dir = get_next_dir(direction)
            map_grid.grid[pos] = get_next_dir(direction)
            direction = next_dir


if __name__ == "__main__":
    data = get_real_data(False)
    print(data)
    guard_map = Grid(data)
    guard_map.print_grid(True)
    current_dir = "^"
    current_pos = guard_map.find_val_in_grid(current_dir)
    print(current_pos)
    guard_map, visited_tiles = explore_map(guard_map, current_pos, current_dir)
    guard_map.print_grid()
    unique_pos = "".join(guard_map.grid.values()).count("X")
    print(f"Total moves: {len(visited_tiles)}, unique positions: {unique_pos}")
    # correct answer 4977
    # Part 2
    # We need to find all the possible closed loops within the path
    # There are six in the example
    # One way to do this would be to do the standard loop over, identifying all the visited squares
    # Then iterate over the map replacing each with a blocker and testing to see if the moves end up looping or not
    # Given the complete path takes 4k+ steps, this is probably not an efficient or clever way to do it
    # However, part 1 runs in less than a second, so maybe it's fine?
    blocking_map = Grid(data)
    starting_pos = blocking_map.find_val_in_grid("^")
    print(starting_pos)
    # The first position cannot be blocked, so remove it from the visited tiles;
    visited_tiles = [i for i in visited_tiles if i.pos != starting_pos]
    for tile in visited_tiles:
        temp_map = Grid(data)
        temp_map.grid[tile.pos] = "#"
        temp_map, closed_loop_squares = explore_map(temp_map, starting_pos, current_dir)
