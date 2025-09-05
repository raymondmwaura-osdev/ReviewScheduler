"""
This module provides functionality to initialize the `.scheduler` environment 
within the current working directory. It creates the necessary directory 
structure and files required by the scheduling system.

Specifically, it generates the `.scheduler` directory along with its 
subdirectories (`schedule`, `schedule/backup`, and `history`) and essential 
files (`daily.json` and `reviews_by_date.json`). If a `.scheduler` entry 
already exists in the working directory, initialization is aborted to avoid 
overwriting existing data.
"""

from pathlib import Path

# Commented directories will be automatically created by setting `parents=True`.
DIRECTORIES = [
#   ".scheduler/",
#   ".scheduler/schedule/",
    ".scheduler/schedule/backup/",
    ".scheduler/history/"
]

FILES = [
    ".scheduler/schedule/daily.json",
    ".scheduler/schedule/reviews_by_date.json"
]

def init_scheduler() -> None:
    """
    Initialize the `.scheduler` environment in the current working directory.

    This function creates the `.scheduler` directory structure and required 
    files if they do not already exist. If a `.scheduler` directory or file 
    with the same name is found in the working directory, a `FileExistsError` 
    is raised to prevent overwriting.
    """
    working_directory = Path().cwd()

    for entry in working_directory.iterdir():
        if entry.name == ".scheduler":
            raise FileExistsError(
                "A file or directory named `.scheduler` already exists in the working directory."
            )

    for directory in DIRECTORIES:
        Path(directory).mkdir(parents=True)
    for file in FILES:
        Path(file).touch()