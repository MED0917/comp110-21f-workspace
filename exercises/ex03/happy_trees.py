"""Drawing forests in a loop."""

__author__ = "730382017"

TREE: str = '\U0001F332'

depth = int(input("Depth:  "))

if depth <= 0:
    print()
else:
    while depth >= 1:
        print(TREE * depth)
        depth = depth - 1

      