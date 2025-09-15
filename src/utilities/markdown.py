def emphasis(text: str, form: str = "italic") -> str:
    """
    Return an emphasized markdown string.

    :param text: Text to emphasize.
    :param form: Can be ["italic", "bold", "both"].
    :return: An emphasized string.
    """
    form = form.lower().strip()

    valid_forms = ["italic", "bold", "both"]
    if form not in valid_forms:
        raise ValueError(
            f"Invalid option for param `form`: {form}\n"
            f"Valid options: {valid_forms}"
        )

    if form == "italic": return f"*{text}*"

def heading(text: str, level: int = 2) -> str:
    """
    Return a markdown heading of the given level.

    FUTURE IDEA: Capitalize the heading. Not all the words. don't capitalize words like "and", etc.

    :param text: A string that will be returned as a heading.
    :param level: Determines how many "#"s to use. Must be in the range(1, 7).
    :return: A string of the heading.
    """
    if level > 6 or level < 1:
        raise ValueError("param `level` can only be in the range(1, 7).")

    return "#"*level + f" {text}"

def italic(text):
    return emphasis(text, form="italic")
