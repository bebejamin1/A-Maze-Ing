
from typing import Any

import random


class Deficient():
    """Generate a deficient (imperfect) maze with loops.

    A deficient maze is a maze that has loops and multiple paths between
    start and finish points, unlike a perfect maze which has exactly one path.
    """

    def __init__(self, width: int, height: int,
                 entry: tuple[int, int], finish: tuple[int, int],
                 perfect: bool, seed: Any | str) -> None:
        """Initialize a deficient maze generator.

        Args:
            width: Width of the maze grid.
            height: Height of the maze grid.
            entry: Tuple (x, y) of the entry point.
            finish: Tuple (x, y) of the exit point.
            perfect: Boolean flag (False for deficient maze).
            seed: Random seed for reproducible maze generation.
        """
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
        """Mark or unmark grid cells to display a "42" pattern.

        Before maze generation, sets cells to -42 to create a 42 pattern.
        After maze generation, converts -42 cells back to normal cells (15).

        Args:
            grid: 2D list representing the maze grid.
            state: Either "before" to mark cells or "after" to unmark them.

        Returns:
            Modified grid with the 42 pattern applied or removed.
        """
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
                    if (self.entry == (w, h)):
                        self.entry = (0, 0)
                    if (self.finish == (w, h)):
                        self.finish = (self.width - 1, self.height - 1)

            elif (state == "after"):
                for y in range(len(grid)):
                    for x in range(len(grid[y])):
                        if (grid[y][x] == -42):
                            grid[y][x] = 15

        return (grid)

# *****************************************************************************
# *                          look_neighbor()                                  *
# *           Check which tile is empty or break a random wall                *

    def look_neighbor(self, grid: list[list[int]], x1: int,
                      y1: int) -> list[str]:
        """Find available neighbors to visit or walls to break.

        Checks all four cardinal directions from the current cell. Returns
        unvisited neighbors (value 15) and potentially includes broken walls
        with a small probability (8% chance).

        Args:
            grid: 2D list representing the maze grid.
            x1: Current cell x-coordinate.
            y1: Current cell y-coordinate.

        Returns:
            List of direction strings ('N', 'E', 'S', 'W') of available
            neighbors.
        """
        directions: list[tuple[int, int, str]] = [(0, -1, "N"), (1, 0, "E"),
                                                  (0, 1, "S"), (-1, 0, "W")]
        virgin_neighbor: list[str] = []

        for x, y, c in directions:
            nx, ny = x1 + x, y1 + y

            if ((nx >= 0 and nx < self.width)
                    and (ny >= 0 and ny < self.height)):

                if (grid[ny][nx] == 15 and grid[ny][nx] != -42):

                    virgin_neighbor.append(c)

                elif (grid[ny][nx] != -42):

                    if (self.width * self.height <= 10
                            and random.random() < 0.35):
                        virgin_neighbor.append(c)

                    elif (random.random() < 0.08):
                        virgin_neighbor.append(c)

        return (virgin_neighbor)

# *****************************************************************************
# *                              min_maze()                                   *
# *                             if maze 2*2                                   *

    def min_maze(self, grid: list[list[int]]) -> list[list[int]]:
        """Generate a minimal 2x2 maze.

        Hardcodes the cell values for a 2x2 maze (the smallest possible maze).

        Args:
            grid: 2D list representing the maze grid (must be 2x2).

        Returns:
            Grid with the minimal 2x2 maze pattern.
        """
        grid[0][0] = 9
        grid[0][1] = 3
        grid[1][1] = 6
        grid[1][0] = 12

        return (grid)

# *****************************************************************************
# *                       base deficient_maze()                               *
# *       Generate the deficient maze algorithm for perfect = false           *

    def maze(self, grid_start: list[list[int]]) -> list[list[int]]:
        """Generate a complete deficient maze.

        Uses a depth-first search algorithm with recursive backtracking to
        generate a deficient maze. Includes a "42" pattern decoration if
        the maze is large enough.

        Args:
            grid_start: 2D list representing the initial maze grid.

        Returns:
            2D list containing the generated deficient maze with wall bits.
        """
        if (self.height == 2 and self.width == 2):
            return (self.min_maze(grid_start))

        if self.seed:
            random.seed(self.seed)

        grid: list[list[int]] = self.print_fortytwo(grid_start, "before")

        x, y = self.entry

        path: list[tuple[int, int]] = [(x, y)]
        mouv = {
            "N": (0, -1, 1, 4),
            "E": (1, 0, 2, 8),
            "S": (0, 1, 4, 1),
            "W": (-1, 0, 8, 2)
        }

        while (path):
            x, y = path[-1]
            neighbors = self.look_neighbor(grid, x, y)

            if (neighbors):
                direction = random.choice(neighbors)
                dx, dy, bit_c, bit_v = mouv[direction]
                nx, ny = x + dx, y + dy

                if (grid[ny][nx] == 15):
                    grid[y][x] &= ~bit_c
                    grid[ny][nx] &= ~bit_v
                    path.append((nx, ny))

                else:

                    if (grid[y][x] & bit_c):
                        grid[y][x] &= ~bit_c
                        grid[ny][nx] &= ~bit_v

            else:
                path.pop()
                if path:
                    x, y = path[-1]

        grid = self.print_fortytwo(grid, "after")
        return (grid)
