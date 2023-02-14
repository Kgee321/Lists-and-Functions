""" Creating a program where you can bid on an item """


# An error checker functions so the right input is entered
def error_checker(message):

    # Loop repeats when wrong input entered
    while True:
        try:

            # Asking user the intended message
            output = int(input(message))
            break

        # If an error occurs like a string or float entered
        except ValueError:
            print("\n Wrong input! Please enter an integer \n")

    # returning the number entered
    return output


# Function to commence the bidding
def bidding():

    # Creating the highest and bid variable
    highest = 0
    bid = 0

    # While loop to stop code when negative number entered
    while bid >= 0:

        # Printing the highest bid
        print(f"Highest bid so far is ${highest}")

        # Asking user for a bid
        bid = error_checker("What is your bid? ")

        #
        if bid > highest:
            highest = bid
        else:
            print("Please enter a higher bid\n")

    # returning highest bid
    return highest


# Main code
print("~~ SILENT AUCTION WARS ~~")

# Asking for bidding item
item = input("\nEnter the bidding item: ").lower()

# Asking for reserve price
reserve_price = error_checker("\nEnter the reserve price of this item: $")

# Telling user action has started
print(f"\nThe auction for the {item} has started!\n")

# Calling bidding function
highest_bid = bidding()

# Outputting auction item and price
if highest_bid >= reserve_price:
    print(f"The auction for the {item} finished with a bid of ${highest_bid}")

# Outputting that item didn't sell
else:
    print(f"Sorry, {item} did not sell")
