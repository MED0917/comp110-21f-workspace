"""Drawing forests in a loop."""

__author__ = "730382017"

TREE: str = '\U0001F332'

counter: int = 0
depth_var = int(input("Depth: "))

if depth_var <= 0:
    print()
else:
    entry: str = ""
    while counter <= depth_var:
        entry = TREE * counter
        print(entry)
        
        counter = counter + 1
        