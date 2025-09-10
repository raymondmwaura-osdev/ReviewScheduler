from scheduler import schedule_review_dates
from datetime import datetime, date
from storage import append_json
from pathlib import Path
import sys

DATE_FORMAT = "%Y-%m-%d"

def add_study_date(study_date: str) -> None:
    """
    Generate review dates for the given study date and save them in `daily.json`.

    :param study_date: Date of study in the format: "YYYY-MM-DD".
    """

    # Validate study date.
    if study_date == "today": study_date = datetime.now().date()
    else:
        study_date = parse_date(study_date)

        if study_date > datetime.now().date():
            print("Study date cannot be in the future.", file=sys.stderr)
            sys.exit()

    # Generate and save review dates.
    review_dates = schedule_review_dates(study_date)

    scheduler_directory = locate_vault()
    json_file = scheduler_directory / "schedule/daily.json"
    append_json(json_file, {study_date.strftime(DATE_FORMAT):review_dates}) 

def locate_vault() -> Path:
    """
    Locate the `.scheduler` directory in the current directory tree.
    Exit if `.scheduler` isn't found or is not a directory.

    :return: A `Path` object of the `.scheduler` directory.
    """
    current_directory = Path.cwd()

    for parent in [current_directory, *current_directory.parents]:
        vault_path = parent / ".scheduler"
        if vault_path.exists() and vault_path.is_dir():
            return vault_path

    sys.exit(
        "Scheduler is not initialized in the current directory tree.\n"
        "Use `scheduler init` to initialize it in the current working directory."
    )

def parse_date(date_str: str) -> date:
    """
    Parse a date string into a `date` object.

    :param date_str: Date string in "YYYY-MM-DD" format.
    :return: A `date` object representing the given date.
    :raises ValueError: If the string does not match the expected format.
    """
    try:
        return datetime.strptime(date_str, DATE_FORMAT).date()

    except ValueError:
        sys.exit(
            f"Invalid date format: {study_date}\n"
            "Expected format: YYYY-MM-DD"
        )
