"""Example of Conditional If/Else Statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a good day!")
else:
    print("Sorry, that is incorrect. :(")
    if guess > SECRET:
        print("Too high!")
    else: 
        print("Too low.")
 
print("Game over.") 