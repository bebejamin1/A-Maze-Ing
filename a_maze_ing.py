import sys
from pydantic import ValidationError
import draw
import parsing




if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit()

    config_file = sys.argv[1]

    config_dict = parsing.extract_config(config_file)
    config = parsing.MazeConfig(**config_dict)

    print()
    print("     .-.   .-.     .--.                         ".center(60, " "))
    print("    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  ".center(60, " "))
    print("    |   | |   |   \  '-. '-'   '-'  '-'   '..'  ".center(60, " "))
    print("    '^^^' '^^^'    '--'                         ".center(60, " "))
    print()


    print("    WELCOME !")
    while True:
        print()
        print("1 - Re-generate a new maze")
        print("2 - Show/Hide path from entry to exit")
        print("3 - Rotate maze colors")
        print("4 - Quit")

        try:
            choice = int(input("\nWhat do you want ? : "))
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
        except Exception as e:
            print(f"ERROR: {e}")
       
