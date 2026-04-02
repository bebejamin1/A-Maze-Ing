from typing import Final

Coords = tuple[int, int]


def is_valid_neighbor(grid: list[list[int]], x: int, y: int,
                      nx: int, ny: int, w: int, h: int) -> bool:
    """Check if a neighbor cell is valid and accessible.

    Verifies that the neighbor is within grid bounds and that there is no wall
    between the current cell and the neighbor cell based on the wall bits.

    Args:
        grid: 2D list of integers representing maze cells with wall bits.
        x: Current cell x-coordinate.
        y: Current cell y-coordinate.
        nx: Neighbor cell x-coordinate.
        ny: Neighbor cell y-coordinate.
        w: Width of the grid.
        h: Height of the grid.

    Returns:
        True if the neighbor is valid and accessible, False otherwise.
    """
    if (not (0 <= nx < w and 0 <= ny < h)):
        return (False)

    dx: int = nx - x
    dy: int = ny - y

    bits: Final[dict[Coords, int]] = {
        (0, -1): 1,
        (1, 0): 2,
        (0, 1): 4,
        (-1, 0): 8
    }

    wall_bit: int = bits.get((dx, dy), 0)

    return ((grid[y][x] & wall_bit) == 0)


def find_way(grid: list[list[int]], start: Coords,
             finish: Coords, width: int, height: int) -> list[str]:
    """Find a path from start to finish using Breadth-First Search (BFS).

    Searches the maze grid for a path from the start coordinates to the finish
    coordinates, avoiding walls. Returns a list of moves as directions.

    Args:
        grid: 2D list of integers representing maze cells with wall bits.
        start: Tuple (x, y) of the starting position.
        finish: Tuple (x, y) of the target position.
        width: Width of the grid.
        height: Height of the grid.

    Returns:
        List of direction strings ('N', 'E', 'S', 'W') representing the path
        from start to finish. Returns empty list if no path exists.
    """
    queue: list[Coords] = [start]

    path_data: dict[Coords, tuple[Coords | None, str]] = {
        start: (None, "")
    }

    moves: Final[list[tuple[int, int, str]]] = [
        (0, -1, 'N'), (1, 0, 'E'), (0, 1, 'S'), (-1, 0, 'W')
    ]

    head: int = 0

    while (head < len(queue)):
        curr: Coords = queue[head]
        head += 1

        if (curr == finish):
            break

        curr_x, curr_y = curr
        for dx, dy, name in moves:
            nx, ny = curr_x + dx, curr_y + dy
            neighbor: Coords = (nx, ny)

            if (neighbor not in path_data and is_valid_neighbor(grid,
                                                                curr_x,
                                                                curr_y,
                                                                nx, ny,
                                                                width,
                                                                height)):
                path_data[neighbor] = (curr, name)
                queue.append(neighbor)

    if (finish not in path_data):
        return []

    path: list[str] = []
    current_pos: Coords | None = finish

    while (current_pos is not None and current_pos != start):
        parent, direction = path_data[current_pos]
        path.append(direction)
        current_pos = parent

    return (path[::-1])
