"""Exercise 05."""

__author__ = "730382017"


def main() -> None:
    """Runs all functions."""
    first_list: list[int] = [1, 2, 4, 4, 5]
    print(only_evens(first_list))
    print(sub(first_list, 1, 3))
    print(concat([1, 2, 3], [4, 5, 6]))


def only_evens(numbers: list[int]) -> list[int]:
    """Returns only the even numbers in a list."""
    give_even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            give_even_numbers.append(number)
    return give_even_numbers
    

def sub(a: list[int], start: int, end: int) -> list[int]:
    """Returns subset of given list between start and end index."""
    i: int = 0
    output_list: list[int] = []
    if start > end:
        return []
    if start < 0:
        start = 0
    if end > len(a):
        end = len(a) - 1
    while i < len(a):
        if i >= start and i < end:
            output_list.append(a[i])
        i += 1
    return output_list   

    
def concat(a: list[int], b: list[int]) -> list[int]:
    """Returns elements of both a and b as one list."""
    concat_list: list[int] = []
    i: int = 0
    for i in a:
        concat_list.append(i)
    for i in b:
        concat_list.append(i)
    return concat_list
   
   
if __name__ == "__main__":
    main()