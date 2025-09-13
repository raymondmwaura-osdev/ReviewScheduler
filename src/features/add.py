from utilities import (
    constants,
    scheduler,
    storage,
    toolbox
)
import datetime, sys

def study_date(date: str) -> None:
    """
    Generate review dates for the given study date and save them in `constants.STUDY_REVIEW_FILE`.
    NOTE: Study date cannot be in the future.

    :param date: Date of study in the format: "YYYY-MM-DD".
    """

    # Validate study date.
    if date == "today": date = datetime.datetime.now().date()
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

    vault_path = toolbox.locate_vault()
    study_review_file = vault_path / constants.STUDY_REVIEW_FILE
    storage.append_json({date.strftime(constants.DATE_FORMAT):review_dates}, study_review_file)
