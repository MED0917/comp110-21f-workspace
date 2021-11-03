"""Counting letters in a string."""

<<<<<<< HEAD
__author__ = "730382017"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

char: str = input("What letter do you want to search for?: ")
string: str = input("Enter a word: ")

<<<<<<< HEAD
i: int = 0
counter: int = 0

while (i < len(string)):
    if (string[i] == char):
        counter = counter + 1

    i += 1

print("Count:", counter)
=======
# Begin your solution here...

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
print("Count: " + str(count))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
