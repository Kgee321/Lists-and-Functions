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
    results = easygui.msgbox(f"You choose {weapon} and the computer choose {computer}")

