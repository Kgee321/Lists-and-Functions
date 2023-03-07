""" finding who got a higher card in a random choice game """

import random
import easygui

while True:

    # Welcome
    yes_no = easygui.buttonbox("Do you want to play", "Starting", choices=["Yes", "No"])

    # Stopping game if players wants to
    if yes_no == "No":
        easygui.msgbox("Thanks for playing. Come again!", "Exit")
        break

    # Lists with card and its suit
    card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

    # Computers random card and suit
    computer_card = random.choice(card)
    computer_suits = random.choice(suits)

    # Players random card and suit
    player_card = random.choice(card)
    player_suits = random.choice(suits)

    # Outputting results
    easygui.msgbox(f"The Computer got the {computer_card} of {computer_suits} while you got the {player_card} of {player_suits}",
                   "Results")

    # if computer card higher then player
    if card.index(computer_card) > card.index(player_card):
        easygui.msgbox("You lose! The Computer's Card was higher than yours", "Losing")

    # if both computer card and player card equal
    elif card.index(computer_card) == card.index(player_card):
        easygui.msgbox(f"You tied! You both had the same number card of {computer_card}", "Tie")

    # if player card higher then computer
    else:
        easygui.msgbox("You Win! Your card was higher than the computers", "Winning")



