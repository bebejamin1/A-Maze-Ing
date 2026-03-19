import sys
from typing import Dict, List, Tuple
from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationError


def maze_data_extract(file: str) -> Tuple[List[str], str, str, str]:
    try:
        with open(file, 'r', encoding="utf-8") as lines:
            all_lines = [line.strip() for line in lines if line.strip()]

            if len(all_lines) < 4:
                raise ValueError("The file must contain at least 4 lines "
                                 "(maze + entry + exit + path)")

            maze = all_lines[:-3]
            entry = all_lines[-3]
            exit_coord = all_lines[-2]
            path = all_lines[-1]

            return maze, entry, exit_coord, path

    except FileNotFoundError:
        print(f"Error : The file {file} has not been generated")
        sys.exit()
    except ValueError as e:
        print(f"Error : {e}")
        sys.exit()


class MazeConfig(BaseModel):
    WIDTH: int = Field(gt=1, le=100)
    HEIGHT: int = Field(gt=1, le=100)
    ENTRY: str
    EXIT: str
    OUTPUT_FILE: str
    PERFECT: bool

    @field_validator("ENTRY", "EXIT")
    @classmethod
    def check_coordinates_format(cls, value) -> str:
        parts = value.split(",")
        if len(parts) != 2:
            raise ValueError("Coordinates must be 'x,y' format")
        return value

    @model_validator(mode="after")
    def validate_maze(self) -> Self:
        x, y = map(int, self.ENTRY.split(","))
        x2, z2 = map(int, self.EXIT.split(","))

        if self.WIDTH * self.HEIGHT < 4:
            raise ValueError("Maze dimensions must be at least 2x2.")
        if not (0 <= x < self.WIDTH and 0 <= y < self.HEIGHT):
            raise ValueError("ENTRY coordinates are out of bounds.")
        if not (0 <= x2 < self.WIDTH and 0 <= z2 < self.HEIGHT):
            raise ValueError("EXIT coordinates are out of bounds.")

        return self


def extract_config(file_path: str) -> Dict[str, str]:
    config = {}
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    config[key] = value

                else:
                    print(f"Error: Invalid line format: {line}")
                    sys.exit()

        mandatory_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE",
                          "PERFECT"]
        for key in mandatory_keys:
            if key not in config:
                print(f"Error: the key {key} is missing")
                sys.exit()

        return config

    except FileNotFoundError:
        print("Error: the file 'config.txt' is missing")
        sys.exit()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(print("Usage: python3 a_maze_ing.py <config_file>"))
        sys.exit()

    config_file = sys.argv[1]

    try:
        config_dict = extract_config(config_file)
        config = MazeConfig(**config_dict)

        print(f"{config_dict}")
        print(f"TEST Config: {config.OUTPUT_FILE}")
        print()
        print(f"TEST E/E : Entry: {config.ENTRY}, Exit: {config.EXIT}")

        print()
        maze = maze_data_extract(config.OUTPUT_FILE)
        print(f"TEST : {maze}")

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])
        sys.exit()
