#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   bfs_algorithm.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/21 15:22:46 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/27 11:37:23 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections import deque
from typing import List, Tuple

# from test_display import debug_display


# *****************************************************************************
# *                            neighbors()                                    *
# *              Check to see if any neighbors are around                     *

def neighbors(grid: List[List[int]], x1: int, y1: int, x2: int, y2: int,
              width: int, height: int) -> bool:

    if (x2 < 0 or y2 < 0 or x2 >= width or y2 >= height):
        return (False)

    dx = x2 - x1
    dy = y2 - y1

    direction_bits = {
        (0, -1): 1,
        (1, 0): 2,
        (0, 1): 4,
        (-1, 0): 8
    }

    if ((dx, dy) not in direction_bits):
        return (False)

    wall_bit = direction_bits[(dx, dy)]

    if (grid[y1][x1] & wall_bit != 0):
        return (False)

    return (True)


# *****************************************************************************
# *                            find_way()                                     *
# *                   Find your way through the maze                          *

def find_way(grid: List[List[int]], start: Tuple[int, int],
             finish: Tuple[int, int], width: int, height: int) -> List[str]:

    directions = [
        (0, -1, 'N'),
        (1, 0, 'E'),
        (0, 1, 'S'),
        (-1, 0, 'W')
    ]

    sx, sy = start
    fx, fy = finish

    queue = deque([(sx, sy)])

    visited = {(sx, sy): None}

    parent_direction = {(sx, sy): None}

    found = False

    while queue and not found:
        x, y = queue.popleft()

        if (x, y) == (fx, fy):
            found = True
            break

        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy

            if ((nx, ny) not in visited and neighbors(grid, x, y, nx,
                                                      ny, width, height)):

                visited[(nx, ny)] = (x, y)
                parent_direction[(nx, ny)] = direction
                queue.append((nx, ny))

    if not found:
        return []

    path = []
    current = (fx, fy)

    while current != (sx, sy):
        parent = visited[current]
        if parent is None:
            break
        direction = parent_direction[current]
        path.append(direction)
        current = parent

    path.reverse()

    return path


# =============================================================================
# ============================== MAIN =========================================
# =============================================================================

# if __name__ == "__main__":

#     grid = [
#         [11,  9,  5,  3,  9,  1,  5,  5,  5,  7],
#         [12,  6, 11, 10, 14, 12,  5,  5,  5,  3],
#         [13,  5,  2, 12,  5,  5,  5,  5,  5,  2],
#         [9,  3, 10,  9,  5,  1,  7,  9,  5,  6],
#         [10, 12,  6, 10,  9,  6,  9,  6,  9,  3],
#         [8,  5,  3, 10, 12,  3, 10,  9,  6, 10],
#         [10, 11, 12,  6, 11, 12,  6, 10, 11, 10],
#         [10,  8,  5,  3, 12,  5,  1,  6, 10, 10],
#         [10, 12,  3, 12,  5,  3, 10, 11,  8,  6],
#         [12,  5,  6, 13,  5,  4,  6, 12,  4,  7],

#     ]

#     width = height = 10

#     start = (0, 0)
#     finish = (9, 9)

#     debug_display(grid, width, height, start, finish)
#     way = find_way(grid, start, finish, width, height)
#     print(f"Chemin trouvé: {way}")
#     print(f"Longueur du chemin: {len(way)}")

#     debug_display(grid, width, height, start, finish, (0, 0), way)
#     print(way)
