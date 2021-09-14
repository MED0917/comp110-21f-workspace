"""Repeating a beat in a loop."""

__author__ = "730382017"

beat = str(input("What beat do you want to repeat? "))
counter = int(input("How many times do you want to repeat it? "))

if counter <= 0:
    print("No beat...")
else: 
    full_beat: str = beat
    while counter > 1:
        full_beat = full_beat + " " + beat

        counter = counter - 1
    print(full_beat)