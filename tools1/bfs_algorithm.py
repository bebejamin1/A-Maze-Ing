#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   bfs_algorithm.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/21 15:22:46 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/24 17:42:25 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any

import random

from test_display import debug_display


def look_neighbor(grid: list[list[int]], x1: int, y1: int,
                  w: int, h: int, prec: str) -> list:

    directions: list[tuple[Any]] = [(0, -1, "N", 1), (1, 0, "E", 2),
                                    (0, 1, "S", 4), (-1, 0, "W", 8)]
    oposite = {"N": "S", "E": "W", "S": "N", "W": "E", "Z": "Z"}
    virgin_neighbor: list[str] = []

    for x, y, c, b in directions:
        nx, ny = x1 + x, y1 + y

        if (c != oposite[prec] and grid[y][x] & b):

            virgin_neighbor.append(c)

    return (virgin_neighbor)


# algorithme bfs
def find_way(grid: list[list[int]], start: tuple[int],
             finish: tuple[int], width: int, height: int, ) -> list[str]:

    prec = "Z"
    x, y = start
    path = [(x, y)]
    way = ["Z"]
    mouv: list[str, tuple[int]] = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    # while (path[-1] != finish):
    for _ in range(8):

        choix = look_neighbor(grid, x, y, width, height, prec)
        direction = random.choice(choix)
        prec = direction
        print(choix)
        print(direction)
        if (direction):

            print("oui")
            dir = mouv[direction]
            print(mouv[direction])
            path.append(dir)
            way.append(direction)

            x, y = dir

        else:

            print("non")
            prec = "Z"
            path.pop()
            way.pop()
            if path:
                x, y = path[-1]

        print(f"prec: {prec}" + "\n")
        debug_display(grid, 15, 15, start, finish, (x, y), path)

    return (path)


if __name__ == "__main__":

    grid = [
        [11, 13,  1,  5,  3, 13,  1,  3,  9,  5,  5,  5,  5,  1,  3],
        [12,  3, 12,  3, 12,  3, 10, 12,  4,  7,  9,  5,  3, 10, 10],
        [11, 12,  3, 10, 11, 10, 10,  9,  5,  5,  6, 11, 12,  6, 10],
        [10,  9,  6, 10,  8,  6, 10, 12,  5,  3, 13,  4,  1,  5,  6],
        [10, 12,  5,  6, 12,  3, 12,  5,  7, 12,  5,  3, 12,  5,  7],
        [10,  9,  5,  3, 15, 12,  5,  3, 15, 15, 15,  8,  5,  5,  3],
        [8,  6,  9,  2, 15, 13,  5, 15,  5,  7, 15, 12,  7,  9,  2],
        [10, 11, 10, 10, 15, 15, 15, 10, 15, 15, 15,  9,  5,  6, 10],
        [12,  2, 10, 12,  5,  3, 15, 10, 15, 13,  5,  4,  3,  9,  6],
        [9,  6, 10, 13,  3, 10, 15, 10, 15, 15, 15,  9,  6, 10, 11],
        [12,  3, 12,  3, 10, 12,  3, 10,  9,  3,  9,  6, 11, 10, 10],
        [9,  6,  9,  6,  8,  3, 10, 10, 10, 12,  6,  9,  6, 10, 10],
        [10, 11, 10, 13,  6, 12,  6, 10, 12,  5,  3,  8,  5,  6, 10],
        [12,  2, 10,  9,  5,  5,  3, 12,  5,  3, 10, 10,  9,  3, 10],
        [13,  6, 12,  4,  5,  7, 12,  5,  5,  4,  6, 12,  6, 12,  6]
    ]

    start = (0, 0)
    finish = (14, 14)
    print(len(grid))
    debug_display(grid, 15, 15, start, finish, (0, 0))
    way = find_way(grid, start, finish, 15, 15)
    debug_display(grid, 15, 15, start, finish, (0, 0), way)
