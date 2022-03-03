"""Test for dctionary."""

__author__ = "730490913"


from dictionary import invert, favorite_color, count
import pytest


def test_invert_abc() -> None:
    """Testing abc."""
    xs: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_single() -> None:
    """Testing single variable."""
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def test_invert_keyerror() -> None:
    """Testing for the repetitive value.""" 
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)
 

def test_favorite_color_single() -> None:
    """Testing for the repetitive value."""
    xs: dict[str, str] = {"Marc": "yellow"}
    assert favorite_color(xs) == "yellow"


def test_favorite_color_color() -> None:
    """Testing for several values."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_several() -> None:
    """Testing for several values."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "yellow", "Nancy": "yellow"}
    assert favorite_color(xs) == "yellow"


def test_count_single() -> None:
    """Testing for single list."""
    xs: list[str] = ["a"]
    assert count(xs) == {"a": 1}


def test_count_several() -> None:
    """Testing for several lists."""
    xs: list[str] = ["a", "b", "a"]
    assert count(xs) == {"a": 2, "b": 1}


def test_count_words() -> None:
    """Testing for several lists."""
    xs: list[str] = ["Nancy", "Nancy", "Bob", "Bob", "June"]
    assert count(xs) == {"Nancy": 2, "Bob": 2, "June": 1}
