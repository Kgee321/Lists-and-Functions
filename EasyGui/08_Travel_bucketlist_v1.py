""" """

import easygui

while True:

    places = easygui.enterbox("Enter 5 places: \n(Use comma to separate)", "Places").split(",")

    number = len(places)

    if number > 5 or number < 5:
        easygui.msgbox(f"Please enter 5 places! You have entered {number}. \n"
                       f"Remember to Separate with a comma! ", "Error")

    else:
        for i in places:
            output = f"\n*".join(places)

        easygui.msgbox(f"Your Bucket list: \n\n"
                       f"*{output}", "Travel bucket list")
        break





