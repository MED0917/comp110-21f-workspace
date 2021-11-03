"""Drawing forests in a loop."""

__author__ = "730382017"

<<<<<<< HEAD
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
        
=======
# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

i: int = 0
duplicate: bool = False
while (i < depth):
    j: int = 0
    tree: str = ""
    while(j < i + 1):
        tree += TREE
        j += 1
    print(tree)
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
