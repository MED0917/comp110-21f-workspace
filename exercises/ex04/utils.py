"""List utility functions."""

__author__ = "730382017"


def main() -> None:
    """Runs all functions."""
    nums: list[int] = [1, 1, 1] 
    nums_in_list: list[int] = []
    max_list: list[int] = [10, -5, 25, 33]
    print(all(nums, 1))
    print(is_equal(nums, nums_in_list))
    print(max(max_list))


def all(a: list[int], b: int) -> bool:
    """Return True if all numbers match indicated number, return false if list is empty."""
    i: int = 0 
    if len(a) == 0:
        return False
    while i < len(a):
        if a[i] != b:
            return False
        i += 1
    return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """Return True if lists are equal, False if otherwise."""
    if len(a) and len(b) == 0:
        return True
    i: int = 0 
    while i < len(a):
        if a != b:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Return largest in list, ValueError if empty."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else: 
        i: int = 0 
        v: int = input[i]
        while i < len(input):
            if input[i] > v:
                v = input[i]
            i += 1
        return v
        

if __name__ == "__main__":
    main()
