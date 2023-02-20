""" Codes purpose is to record data about people absent in a work place
Katelyn Gee
16/02/2023 """


# Error checking number of days absent
def error_checker(message):

    while True:
        try:
            number = int(input(message))
            return number

        except ValueError:
            print("Please enter an integer for absents days.\n")


def average_absences():

    # starting variable
    total_values = 0

    # Calculating average days absent
    for value in everyone.values():
        total_values += value

    # Finding average of absent days
    average = total_values/len(everyone)
    return average


# Setting variables
total_days = 0
average_absent = 0  # Probs get rid of later
highest = 0
no_absense = []
above_average = []

# Variables being used
everyone = {}
not_absent = []


# Input so user enters name then days absent
while True:

    # Asking for username
    name = input("Name: ").title()

    # When $ inputted, code ends
    if name == "$":
        break

    # Asking for user absent days
    absent = error_checker("Absent days: ")

    # Adding to people and absences to dictionary
    everyone[name] = absent
    print(everyone)

    # Adding people who are not absent to a list
    if absent == 0:
        not_absent.append(name)

    # Finding person with most days absent
    if absent > highest:
        highest = absent
        high_person = name

# Finding average of absences
average_of_absents = average_absences()

# Sorting people who are not absent
sorted_not_absent = sorted(not_absent)
