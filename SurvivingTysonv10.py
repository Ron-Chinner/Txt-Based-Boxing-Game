import time
import random
import string


items = []
punches = ["Hook", "Jab", "Uppercut", "Straight", "Overhand",
           "Body-Hook", "Ear-bite"]
rounds = ["round", "round", "round", "round",
          "round", "round", "round", "round"]
matrix = {'1': 'Jab',
          '2': 'Uppercut',
          '3': 'Hook',
          '4': 'Straight',
          '5': 'Overhand',
          '6': 'Body-Hook',
          '7': 'Ear-Bite',
          '8': None,
          '9': None}


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry,the option :"{option}" is invalid. Try again!')


def intro_option():
    print_pause("where would you like to head next?")
    print_pause("Press, a to head to the ring")
    print_pause("Press, b to head to gear up")
    print_pause("Press, c to exit")
    choice = valid_input("Select your option: ", ['a', 'b', 'c'])
    if choice == 'a':
        referee()
    elif choice == 'b':
        gear_up(items)
    elif choice == 'c':
        exit()


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    print(message)
    time.sleep(delay)


def reset():
    rounds.clear()
    rounds.extend(("round", "round", "round", "round",
                   "round", "round", "round", "round"))
    play_game()


def play_again():
    print_pause("would you like to try again?")
    choice = valid_input("yes or no:", ['yes', 'no'])
    if choice == "yes":
        reset()
    if choice == "no":
        print_pause("Goodbye!")
        exit()


def unsuccesful_defence():
    print_pause("you have been knocked out")
    print_pause("Thank you for playing")
    print_pause("......")
    print_pause("You almost endured, you had")
    print_pause(rounds.count("round"))
    print_pause("Rounds left")
    play_again()


def succesful_defence():
    rounds.remove("round")
    print_pause("succesful defence.....")
    print_pause(rounds.count("round"))
    print_pause("rounds to go")
    punch()


def punch_matrix():
    punch_thrown = random.choice(punches)
    print_pause(punch_thrown)
    print_pause("Please select your method of defending the attack")
    prompt = (
        "1. High block\n"
        "2. Low block\n"
        "3. Duck\n"
        "4. Move Head to the side\n"
        "5. Step backwards\n"
        "6. Block the ribcage\n"
        "7. Complain to the ref\n"
        "8. Launch a swift Counterpunch!\n"
        "9. Flex to the crowd\n")
    options = matrix.keys()
    typeofblock = valid_input(prompt, options)
    if matrix[typeofblock] == punch_thrown:
        succesful_defence()
    else:
        unsuccesful_defence()


def punch():
    while "round" not in rounds:
        print_pause("Congratulations You are victorious", 3)
        play_again()
    while "round" in rounds:
        print_pause("Tyson attacks")
        print_pause("............")
        print_pause("It is a", 1)
        punch_matrix()


def gear_up(items):
    if "Safety_Gear" in items:
        print_pause("You are all dressed up already", 1)
        print_pause("Nothing we can do for you here anymore", 1)
        locker_room()
    else:
        print_pause("Let's get you dressed!", 3)
        print_pause("....")
        print_pause("Look at you! Ready to box!!!!")
        items.append("Safety_Gear")
        locker_room()


def referee():
    print_pause("HMMM, do you have all of your safety gear on young gun ?", 1)
    print_pause("Lemme have a look!", 1)
    print_pause("..........")
    if "Safety_Gear" in items:
        print_pause("You seem safe....ish, let's Box.", 3)
        insideringwelcome()
    else:
        print_pause("You will get killed out there,\n"
                    "I am sending you back to the locker", 3)
        locker_room()


def insideringwelcome():
    print_pause("Welcome to the ring", 3)
    print_pause("...........")
    punch()


def locker_room():
    print_pause("You find yourself in the dressing room.", 2)
    if "Safety_Gear" not in items:
        print_pause("An amateur such as yourself cannot enter the\n"
                    "ring without Head Gear and a Mouth Piece.", 2)
        intro_option()
    elif "Safety_Gear" in items:
        print_pause("You are already dressed up")
        print_pause("")
        insideringwelcome()


def intro():
    print_pause("Hello! Today you are a Boxer.", 2)
    print_pause("You will try to beat legendary boxer, Mike Tyson.", 2)
    print_pause("In order to win, you need to sucessfully"
                " defend against Mike's punches.", 2)
    print_pause("Mike will try to connect with 8 attacks.", 2)
    print_pause("your goal is to select the correct defence", 2)
    locker_room()


def play_game():

    while "Safety_Gear" not in items:
        intro()
    if "Safety_Gear" in items:
        print_pause("Skip the intro, straight to the ring for you")
        rounds.clear()
        rounds.extend(("round", "round", "round", "round",
                       "round", "round", "round", "round"))
        insideringwelcome()
  

play_game()
