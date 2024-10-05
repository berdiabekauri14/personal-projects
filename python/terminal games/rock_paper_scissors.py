import random

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
choices = ["rock", "paper", "scissors"]

print(f"Welcome back {name} {last_name} to rock, paper, scissors!".title())
print("Here are the rules you will need for the game".title())
print("1. if the computer chooses rock and you choose paper, you win".title())
print("2. if the computer chooses paper and you choose rock, you lose".title())
print("3. if the computer chooses scissors and you choose rock, you win".title())
print("4. if the computer chooses rock and you choose scissors, you lose".title())
print("5. if the computer chooses scissors and you choose rock, you lose".title())
print("6. if the computer choice is the same choice as yours, it a tie".title())
print("You have 3 chances, you can try again 1 time".title())
print("Whoever reaches score 3 wins!".title())

def start(p1, p2):
    if p1 == "rock" and p2 == choices[1]:
        print("You lost!".title())
        p2
    elif p1 == "paper" and p2 == choices[0]:
        print("You won!".title())
        p2
    elif p1 == "rock" and p2 == choices[2]:
        print("You won!".title())
        p2
    elif p1 == "scissors" and p2 == choices[0]:
        print("You lost!".title())
        p2
    elif p1 == "scissors" and p2 == choices[1]:
        print("You won!".title())
        p2
    elif p1 == "paper" and p2 == choices[2]:
        print("You lost!".title())
        p2
    elif p1 == p2:
        print("It a tie!".title())
        p2
    else:
        print("That is not a choice")
        p1
        p2

def exit():
    print(f"Good bye {name} {last_name}, Have a great day!".title())
    quit

def try_again():
    try:
        accept2 = int(input("Do you want to try again? (1 - yes, 2 - no): "))
    except ValueError:
        print("Incorrect, you must enter a number not an string".title())

    if accept2 == 1:
        for i in range(3):
            start(input("Enter your choice: "), random.choice(choices))

    if accept2 == 2:
        exit()

def game():
    try:
        accept = int(input("Do you want to start the game? (1 - yes, 2 - no): "))
    except ValueError:
        print("Incorrect, you must enter a number not an string".title())

    if accept == 1:
        for i in range(3):
            start(input("Enter your choice: "), random.choice(choices))
        
        try_again()

    if accept == 2:
        exit()

game()