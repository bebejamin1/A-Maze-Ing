
from typing import Union, Any

from maze_algorithm.growing_tree import GrowTree
from maze_algorithm.defective_maze import Deficient
from tools1.bfs_algorithm import find_way


red = "\033[31m\033[5m\033[1m"
reset = "\033[0m"


def output(width, height, start: tuple[int, int], finish: tuple[int, int],
           perfect: bool, name_file: str, seed: Any | None) -> None:

    maze_gen: Union[GrowTree, Deficient]

    if (perfect):
        maze_gen = GrowTree(width, height, start, finish, perfect, seed)
    else:
        maze_gen = Deficient(width, height, start, finish, perfect, seed)

    grid_start: list[list[int]] = [[15 for _ in range(width)]
                                   for _ in range(height)]

    grid: list[list[int]] = maze_gen.maze(grid_start)

    if (grid[start[1]][start[0]] == 15):
        entry = f"{0},{0}"
        sx = sy = 0
    else:
        entry = f"{start[0]},{start[1]}"
        sx, sy = start

    if (grid[finish[1]][finish[0]] == 15):
        end = f"{height - 1},{width - 1}"
        fx = height - 1
        fy = width - 1
    else:
        end = f"{finish[0]},{finish[1]}"
        fx = finish[0]
        fy = finish[1]

    way = find_way(grid, (sx, sy), (fx, fy), width, height)

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
