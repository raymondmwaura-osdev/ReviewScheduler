from utilities import (
    constants,
    markdown,
    scheduler,
    storage,
    toolbox
)
import datetime

def get_reviews(review_date: str) -> None:
    """
    Generate a markdown file showing study dates to review for the given date.

    + Get a list of study dates to review on the given review date.
    + Get the list from 'reviews_by_date.json`. If it doesn't exist, generate and save the list.
    + Generate markdown output.

    :param review_date: The review date. Can be "today" or a date string in this format: YYYY-MM-DD.
    """
    review_date = (
        datetime.datetime.now().date() if review_date == "today"
        else toolbox.parse_date(review_date)
    )

    # Get study dates to review.
    review_study_file = toolbox.locate_vault() / constants.REVIEW_STUDY_FILE
    study_dates = storage.get_item(review_date, review_study_file)
    if not study_dates: study_dates = generate_and_save_review_date(review_date)

    # Generate markdown output.
    main_heading = markdown.heading(, level=1)
    top_priority_heading = markdown.heading("Top Priority Reviews", level=2)
    mid_priority_heading = markdown.heading("Mid Priority Reviews", level=2)
    least_priority_heading = markdown.heading("Least Priotiry Reviews", level=2)

def generate_and_save_review_date(review_date: datetime.date) -> list[str]:
    """
    Generate and save a dictionary with the given review date as the key
    and a list of study dates as the value. Return the list of study dates.

    :param review_date: A `datetime.date` object of the review date.
    :return: A generated list of valid study dates as strings.
    """
    # Generate.
    study_review_file = toolbox.locate_vault() / constants.STUDY_REVIEW_FILE
    possible_study_dates = scheduler.get_study_dates(review_date)
    actual_study_dates = storage.get_keys(study_review_file)

    valid_study_dates = (
        [] if len(actual_study_dates) == 0
        else [
            study_date
            for study_date in possible_study_dates
            if study_date in actual_study_dates
        ]
    )
    valid_study_dates.sort()

    # Save to REVIEW_STUDY_FILE.
    review_study_dict = {review_date.strftime(constants.DATE_FORMAT): valid_study_dates}
    review_study_file = toolbox.locate_vault() / constants.REVIEW_STUDY_FILE
    storage.append_json(review_study_dict, review_study_file)

    return valid_study_dates
