"""Fortune Cookie EX02."""

__author__ = "730382017"

from random import randint
random = randint(1, 4)

print("Your fortune cookie says...")

if random == 1:
    print("You will meet the love of your life soon!")
else:
    if random == 2:
        print("You will win the lottery!")
    else:
        if random == 3:
            print("You will prosper in life!")
        else:
            if random == 4:
                print("You will make As in all your classes!")
            else:
                print() 

print("Now, go spread positive vibes!")