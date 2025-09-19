"""
This module handles adding study dates and generating their review dates. 

Review dates are calculated automatically using a fixed schedule 
and then stored in a file for later use.
"""

from utilities import (
    constants,
    scheduler,
    storage,
    toolbox
)
import datetime, sys

def study_date(date: str) -> None:
    """
    Save a study date and create its review dates.

    The function checks that the study date is valid, generates 
    the review dates using the scheduling rules, and saves them 
    in the review storage file. A study date cannot be in the 
    future. If `"today"` is given, the current system date is used.

    Parameters
    ----------
    date : str
        The study date in `"YYYY-MM-DD"` format, or the string 
        `"today"` to use the current date.

    Raises
    ------
    SystemExit
        If the study date is later than the current date.

    Side Effects
    ------------
    Adds a JSON entry that links the study date to its review 
    dates in the file defined by `constants.STUDY_REVIEW_FILE`.
    """

    # Validate study date.
    if date == "today":
        date = datetime.datetime.now().date()
    else:
        date = toolbox.parse_date(date)

        current_date = datetime.datetime.now().date()
        if date > current_date:
            sys.exit(
                "Study date cannot be in the future.\n"
                f"Current date: {current_date}\n"
                f"Study date  : {date}\n"
            )

    # Generate and save review dates.
    review_dates = scheduler.schedule_review_dates(date)

    vault_parent = toolbox.locate_vault()
    study_review_file = vault_parent / constants.STUDY_REVIEW_FILE
    storage.append_json(
        {date.strftime(constants.DATE_FORMAT):review_dates},
        study_review_file
    )
