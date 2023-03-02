""" Working out the ratio of teacher and student """

import easygui
yes_no = "Yes"

while yes_no == "Yes":
    school = easygui.enterbox("Enter the name of the school")
    per_class = easygui.integerbox(f"Total number of {school} children allowed per class: \n "
                                   f"Enter a number between 10 and 30", "Children per class", upperbound=30, lowerbound=10)
    total = easygui.integerbox(f"Total number of {school} students: \n"
                               "Enter a number between 10 and 1400", "Children Total", upperbound=1400, lowerbound=10)

    amount_of_classes = total // per_class

    teachers = easygui.integerbox("Number of teachers available \n"
                                  "Must be a number between 1 and 120", "Teachers Available", upperbound=120, lowerbound=1)

    if teachers == amount_of_classes:
        easygui.msgbox(f"There are the exact amount of teachers of the school! ({teachers} teachers) ",
                       "Exact right amount of teachers")
    elif teachers > amount_of_classes:
        easygui.msgbox("More teachers then needed for each class! Yay! You have enough staff! "
                       f"You have {teachers - amount_of_classes} extra teachers", "To many Teachers")
    else:
        easygui.msgbox("You don't have enough teacher for each class! Get more staff! "
                       f"You need {amount_of_classes - teachers} more teachers", "Not enough Teachers")

    yes_no = easygui.buttonbox("Do you want to perform another calculation? ", "Repeat or end", choices=["Yes", "No"])

easygui.msgbox("Goodbye!", "End Screen")

