"""Test for function skeletons. Unit testing."""

__author__ = "730490913"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None:
    xs: list[int] = [6]
    assert only_evens(xs) == [6]


def test_only_evens_items() -> None:
    xs: list[int] = [0, 1, 2, 2, 3, 5, 8]
    assert only_evens(xs) == [0, 2, 2, 8]


def test_sub_