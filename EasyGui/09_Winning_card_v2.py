""" Adding onto winning_card. Code will shuffle deck."""

import random
import easygui
import random

while True:

    # Welcome
    yes_no = easygui.buttonbox("Do you want to play", "Starting", choices=["Yes", "No"])

    # Stopping game if players wants to
    if yes_no == "No":
        easygui.msgbox("Thanks for playing. Come again!", "Exit")
        break

    # Lists with card and its suit
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

    # Creating a deck of cards
    deck = []
    draw = []
    for suit in suits:
        for card in cards:
            deck.append([card, suit])

    # Randomly shuffling the deck
    random.shuffle(deck)

    # 7 random cards selected
    for item in deck[0:7]:
        draw.append(f"Card {deck.index(item) + 1}: {item[0]} of {item[1]}")

    # Joining 7 cards
    for value in draw:
        show_cards = f"\n   ".join(draw)

    # outputing cards
    easygui.msgbox(f"Your cards drawn: \n\n"
                   f" {show_cards}", "7 Cards")


