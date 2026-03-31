
from typing import Any

import random


class Deficient():

    def __init__(self, width: int, height: int,
                 entry: tuple[int, int], finish: tuple[int, int],
                 perfect: bool, seed: Any | str) -> None:

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

        if (self.width >= 11 and self.height >= 9):

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
                    grid[h][w] = -42

            elif (state == "after"):
                for y in range(len(grid)):
                    for x in range(len(grid[y])):
                        if (grid[y][x] == -42):
                            grid[y][x] = 15

        return (grid)

# *****************************************************************************
# *                          look_neighbor()                                  *
# *           Check which tile is empty or break a random wall                *

    def look_neighbor(self, grid: list[list[int]], x1: int, y1: int) -> list:

        directions: list[tuple[int, int, str]] = [(0, -1, "N"), (1, 0, "E"),
                                                  (0, 1, "S"), (-1, 0, "W")]
        virgin_neighbor: list[str] = []

        for x, y, c in directions:
            nx, ny = x1 + x, y1 + y

            if ((nx >= 0 and nx < self.width)
                    and (ny >= 0 and ny < self.height)):

                if (grid[ny][nx] == 15 and grid[ny][nx] != -42):

                    virgin_neighbor.append(c)

                elif (grid[ny][nx] != -42 and random.random() < 0.08):

                    virgin_neighbor.append(c)

        return (virgin_neighbor)

    def min_maze(self, grid: list[list[int]]) -> list[list[int]]:

        grid[0][0] = 9
        grid[0][1] = 3
        grid[1][1] = 6
        grid[1][0] = 12

        return (grid)

# *****************************************************************************
# *                       base deficient_maze()                               *
# *       Generate the deficient maze algorithm for perfect = false           *

    def maze(self, grid_start: list[list[int]]) -> list[list[int]]:

        if (self.height == 2 and self.width == 2):
            return (self.min_maze(grid_start))

        if self.seed:
            random.seed(self.seed)

        grid: list[list[int]] = self.print_fortytwo(grid_start, "before")

        x, y = self.entry

        parkour: list[tuple[int, int]] = [(x, y)]
        mouv = {
            "N": (0, -1, 1, 4),
            "E": (1, 0, 2, 8),
            "S": (0, 1, 4, 1),
            "W": (-1, 0, 8, 2)
        }

        while parkour:
            x, y = parkour[-1]
            neighbors = self.look_neighbor(grid, x, y)

            if (neighbors):
                direction = random.choice(neighbors)
                dx, dy, bit_c, bit_v = mouv[direction]
                nx, ny = x + dx, y + dy

                if (grid[ny][nx] == 15):
                    grid[y][x] &= ~bit_c
                    grid[ny][nx] &= ~bit_v
                    parkour.append((nx, ny))

                else:

                    if (grid[y][x] & bit_c):
                        grid[y][x] &= ~bit_c
                        grid[ny][nx] &= ~bit_v

            else:
                parkour.pop()
                if parkour:
                    x, y = parkour[-1]

        grid = self.print_fortytwo(grid, "after")
        return (grid)
