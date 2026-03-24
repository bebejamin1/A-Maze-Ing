#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   defective_maze.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/21 12:17:31 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/24 12:54:29 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Optional, Any

# import numpy as np
import random


# voir porte logique


# *****************************************************************************
# *                        print_fortytwo()                                   *
# *             generates 42 if the size is large enough                      *

def print_fortytwo(grid: list[list[int]], finish: str,
                   width: int, height: int) -> list[list[int]]:

    if (width >= 11 and height >= 9):

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
                grid[h][w] = -42

        elif (finish == "after"):
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if (grid[y][x] == -42):
                        grid[y][x] = 15

    return (grid)


# *****************************************************************************
# *                         look_neighbor()                                   *
# *          Check to see if the current position can move                    *

def look_neighbor(grid: list[list[int]], x1: int, y1: int,
                  w: int, h: int) -> list:

    directions: list[tuple[Any]] = [(0, -1, "N"), (1, 0, "E"),
                                    (0, 1, "S"), (-1, 0, "W")]
    virgin_neighbor: list[str] = []

    for x, y, c in directions:
        nx, ny = x1 + x, y1 + y

        if ((nx >= 0 and nx < w) and (ny >= 0 and ny < h)):

            if (grid[ny][nx] == 15 and grid[ny][nx] != -42):

                virgin_neighbor.append(c)

            elif (grid[ny][nx] != -42 and random.random() < 0.08):

                virgin_neighbor.append(c)

    return (virgin_neighbor)


# *****************************************************************************
# *                     base deficient_maze()                                 *
# *     Generate the deficient maze algorithm for perfect = false             *

def deficient_maze(grid: list[list[int]], width: int, height: int,
                   entry: tuple[int, int],
                   seed: Optional[str]) -> list[list[int]]:

    if seed:
        random.seed(seed)

    grid = print_fortytwo(grid, "before", width, height)
    x, y = entry
    parkour: list[tuple[int, int]] = [(x, y)]

    mouv = {
        "N": (0, -1, 1, 4),
        "E": (1, 0, 2, 8),
        "S": (0, 1, 4, 1),
        "W": (-1, 0, 8, 2)
    }

    while parkour:
        x, y = parkour[-1]
        neighbors = look_neighbor(grid, x, y, width, height)

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

    grid = print_fortytwo(grid, "after", width, height)
    return (grid)
