from scheduler import schedule_review_dates
from storage import append_json
from datetime import datetime, date
import sys

DATE_FORMAT = "%Y-%m-%d"

def add_study_date(study_date: str) -> None:
    """
    + Take a study date.
    + Generate review dates.
    + Update `daily.json`.
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
    append_json("daily.json", {study_date.strftime(DATE_FORMAT):review_dates}) 

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
        print(f"Invalid date format: {study_date}\nExpected format: YYYY-MM-DD",
            file=sys.stderr)
        sys.exit()
