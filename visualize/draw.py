import os
import random
import time
from typing import Dict, List, Tuple
from visualize.parsing import MazeConfig


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

COLORS_42 = [
    "\033[30m",
    "\033[37m",
    "\033[0;96m",
]

RESET = "\033[0m"


def get_wall_color() -> str:
    print()
    print("Choose your color:")
    print(COLORS[0] + "1 - Red")
    print(COLORS[1] + "2 - Green")
    print(COLORS[2] + "3 - Yellow")
    print(COLORS[3] + "4 - Blue")
    print(COLORS[4] + "5 - Purple")
    print(COLORS[5] + "6 - Cyan" + RESET)
    print("7 - Default (white)")

    choice = input("\nSo, what would you like? : ")

    try:
        choice_int = int(choice)
        if 0 < choice_int < 8:
            if choice_int == 7:
                return "\033[37m"
            return COLORS[choice_int - 1]
        else:
            raise ValueError
    except ValueError:
        print(f"\nIncorrect input: you must choose a number between 1 and 7")


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
               color: bool, show_path: bool) -> None:
    ent_x, ent_y = map(int, config.ENTRY.split(","))
    ext_x, ext_y = map(int, config.EXIT.split(","))

    if color is True:
        color = get_wall_color()
    else:
        color = "\033[37m"

    try:
        while True:

            os.system('clear')

            wall = color + "██" + RESET

            coord_path = decode_path(ent_x, ent_y, path)

            for y, line in enumerate(coord):
                top_line = ""
                mid_line = ""

                for x, hexa in enumerate(line):

                    walls = decode_walls(hexa)

                    top_line += wall
                    top_line += wall if walls["N"] else "  "

                    mid_line += wall if walls["W"] else "  "

                    if x == ent_x and y == ent_y and show_path:
                        mid_line += "🟩"
                    elif x == ext_x and y == ext_y and show_path:
                        mid_line += "🏁"
                    elif hexa.upper() == "F":
                        if color != "\033[37m":
                            other_color = random.choice(COLORS_42)
                            mid_line += other_color + "██" + RESET
                            continue
                        color_42 = random.choice(COLORS)
                        mid_line += color_42 + "██" + RESET
                    elif (x, y) in coord_path and show_path:
                        mid_line += "⭐"
                    else:
                        mid_line += "  "

                print(top_line + wall)
                print(mid_line + wall)

            print(wall * (config.WIDTH * 2 + 1))

            print("\nTo display the menu: Ctrl + C :)\n")

            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nThe animation has stopped :(\n")
