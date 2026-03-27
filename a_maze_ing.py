import sys
from pydantic import ValidationError
import draw
import parsing


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit()

    config_file = sys.argv[1]

    try:
        config_dict = parsing.extract_config(config_file)
        config = parsing.MazeConfig(**config_dict)
    except (ValueError, ValidationError) as e:
        print("\nExpected validation error:")
        print(e.errors()[0]["msg"])
        print()
        sys.exit()

    print()
    print("     .-.   .-.     .--.                         ".center(60, " "))
    print("    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  ".center(60, " "))
    print("    |   | |   |   \  '-. '-'   '-'  '-'   '..'  ".center(60, " "))
    print("    '^^^' '^^^'    '--'                         ".center(60, " "))
    print()


    print('\033[43m  WELCOME !  \033[0m'.center(68, " "))
    while True:
        print()
        print("1 - Re-generate a new maze")
        print("2 - Show/Hide path from entry to exit")
        print("3 - Rotate maze colors")
        print("4 - Quit")

        try:
            choice = int(input("\n" + "\033[40m What do you want ? \033[0m" + ": "))
            maze, entry, exit_coord, path = parsing.maze_data_extract(config.OUTPUT_FILE)
            if choice == 1:
                draw.draw_walls(maze, config, path, False)
            elif choice == 2:
                pass
            elif choice == 3:
                color = True
                draw.draw_walls(maze, config, path, True)
            elif choice == 4:
                print("Goodbye!")
                sys.exit()
            else:
                print("\nIt's not on the menu :/\n")
        except (ValueError, TypeError, ValidationError) as e:
            print(f"\nERROR main: {e}\n")
            sys.exit()
        except KeyboardInterrupt:
            print("\n\nWhy shut down the programme so abruptly? :(\n")
            sys.exit()
