"""Unit tests for dictionary functions."""

__author__ = "730302017"


from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests invert function."""
    assert invert({}) == {}


def test_invert_one_item() -> None:
    """Tests invert function."""
    assert invert({"Marr": "AMST102"}) == {"AMST102": "Marr"}


def test_invert_multiple_items() -> None:
    """Tests invert function."""
    assert invert({"Marr": "AMST102", "Jordan": "COMP110"}) == {"AMST102": "Marr", "COMP110": "Jordan"}


def test_favorite_color_empty() -> None:
    """Tests invert function."""
    assert favorite_color({}) == ""


def test_favorite_color_one_item() -> None:
    """Tests invert function."""
    assert favorite_color({"Morgan": "Pink"}) == "Pink"


def test_favorite_color_multiple_items() -> None:
    """Tests invert function."""
    assert favorite_color({"Morgan": "Pink", "Jess": "Purple", "Beth": "Pink"}) == "Pink"


def test_count_empty() -> None:
    """Tests count function."""
    assert count([]) == {}


def test_count_one_item() -> None:
    """Tests count function."""
    assert count(["1"]) == {"1": 1}


def test_count_multiple_items() -> None:
    """Tests count function."""
    assert count(["1", "3", "5"]) == {"1": 1, "3": 1, "5": 1}
  
  
