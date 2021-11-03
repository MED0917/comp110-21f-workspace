"""Repeating a beat in a loop."""

<<<<<<< HEAD
__author__ = "730382017"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

beat = str(input("What beat do you want to repeat? "))
counter = int(input("How many times do you want to repeat it? "))

<<<<<<< HEAD
if counter <= 0:
    print("No beat...")
else: 
    full_beat: str = beat
    while counter > 1:
        full_beat = full_beat + " " + beat

        counter = counter - 1
    print(full_beat)
=======
# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0
if (number < 1):
    print("No beat...")
else:
    print_beat = beat
    while (i < number - 1):
        print_beat += "" + beat

    print(print_beat)
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
