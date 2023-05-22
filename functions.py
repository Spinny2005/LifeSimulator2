import time
import random

# import keyboard

# PUBLIC VARIABLES
nerdyness = 10
strength = 10
happiness = 10
health = 10

# CHARACTER VARIABLES
player_name = ""
player_gender = ""
player_hair_color = ""
player_eye_color = ""

first_name = ""

# GET METHODS


def get_name():
    return player_name


def get_gender():
    return player_gender


def get_hair_color():
    return player_hair_color


def get_eye_color():
    return player_eye_color


def get_nerdyness():
    return nerdyness


def get_strength():
    return strength


def get_happiness():
    return happiness


def get_health():
    return health

# SET METHODS


def update_nerdyness(add):
    global nerdyness
    nerdyness += add


def update_strength(add):
    global strength
    strength += add


def update_happiness(add):
    global happiness
    happiness += add


def update_health(add):
    global health
    health += add


# UTILITY FUNCTIONS
def clear_screen():
    print("\033[2J", end="", flush=True)


def wait(seconds):
    time.sleep(seconds)


def slow_print(string):
    for char in string:
        print(char, end="", flush=True)
        wait(0.08)
    print()


def fast_print(string):
    for char in string:
        print(char, end="", flush=True)
        wait(0.02)
    print()


def blink_print(string):
    for i in range(3):
        print(" " * len(string), end="\r", flush=True)
        wait(0.2)
        print(string, end="\r", flush=True)
        wait(0.2)
    print(" " * len(string), end="\r", flush=True)
    print(string)


def menu(max):
    x = False
    while (x == False):
        try:
            x = int(input(" > "))
            if (x > max or x < 1):
                x = False
        except:
            pass
        if (x == False):
            print("Invalid Input")
            wait(0.6)
            menu(max)
    return x

# TEXT OUTPUT FUNCTIONS


def start():
    print("------------------------------")
    fast_print("        LIFE SIMULATOR")
    fast_print("           PART TWO")
    print("------------------------------")
    fast_print("   CREATED BY SPENCER BOGGS")
    wait(0.2)
    print("")
    blink_print("    PRESS [ENTER] TO START")
    print("------------------------------")
    input()
    clear_screen()


def name():
    slow_print(" Character Creation")
    fast_print(" Your Name:")
    name = input(" > ")
    clear_screen()
    global player_name
    player_name = name
    global first_name
    first_name = player_name.split(" ")[0].lower()
    return name


def gender():
    slow_print(" Select Your Gender:")
    fast_print(" 1. Male")
    fast_print(" 2. Female")
    fast_print(" 3. Other")
    gender = menu(3)
    if (gender == 1):
        gender = "Male"
    elif (gender == 2):
        gender = "Female"
    else:
        gender = "Other"
    clear_screen()
    global player_gender
    player_gender = gender
    return gender


def hair_color():
    slow_print(" Select Your Hair Color:")
    fast_print(" 1. Blonde")
    fast_print(" 2. Brown")
    fast_print(" 3. Black")
    fast_print(" 4. Red")
    fast_print(" 5. Other")
    hair_color = menu(5)
    if (hair_color == 1):
        hair_color = "Blonde"
    elif (hair_color == 2):
        hair_color = "Brown"
    elif (hair_color == 3):
        hair_color = "Black"
    elif (hair_color == 4):
        hair_color = "Red"
    else:
        hair_color = "Other"
    clear_screen()
    global player_hair_color
    player_hair_color = hair_color
    return hair_color


def eye_color():
    slow_print(" Select Your Eye Color:")
    fast_print(" 1. Blue")
    fast_print(" 2. Brown")
    fast_print(" 3. Hazel")
    fast_print(" 4. Black")
    fast_print(" 5. Other")
    eye_color = menu(5)
    if (eye_color == 1):
        eye_color = "Blue"
    elif (eye_color == 2):
        eye_color = "Brown"
    elif (eye_color == 3):
        eye_color = "Hazel"
    elif (eye_color == 4):
        eye_color = "Black"
    else:
        eye_color = "Other"
    clear_screen()
    global player_eye_color
    player_eye_color = eye_color
    return eye_color
