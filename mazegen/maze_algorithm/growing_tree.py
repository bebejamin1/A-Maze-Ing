from typing import Any

import random


class GrowTree():
    """Generate a perfect maze using the growing tree algorithm.

    A perfect maze has exactly one path between any two points and no loops.
    Uses the growing tree algorithm to generate such mazes.
    """

    def __init__(self, width: int, height: int,
                 entry: tuple[int, int], finish: tuple[int, int],
                 perfect: bool, seed: Any | None) -> None:
        """Initialize a perfect maze generator using growing tree algorithm.

        Args:
            width: Width of the maze grid.
            height: Height of the maze grid.
            entry: Tuple (x, y) of the entry point.
            finish: Tuple (x, y) of the exit point.
            perfect: Boolean flag (True for perfect maze).
            seed: Random seed for reproducible maze generation. If None, uses
            random.
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

        Before maze generation, sets cells to -1 to create a 42 pattern.
        After maze generation, converts -1 cells back to normal cells (15).

        Args:
            grid: 2D list representing the maze grid.
            state: Either "before" to mark cells or "after" to unmark them.

        Returns:
            Modified grid with the 42 pattern applied or removed.
        """
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
                    if (self.entry == (w, h)):
                        self.entry = (0, 0)
                    if (self.finish == (w, h)):
                        self.finish = (self.width - 1, self.height - 1)

            elif (state == "after"):
                for y in range(len(grid)):
                    for x in range(len(grid[y])):
                        if (grid[y][x] <= -1):
                            grid[y][x] = 15

        return (grid)

# *****************************************************************************
# *                          look_neighbor()                                  *
# *           Check which tile is empty or break a random wall                *

    def look_neighbor(self, grid: list[list[int]], x1: int,
                      y1: int) -> list[str]:
        """Find unvisited neighboring cells.

        Checks all four cardinal directions from the current cell and returns
        the directions of unvisited cells (with value 15).

        Args:
            grid: 2D list representing the maze grid.
            x1: Current cell x-coordinate.
            y1: Current cell y-coordinate.

        Returns:
            List of direction strings ('N', 'E', 'S', 'W') of unvisited
            neighbors.
        """
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

    def maze(self, grid_start: list[list[int]]) -> list[list[int]]:
        """Generate a complete perfect maze using the growing tree algorithm.

        Implements the growing tree algorithm to create a perfect maze with
        exactly one path between any two cells. Includes a "42" pattern
        decoration if the maze is large enough.

        Args:
            grid_start: 2D list representing the initial maze grid (all cells
            set to 15).

        Returns:
            2D list containing the generated perfect maze with wall bits.
        """
        if (self.seed):
            random.seed(self.seed)

        grid: list[list[int]] = self.print_fortytwo(grid_start, "before")

        x, y = self.entry

        path: list[tuple[int, int]] = [(x, y)]
        mouv: dict[str, tuple[int, int, int, int]] = {
            "N": (0, -1, 1, 4),
            "E": (1, 0, 2, 8),
            "S": (0, 1, 4, 1),
            "W": (-1, 0, 8, 2)
        }

        while any(15 in row for row in grid):
            neighbor: list[str] = self.look_neighbor(grid, x, y)

            if (neighbor):
                dir: str = random.choice(neighbor)
                dx, dy, bits_dir, bits_next = mouv[dir]
                nx, ny = x + dx, y + dy

                grid[y][x] &= ~bits_dir
                grid[ny][nx] &= ~bits_next
                path.append((nx, ny))
                x, y = nx, ny

            else:
                path.pop()
                x, y = path[-1]

        grid_finish: list[list[int]] = self.print_fortytwo(grid, "after")
        return (grid_finish)
