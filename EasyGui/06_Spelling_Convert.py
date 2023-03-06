""" Changing NZ spelling rules to US. This means removing the u"""

import easygui

word_nz = easygui.enterbox("Enter NZ word: ", "NZ word")
word_nz = list(word_nz)
word_nz.remove("u")
us_word = "".join(word_nz)
easygui.msgbox(f"The word in US spelling is: {us_word}")


