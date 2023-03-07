""" Adding onto 06_Spelling_Convert.v1. This code should now change NZ words with ise or yse
to ize in US
Katelyn Gee
8/03/2023"""

import easygui

# Loop breaks when user quits
while True:

    # Asking user if they want to play
    yes_no = easygui.buttonbox("Do you want to play", "Starting", choices=["Yes", "No"])

    # Stopping game if players wants to
    if yes_no == "No":
        easygui.msgbox("Thanks for playing. Come again!", "Exit")
        break

    # Asking user to input NZ word -- Converting letters to a list
    word_nz = easygui.enterbox("Enter NZ word: ", "NZ word")

    # if ise in word
    if "ise" in word_nz:
        word_nz = word_nz.replace("ise", "ize")

    # if yse in word
    elif "yse" in word_nz:
        word_nz = word_nz.replace("yse", "ize")

    # if our in word
    elif "our" in word_nz:

        # Convert word to a list
        word_nz = list(word_nz)

        # Repeating loop
        for letters in word_nz:

            # Removing the u from NZ words
            if letters == "u":
                word_nz.remove("u")

        # Join letters to make word
        word_nz = "".join(word_nz)

    # if no spelling changes needed
    else:
        easygui.msgbox("No spelling changes!", "No changes")
        continue

    # Outputting final word
    easygui.msgbox(f"The word in US spelling is: {word_nz}", "US word")

