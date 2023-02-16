""" Code will keep track of details for a taxi
 Katelyn Gee
 16/02/2023 """


def error_checker(message):

    # Loop breaks if number not in right range
    while True:
        try:

            # asking user
            num_to_check = int(input(message))
            break

        # Error message print if wrong input entered
        except ValueError:
            print("\nWrong input. Please try again and enter the right integer. \n")

    # Returning
    return num_to_check


# Welcome screen
print("~~ TAXI SERVICE ~~")

# setting variables
overall_total_cost = 0
total_time = 0
total_trips = 0

# Asking for driver name and new trip
name = input("Enter driver name: ")
trip = input("Start a new trip? ").lower()

# while loop breaks when no entered
while trip != "no":

    # Code continues if yes entered
    if trip == "yes":

        # Asking user for amount of minutes
        minutes = error_checker("How many minutes: ")

        # Adding total cost of trip
        overall_total_cost += minutes * 2 + 10
        
        # Adding time to get total time of all the trips
        total_time += minutes

        # Adding to total trips
        total_trips += 1

        # asking trip question again
        print()
        trip = input("Start a new trip? ").lower()

    else:

        # Code break if other input entered
        print("Please enter yes or no. Try again")

        # asking trip question again so loop repeats
        print()
        trip = input("Start a new trip? ").lower()


# Outputting the all the information
print()
print(f"Driver name: {name.title()}:")
print(f"Overall time total of the trips: {total_time}")
print(f"Average time of the trips: {(total_time/total_trips):.2f}")
print(f"Total day income: {overall_total_cost}")
print(f"Average trip cost: {(overall_total_cost/total_trips):.2f}")
print("Goodbye :)")




