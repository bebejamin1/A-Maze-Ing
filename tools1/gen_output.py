
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

    if (grid[start[1]][start[0]] == 15):
        print("start deplace")
        entry = f"{0},{0}"
    else:
        entry = f"{start[0]},{start[1]}"

    if (grid[finish[1]][finish[0]] == 15):
        print("finish deplace")
        end = f"{height - 1},{width - 1}"
    else:
        end = f"{finish[0]},{finish[1]}"
    print(end, start)
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
