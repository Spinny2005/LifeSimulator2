import time
import random
from day_one import day_one
from functions import *

import keyboard
# from ti_system import wait_key

# UTILITY FUNCTIONS

clear_screen()

# Display the title screen
start()

# Get the character's name
player_name = name()

# Get the character's gender
player_gender = gender()

# Get the character's hair color
player_hair_color = hair_color()

# Get the character's eye color
player_eye_color = eye_color()

# Combine the variables into a list
player_info = [get_name(), get_gender(), get_hair_color(), get_eye_color()]

first_name = player_info[0].split(" ")[0].lower()

# Special traits for certain names
if (first_name == "spencer"):
    pass
if (first_name == "sydney"):
    pass
if (first_name == "rohan"):
    update_nerdyness(90)
if (first_name == "lauren"):
    pass
if (first_name == "christian"):
    pass
if (first_name == "jason"):
    pass
if (first_name == "theo"):
    pass

fast_print(" Here are your base stats:")
fast_print(" Nerdyness: " + str(get_nerdyness()))
fast_print(" Strength: " + str(get_strength()))
fast_print(" Happiness: " + str(get_happiness()))
fast_print(
    " \n As you progress through the\n game, you will be able to\n increase these stats.")
fast_print(" \n Press [ENTER] to continue")
input()
clear_screen()

fast_print(" Welcome to Life Simulator,\n " + player_info[0] + "!")
wait(0.9)
clear_screen()
fast_print(" The best fucking text based\n game you'll ever play.")
wait(0.9)
clear_screen()
fast_print(" You're probably wondering\n what the fuck this game even\n is.")
wait(0.9)
clear_screen()
fast_print(
    " Well... It's so fucking slay\n that you won't even know what\n to do with yourself.")
wait(0.9)
clear_screen()
fast_print(" Anyways. Let's begin")
wait(0.5)
clear_screen()
blink_print(" HAHAHAHAHAHAHAHAHAHAHAHAHA")
wait(0.5)
clear_screen()

# DAY ONE
day_one()

fast_print(" You survived Day One!")
wait(0.5)
fast_print(" Here are your current stats:")
fast_print(" Nerdyness: " + str(get_nerdyness()))
fast_print(" Strength: " + str(get_strength()))
fast_print(" Happiness: " + str(get_happiness()))
fast_print(" Health: " + str(get_health()))

# DAY TWO
