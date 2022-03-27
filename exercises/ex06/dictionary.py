"""Dictionary Functions."""

__author__ = "730490913"


def invert(iv_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values."""
    result: dict[str, str] = dict()
    for key in iv_dict:
        if iv_dict[key] in result:
            raise KeyError("error message of your choice here!")
        result[iv_dict[key]] = key
    return result


def favorite_color(color: dict[str, str]) -> str:
    """Return color that appear most frequently."""
    empty: dict[str, int] = {}
    max: int = 0
    result: str = ""
    for key in color:
        if color[key] in empty:
            empty[color[key]] += 1
        else:
            empty[color[key]] = 1
    for item in empty:
        if empty[item] > max:
            max = empty[item]
            result = item
    return result


def count(orig_dict: list[str]) -> dict[str, int]:
    """Count the number of times that value appeared in the input list."""
    empty: dict[str, int] = {}
    for item in orig_dict:
        if item in empty:
            empty[item] += 1
        else:
            empty[item] = 1
    return empty