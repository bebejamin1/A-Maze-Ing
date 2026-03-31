from visualize.parsing import MazeConfig


def check_change(config: 'MazeConfig', entry: str, exit_coord:
                 str) -> str:
    """Return a warning message when visualized entry/exit is adjusted.

    Args:
        config: Validated maze configuration.
        entry: Effective entry coordinate from generated maze.
        exit_coord: Effective exit coordinate from generated maze.

    Returns:
        Human-readable warning message, or an empty string if unchanged.
    """

    if config.ENTRY != entry:
        return ("\n" + "The entrance cannot be on the walls 42. "
                "It has been moved to the start of the maze." + "\n")

    if config.EXIT != exit_coord:
        return ("\n" + "The exit cannot be on the walls 42. "
                "It has been moved to the end of the maze." + "\n")

    if (config.WIDTH <= 11 or config.HEIGHT <= 9):
        return ("\n" + "To display the number 42, the minimum size "
                "required is 11x9" + "\n")

    return ""
