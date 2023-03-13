""" Basic game of Yatzee. Player has to get 3,4, or 5 of the same number to win """

# Importing functions
import easygui, random

# setting variables
NUMBERS = ["1", "2", "3", "4", "5", "6"]
count = 0

# Loop so code repeats
while True:

    # Welcome
    yes_no = easygui.buttonbox("Do you want to play", "Starting", choices=["Yes", "No"])

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
        choice = easygui.buttonbox(f"Round {count+1}: \nYou Rolled: {joined_num}", "Players Roll",
                                   choices=["Roll Again", "Stick"])

        # if player choose to stick, rounds end
        if choice == "Stick":
            easygui.msgbox("Game will proceed with these numbers")
            break

        # if player rolls again, rounds continue
        else:
            easygui.msgbox("Playing again")

        # Adding to count
        count += 1

    # sorting the results
    results = sorted(new_numbers)

    # # Joining numbers
    # for num in results:
    #     joined_results = ", ".join(results) # Maybe make into a functions

    for i in results:
        if results[i] == results[i+1] and results[i+1] == results[i+2]:
            print("3 or more in a row")
        else:
            continue


    # printing results
    easygui.msgbox(f"{joined_results}")








