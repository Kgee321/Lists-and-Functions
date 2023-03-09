""" 5 places to travel to """

import easygui


# Function that prints bucket list
def bucket_list(lists):
    for i in places:
        output = f"\n*  ".join(lists)

    easygui.msgbox(f"Your Bucket list: \n\n"
                   f"*  {output}", "Travel bucket list")


# loop to repeat in input wrong
while True:

    # Asking user to enter 5 places
    places = easygui.enterbox("Enter 5 places: \n(Use comma to separate)", "Places").split(",")

    # Finding on many items in list
    number = len(places)

    # Restarting loop if more/less than 5 strings inputted
    if number > 5 or number < 5:
        easygui.msgbox(f"Please enter 5 places! You have entered {number}. \n"
                       f"Remember to Separate with a comma! ", "Error")
        continue

    # printing items in bucket list
    else:
        bucket_list(places)
        break

# new loop if wrong input entered in changes
while True:

    # Asking user to enter original value and change
    change = easygui.enterbox("Enter the name of the place you want to change and the place "
                              "you want to go: \nSeparate with a comma:", "Changes").split(",")

    # Restarting loop if wrong input
    if change[0] not in places:
        easygui.msgbox("Please make sure your first value is already in the bucket list "
                       "and separated by commas", "Wrong input")
        continue

    # Finding index of string that users wants to change
    index_of_change = places.index(change[0])

    # Replacing the old value with the new value users wants to change
    places[index_of_change] = change[1]

    # reprinting bucket list
    bucket_list(places)
    break
