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
    vault_parent_directory = toolbox.locate_vault()

    # Get study dates to review.
    review_study_file = vault_parent_directory / constants.REVIEW_STUDY_FILE
    study_dates = storage.get_item(review_date, review_study_file)
    if not study_dates: study_dates = generate_and_save_reviews(review_date)

    # Generate and save markdown output.
    output = generate_markdown_output(review_date, study_dates)
    output_file = vault_parent_directory / "output.md"
    output_file.write_text(output)
    
def generate_and_save_reviews(review_date: datetime.date) -> list[str]:
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
    valid_study_dates.sort(reverse=True)

    # Save to REVIEW_STUDY_FILE.
    review_study_dict = {review_date.strftime(constants.DATE_FORMAT): valid_study_dates}
    review_study_file = toolbox.locate_vault() / constants.REVIEW_STUDY_FILE
    storage.append_json(review_study_dict, review_study_file)

    return valid_study_dates

def generate_markdown_output(review_date: datetime.date, study_dates: list[str]):
    """
    Generate and return markdown output that groups reviews by priority.
    
    :param review_date: The date when the review is taking place.
    :param study_dates: A list of study dates to review.
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
    Group the dates in the given list (study_dates) into 3:
        
        Top Priority: Reviews for 2 and 6 days after learning.
        Mid Priority: Reviews for 13 and 29 days after learning.
        Least Priority: Reviews for 59 and 119 days after learning.

    :param review_date: A `datetime.date` object representing the review date.
    :param study_dates: A list of date strings in the format "YYYY-MM-DD".
    :return: A 2 dimensional list: [[top priority reviews], [mid priority reviews], [least priority reviews]].
    """
    priority_list = [[] for _ in range(3)]

    # Lambda Function: Append date string to the list in the given index in `priority_list`.
    append_date = lambda index: priority_list[index].append(study_date.strftime(constants.DATE_FORMAT))

    for study_date in study_dates:
        study_date = datetime.datetime.strptime(study_date, constants.DATE_FORMAT).date()
        delta = (review_date - study_date).days

        if delta in (2, 6): append_date(0)
        elif delta in (13, 29): append_date(1)
        elif delta in (59, 119): append_date(2)

    return priority_list

