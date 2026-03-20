#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   growing_tree.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/18 11:31:23 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/20 15:55:51 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from typing import Optional

import numpy as np
import random

from test_display import debug_display


def print_fortytwo(grid: list[list[int]], finish: str,
                   width: int, height: int) -> list[list[int]]:

    if (width >= 10 and height >= 8):

        w: int = int(round(((width - 7) / 2), 0))
        h: int = int(round(((height - 5) / 2), 0))

        paterns = [(0, 0), (1, 0), (1, 0), (0, 1), (0, 1), (1, 0), (1, 0),  # 4
                   (-4, 2), (0, 1), (0, 1), (1, 0), (1, 0),  # 2
                   (0, -1), (0, -1), (1, 0), (1, 0), (0, 1), (0, 1)]  # 2

        if (finish == "before"):
            for p in paterns:
                h += p[0]
                w += p[1]
                grid[h][w] = 0

        elif (finish == "after"):
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if grid[y][x] == 0:
                        grid[y][x] = 15

    return (grid)


def look_neighbor(grid: list[list[int]], x1: int, y1: int,
                  w: int, h: int) -> list:

    x_axes = [0, 1, 0, -1]
    y_axes = [-1, 0, 1, 0]
    compass = ["N", "E", "S", "W"]
    virgin_neighbor = []

    for x, y, c in zip(x_axes, y_axes, compass):
        if (x1+x >= 0 and y1+y >= 0 and x1+x < w and y1+y < h
                and grid[y1+y][x1+x] == 15 and grid[y1+y][x1+x] != 0):

            virgin_neighbor.append(c)

    return (virgin_neighbor)


def maze(grid: list[list[int]], width: int, height: int,
         entry: tuple[int, int], perfect: bool,
         seed: Optional[str]) -> list[list[int]]:

    new_grid: list[list[int]] = print_fortytwo(grid, "before", width, height)

    x1: int = entry[0]
    y1: int = entry[1]
    n, e, s, w = 1, 2, 4, 8
    back: int = -1
    parkour: list = []
    # print(*new_grid, sep="\n")

    while (np.max(new_grid) == 15):
        test: list[str] = look_neighbor(new_grid, x1, y1, width, height)

        if (test):
            back = -1
            dir = random.choice(test)
            if (dir == "N"):
                grid[y1][x1] -= n  # N
                y1 += -1
                grid[y1][x1] -= s  # S

            elif (dir == "E"):
                grid[y1][x1] -= e  # E
                x1 += 1
                grid[y1][x1] -= w  # W

            elif (dir == "S"):
                grid[y1][x1] -= s  # S
                y1 += 1
                grid[y1][x1] -= n  # N

            elif (dir == "W"):
                grid[y1][x1] -= w  # W
                x1 += -1
                grid[y1][x1] -= e  # E
            parkour.append((x1, y1))

        else:
            x1, y1 = parkour[back][0], parkour[back][1]
            back -= 1

        # print(debug_display(grid, width, height, entry, (0, 0), (x1, y1)))
    new_grid = print_fortytwo(new_grid, "after", width, height)
    return (new_grid)


def main() -> None:
    width = height = 15

    entry = (0, 0)
    finish = (14, 11)

    grid = np.array([[15 for _ in range(width)] for _ in range(height)])

    grid = maze(grid, width, height, entry, True, "")
    print(*grid, sep="\n")

    debug_display(grid, width, height, entry, finish, entry)


if __name__ == "__main__":
    main()
