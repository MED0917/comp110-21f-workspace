__author__ = "730382017"

points: int = 0
player: str
counter: int = 0
heart_face: str = '\U0001F970'


def main() -> None:
    global points
    global counter
    greet()
    print(f'Nice to meet you, {player}!')
    answer = input("Do you want to: A) Start the game, B) Say goodbye for now C) See your points (only after you have played the game though!) and a cute emoji :) : ")

    if answer == "B":
        print("Have a good day!")
    else:
        if answer == "C":
            total_game_points(points) 

    while points < 10:
        if answer == "A":
            game()
    counter + 1

    if points == 10:
        answer_again: str = input("You have finished the game. Return to the main menu to play again or choose another option? 1) Yes! 2) No, I'm bored. : ")
    if answer_again == "1":
        points = 0 
        main()
    else: 
        if answer_again == "2":
            print("See ya later!") 

        
def greet() -> None:
    global player 
    player = input(" Welcome to a game of numbers, where you'll see if you can guess a higher number than the computer can! If you do guess higher, you'll gain a point. Let's get started. What's your name? ")


def game() -> None:
    global points
    number = int(input("Choose a number between 1 and 20: "))
    from random import randint
    random_num = randint(1, 20)
    print(f'The computer guessed {random_num}')
    if number < random_num:
        print("You guessed lower than the computer. Try again to gain a point!")
        print(f'Points: {points}')
    else: 
        if number > random_num: 
            print("Good job, you guessed higher than the computer! You get a point!")
            points = points + 1
            print("Points: " + str(points))
        else: 
            if number == random_num:
                print("You and the computer guessed the same. No points gained.")


def total_game_points(a: int) -> None: 
    global player
    points = 10
    print(f'Congrats {player}! You have {points} points! That is so exciting!' + heart_face)
    
    answer_again_two: str = input("Return to main menu? 1) Yes! 2) No, I'm bored.")
    if answer_again_two == "1":
        main()
    else:
        if answer_again_two == "2":
            print(f'Goodbye, {player}!')

        
if __name__ == "__main__":
    main()