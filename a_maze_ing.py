import sys
from pydantic import ValidationError
from visualize.draw import draw_walls
from visualize.parsing import maze_data_extract, get_tuple, extract_config
from visualize.parsing import MazeConfig
from tools1.gen_output import output


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit()

    config_file = sys.argv[1]

    try:
        config_dict = extract_config(config_file)
        config = MazeConfig(**config_dict)
    except (ValueError, ValidationError) as e:
        print("\nExpected validation error:")
        print(e.errors()[0]["msg"])
        print()
        sys.exit()

    print()
    print("     .-.   .-.     .--.                         ".center(60, " "))
    print("    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  ".center(60, " "))
    print("    |   | |   |   \\  '-. '-'   '-'  '-'   '..'  ".center(60, " "))
    print("    '^^^' '^^^'    '--'                         ".center(60, " "))
    print()

    print('\033[43m  WELCOME !  \033[0m'.center(68, " "))
    show_path = False
    while True:
        print()
        print("1 - Re-generate a new maze")
        print("2 - Show/Hide path from entry to exit")
        print("3 - Rotate maze colors")
        print("4 - Quit")
        try:
            choice = int(input("\n" + "\033[40m What do you want ? \033[0m" + ": "))
            if choice == 1:
                coord = get_tuple(config.ENTRY, config.EXIT)
                output(config.WIDTH, config.HEIGHT, coord[0], coord[1],
                       config.PERFECT, config.OUTPUT_FILE, config.SEED)
                maze, entry, exit_coord, path = maze_data_extract(config.OUTPUT_FILE)
                draw_walls(maze, config, path, False, show_path)
            elif choice == 2:
                if show_path is False:
                    show_path = True
                else:
                    show_path = False
                draw_walls(maze, config, path, False, show_path)
            elif choice == 3:
                color = True
                maze, entry, exit_coord, path = maze_data_extract(config.OUTPUT_FILE)
                draw_walls(maze, config, path, color, show_path)
            elif choice == 4:
                print()
                print("█████████████████████████████████████".center(70, " "))
                print("███████▀█████████████████████████████".center(70, " "))
                print("██████░░█████████████████████████████".center(70, " "))
                print("█████▀░▄█████████████████████████████".center(70, " "))
                print("█████░░▀▀▀▀▀███▀▀█████▀▀███▀▀▀▀▀█████".center(70, " "))
                print("█████░░▄██▄░░███░░███░░███░░███░░████".center(70, " "))
                print("████░░█████░░███░▄███░░██░░▀▀▀░▄█████".center(70, " "))
                print("████░░████▀░███░░███▀░███░░██████████".center(70, " "))
                print("████░░█▀▀░▄████▄░▀▀▀░▄███▄░▀▀▀░▄█████".center(70, " "))
                print("█████▄▄▄███████████░░██████▄▄████████".center(70, " "))
                print("██████████████░▀█▀░▄█████████████████".center(70, " "))
                print("███████████████▄▄▄███████████████████".center(70, " "))
                print("█████████████████████████████████████".center(70, " "))
                print()
                sys.exit()
            else:
                print("\nIt's not on the menu :/\n")
        except (ValueError, TypeError, ValidationError) as e:
            print(f"\nERROR main: {e}\n")
            sys.exit()
        except KeyboardInterrupt:
            print("\n\nWhy shut down the programme so abruptly? :(\n")
            sys.exit()
