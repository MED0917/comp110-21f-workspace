"""Counting letters in a string."""

__author__ = "730382017"

char: str = input("What letter do you want to search for?: ")
string: str = input("Enter a word: ")

i: int = 0
counter: int = 0

while (i < len(string)):
    if (string[i] == char):
        counter = counter + 1

    i += 1

print("Count:", counter)