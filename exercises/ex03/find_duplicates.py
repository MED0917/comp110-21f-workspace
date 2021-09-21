"""Finding duplicate letters in a word."""

__author__ = "730382017"

word = str(input("Enter a word: "))
dup: bool = False

i: int = 0

while i < len(word):
    char = word[i]
    j: int = i + 1
    while j < len(word):
        if word[j] == char:
            dup = True 
        j += 1
    i += 1
print("Found duplicate: " + str(dup))