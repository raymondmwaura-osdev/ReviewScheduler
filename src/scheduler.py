"""
This module generates review dates based on a given study date.

The study date is provided as a string in the format "YYYY-MM-DD". Review
dates are calculated using fixed day intervals and returned as a dictionary
mapping the study date to its scheduled review dates.
"""

from datetime import datetime, timedelta

REVIEW_DATE_DELTAS = [2, 6, 13, 29, 59, 119]
DATE_FORMAT = "%Y-%m-%d"

def schedule_review_dates(study_date: str) -> dict[str, list[str]]:
    """
    Generate spaced review dates starting from a given study date.

    :param study_date: A string representing the study date in "YYYY-MM-DD" format.
    :return: A mapping from the study date to a list of review dates.
    """
  
    try:
        study_date = datetime.strptime(study_date, DATE_FORMAT).date()
    except ValueError:
        raise ValueError(
            f"Invalid date format: `{study_date}`.Expected format is 'YYYY-MM-DD'."
        )

    # Calculate review dates.
    return {
        study_date.strftime(DATE_FORMAT): [
            (study_date + timedelta(days = review_date_delta)).strftime(DATE_FORMAT)
            for review_date_delta in REVIEW_DATE_DELTAS
        ]
    }
