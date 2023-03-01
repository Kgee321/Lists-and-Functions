""" Classic game of paper scissors rock against computer"""

import easygui
import random

# looping code unless users wants to stop
while True:
    # Welcome screen
    want_to_play = easygui.buttonbox("Welcome to Rock Paper Scissors \n\n"
                                     "Do you want to play? ", "Welcome Screen", choices=["Yes", "No"])

    # breaks code if no
    if want_to_play == "No":
        break

    # Items
    items = ["Paper", "Scissors", "Rock"]

    # Asking user to choose paper scissors or rock
    weapon = easygui.buttonbox("Choose your weapon", "Choosing Weapon", choices=items)

    # Computer chooses paper scissor or rock
    computer = random.choice(items)

    # Showing user what they choose and computer chooses
    results = easygui.msgbox(f"You choose {weapon} and the computer choose {computer}", "Computer Choice and User Choice")

    # choosing winner
    if computer == weapon:
        easygui.msgbox("This is a draw", "Tie")
    elif computer == "Paper" and weapon == "Rock" or computer == "Rock" \
            and computer == "Scissors" or computer == "Scissors" and \
            computer == "Paper":
        easygui.msgbox("You lose", "User Loses")
    else:
        easygui.msgbox("You win!", "User Wins")

easygui.msgbox("Thanks for playing!", "Goodbye")
