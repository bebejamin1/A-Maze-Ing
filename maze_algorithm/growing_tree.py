
from typing import Any

import numpy as np
import random


class GrowTree():

    def __init__(self, width: int, height: int,
                 entry: tuple[int, int], finish: tuple[int, int],
                 perfect: bool, seed: Any | None) -> None:

        self.width = width
        self.height = height
        self.entry = entry
        self.finish = finish
        self.perfect = perfect
        self.seed = seed

# *****************************************************************************
# *                          print_fortytwo()                                 *
# *          Set the boxes to negative so you can place the 42                *

    def print_fortytwo(self, grid: list[list[int]],
                       state: str) -> list[list[int]]:

        width_int: int = int(self.width)
        height_int: int = int(self.height)

        if (width_int >= 11 and height_int >= 9):

            w: int = int(round(((self.width - 7) / 2), 0))
            h: int = int(round(((self.height - 5) / 2), 0))

            paterns: list[tuple[int, int]] = [
                (0, 0), (1, 0), (1, 0), (0, 1), (0, 1), (1, 0), (1, 0),  # 4
                (-4, 2), (0, 1), (0, 1), (1, 0), (1, 0),  # 2
                (0, -1), (0, -1), (1, 0), (1, 0), (0, 1), (0, 1)]  # 2

            if (state == "before"):
                for p in paterns:
                    h += p[0]
                    w += p[1]
                    grid[h][w] = -1

            elif (state == "after"):
                for y in range(len(grid)):
                    for x in range(len(grid[y])):
                        if (grid[y][x] == -1):
                            grid[y][x] = 15

        return (grid)

# *****************************************************************************
# *                          look_neighbor()                                  *
# *           Check which tile is empty or break a random wall                *

    def look_neighbor(self, grid: list[list[int]], x1, y1) -> list:

        x_axes: list[int] = [0, 1, 0, -1]
        y_axes: list[int] = [-1, 0, 1, 0]
        compass: list[str] = ["N", "E", "S", "W"]
        virgin_neighbor: list[str] = []

        for x, y, c in zip(x_axes, y_axes, compass):
            if (x1+x >= 0 and y1+y >= 0
                and x1+x < self.width and y1+y < self.height
                and grid[y1+y][x1+x] == 15
                    and grid[y1+y][x1+x] != -1):

                virgin_neighbor.append(c)

        return (virgin_neighbor)

# *****************************************************************************
# *                            base growin_tree()                             *
# *     générer un labyrinthe à l'aide de l'algorithme « growing tree »       *

    def maze(self, grid_start) -> list[list[int]]:

        if (self.seed):
            random.seed(self.seed)

        grid: list[list[int]] = self.print_fortytwo(grid_start, "before")

        x, y = self.entry

        parkour: list[tuple[int, int]] = [(x, y)]
        mouv: dict[str, tuple[int, int, int, int]] = {
            "N": (0, -1, 1, 4),
            "E": (1, 0, 2, 8),
            "S": (0, 1, 4, 1),
            "W": (-1, 0, 8, 2)
        }

        while (np.max(grid) == 15):
            neighbor: list[str] = self.look_neighbor(grid, x, y)

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

        grid_finish: list[list[int]] = self.print_fortytwo(grid, "after")
        return (grid_finish)
