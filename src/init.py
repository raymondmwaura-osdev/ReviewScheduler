"""
+ Check if a `.scheduler` directory already exists in the current working directory.
+ Create a `.scheduler` directory with these subdirectories:
    - schedule
    - schedule/backup
    - history
"""

from pathlib import Path

# Commented directories will be automatically created by setting `parents=True`.
DIRECTORIES = [
#   ".scheduler/",
#   ".scheduler/schedule/",
    ".scheduler/schedule/backup/",
    ".scheduler/history/"
]

def init_scheduler() -> None:
    """
    Create a `.scheduler` directory in the current working directory if
    it doesn't already exist.
    """

    working_directory = Path().cwd()

    for entry in working_directory.iterdir():
        if entry.name == ".scheduler":
            raise FileExistsError(
                "A file or directory named `.scheduler` already exists in the working directory."
            )

    for directory in DIRECTORIES:
        Path(directory).mkdir(parents=True)
