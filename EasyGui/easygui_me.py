"Using easy gui for the first time"

import easygui
import random

name = easygui.enterbox("Hi! What is your name? ", "Name")
age = easygui.integerbox("How old are you? ", "Age")
button = easygui.buttonbox("Do want to continue", "Game Continue", choices=["Yes", "No", "Maybe"])

if button == "No":
    easygui.msgbox("Ok, Goodbye")
elif button == "Yes":
    easygui.msgbox("Kia ora! Welcome to Easygui")

for i in range(50):
    number = random.randint(0, 5)
    print(number)

words = ["Molly", "Jireh", "Katelyn", "Libby"]
favourite = random.choice(words)
print(favourite)

word = "Katelyn_Gee"
letter = random.choice(word)
print(letter)

