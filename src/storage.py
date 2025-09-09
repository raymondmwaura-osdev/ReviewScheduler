
from pathlib import Path
import json

def backup_file(file: str) -> None:
    """
    If file in ["daily.json", "reviews_by_date.json"], backup to the `schedule/backup` directory.
    If file is "today.md", then backup in the `history` directory.
    """
    pass

def append_json(file: str | Path, content: dict) -> None:
    """
    Append the given dictionary to the dictionary in the given JSON file.

    :param file: JSON file to append to. Can be a string or a `pathlib.Path` object.
    :param content: A dictionary containing the information to append to the file.
    """
    if not isinstance(file, (str, Path)):
        raise ValueError("Expected `str` or `Path` for `file`.")

    file = Path(file)
    main_dict = read_json(file)
    main_dict = main_dict | content
    print(main_dict)

def read_json(file: str | Path) -> dict[str, list[str]]:
    """
    Read the given JSON file and return a Python dictionary.
    Return an empty dictionary if the given file does not exist.

    :param file: JSON file to read. Can be a string or a `pathlib.Path` object.
    """
    if not isinstance(file, (str, Path)):
        raise ValueError("Expected `str` or `Path` for `file`.")

    file = Path(file)
    try:
        return json.loads(file.read_text(encoding="utf-8"))

    except FileNotFoundError:
        print(f"WARNING: File not found: {file}. Proceeding with empty content.")
        return {}
