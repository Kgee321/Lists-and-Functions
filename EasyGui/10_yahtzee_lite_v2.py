""" Adding onto 10_yahtzee_lite_v1 so there are now 2 players """

# Importing functions
import easygui
import random

# setting variables
NUMBERS = ["1", "2", "3", "4", "5", "6"]
answer = ""


# Finding players names
def player_name(number):
    # Asking each player to input name
    name = easygui.enterbox(f"Enter your name of player {number}", "Players name")
    return name


# Each player rolling the dice
def rolling(player):
    # Player that is rolling
    easygui.msgbox(f"{player}'s turn to roll!")
    count = 0

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

    # if all 3 rounds used
    if count == 3:

        # Asking user if they want to use their last round
        answers = easygui.buttonbox("You have used all your 3 rolls. Do you wish to use your last roll?",
                                    "3 rounds used", choices=["Yes", "No"])

        # if no, user gets 0 points and bad message
        if answers == "No":
            return [0, ["0", "0", "0", "0", "0", "0"]]

    # sorting the results
    result = sorted(new_numbers)

    # new variable
    double_ups = []

    # Finding double ups and adding to new list
    for thing in result:
        total = result.count(thing)
        double_ups.append(total)

    # Sorting double ups
    double_ups = sorted(double_ups)

    # Making end value of double_up list a variable
    of_a_kind = double_ups[-1]

    return [of_a_kind, result]


# Finding player scores
def scoring(num):
    # Setting score variable
    score = 0

    # if 3 of a kind
    if num == 3:
        message = "3 of a kind!"
        score += 10

    # if 4 of a kind
    elif num == 4:
        message = "4 of a kind!"
        score += 30

    # if 5 of a kind
    elif num == 5:
        message = "Yahtzee"
        score += 50

    # if 2 or less of a kind
    else:
        message = "Better luck next time"
        score += 0

    # returning value
    return [score, message]


# outputting user results
def results(name, numbers, outcome):
    # printing results
    easygui.msgbox(f"{name}'s roll: {', '.join(numbers)}\n\n{outcome[1]}\n"
                   f"{name}'s score is {outcome[0]} points", f"{name}'s Results")


# printing winner results
def winner(name_win, win_score, lose_score, name_lose):
    # returning the winner
    return f"{name_win} is the winner with a score of {win_score} points!\n\n" \
           f"{name_lose} scored {lose_score} points"


# Main Function

# Player 1 name
one = player_name(1).title()

# Player 2 name
two = player_name(2).title()

# Loop so code repeats
while True:

    # Player 1 role
    roll_one = rolling(one)

    # Player 1 score
    score_one = scoring(roll_one[0])

    # Player 1 results
    results(one, roll_one[1], score_one)

    # Player 2 role
    roll_two = rolling(two)

    # Player 2 score
    score_two = scoring(roll_two[0])

    # Player 2 results
    results(two, roll_two[1], score_two)

    # Player two winning
    if score_two[0] > score_one[0]:
        conclusion = winner(two, score_two[0], score_one[0], one)

    # Player one winning
    elif score_one[0] > score_two[0]:
        conclusion = winner(one, score_one[0], score_two[0], two)

    # Players tied
    else:
        conclusion = f"You both tied with {score_one[0]} points"

    # playing again
    yes_no = easygui.buttonbox(f"{conclusion} \n\nDo you want to play again?", "Play again", choices=["Yes", "No"])

    # Stopping game if players wants to
    if yes_no == "No":
        easygui.msgbox("Thanks for playing. Come again!", "Exit")
        break
