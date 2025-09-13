"""
Generate study and review dates using fixed day intervals.
The study/review date is provided as a string in the format "YYYY-MM-DD".
"""

from datetime import datetime, timedelta, date

INTERVAL_OFFSETS = [2, 6, 13, 29, 59, 119]  # Days between study date and each review.
DATE_FORMAT = "%Y-%m-%d"

def schedule_review_dates(study_date: date) -> list[str]:
    """
    Generate review dates from a given study date.

    The review dates are calculated by adding predefined day offsets
    to the provided study date.

    :param study_date: A `date` object representing the study date.
    :return: List of review dates in "YYYY-MM-DD" format.
    """
    review_dates = [
        study_date + timedelta(days=offset)
        for offset in INTERVAL_OFFSETS
    ]
    return format_dates(review_dates)

def get_study_dates(review_date: date) -> list[str]:
    """
    Generate possible study dates from a given review date.

    The study dates are calculated by subtracting predefined day offsets
    from the provided review date.

    :param review_date: Review date in "YYYY-MM-DD" format.
    :return: List of study dates in "YYYY-MM-DD" format.
    """
    study_dates = [
        review_date - timedelta(days=offset)
        for offset in INTERVAL_OFFSETS
    ]
    return format_dates(study_dates)

def format_dates(dates: list[date]) -> list[str]:
    """
    Format a list of `date` objects into strings.

    :param dates: List of `date` objects.
    :return: List of date strings in "YYYY-MM-DD" format.
    """
    return [d.strftime(DATE_FORMAT) for d in dates]
