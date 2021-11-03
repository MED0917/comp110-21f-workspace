"""Example of functions imported elsewhere."""


THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


if __name__ is "__main__":
    # Python idiom: typically you could call main here
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program")
else:
    # Typically not common to do anything in
    print("Evaluated as an imported module")