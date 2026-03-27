#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   gen_output.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/20 09:02:11 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/27 14:19:54 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Optional, Any

from maze_algorithm.growing_tree import grow_tree
from tools1.bfs_algorithm import find_way
import numpy as np

red = "\033[31m\033[5m\033[1m"
reset = "\033[0m"


def output(width, height, start: tuple[int], finish: tuple[int],
           perfect: list[str], name_file: str, seed: Optional[Any]) -> None:

    gr = np.array([[15 for _ in range(width)] for _ in range(height)])
    grid = grow_tree(gr, width, height, start, perfect, seed)
    way = find_way(grid, start, finish, width, height)

    entry = f"{start[0]},{start[1]}"
    end = f"{finish[0]},{finish[1]}"
    try:
        with open(name_file, "w") as f:
            for y, row in enumerate(grid):  # rangee
                for x, value in enumerate(row):
                    number = hex(value)[2:]
                    f.write(number)
                f.write("\n")
            f.write("\n")
            f.write(entry)
            f.write("\n")
            f.write(end)
            f.write("\n")
            for w in way:
                f.write(w)
    except (ValueError, AttributeError) as e:
        print(f"{red}[ERROR]{reset}: in gen_output.py {e}")
        exit()


if __name__ == "__main__":

    grid = [
        [11,  9,  3, 13,  1,  3, 11,  9,  5,  5,  1,  5,  5,  5,  3],
        [10, 10, 10,  9,  6, 10, 10,  8,  5,  7, 12,  3, 13,  3, 10],
        [12,  6, 10, 10, 11, 10, 12,  6,  9,  5,  3, 12,  3, 10, 10],
        [11,  9,  6, 10,  8,  6,  9,  3, 10, 11, 12,  5,  6, 10, 10],
        [10, 12,  3, 10, 12,  5,  6,  8,  6, 12,  5,  1,  5,  6, 10],
        [8,  5,  6, 10, 15,  9,  7, 10, 15, 15, 15,  8,  5,  5,  6],
        [12,  3, 13,  2, 15, 12,  5,  0,  5,  7, 15, 10, 13,  1,  3],
        [11, 12,  3, 10, 15, 15, 15, 10, 15, 15, 15, 12,  5,  6, 10],
        [8,  7, 10, 12,  5,  3, 15, 10, 15, 13,  5,  1,  5,  3, 10],
        [8,  5,  6,  9,  5,  6, 15, 14, 15, 15, 15, 14,  9,  2, 10],
        [12,  3, 13,  4,  5,  5,  5,  5,  5,  5,  3,  9,  6, 14, 10],
        [9,  6,  9,  5,  5,  5,  5,  5,  5,  3, 10, 12,  3,  9,  6],
        [12,  3,  8,  3, 11,  9,  5,  5,  3, 10, 12,  3, 10, 12,  3],
        [11, 10, 14, 10,  8,  6,  9,  3, 12,  6,  9,  6,  8,  7, 10],
        [12,  4,  5,  6, 12,  5,  6, 12,  5,  5,  6, 13,  4,  5,  6],
    ]

    start = (0, 0)
    finish = (14, 14)

    koi = output(15, 15, start, finish, True, "maze.txt")
    print(koi)
