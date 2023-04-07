import time

def clear_screen():
    print("\033[2J", end="", flush=True)

def wait(seconds):
    time.sleep(seconds)

def slow_print(string):
    for char in string:
        print(char, end="", flush=True)
        wait(0.08)
    print()

# Backspace for TI 84
def backspace(lines):
    for i in range(lines):
        print("\b \b", end="", flush=True)

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
            backspace(1)
            print("Invalid Input")
            wait(0.6)
            backspace(1)
    return x

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
    slow_print(" Your Name:")
    name = input(" > ")
    backspace(2)
    slow_print(" Hello, " + name + "!")
    wait(0.5)
    backspace(1)
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
    backspace(5)
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
    backspace(7)
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
    backspace(7)
    return eye_color

#start()
#player_name = name()
#player_gender = gender()
#player_hair_color = hair_color()
#player_eye_color = eye_color()

def confirmation_menu(info):
    fast_print(" Is the following information \n correct?")
    fast_print(" Name: " + info[0])
    fast_print(" Gender: " + info[1])
    fast_print(" Hair Color: " + info[2])
    fast_print(" Eye Color: " + info[3])
    fast_print(" 1. Yes")
    fast_print(" 2. No")
    choice = menu(2)
    if (choice == 1):
        backspace(9)
        return info
    elif (choice == 2):
        backspace(9)
        fast_print(" Select what to change:")
        fast_print(" 1. Name\t\t")
        fast_print(" 2. Gender\t\t")
        fast_print(" 3. Hair Color\t")
        fast_print(" 4. Eye Color\t")
        fast_print(" 5. Exit\t\t")
        edit = 0
        while (edit != 5):
            edit = menu(5)
            if (edit == 1):
                clear_screen()
                info[0] = name()
                confirmation_menu(info)
            elif (edit == 2):
                clear_screen()
                info[1] = gender()
                confirmation_menu(info)
            elif (edit == 3):
                clear_screen()
                info[2] = hair_color()
                confirmation_menu(info)
            elif (edit == 4):
                clear_screen()
                info[3] = eye_color()
                confirmation_menu(info)
            elif (edit == 5):
                break
        clear_screen()
        return info
    
#player_info = [player_name, player_gender, player_hair_color, player_eye_color]
#player_info = confirmation_menu(player_info)

player_info = ["Spencer", "Male", "Black", "Brown"]

# Special traits for certain names
#if (player_info[0] == "Spencer"):



# THE GAME

#----print("------------------------------")------------------------------")
fast_print(" Welcome to Life Simulator,\n " + player_info[0] + "!")
wait(0.9)
backspace(2)
fast_print(" The best fucking text based\n game you'll ever play.")
wait(0.9)
backspace(2)
fast_print(" You're probably wondering\n what the fuck this game even\n is.")
wait(0.9)
backspace(2)
fast_print(" Well... It's so fucking slay\n that you won't even know what\n to do with yourself.")
wait(0.9)
backspace(3)
fast_print(" Anyways. Let's begin")
wait(0.5)
backspace(1)
blink_print(" HAHAHAHAHAHAHAHAHAHAHAHAHA")
wait(0.5)
backspace(1)
clear_screen()

fast_print(" Day One")
fast_print(" The fucking bitchass\n government is making you\n go to school.")
wait(1)
fast_print(" You're going to Poly. Deal\n with it")
wait(0.7)
backspace(6)

fast_print(" 8:45 AM : Poly High School")
fast_print(" Freshman Orientation")
wait(0.7)
backspace(2)
