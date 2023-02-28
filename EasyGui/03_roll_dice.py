""" Rolling Dice -- To players"""

import easygui
import random


def rolling(number):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice = [die1, die2]
    easygui.msgbox(f"Player {number} you rolled:\n\n"
                   f"{die1} and {die2}\n\n"
                   f"With a total of {sum(dice)}")
    return dice


# Setting varaibles
player = 0

# Loop for 2 rolls from 2 players
for i in range(2):

    # Giving player the value of the player
    player += 1

    player_one_rolling = easygui.buttonbox(f"Player {player}, do you want to roll? ", f"Player {player} Rolling",
                                           choices=["Yes, Lets Roll!", "No"])

    if player_one_rolling == "Yes, Lets Roll!":
        dice_roll = rolling(player)
