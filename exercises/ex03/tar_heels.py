"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
__author__ = "730382017"


num = int(input("Enter an int: "))


if num % 2 == 0 and num % 7 == 0:
    print("TAR HEELS")
else:
    if num % 2 == 0:
        print("TAR")
    else:
        if num % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
=======
__author__ = "730243388"


# Begin your solution here...
num: int = int(input("Enter an int: "))

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
