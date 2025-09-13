"""
This module provides functionality to initialize the `.scheduler` environment 
within the current working directory. It creates the necessary directory 
structure and files required by the scheduling system.

Specifically, it generates the `.rs` directory along with its
subdirectories (`backup` and `history`) and essential files
(`study_review.json` and `review_study.json`). If a `.rs` entry
already exists in the working directory, initialization is aborted to avoid
overwriting existing data.
"""

from utilities import storage, constants
import pathlib, sys

# Commented directories will be automatically created by setting `parents=True`.
DIRECTORIES = [
#   f"{constants.VAULT}",
    f"{constants.VAULT}/backup",
    f"{constants.VAULT}/history"
]

JSON_FILES = [
    f"{constants.VAULT}/{constants.STUDY_REVIEW_FILE}",
    f"{constants.VAULT}/{constants.REVIEW_STUDY_FILE}"
]

def init_rs() -> None:
    """
    Initialize the `.rs` environment in the current working directory.

    :raises `FileExistsError`: If a `.rs` directory or file is found
        in the working directory.
    """
    working_directory = pathlib.Path().cwd()

    for entry in working_directory.iterdir():
        if entry.name != constants.VAULT: continue
        sys.exit(
            f"ERROR: A file or directory named `{constants.VAULT}` "
            "already exists in the working directory."
        )

    for directory in DIRECTORIES:
        pathlib.Path(directory).mkdir(parents=True)
    for file in JSON_FILES:
        # Initialize JSON files with an empty dictionary.
        # This prevents `json.decoder.JSONDecodeError` which is raised when
        # attempting to read an empty JSON file.
        storage.write_json({}, pathlib.Path(file))
