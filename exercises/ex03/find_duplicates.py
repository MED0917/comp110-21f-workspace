"""Finding duplicate letters in a word."""

<<<<<<< HEAD
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
=======
__author__ = "123456789"

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
