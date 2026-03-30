
from collections import deque
from typing import List, Tuple


# *****************************************************************************
# *                            neighbors()                                    *
# *              Check to see if any neighbors are around                     *

def is_valid_neighbor(grid: List[List[int]], current_x: int, current_y: int,
                      next_x: int, next_y: int,
                      width: int, height: int) -> bool:

    is_within_bounds = 0 <= next_x < width and 0 <= next_y < height
    if (not is_within_bounds):
        return (False)

    direction_offset_x = next_x - current_x
    direction_offset_y = next_y - current_y

    direction_to_wall_bit = {
        (0, -1): 1,
        (1, 0): 2,
        (0, 1): 4,
        (-1, 0): 8
    }

    direction = (direction_offset_x, direction_offset_y)
    if (direction not in direction_to_wall_bit):
        return (False)

    wall_bit = direction_to_wall_bit[direction]
    has_wall = grid[current_y][current_x] & wall_bit != 0

    return (not has_wall)


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

    start_x, start_y = start
    finish_x, finish_y = finish

    frontier = deque([(start_x, start_y)])
    position_to_parent = {(start_x, start_y): None}
    position_to_direction = {(start_x, start_y): None}

    while (frontier):
        current_x, current_y = frontier.popleft()

        if ((current_x, current_y) == (finish_x, finish_y)):
            break

        for offset_x, offset_y, direction_name in directions:
            next_x = current_x + offset_x
            next_y = current_y + offset_y
            next_position = (next_x, next_y)

            is_unvisited = next_position not in position_to_parent
            is_accessible = is_valid_neighbor(grid, current_x, current_y,
                                              next_x, next_y, width, height)

            if is_unvisited and is_accessible:
                position_to_parent[next_position] = (current_x, current_y)
                position_to_direction[next_position] = direction_name
                frontier.append(next_position)

    finish_position = (finish_x, finish_y)
    if (finish_position not in position_to_parent):
        return []

    path_directions = []
    current_position = finish_position

    while (current_position != (start_x, start_y)):
        parent_position = position_to_parent[current_position]
        direction_to_parent = position_to_direction[current_position]
        path_directions.append(direction_to_parent)
        current_position = parent_position

    path_directions.reverse()

    return (path_directions)
