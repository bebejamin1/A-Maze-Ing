import sys
from typing import Dict, List, Tuple, Optional, Any
from typing_extensions import Self
from pydantic import (BaseModel, Field, field_validator, model_validator)


def get_tuple(entry: str, exit_coord: str) -> List[Tuple[int]]:
    ent_x, ent_y = map(int, entry.split(","))
    ext_x, ext_y = map(int, exit_coord.split(","))

    return [(ent_x, ent_y), (ext_x, ext_y)]


def maze_data_extract(file: str) -> Tuple[List[str], str, str, str]:
    try:
        with open(file, 'r', encoding="utf-8") as lines:
            all_lines = [line.strip() for line in lines if line.strip()]

            if len(all_lines) <= 4:
                raise ValueError("The file must contain at least 4 lines "
                                 "(maze + entry + exit + path)")

            maze = all_lines[:-3]
            entry = all_lines[-3]
            exit_coord = all_lines[-2]
            path = all_lines[-1]

            return maze, entry, exit_coord, path

    except FileNotFoundError:
        print(f"\nError : The file {file} has not been generated\n")
        sys.exit()
    except ValueError as e:
        print(f"\nError : {e}\n")
        sys.exit()


class MazeConfig(BaseModel):
    WIDTH: int = Field(gt=1, le=50)
    HEIGHT: int = Field(gt=1, le=50)
    ENTRY: str
    EXIT: str
    OUTPUT_FILE: str
    PERFECT: bool
    SEED: Optional[Any] = Field(default="")

    @field_validator("ENTRY", "EXIT")
    @classmethod
    def check_coordinates_format(cls, value) -> str:
        if not "," in value:
            raise ValueError("Coordinates must be 'x,y' format")
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
            if key not in config or not config[key]:
                raise ValueError(f"the key {key} is missing or empty")

        return config

    except (FileNotFoundError, ValueError) as e:
        print(f"\nERROR parsing: {e}\n")
        sys.exit()
