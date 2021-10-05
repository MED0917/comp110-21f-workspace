"""Unit tests for list utility functions."""

from exercises.ex05.utils import concat, only_evens, sub

__author__ = "730382017"


def test_only_evens_empty() -> None:
    """Tests evens."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None:
    """Tests evens."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_multiple_items() -> None:
    """Test evens."""
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_sub_empty() -> None:
    """Tests sub function."""
    xs: list[int] = []
    assert sub(xs, 1, 3) == []


def test_sub_multiple_items() -> None:
    """Tests sub function."""
    xs: list[int] = [2, 4, 6]
    assert sub(xs, -1, 2) == [2, 4]


def test_sub_single_item() -> None:
    """Tests sub function."""
    xs: list[int] = [2]
    assert sub(xs, 0, 1) == [2]
    

def test_concat_empty() -> None:
    """Tests concat function."""
    assert concat([], []) == []


def test_concat_single_item() -> None:
    """Tests concat function."""
    assert concat([1], [2]) == [1, 2]


def test_concat_multiple_items() -> None:
    """Tests concat function."""
    assert concat([5, 4, 3], [2, 1, 0]) == [5, 4, 3, 2, 1, 0]