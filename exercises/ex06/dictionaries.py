"""Practice with dictionaries."""

__author__ = "730382017"


def main() -> None:
    """Runs all functions."""
    print(invert({
        "AMST102": "Marr", 
        "PSYC220": "Stevens", 
        "COMP110": "Jordan", 
        "PSYC242": "Griffin"}))

    print(favorite_color({
        "Morgan": "Pink",
        "Grace": "Pink",
        "Beth": "Pink"}))

    print(count(["1", "2", "3"]))


def invert(classes: dict[str, str]) -> dict[str, str]:
    """Inverts dict."""

    inverted_dict = dict((v, k) for k, v in classes.items())
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str: 
    """Returns color that appears most frequently."""
    color_dict: dict[str, int] = {}

    for key in colors:
        if colors[key] in color_dict:
            color_dict[colors[key]] += 1
        else:
            color_dict[colors[key]] = 1

    max_value: int = 0 
    winning_color: str = ""
    for key in color_dict:
        if color_dict[key] > max_value:
            max_value = color_dict[key]
            winning_color = key 
    return winning_color


def count(a: list[str]) -> dict[str, int]:
    """Returns dictionary with number keys and count values."""
    empty_dict: dict[str, int] = {}

    for num in a:
        if num in empty_dict: 
            empty_dict[num] += 1
        else:
            empty_dict[num] = 1

    return empty_dict
    

if __name__ == "__main__":
    main()