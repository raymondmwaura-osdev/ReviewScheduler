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
    write_json(main_dict, file)

    # In the future, check for keys that are present in both dictionaries (main_dict and content).

def get_item(key: str, file: str | Path) -> dict | None:
    """
    Extract and return the given key and its value from the dictionary in the given file.
    Return None if the key doesn't exist.

    :param key: A string of the key to extract.
    :param file: A string or `Path` object of the file to read.
    """
    file_dict = read_json(file)
    return file_dict.get(key, default=None)

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
        print(f"WARNING: File not found: \"{file}\". Proceeding with empty content.")
        return {}

def write_json(content: dict, file: str | Path) -> None:
    """
    Write the given dictionary to the given file.

    :param content: The dictionary to write to the JSON file.
    :param file: The JSON file to write to. Can be a string or a `Path` object.
    """
    if not isinstance(file, (str, Path)):
        raise ValueError("Expected `str` or `Path` for `file`.")

    file = Path(file)
    with file.open(mode="w", encoding="utf-8") as f:
        json.dump(content, f, sort_keys=True, indent=4)
