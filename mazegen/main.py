from mazegen.visualize.parsing import (get_tuple, extract_config)
from mazegen.visualize.parsing import MazeConfig
import sys
from pydantic import ValidationError
from mazegen.tools1.gen_output import output


def createmaze(file: str) -> None:

    try:
        config_dict = extract_config(file)
        config = MazeConfig.model_validate(config_dict)
        coord = get_tuple(config.ENTRY, config.EXIT)
        output(config.WIDTH, config.HEIGHT, coord[0], coord[1],
               config.PERFECT, config.OUTPUT_FILE, config.SEED)
    except (ValidationError) as e:
        print("\nExpected validation error:")
        print(e.errors()[0]["msg"])
        print()
        sys.exit()
    except (ValueError) as e:
        print("\nExpected validation error:")
        print(e)
        print()
        sys.exit()


if __name__ == "__main__":
    file = "config.txt"
    maze = createmaze(file)
    print(f"Generated file : {maze.OUTPUT_FILE}")
