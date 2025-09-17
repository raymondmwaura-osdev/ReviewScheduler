from utilities import constants
import datetime, pathlib, sys

# The functions are arranged in ascending alphabetical order.
def locate_vault() -> pathlib.Path:
    """
    Locate the `.rs` directory in the current directory tree.
    Exit if it isn't found or is not a directory.

    :return: A `pathlib.Path` object of the directory containing the `.rs` directory.
    """
    current_directory = pathlib.Path.cwd()

    for parent in [current_directory, *current_directory.parents]:
        vault_path = parent / constants.VAULT 
        if vault_path.exists() and vault_path.is_dir():
            return vault_path.parent

    sys.exit(
        "ReviewScheduler is not initialized in the current directory tree.\n"
        "Use `rs init` to initialize it in the current working directory."
    )

def parse_date(date_str: str) -> datetime.date:
    """
    Parse a date string into a `datetime.date` object.

    :param date_str: Date string in "YYYY-MM-DD" format.
    :return: A `datetime.date` object representing the given date.
    :raises ValueError: If the string does not match the expected format.
    """
    try:
        return datetime.datetime.strptime(date_str, constants.DATE_FORMAT).date()

    except ValueError:
        sys.exit(
            f"Invalid date format: {date_str}\n"
            "Expected format: YYYY-MM-DD"
        )
