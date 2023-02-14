""" This code will keep track of the children throughout the day
Katelyn Gee
14/02/2023 """


def main():

    # Code instructions
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()


def error_checker(num1, num2, message):

    # Setting starting number
    num_to_check = 0

    # Loop breaks if number not in right range
    while not num1 <= num_to_check <= num2:
        try:

            # asking user
            num_to_check = int(input(message))

        # Error message print if wrong input entered
        except ValueError:
            print("\nWrong input. Please try again and enter the right integer. \n")

    # Returning number user inputted
    return num_to_check


def drop_off():

    # Asking user for child name
    add = input("Enter the name of the child you want to drop off: ").title()

    # Adding child to list
    child.append(add)

    # Confirming child name has been dropped off
    print(f"\nOk, {add} has been dropped off. ")
    print()


def pick_up():

    while True:
        # Asking for child name
        removing = input("Enter the name of the child you want to pick up: ").title()

        # Checking if child in system
        if removing in child:
            child.remove(removing)
            print(f"\n{removing} has been removed." )
            break

        # Breaking loop and asking question again if child not in system
        else:
            print(f"\nSorry, {removing} is not in our system. Please make sure the "
                  f"name is spelt correctly or the right name has been entered. \n") # Maybe have a way to exit back to menu screen


def calc_cost():

    # User inputs hours to charge
    hours = error_checker(1, 100, "Enter the number of hours to charge: ")

    # Calculate the total charge for the chosen amount of hours
    total_charge = hours * 12

    # outputting total charge
    print(f"\nThe total charge of looking after the child for {hours} at "
          f"a rate of $12 an hour is {total_charge}\n")


def print_roll():

    # Outputting child on list
    for children in child:
        print(children, end=", ")
    print("\n")


# Setting variables
choice = 0
child = []

# Outputting code instructions
main()

# Code stops when 5 inputted
while choice != 5:

    # Asking using to enter a number
    choice = error_checker(1, 5, "Enter your choice (number between 1 and 5): ")
    print()

    # Running the function depending on number entered by user
    if choice == 1:
        drop_off()

    elif choice == 2:
        pick_up()

    elif choice == 3:
        calc_cost()

    elif choice == 4:
        print_roll()

    else:

        # If 5 entered, outputting goodbye and loop breaks
        print("Goodbye")



