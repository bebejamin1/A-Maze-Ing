#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   test.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/18 11:31:23 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/18 16:10:48 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import numpy as np


def look_neighbor(grid: list[list[int]], x1: int, y1: int) -> list:

    x_axes = [0, 1, 0, -1]
    y_axes = [1, 0, -1, 0]
    compass = ["n", "e", "s", "w"]
    virgin_neighbor = []

    for x, y, c in zip(x_axes, y_axes, compass):
        print()
        if (grid[x1+x][y1+y] == 15 or grid[x1+x][y1+y] > 0):
            virgin_neighbor.append(c)
    return (virgin_neighbor)


def maze(grid: list[list[int]], width: int, height: int,
         entry: tuple[int, int],
         finish: tuple[int, int]) -> list[list[int]]:

    x1, y1 = entry
    x2, y2 = finish
    n, e, s, w = 1, 2, 4, 8

    while (np.max(grid) == 15):
        test = look_neighbor(grid, x1, y1)
        print(test)
        break

    return (grid)


def debug_display(grid: list[list[int]], width: int, height: int,
                  entry: tuple[int, int] = (0, 0),
                  finish: tuple[int, int] = (0, 0)) -> None:
    """
    Affiche le labyrinthe avec des bordures fines et des couleurs.
    Conforme aux exigences de rendu ASCII[cite: 189].
    """
    # Codes couleurs ANSI
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    WALL = "█"  # Caractère plein pour les murs

    for y in range(height):
        top_line = ""
        mid_line = ""

        for x in range(width):
            val = grid[y][x]
            is_entry = (x, y) == entry
            is_exit = (x, y) == finish

            # 1. Gestion du mur NORD (Bit 0)
            top_line += WALL * 3 if (val & 1) else WALL + "  "

            # 2. Gestion du mur OUEST (Bit 3)
            char_center = "  "
            if is_entry: char_center = GREEN + "S " + RESET  # S pour Start
            elif is_exit: char_center = RED + "E " + RESET   # E pour End

            mid_line += WALL if (val & 8) else " "
            mid_line += char_center

        print(top_line + WALL)
        print(mid_line + WALL)

    # Ligne finale pour fermer le SUD
    print(WALL * (width * 3 + 1))


def main() -> None:
    width = height = 5
    entry = (0, 0)
    finish = (4, 4)
    grid = np.array([[15 for _ in range(width)] for _ in range(height)])
    print("Grille:", grid.shape)

    maze_finish = maze(grid, width, height, entry, finish)
    print(*grid, sep="\n")

    debug_display(maze_finish, width, height, entry, finish)


if __name__ == "__main__":
    main()
