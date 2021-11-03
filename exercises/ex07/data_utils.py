"""Utility functions."""

__author__ = "123456789"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the file as a CSV, not a string
    csv_reader = DictReader(file_handle)
    
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done to free resources
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform table from rows to columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produces a column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for items in table:
        if number_of_rows >= len(table[items]):  
            return table  
        empty_list: list[str] = []
        i: int = 0
        while i < number_of_rows:
            empty_list.append(table[items][i])
            i += 1

        result[items] = empty_list

    return result


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]:
    """Produces a column based table with only a specific subset of original columns."""
    empty_dict: dict[str, list[str]] = {}
    for item in b:
        empty_dict[item] = a[item]

    return empty_dict


def concat(dict_one: dict[str, list[str]], dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column based tables combined."""
    empty_dict: dict[str, list[str]] = {}

    for key in dict_one:
        empty_dict[key] = dict_one[key]

    for key in dict_two:
        if key in empty_dict:
            empty_dict[key].append(key)
        else: 
            empty_dict[key] = dict_two[key]

    return empty_dict
    

def count(a: list[str]) -> dict[str, int]:
    """Returns a dict in which each key is a unqiue value in the given list and the value is the count of the number of times the valie appeared in the list."""
    empty_dict: dict[str, int] = {}
    for item in a:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1

    return empty_dict