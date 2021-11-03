"""Fortune Cookie EX02."""

<<<<<<< HEAD
__author__ = "730382017"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

from random import randint
random = randint(1, 4)

print("Your fortune cookie says...")

<<<<<<< HEAD
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
=======
# Begin your solution here...

rand_int: int = randint(0, 3)
print("Your fortune cookie says...")
if (rand_int == 0):
    print("you will get married")
elif (rand_int == 1):
    print("you should take a nap")
elif (rand_int == 2):
    print("you need therapy")
else:
    print("you will meet a new friend tommorow")
print("Now, go spread positive vibes!")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
