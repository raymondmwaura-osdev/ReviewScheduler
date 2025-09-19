"""
This module generates and organizes review data for study dates.

It retrieves study dates scheduled for a given review date, groups 
them by priority levels, and produces a Markdown file summarizing 
the results. The priorities are based on fixed intervals after the 
study date (2, 6, 13, 29, 59, and 119 days).
"""

from utilities import (
    constants,
    markdown,
    scheduler,
    storage,
    toolbox
)
import datetime, pathlib

VAULT_PARENT = toolbox.locate_vault()

def get_reviews(review_date: str) -> None:
    """
    Generate a Markdown file of study dates to review on the given date.

    The function checks for study dates scheduled on the given 
    review date, generates them if they do not exist, and writes 
    a Markdown file grouping the dates by priority.

    Parameters
    ----------
    review_date : str
        The review date, either the string "today" or a date in the 
        format "YYYY-MM-DD".

    Side Effects
    ------------
    Creates a file named "reviews.md" in the current working 
    directory containing the formatted output.
    """

    review_date = (
        datetime.datetime.now().date() if review_date == "today"
        else toolbox.parse_date(review_date)
    )

    # Get study dates to review.
    review_study_file = VAULT_PARENT / constants.REVIEW_STUDY_FILE
    study_dates = storage.get_item(review_date, review_study_file)
    if not study_dates:
        study_dates = generate_and_save_reviews(review_date)

    # Generate and save markdown output.
    output = generate_markdown_output(review_date, study_dates)
    output_file = pathlib.Path.cwd() / "reviews.md"
    output_file.write_text(output)
    
def generate_and_save_reviews(review_date: datetime.date) -> list[str]:
    """
    Generate study dates for a review date and save them.

    This function determines which study dates map to the given 
    review date, saves the mapping to the review storage file, and 
    returns the list of valid study dates.

    Parameters
    ----------
    review_date : datetime.date
        The review date.

    Returns
    -------
    list[str]
        A list of valid study dates in string format ("YYYY-MM-DD").
    """
    # Generate.
    study_review_file = VAULT_PARENT / constants.STUDY_REVIEW_FILE
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
    valid_study_dates.sort(reverse=True)

    # Save to REVIEW_STUDY_FILE.
    review_study_dict = {review_date.strftime(constants.DATE_FORMAT): valid_study_dates}
    review_study_file = VAULT_PARENT / constants.REVIEW_STUDY_FILE
    storage.append_json(review_study_dict, review_study_file)

    return valid_study_dates

def generate_markdown_output(review_date: datetime.date, study_dates: list[str]):
    """
    Build Markdown output grouping reviews by priority.

    The output includes headings, notes, and lists of study dates, 
    grouped into three categories: top, middle, and least priority 
    reviews.

    Parameters
    ----------
    review_date : datetime.date
        The date when the review is scheduled.
    study_dates : list[str]
        The study dates that map to the review date.

    Returns
    -------
    str
        A formatted Markdown string ready to be written to a file.
    """
    priority_list = group_by_priority(review_date, study_dates)
    output_skeleton = {
        "Top Priority Reviews": {
            "note": "Reviews scheduled for 2 and 6 days after learning.",
            "dates": priority_list[0],
        },
        "Middle Priority Reviews": {
            "note": "Reviews scheduled for 13 and 29 days after learning.",
            "dates": priority_list[1],
        },
        "Least Priority Reviews": {
            "note": "Reviews scheduled for 59 and 119 days after learning.",
            "dates": priority_list[2],
        }
    }

    output_list = []

    # "# <Review Date>"
    main_heading = markdown.heading(
        review_date.strftime(constants.DATE_FORMAT),
        level=1
    )
    output_list.append(main_heading)

    for title, content in output_skeleton.items():
        # "## <Level> Priority Reviews"
        title = f"\n{markdown.heading(title, level=2)}\n"
        output_list.append(title)

        # "Review scheduled for <interval1> and <interval2> days after learning."
        note = markdown.italic(content["note"]) + ("\n" * 2)
        output_list.append(note)

        # Dates or "None".
        dates_list = content["dates"]
        if len(dates_list) == 0:
            none_string = markdown.bold("None") + "\n"
            output_list.append(none_string)

        else:
            output_list.extend(
                markdown.list_item(date) for date in dates_list
            )

        # Separator.
        output_list.append("\n---\n")

    output_string = "".join(output_list)
    return output_string

def group_by_priority(review_date: datetime.date, study_dates: list[str]) -> list[tuple[str]]:
    """
    Group study dates into priority levels based on time since learning.

    The priority levels are defined as follows:
        - Top Priority: 2 or 6 days after learning
        - Middle Priority: 13 or 29 days after learning
        - Least Priority: 59 or 119 days after learning

    Parameters
    ----------
    review_date : datetime.date
        The review date.
    study_dates : list[str]
        Study dates in "YYYY-MM-DD" format.

    Returns
    -------
    list[list[str]]
        A list of three lists containing study dates grouped into 
        top, middle, and least priority reviews.
    """
    priority_list = [[] for _ in range(3)]

    # Lambda Function: Append date string to the list in the given index in `priority_list`.
    append_date = lambda index: priority_list[index].append(
            study_date.strftime(constants.DATE_FORMAT)
        )

    for study_date in study_dates:
        study_date = datetime.datetime.strptime(study_date, constants.DATE_FORMAT).date()
        delta = (review_date - study_date).days

        if delta in (2, 6): append_date(0)
        elif delta in (13, 29): append_date(1)
        elif delta in (59, 119): append_date(2)

    return priority_list
