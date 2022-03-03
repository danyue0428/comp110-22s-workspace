"""Test for function skeletons. Unit testing."""

__author__ = "730490913"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Testing one edge case."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None:
    """Testing use case."""
    xs: list[int] = [6, 7, 10]
    assert only_evens(xs) == [6, 10]


def test_only_evens_items() -> None:
    """Testing use case."""
    xs: list[int] = [0, 1, 2, 2, 3, 5, 8]
    assert only_evens(xs) == [0, 2, 2, 8]


def test_sub_empty() -> None:
    """Testing edge case."""
    xs: list[int] = []
    start: int = 3
    end: int = 5
    assert sub(xs, start, end) == []


def test_sub_short_item() -> None:
    """Testing use case."""
    xs: list[int] = [10, 20]
    start: int = 0
    end: int = 4
    assert sub(xs, start, end) == [10, 20]


def test_sub_many_items() -> None:
    """Testing use case."""
    xs: list[int] = [10, 20, 30, 40, 50]
    start: int = 1
    end: int = 5
    assert sub(xs, start, end) == [20, 30, 40, 50]


def test_concat_empty() -> None:
    """Testing edge case."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_single_item() -> None:
    """Testing use case."""
    a: list[int] = [4]
    b: list[int] = [9]
    assert concat(a, b) == [4, 9]


def test_concat_many_item() -> None:
    """Testing use case."""
    a: list[int] = [4, 9, 10, 15]
    b: list[int] = [9, 100, 49]
    assert concat(a, b) == [4, 9, 10, 15, 9, 100, 49]

