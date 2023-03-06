""" If user has more than 3 tech free days, congratulate him
If user has less than 3 tech free days, it is bad"""

import easygui

GOAL = 3

tech_days = easygui.enterbox("Enter the tech days you had: ", "Days tech was used").split(" ")

num = len(tech_days)

days_tech_free = 7 - num

if days_tech_free >= GOAL:
    easygui.msgbox(f"Congrats! You had 3 tech free days! You meet your goal with {days_tech_free} tech "
                   f"free days", "Goal achieved")
else:
    easygui.msgbox(f"Oh no! You had {days_tech_free} tech free days. This is {GOAL - days_tech_free} day"
                   f" more than should have", "Goal not achieved")
