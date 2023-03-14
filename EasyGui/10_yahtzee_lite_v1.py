""" Basic game of Yahtzee. Player has to get 3,4, or 5 of the same number to win """

# Importing functions
import easygui
import random

# setting variables
NUMBERS = ["1", "2", "3", "4", "5", "6"]

# Loop so code repeats
while True:

    # Welcome
    yes_no = easygui.buttonbox("Do you want to play", "Starting", choices=["Yes", "No"])
    count = 0

    # Stopping game if players wants to
    if yes_no == "No":
        easygui.msgbox("Thanks for playing. Come again!", "Exit")
        break

    # looping for 3 moves
    while count != 3:

        # Resetting variable
        new_numbers = []

        # Choosing random numbers
        for i in range(5):
            thing = random.choice(NUMBERS)
            new_numbers.append(thing)

        # Joining numbers
        for values in new_numbers:
            joined_num = ", ".join(new_numbers)

        # Telling user what they rolled
        choice = easygui.buttonbox(f"Round {count + 1}: \nYou Rolled: {joined_num}", "Players Roll",
                                   choices=["Roll Again", "Stick"])

        # if player choose to stick, rounds end
        if choice == "Stick":
            break

        # Adding to count
        count += 1

        # if player reached 3 rounds
        if count == 3:
            answer = easygui.buttonbox("You have finished 3 rounds. \n"
                                       "Do you want to continue with your last roll or play again?", "Rounds ended",
                                       choices=["Continue", "Play again"])

            # Repeating the game when player asks
            if answer == "Play again":
                break

    # sorting the results
    results = sorted(new_numbers)

    # new variable
    counting = 0
    double_ups = []

    # Finding double ups and adding to new list
    for thing in results:
        total = results.count(thing)
        double_ups.append(total)

    # Sorting double ups
    double_ups = sorted(double_ups)

    # Making end value of double_up list a variable
    of_a_kind = double_ups[-1]
    print(of_a_kind)

    # if 3 double ups
    if of_a_kind == 3:
        message = "3 of a kind!"

    # if 4 double ups
    elif of_a_kind == 4:
        message = "4 of a kind!"

    # if 5 double ups
    elif of_a_kind == 5:
        message = "Yahtzee"

    # if 2 or less double ups
    else:
        message = "Better luck next time"

    # printing results
    easygui.msgbox(f"{', '.join(results)}\n\n{message}", "Results")
