"""Exercise 5.1 - That's the way.

Find all the files in a directory whose names start with "deep".
"""
import os

PREFIX = "deep"


def thats_the_way(directory_path: str) -> list[str]:
    """Return the names of the files in a directory that start with "deep".

    Sub-directories are skipped, even if their name starts with "deep".

    Args:
        directory_path: Path to the directory to search in.

    Returns:
        A list of file names (not full paths) that start with "deep".

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    with os.scandir(directory_path) as entries:
        return sorted(
            entry.name
            for entry in entries
            if entry.is_file() and entry.name.startswith(PREFIX)
        )


if __name__ == "__main__":
    print(thats_the_way("images"))
