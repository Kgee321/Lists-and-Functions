""


# error checker
def error_checker(message):

    while True:
        try:
            number = int(input(message))
            return number

        except ValueError:
            print("Please enter an integer for absents days.\n")


# fine Calculated
def fine(speed):

    cost = 0

    # Find fined from speed user went
    if speed >= 45:
        cost = 630
    elif speed > 40:
        cost = 510
    elif speed > 35:
        cost = 400
    elif speed > 30:
        cost = 300
    elif speed > 25:
        cost = 230
    elif speed > 20:
        cost = 170
    elif speed > 15:
        cost = 120
    elif speed > 10:
        cost = 80
    elif speed < 10:
        cost = 30
    return cost

# Loop that breaks when user says so
while True:

    # Users enters input
    name = input("Name: ").title()
    speeding = error_checker(f"{name}'s speed: ")

    # fine calc
    speeding_cost = fine()

