import os
import sys
import random
import time
from typing import Dict, List, Tuple
from parsing import MazeConfig


COLORS = [
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
    "\033[0;91m",
    "\033[0;95m",
]

RESET = "\033[0m"

def get_wall_color() -> str:
        print("Choose your color:")
        print("1 - Red")
        print("2 - Green")
        print("3 - Yellow")
        print("4 - Blue")
        print("5 - Purple")
        print("6 - Cyan")
        print("7 - Default (white)")

        choice = input(("So, what would you like? : "))
        
        try:
            choice_int = int(choice)
            return COLORS[choice_int - 1]
        except (ValueError, IndexError):
            print(f"Incorrect input: you must choose a number between 1 and 7")
            sys.exit()


def decode_path(ent_x: int, ent_y: int, coord: List[str]) -> Tuple[int]:
    path_coord = set()

    for direction in coord:
        if direction == 'N':
            ent_y -= 1
        elif direction == "E":
            ent_x += 1
        elif direction == "S":
            ent_y += 1
        elif direction == "W":
            ent_x -= 1

        path_coord.add((ent_x, ent_y))

    print(path_coord)
    return path_coord


def decode_walls(maze: str) -> Dict[str, bool]:
    
    wall = int(maze, 16)

    return {
        "N": bool(wall & 1),
        "E": bool(wall & 2),
        "S": bool(wall & 4),
        "W": bool(wall & 8) 
    }


def draw_walls(coord: List[str], config: 'MazeConfig', path: List[str],
               ) -> None:
    ent_x, ent_y = map(int, config.ENTRY.split(","))
    ext_x, ext_y = map(int, config.EXIT.split(","))

    try:
        while True:

            os.system('clear')

            #color = get_wall_color()

            wall = "██"

            coord_path = decode_path(ent_x, ent_y, path)

            for y, line in enumerate(coord):
                top_line = ""
                mid_line = ""

                for x, hexa in enumerate(line):

                    walls = decode_walls(hexa)

                    top_line += wall
                    top_line += wall if walls["N"] else "  "

                    mid_line += wall if walls["W"] else "  "
                    
                    if x == ent_x and y == ent_y:
                        mid_line += "🟩"
                    elif x == ext_x and y == ext_y:
                        mid_line += "🏁"
                    elif hexa.upper() == "F":
                        color = random.choice(COLORS)
                        mid_line += color + wall + RESET
                    elif (x, y) in coord_path:
                        mid_line += "⭐"
                    else:
                        mid_line += "  "

                print(top_line + wall)
                print(mid_line + wall)

            print(wall * (config.WIDTH * 2 + 1))

            time.sleep(0.2)

    except KeyboardInterrupt:
        print("The animation has stopped :(")
