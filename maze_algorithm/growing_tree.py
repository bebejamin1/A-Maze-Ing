
from typing import Optional

import numpy as np
import random

from maze_algorithm.defective_maze import deficient_maze


# *****************************************************************************
# *                        print_fortytwo()                                   *
# *             generates 42 if the size is large enough                      *


def print_fortytwo(grid: list[list[int]], finish: str,
                   width: int, height: int) -> list[list[int]]:
    """Write or clear the decorative 42 pattern in the maze grid.

    Args:
        grid: Maze grid.
        finish: Phase marker, either "before" or "after".
        width: Maze width.
        height: Maze height.

    Returns:
        Updated maze grid.
    """

    width_int = int(width)
    height_int = int(height)

    if (width_int >= 11 and height_int >= 9):

        w: int = int(round(((width - 7) / 2), 0))
        h: int = int(round(((height - 5) / 2), 0))

        paterns: list[tuple[int, int]] = [
            (0, 0), (1, 0), (1, 0), (0, 1), (0, 1), (1, 0), (1, 0),  # 4
            (-4, 2), (0, 1), (0, 1), (1, 0), (1, 0),  # 2
            (0, -1), (0, -1), (1, 0), (1, 0), (0, 1), (0, 1)]  # 2

        if (finish == "before"):
            for p in paterns:
                h += p[0]
                w += p[1]
                grid[h][w] = -1

        elif (finish == "after"):
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if (grid[y][x] == -1):
                        grid[y][x] = 15

    return (grid)


# *****************************************************************************
# *                         look_neighbor()                                   *
# *  Check to see if the current position can move to an virgin square        *


def look_neighbor(grid: list[list[int]], x1: int, y1: int,
                  w: int, h: int) -> list:
    """Collect unvisited neighboring cells around the current position.

    Args:
        grid: Maze grid.
        x1: Current x-coordinate.
        y1: Current y-coordinate.
        w: Maze width.
        h: Maze height.

    Returns:
        List of available movement directions.
    """

    x_axes: list[int] = [0, 1, 0, -1]
    y_axes: list[int] = [-1, 0, 1, 0]
    compass: list[str] = ["N", "E", "S", "W"]
    virgin_neighbor: list[str] = []

    for x, y, c in zip(x_axes, y_axes, compass):
        if (x1+x >= 0 and y1+y >= 0 and x1+x < w and y1+y < h
                and grid[y1+y][x1+x] == 15 and grid[y1+y][x1+x] != -1):

            virgin_neighbor.append(c)

    return (virgin_neighbor)


# *****************************************************************************
# *                         growing_tree()                                    *
# *         Generate the maze using the growing tree algorithm                *


def grow_tree(grid: list[list[int]], width: int, height: int,
              entry: tuple[int, int], perfect: bool,
              seed: Optional[str]) -> list[list[int]]:
    """Generate a maze using the growing tree algorithm.

    Args:
        grid: Initial maze grid.
        width: Maze width.
        height: Maze height.
        entry: Starting coordinate for generation.
        perfect: Whether to generate a perfect maze.
        seed: Optional random seed.

    Returns:
        Generated maze grid.
    """

    if (perfect is False and width > 3 and height > 3):
        return (deficient_maze(grid, width, height, entry, seed))
    if (seed):
        random.seed(seed)

    grid: list[list[int]] = print_fortytwo(grid, "before", width, height)

    x: int = entry[0]
    y: int = entry[1]

    parkour: list[tuple[int, int]] = [(x, y)]
    mouv: list[str, tuple[int]] = {
        "N": (0, -1, 1, 4),
        "E": (1, 0, 2, 8),
        "S": (0, 1, 4, 1),
        "W": (-1, 0, 8, 2)
    }

    while (np.max(grid) == 15):
        neighbor: list[str] = look_neighbor(grid, x, y, width, height)

        if (neighbor):
            dir: str = random.choice(neighbor)
            dx, dy, bits_dir, bits_next = mouv[dir]
            nx, ny = x + dx, y + dy

            grid[y][x] &= ~bits_dir
            grid[ny][nx] &= ~bits_next
            parkour.append((nx, ny))
            x, y = nx, ny

        else:
            parkour.pop()
            x, y = parkour[-1]

    grid: list[list[int]] = print_fortytwo(grid, "after", width, height)
    return (grid)
