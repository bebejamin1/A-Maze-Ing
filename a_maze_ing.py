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

        print(f"{config_dict}")
        print(f"TEST Config: {config.OUTPUT_FILE}")
        print()
        print(f"TEST E/E : Entry: {config.ENTRY}, Exit: {config.EXIT}")

        print()
        maze, entry, exit_coord, path = parsing.maze_data_extract(config.OUTPUT_FILE)
        print(f"TEST : {maze}")
        
        print("\n" + "Dessin".center(65, "="))

        draw.draw_walls(maze, config, path)

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])
        sys.exit()
