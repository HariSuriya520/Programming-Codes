# Author of this code: Hari Hara Sudhan S
# importing required modules

import time
import random

# A game for KCE students all the contents here
# are for fantasy only not to promote violence
# Please enjoy the game friends


def print_pause(statement):     # print and sleep function
    print(statement)
    time.sleep(2)


def intro(infestation, pl_name, friend_name):        # Introduction function
    print_pause("Hi "+pl_name+" welcome to The Adventure game of KCE V1.0")
    print_pause("You find yourself at your college entrance,"
                " The instituition is infested by "+infestation+".")
    print_pause("The task for you is to find your "
                "bestfriend "+friend_name+" who's trapped inside somewhere.")
    print_pause("And save your friend before "
                "the "+infestation+" attack "+friend_name+".")
    print_pause("There is only two places your friend could have been hiding!")
    print_pause("You're standing near the "
                "'A'-Block.")
    print_pause("To your left is the Food Court.")
    print_pause("To your right is the Library.")
    print_pause("In your hand you have your cricket bat "
                "(lucky and trust worthy but ineffective).")
    print_pause("Enter 1 to enter the Library.\n"
                "Enter 2 to enter the Food Court.\n"
                "What would you like to do ?")


def Foor_Court(items, infestation, friend_name):      # Food Court function
    print_pause("You've cautiously entered"
                " the Food court.")
    if "Fire extinguisher" in items:
        print_pause("You've been here before,, and gotten all the good stuff.")
    else:
        print_pause("The place is empty "+friend_name+" is not there but you "
                    "find a 'fire axe' next to the fire extinguisher.")
        print_pause("You discarded the bat and picked up the Fire Axe.")
        items.append("Fire extinguisher")
    print_pause("You walked back to 'A'-Block.")
    choice(items, infestation, friend_name)


def Library(items, infestation, friend_name):     # Library function
    print_pause("You've entered the Library.")
    print_pause("You found "+friend_name+" hiding under a desk.")
    print_pause("But there is the "+infestation+" roaming near the desk.")
    print_pause("The "+infestation+" saw you and "
                "It's running towards yourself to attack you")
    print_pause("You only have your lucky bat with you.")
    selection = input("Would you like to (1) Fight or (2) Run away\n")
    if "Fire extinguisher" in items and selection == "1":
        print_pause("You attack the "+infestation+" once"
                    " with the axe you hold.")
        print_pause("Then it runs off scared.")
        print_pause("Congradulations! You've saved your "
                    "bestfriend"+friend_name+".")
    elif selection == "1":
        print_pause("You do your best...")
        print_pause("But your lucky bat is no match for the "+infestation+".")
        print_pause("You have been defeated!")
    elif selection == "2":
        print_pause("You run back to the 'A'-Block luckily,"
                    " you don't seem to be followed.")
        choice(items, infestation)
    else:
        selection = input("Would you like to (1) Fight or (2) Run away\n")


def choice(items, infestation, friend_name):       # getting input from player
    value = input("(Please enter 1 or 2).\n")
    if value == "1":
        Library(items, infestation, friend_name)
    elif value == "2":
        Foor_Court(items, infestation, friend_name)
    else:
        choice(items, infestation, friend_name)


def game_over():        # prints game over
    print_pause("GAME OVER!")


def play_again():       # prompt to ask the player play again
    play = input("Would you like to play again? (y/n)\n").lower()
    if play == "y":
        Game_on()
    elif play == "n":
        print_pause("Thank you for playing!")
        return
    else:
        play_again()


def Game_on():      # to start the game function
    pl_name = input("Enter your name:\n")
    friend_name = input("Enter your friend's name:\n")
    random_list = ["demogorgon", "vampire", "werewolf",
                   "alien", "demodog", "Annebelle"]
    infestation = random.choice(random_list)
    items = []
    intro(infestation, pl_name, friend_name)
    choice(items, infestation, friend_name)
    game_over()
    play_again()


Game_on()
