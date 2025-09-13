from utilities import constants
import datetime, sys

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
