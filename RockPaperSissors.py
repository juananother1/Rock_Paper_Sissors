import random as r

List = ["rock", "paper", "sissors"]

autoChoice = r.choice(List)

print("Your choice: ")

choice = (str)(input())

if choice == "rock":
    if autoChoice == "paper":
       print("You lose")
    if autoChoice == "sissors":
        print("You win")
    if autoChoice == "rock":
        print("Draw")

if choice == "paper":
    if autoChoice == "paper":
        print("Draw")
    if autoChoice == "sissors":
        print("You lose")
    if autoChoice == "rock":
        print("You win")

if choice == "sissors":
    if autoChoice == "paper":
        print("You win")
    if autoChoice == "sissors":
        print("Draw")
    if autoChoice == "rock":
        print("You lose")

else:
    print("Invalid Input")