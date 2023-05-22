try:
    from lifefunc import *
except:
    from LIFEFUNC import *

# DAY ONE


def day_one():
    fast_print(" Day One")
    fast_print(
        " The fucking bitchass\n government is making you\n go to school.\n")
    wait(1.2)
    fast_print(" You're going to Poly. Deal\n with it")
    wait(0.7)
    clear_screen()

    fast_print(" 8:45 AM : Poly High School")
    fast_print(" Freshman Orientation")
    wait(0.7)
    clear_screen()

    fast_print(" The overly-enthusiastic\n seniors and juniors who\n haven't had their souls\n crushed by The College Board\n are about to annoy the\n fuck out of you...\n")
    wait(3.5)
    fast_print(" YOUR MISSON: Survive...")
    wait(1)
    clear_screen()

    fast_print(" You ready???\n")
    wait(0.7)
    if (first_name == "rohan"):
        fast_print(" Shut the fuck up Rohan\n we know o_o.\n")
        wait(1)
    fast_print(" Let's go!")
    wait(0.7)
    clear_screen()

    correct_hide_1 = random.randint(0, 2)
    fast_print(" Will you:")
    fast_print(" 1. Hide behind the trees")
    fast_print(" 2. Hide behind the crowd")
    fast_print(" 3. Hide in the hallway")
    hide_choice = menu(3)

    success_level = True
    if (hide_choice == correct_hide_1 + 1):
        fast_print(" The seniors and juniors walk\n past you without noticing.\n")
        wait(0.7)
        fast_print(" You notice them coming back\n toward you.")
        wait(0.5)
        clear_screen()
        correct_hide_2 = random.randint(0, 2)
        fast_print(" Will you:")
        if (hide_choice == 1):
            fast_print(" 1. Stay behind the trees")
            fast_print(" 2. Hide behind the crowd")
            fast_print(" 3. Hide in the hallway")
        elif (hide_choice == 2):
            fast_print(" 1. Hide behind the trees")
            fast_print(" 2. Stay behind the crowd")
            fast_print(" 3. Hide in the hallway")
        elif (hide_choice == 3):
            fast_print(" 1. Hide behind the trees")
            fast_print(" 2. Hide behind the crowd")
            fast_print(" 3. Stay in the hallway")
        hide_choice = menu(3)
        clear_screen()
        if (hide_choice == correct_hide_2 + 1):
            fast_print(" The seniors and juniors still\n do not find you.")
            wait(1)
            clear_screen()
        else:
            fast_print(
                " They catch you hiding and\n start talking to you about\n their clubs and personal\n experiences.")
            wait(1.2)
            success_level = False
    else:
        fast_print(
            " They catch you hiding and\n start talking to you about\n their clubs and personal\n experiences.")
        wait(1.2)
        success_level = False

    clear_screen()
    fast_print(" Wow. You made it. Crazy.")
    wait(1)
    clear_screen()

    if (success_level == False):
        fast_print(" Maybe if you were better you\n could have saved your ears.")
        wait(1)
        fast_print(" So now your stats are fucked")
        wait(0.7)
        clear_screen()
        fast_print(" Your Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(1)
        update_happiness(-1)
        clear_screen()
        print(" Your Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        wait(1.5)
    else:
        fast_print(" Nice job avoiding the\n hellspawn.")
        wait(1)
        fast_print(
            " You see some other kids\n getting talked to by them and\n realize how lucky you are.")
        wait(1)
        clear_screen()
        fast_print(" Updated Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(1)
        update_happiness(1)
        clear_screen()
        print(" Updated Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        wait(1.5)

    clear_screen()
    fast_print(" Anyways.")
    wait(0.2)
    fast_print(
        " The seniors and juniors are\n preparing to start the\n activities.\n")
    wait(1.2)
    clear_screen()

    fast_print(" You are told to join a group\n to be shown around the school.")
    wait(1.2)
    clear_screen()

    fast_print(" You are assigned to a group\n with a bunch of other\n freshmen.")
    wait(1.2)
    clear_screen()

    fast_print(" You are told to introduce\n yourself to the group.")
    wait(1)
    clear_screen()

    fast_print(" What do you say?")
    wait(0.7)
    clear_screen()

    fast_print(" 1. Hi, I'm " + get_name())
    fast_print(" 2. Hi, I'm " +
               get_name() + " \n I like to play video games.")
    fast_print(" 3. Hi, I'm " + get_name() + " \n I like to read.")
    fast_print(" 4. Hi, I'm " + get_name() + " \n I like to play sports.")

    intro = menu(4)

    clear_screen()
    fast_print(" You introduce yourself.")
    wait(0.7)
    fast_print(" They do not give a fuck.\n")
    wait(0.7)
    fast_print(" They start making fun of you\n for your dumbass name.\n")
    wait(1)
    fast_print(" Honestly...\n Understandable.")
    wait(1)
    clear_screen()

    if (intro == 2):
        fast_print(
            " Some of the other kids like\n video games though so at\n least you made some friends.")
        wait(1.5)
        clear_screen()
        fast_print(" Updated Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(1)
        update_happiness(1)
        clear_screen()
        print(" Updated Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        wait(1.5)
    elif (intro == 3):
        fast_print(" And they make fun of you for\n reading.")
        wait(1)
        clear_screen()
        fast_print(" Updated Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(1)
        update_nerdyness(5)
        update_happiness(-1)
        clear_screen()
        print(" Updated Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        wait(1.5)
    elif (intro == 4):
        fast_print(" They don't seem to care about\n sports.\n")
        wait(0.7)
        fast_print(" But that means your strong or\n something. Idk.\n")
        wait(1)
        fast_print(
            " So you get bonus stats!\n It makes no sense but just go\n with it.")
        wait(1.5)
        clear_screen()
        fast_print(" Updated Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(1)
        update_strength(5)
        clear_screen()
        print(" Updated Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        wait(1.5)

    clear_screen()
    fast_print(" The groups begin to lead you\n to different classes.")
    wait(0.7)
    fast_print(" Here are the classes that you\n could be visiting:")
    wait(0.7)
    fast_print(" 1. English 1-2")
    fast_print(" 2. Algebra 2")
    fast_print(" 3. Environmental Science")
    fast_print(" 4. U.S. Government\n")
    wait(1.2)
    clear_screen()
    fast_print(
        " Since other groups are also\n visiting these classes, you\n won't be able to visit all of\n them.")
    wait(1.2)
    clear_screen()

    classes = ["English 1-2", "Algebra 2",
               "Environmental Science", "U.S. Government"]

    fast_print(" The class you will be visiting\n is...\n")
    wait(0.7)
    clear_screen()

    random_class = random.randint(0, 3)
    selected_class = classes[random_class]
    for i in range(random_class + 16):
        print("")
        print("")
        print(" " + classes[i % 4], end="\r", flush=True)
        wait(0.1 + (i * 0.02))
        clear_screen()

    print("")
    print("")
    blink_print(" " + selected_class)
    wait(2)

    fast_print(" The class you will be visiting\n is " + selected_class + ".")
    wait(1)
    clear_screen()

    fast_print(" The group leads you to the\n " +
               selected_class + "\n classroom.")
    wait(0.7)
    clear_screen()

    has_phone = True

    has_teachers_book = False
    knows_website = False
    knows_email = False
    bathroom = False

    def english_class():
        fast_print(
            " You enter the English class.\n The teacher is not there yet.\n")
        fast_print(
            " Some of the other kids grab\n the books that are on display.\n")
        wait(0.7)
        fast_print(" Will you:")
        fast_print(" 1. Pick up a book to read")
        fast_print(" 2. Sit down at a desk")
        book_choice = menu(2)
        clear_screen()
        if (book_choice == 1):
            fast_print(" Which book will you take?")
            fast_print(" 1. To Kill a Mockingbird")
            fast_print(" 2. 1984")
            fast_print(" 3. The teacher's notebook")
            english_choice = menu(3)
            clear_screen()
            if (english_choice == 1) or (english_choice == 2):
                fast_print(" You take the book...\n nerd.\n")
                wait(0.4)
                clear_screen()
                fast_print(" You know what that means!")
                wait(1)
                clear_screen()
                fast_print(" Updated Stats:")
                fast_print(" Nerdyness: " + str(get_nerdyness()))
                fast_print(" Strength: " + str(get_strength()))
                fast_print(" Happiness: " + str(get_happiness()))
                wait(1)
                update_nerdyness(2)
                clear_screen()
                print(" Updated Stats:")
                print(" Nerdyness: " + str(get_nerdyness()))
                print(" Strength: " + str(get_strength()))
                print(" Happiness: " + str(get_happiness()))
                wait(1.5)
                clear_screen()
                fast_print(" You're asked to take a seat.\n")
                wait(1.2)
                clear_screen()
                book_choice = 2
            elif (english_choice == 3):
                has_teachers_book = True
                fast_print(" No one sees you take the book.\n")
                wait(0.7)
                fast_print(" You're asked to take a seat.\n")
                wait(1.2)
                clear_screen()
                book_choice = 2
        if (book_choice == 2):
            fast_print(" You sit down at a empty table\n in the back.\n")
            wait(0.7)
            fast_print(" The teacher comes in to talk\n about their class.\n")
            wait(0.7)
            fast_print(" Will you:")
            fast_print(" 1. Pay attention")
            fast_print(" 2. Go to the bathroom")
            english_choice = menu(2)
            if (english_choice == 1):
                fast_print(" Wow. You nerdy ass bitch.\n ")
                wait(1)
                clear_screen()
                fast_print(" Updated Stats:")
                fast_print(" Nerdyness: " + str(get_nerdyness()))
                fast_print(" Strength: " + str(get_strength()))
                fast_print(" Happiness: " + str(get_happiness()))
                wait(1)
                update_nerdyness(2)
                clear_screen()
                print(" Updated Stats:")
                print(" Nerdyness: " + str(get_nerdyness()))
                print(" Strength: " + str(get_strength()))
                print(" Happiness: " + str(get_happiness()))
                wait(1.5)
                clear_screen()

                fast_print(" You know this game gets\n better right?\n")
                wait(0.5)
                fast_print(" Well...")
                wait(0.5)
                fast_print(" Boring choice. Boring game...\n")
                wait(2)
                fast_print(" Just Kidding... >:)")
                wait(1)
                clear_screen()
                fast_print(
                    " You and your group leave the\n classroom after the teacher\n finishes talking")
                wait(1)
                clear_screen()
            elif (english_choice == 2):
                fast_print(" You go to the bathroom.\n")
                wait(0.5)
                bathroom = True
                return

    def algebra_class():
        fast_print(" You enter the Algebra class.\n")
        wait(0.5)
        fast_print(
            " You get yelled at by the\n teacher for having your phone\n sticking out of your pocket\n by 0.5 inches.\n")
        wait(1)
        fast_print(
            " Your phone gets taken by the\n group leader. You will get it\n back at the end of the day.")
        wait(1)
        clear_screen()
        fast_print(" Updated Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(1)
        update_happiness(-1)
        clear_screen()
        print(" Updated Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        wait(1.5)
        clear_screen()
        fast_print(" You're asked to take a seat.\n")
        wait(0.2)
        fast_print(
            " You notice the teacher and the\n group leader talking in the\n corner of the room.\n")
        wait(1)
        fast_print(" Will you:")
        fast_print(" 1. Listen to their conversation")
        fast_print(" 2. Wait patiently")
        fast_print(" 3. Go to the bathroom")
        algebra_choice = menu(3)
        if (algebra_choice == 1):
            fast_print(" You listen to their conversation.\n")
            wait(0.5)
            fast_print(" You hear them talking about\n how the school just updated\n their accounts and how the\n passwords were sent to each\n teacher through email.\n")
            wait(2)
            fast_print(
                " The teacher and group leader\n stop talking and the teacher\n begins to talk to the class.\n")
            wait(1.5)
            knows_email = True
            clear_screen()
        if (algebra_choice == 2):
            fast_print(" You wait patiently.\n")
            wait(0.5)
            fast_print(
                " The teacher and group leader\n stop talking and the teacher\n begins to talk to the class.\n")
            wait(1)
            clear_screen()
        if (algebra_choice == 3):
            fast_print(" You go to the bathroom.\n")
            wait(0.5)
            bathroom = True
            return
        fast_print(
            " The teacher tells you to grab\n a chromebook so they can\n show you how to log in.\n")
        wait(1.5)
        fast_print(
            " They show you the website\n that you will use to see your\n grades and assignments.\n")
        wait(1.5)
        clear_screen()
        fast_print(" *You remember the website*")
        wait(0.7)
        clear_screen()
        fast_print(
            " The group leader tells everyone\n that they are moving on to\n the next activity.\n")
        wait(1.5)
        clear_screen()
        knows_website = True

    def environmental_science_class():
        fast_print(" You enter the Environmental\n Science class.\n")
        wait(0.5)
        fast_print(" The teacher is not there yet.\n")
        wait(0.5)
        fast_print(
            " The group leader tells you to\n grab a chromebook so they can\n show you how to log in.\n")
        wait(1)
        clear_screen()
        fast_print(
            " They show you the website\n that you will use to see your\n grades and assignments.\n")
        wait(1)
        clear_screen()
        fast_print(" *You remember the website*")
        wait(0.7)
        clear_screen()
        knows_website = True
        fast_print(" The teacher comes in to talk\n about their class.\n")
        wait(0.5)
        fast_print(" Will you:")
        fast_print(" 1. Play games on your phone")
        fast_print(" 2. Pay attention")
        fast_print(" 3. Go to the bathroom")
        environmental_choice = menu(3)
        clear_screen()
        if (environmental_choice == 1):
            fast_print(" You pull up Cool Math Games\n and start playing.\n")
            wait(0.5)
            fast_print(
                " The teacher sees you playing\n games and takes your phone.\n")
            wait(0.5)
            fast_print(" You will get it back at the\n end of the day.\n")
            has_phone = False
            wait(1)
            clear_screen()
            fast_print(" Updated Stats:")
            fast_print(" Nerdyness: " + str(get_nerdyness()))
            fast_print(" Strength: " + str(get_strength()))
            fast_print(" Happiness: " + str(get_happiness()))
            wait(1)
            update_happiness(-1)
            update_nerdyness(-1)
            clear_screen()
            print(" Updated Stats:")
            print(" Nerdyness: " + str(get_nerdyness()))
            print(" Strength: " + str(get_strength()))
            print(" Happiness: " + str(get_happiness()))
            wait(1.5)
            clear_screen()
        elif (environmental_choice == 2):
            fast_print(" You pay attention.\n")
            wait(0.5)
            fast_print(
                " The teacher recognizes you\n for paying attention and\n gives you a piece of candy.\n")
            wait(1)
            clear_screen()
            fast_print(" Updated Stats:")
            fast_print(" Nerdyness: " + str(get_nerdyness()))
            fast_print(" Strength: " + str(get_strength()))
            fast_print(" Happiness: " + str(get_happiness()))
            wait(1)
            update_happiness(2)
            clear_screen()
            print(" Updated Stats:")
            print(" Nerdyness: " + str(get_nerdyness()))
            print(" Strength: " + str(get_strength()))
            print(" Happiness: " + str(get_happiness()))
            wait(1.5)
            clear_screen()
        elif (environmental_choice == 3):
            fast_print(" You go to the bathroom.\n")
            wait(0.5)
            bathroom = True
            return
        fast_print(
            " The group leader tells everyone\n that they are moving on to\n the next activity.\n")

    def us_government_class():
        fast_print(" You enter the U.S. Government\n class.\n")
        wait(0.5)
        fast_print(" There are already some kids\n in the class.\n")
        wait(0.5)
        fast_print(" The teacher is not there yet.\n")
        wait(0.5)
        clear_screen()
        fast_print(" Will you:")
        fast_print(" 1. Talk to the other kids")
        fast_print(" 2. Sit down at a desk")
        fast_print(" 3. Go to the bathroom")
        government_choice = menu(3)
        clear_screen()
        if (government_choice == 1):
            fast_print(" You talk to the other kids.\n")
            wait(0.5)
            fast_print(
                " They tell you about the\n teacher and how they are\n really chill.\n")
            wait(0.5)
            fast_print(" You make some friends.\n")
            wait(0.5)
            clear_screen()
            wait(1)
            clear_screen()
            fast_print(" Updated Stats:")
            fast_print(" Nerdyness: " + str(get_nerdyness()))
            fast_print(" Strength: " + str(get_strength()))
            fast_print(" Happiness: " + str(get_happiness()))
            wait(1)
            update_happiness(2)
            clear_screen()
            print(" Updated Stats:")
            print(" Nerdyness: " + str(get_nerdyness()))
            print(" Strength: " + str(get_strength()))
            print(" Happiness: " + str(get_happiness()))
            wait(1.5)
            clear_screen()
        elif (government_choice == 2):
            fast_print(" You sit down at a desk.\n")
            wait(0.5)
            fast_print(
                " You notice the teacher and\n the group leader talking in\n the corner of the room.\n")
            wait(0.5)
            fast_print(" Will you:")
            fast_print(" 1. Listen to their conversation")
            fast_print(" 2. Wait patiently")
            fast_print(" 3. Go to the bathroom")
            government_choice = menu(3)
            clear_screen()
            if (government_choice == 1):
                fast_print(" You listen to their conversation.\n")
                wait(0.5)
                fast_print(
                    " You hear them talking about\n how the school just updated\n their accounts and how the\n passwords were sent to each\n teacher through email.\n")
                wait(1.5)
                fast_print(
                    " The teacher and group leader\n stop talking and the teacher\n begins to talk to the class.\n")
                wait(1)
                knows_email = True
                clear_screen()
            if (government_choice == 2):
                fast_print(" You wait patiently.\n")
                wait(0.5)
                fast_print(
                    " The teacher and group leader\n stop talking and the teacher\n begins to talk to the class.\n")
                wait(1)
                clear_screen()
            if (government_choice == 3):
                fast_print(" You go to the bathroom.\n")
                wait(0.5)
                bathroom = True
                return
        elif (government_choice == 3):
            fast_print(" You go to the bathroom.\n")
            wait(0.5)
            bathroom = True
            return
        fast_print(" The teacher begins to talk\n about their class.\n")
        wait(0.5)
        fast_print(
            " The teacher tells you to grab\n a chromebook so they can\n show you how to log in.\n")
        wait(1)
        fast_print(
            " They show you the website\n that you will use to see your\n grades and assignments.\n")
        wait(1)
        clear_screen()
        fast_print(" *You remember the website*")
        wait(0.7)
        clear_screen()
        fast_print(
            " The group leader tells everyone\n that they are moving on to\n the next activity.\n")
        wait(1)
        clear_screen()
        knows_website = True

    fast_print(" Will you:")
    fast_print(" 1. Follow them to the class")
    fast_print(" 2. Run away and explore")
    fast_print(" 3. Jump in front of a bus")
    choice = menu(3)
    clear_screen()

    if (choice == 3):
        fast_print(" Hahahahahahaha\n")
        wait(0.5)
        fast_print(" You're so funny and edgy.\n")
        wait(0.5)
        fast_print(" You must be the funniest person\n on Earth!\n")
        wait(0.5)
        fast_print(
            " The group members see you leave\n to jump in front of the\n bus and stop you.")
        wait(1.5)
        clear_screen()
        fast_print(" Now you don't get a choice...")
        wait(0.7)
        choice = 1

    if (choice == 1):
        # Go to the selected class
        if (selected_class == "English 1-2"):
            english_class()
        elif (selected_class == "Algebra 2"):
            algebra_class()
        elif (selected_class == "Environmental Science"):
            environmental_science_class()
        else:
            us_government_class()

    elif (choice == 2):
        # Go to a different class
        fast_print(
            " You decide to explore the\n school instead of going to\n the class.\n")
        wait(1)
        fast_print(" Where do you go?")
        fast_print(" 1. English 1-2")
        fast_print(" 2. Algebra 2")
        fast_print(" 3. Environmental Science")
        fast_print(" 4. U.S. Government")
        fast_print(" 5. The bathroom")
        different_class = menu(5)
        clear_screen()
        if (different_class == 1):
            if selected_class == "English 1-2":
                fast_print(" You rejoin the group.\n")
                wait(0.5)
            else:
                fast_print(
                    " You sneak into a different\n group and head to the\n English class.\n")
                wait(1)
            english_class()
        elif (different_class == 2):
            if selected_class == "Algebra 2":
                fast_print(" You rejoin the group.\n")
                wait(0.5)
            else:
                fast_print(
                    " You sneak into a different\n group and head to the\n Algebra class.\n")
                wait(1)
            algebra_class()
        elif (different_class == 3):
            if selected_class == "Environmental Science":
                fast_print(" You rejoin the group.\n")
                wait(0.5)
            else:
                fast_print(
                    " You sneak into a different\n group and head to the\n Environmental Science class.\n")
                wait(1)
            environmental_science_class()
        elif (different_class == 4):
            if selected_class == "U.S. Government":
                fast_print(" You rejoin the group.\n")
                wait(0.5)
            else:
                fast_print(
                    " You sneak into a different\n group and head to the\n Government class.\n")
                wait(1)
            us_government_class()
        else:
            fast_print(" You go to the bathroom.\n")
            wait(0.5)
            bathroom = True

    clear_screen()
    if (bathroom == True):
        fast_print(" You enter the bathroom. The\n ")
        fast_print(" fresh scent of drugs fills the\n air.")
        wait(1)
        fast_print(" You see a group of kids\n smoking weed in the corner.\n")
        wait(1)
        fast_print(" Will you:")
        fast_print(" 1. Join them")
        fast_print(" 2. Use the bathroom")
        fast_print(" 3. Leave")
        bathroom_choice = menu(3)
        clear_screen()
        if (bathroom_choice == 1):
            fast_print(" You join the group and smoke\n some weed.\n")
            wait(0.5)
            fast_print(" You feel a little happier.\n")
            wait(0.5)
            clear_screen()
            fast_print(" Updated Stats:")
            fast_print(" Nerdyness: " + str(get_nerdyness()))
            fast_print(" Strength: " + str(get_strength()))
            fast_print(" Happiness: " + str(get_happiness()))
            wait(1)
            update_happiness(2)
            clear_screen()
            print(" Updated Stats:")
            print(" Nerdyness: " + str(get_nerdyness()))
            print(" Strength: " + str(get_strength()))
            print(" Happiness: " + str(get_happiness()))
            wait(1.5)
            clear_screen()
            fast_print(
                " But then you get caught by\n the group leader and get\n sent to the office.\n")
            wait(1)
            fast_print(" You get suspended for 3 days.\n")
            wait(0.5)
            clear_screen()
            fast_print(" Updated Stats:")
            fast_print(" Nerdyness: " + str(get_nerdyness()))
            fast_print(" Strength: " + str(get_strength()))
            fast_print(" Happiness: " + str(get_happiness()))
            wait(1)
            update_happiness(-3)
            clear_screen()
            print(" Updated Stats:")
            print(" Nerdyness: " + str(get_nerdyness()))
            print(" Strength: " + str(get_strength()))
            print(" Happiness: " + str(get_happiness()))
            wait(1.5)
            clear_screen()
            fast_print(
                " As you are leaving the office\n the ground begins to shake.")
            wait(0.5)
        elif (bathroom_choice == 2):
            fast_print(" You use the bathroom.\n")
            wait(0.5)
            fast_print(
                " You hear the group of kids\n smoking weed get caught by\n the group leader.\n")
            wait(0.5)
            fast_print(" You leave the bathroom.\n")
            wait(0.5)
            clear_screen()
            fast_print(
                " As you are leaving the bathroom\n the ground begins to shake.")
            wait(0.5)
        else:
            fast_print(" You leave the bathroom.\n")
            wait(0.5)
            fast_print(
                " You see your group leader\n go into the bathroom and\n hear them yell at the kids.\n")
            wait(0.5)
            clear_screen()
            fast_print(" You run away and aren't caught.\n")
            wait(0.5)
            fast_print(" As you are leaving the ground\n begins to shake.")
            wait(0.5)
    else:
        fast_print(
            " As you are leaving with your\n group the ground begins to\n shake.")
        wait(1)

    clear_screen()
    fast_print(" You hear a loud noise and\n see a bright light.\n")
    wait(0.5)
    fast_print(" You get knocked out.\n")
    wait(0.5)
    clear_screen()
    fast_print(
        " You wake up in a dark room.\n The walls are cracked and\n the ceiling is falling apart.\n")
    wait(1)
    fast_print(" You see a door on the other\n side of the room.\n")
    wait(0.5)
    fast_print(" It is blocked by debris on\n the other side.\n")
    wait(0.5)
    clear_screen()

    fast_print(" Will you:")
    fast_print(" 1. Try to find another way out")
    fast_print(" 2. Use your phone to call for\n help")
    fast_print(" 3. Try to break down the door")
    fast_print(" 4. Wait for someone to find you")
    escape_choice = menu(4)
    clear_screen()

    damage_taken = False
    if (escape_choice == 1):
        fast_print(" You look around the room.\n")
        wait(0.7)
        fast_print(" You see a hole in the wall.\n")
        wait(0.7)
        fast_print(" You crawl through the hole.\n")
        wait(1)
        clear_screen()
        fast_print(" You realize the wall leads to\n the bathroom.\n")
        wait(1)
        fast_print(
            " You run for the door but\n the ground begins to shake\n again.\n")
        wait(1)
        fast_print(" You slip and fall and hit\n your head on the toilet.\n")
        wait(1)
        clear_screen()
        fast_print(" You take 2 damage\n")
        wait(1)
        fast_print(" Yeah thats right... I'm\n adding damage now.\n")
        wait(1)
        clear_screen()
        fast_print(" Updated Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(0.7)
        fast_print(" Health: " + str(get_health()))
        wait(1)
        update_happiness(-3)
        update_health(-2)
        clear_screen()
        print(" Updated Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        print(" Health: " + str(get_health()))
        wait(1.5)
        fast_print(" Deal with it, bitch.\n")
        wait(0.7)
        fast_print(" Anyways...")
        wait(0.7)
        fast_print(" You're knocked out now.")
        wait(1)
        damage_taken = True
    elif (escape_choice == 2):
        if (has_phone):
            fast_print(" You call your parents for\n help.\n")
            wait(0.5)
            fast_print(" They tell you that there\n are people coming to help.")
            wait(0.5)
            fast_print(" You wait in the room for\n someone to find you.")
            wait(0.7)
            clear_screen()
            fast_print(" You fall asleep...")
            wait(0.5)
            clear_screen()
        else:
            fast_print(
                " You reach into your pocket\n for your phone but realize\n that it was taken by the\n teacher.")
            wait(1.5)
            fast_print(
                " You walk towards the door\n to see if you can see anyone\n through the window.\n")
            wait(1.5)
            fast_print(
                " Suddenly you are hit on the\n head by a lose ceiling panel.\n")
            wait(1)
            clear_screen()
            fast_print(" You take 2 damage\n")
            wait(1)
            fast_print(" Yeah thats right... I'm\n adding damage now.\n")
            wait(1)
            clear_screen()
            fast_print(" Updated Stats:")
            fast_print(" Nerdyness: " + str(get_nerdyness()))
            fast_print(" Strength: " + str(get_strength()))
            fast_print(" Happiness: " + str(get_happiness()))
            wait(0.7)
            fast_print(" Health: " + str(get_health()))
            wait(1)
            update_happiness(-3)
            update_health(-2)
            clear_screen()
            print(" Updated Stats:")
            print(" Nerdyness: " + str(get_nerdyness()))
            print(" Strength: " + str(get_strength()))
            print(" Happiness: " + str(get_happiness()))
            print(" Health: " + str(get_health()))
            wait(1.5)
            fast_print(" Deal with it, bitch.\n")
            wait(0.7)
            fast_print(" Anyways...")
            wait(0.7)
            fast_print(" You're knocked out now.")
            wait(1)
            damage_taken = True
    elif (escape_choice == 3):
        if (int(get_strength()) > 10):
            fast_print(
                " You bang on the door until\n it breaks open and you\n fall throught it.")
            wait(1)
            fast_print(
                " You get up and see a rescue\n team helping other students.")
            wait(1.2)
            fast_print(
                " They start rushing over to\n you as you pass out from\n exhaustion.")
            wait(1.2)
            clear_screen()
        else:
            fast_print(
                " You bang on the door but\n arent strong enough to\n break it open.")
            wait(1.2)
            fast_print(
                " Suddenly you are hit on the\n head by a lose ceiling panel.\n")
            wait(1)
            clear_screen()
            fast_print(" You take 2 damage\n")
            wait(1)
            fast_print(" Yeah thats right... I'm\n adding damage now.\n")
            wait(1)
            clear_screen()
            fast_print(" Updated Stats:")
            fast_print(" Nerdyness: " + str(get_nerdyness()))
            fast_print(" Strength: " + str(get_strength()))
            fast_print(" Happiness: " + str(get_happiness()))
            wait(0.7)
            fast_print(" Health: " + str(get_health()))
            wait(1)
            update_happiness(-3)
            update_health(-2)
            clear_screen()
            print(" Updated Stats:")
            print(" Nerdyness: " + str(get_nerdyness()))
            print(" Strength: " + str(get_strength()))
            print(" Happiness: " + str(get_happiness()))
            print(" Health: " + str(get_health()))
            wait(1.5)
            fast_print(" Deal with it, bitch.\n")
            wait(0.7)
            fast_print(" Anyways...")
            wait(0.7)
            fast_print(" You're knocked out now.")
            wait(1)
            damage_taken = True
    else:
        fast_print(" You wait for someone to find\n you.\n")
        wait(1)
        fast_print(" You begin to fall asleep.\n")
        wait(1)
        fast_print(" In your sleep you roll onto\n sharp debris.")
        wait(1)
        clear_screen()
        fast_print(" You take 1 damage\n")
        wait(1)
        fast_print(" Yeah thats right... I'm\n adding damage now.\n")
        wait(1)
        clear_screen()
        fast_print(" Updated Stats:")
        fast_print(" Nerdyness: " + str(get_nerdyness()))
        fast_print(" Strength: " + str(get_strength()))
        fast_print(" Happiness: " + str(get_happiness()))
        wait(0.7)
        fast_print(" Health: " + str(get_health()))
        wait(1)
        update_happiness(-3)
        update_health(-1)
        clear_screen()
        print(" Updated Stats:")
        print(" Nerdyness: " + str(get_nerdyness()))
        print(" Strength: " + str(get_strength()))
        print(" Happiness: " + str(get_happiness()))
        print(" Health: " + str(get_health()))
        wait(1.5)
        fast_print(" Deal with it, bitch.\n")
        wait(0.7)
        fast_print(" Anyways...")
        wait(0.7)
        fast_print(" You're knocked out now.")
        wait(1)
        damage_taken = True

    fast_print(
        " You dream sad miserable dreams\n as you are taken away from\n the school.")
    wait(1.2)
    clear_screen()

    return
