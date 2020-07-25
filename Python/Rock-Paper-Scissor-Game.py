import random
import sys

Player = 0
Bot = 0
Tied = 0

def play():
    Player_Choice = input("\nWhat do you choose? \n[Rock, Paper or Scissors]: ").capitalize()
    choices = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissors'}
    Bot_Choice = choices[random.randint(1,3)]
    print("\nYou Chose: ",Player_Choice)
    print("Bot Chose: ",Bot_Choice)
    global Player
    global Bot
    global Tied
    if Player_Choice == Bot_Choice:
        Tied += 1
        print('\nTie!')
    elif compare(Player_Choice,Bot_Choice):
        Player += 1
        print('\nYou Win!')
    else:
        Bot += 1
        print('\nYou Lose!')
    print("\nYour Score is: ",Player)
    print("Bot Score is: ",Bot)
    print("Tied Score is: ",Tied)

def compare(playerChoice,cpuChoice):
    results = {('Paper','Rock') : True,
               ('Paper','Scissors') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissors') : True,
               ('Scissors','Paper') : True,
               ('Scissors','Rock') : False}
    return results[(playerChoice,cpuChoice)]

def game_start():
    begin = input("Would you like to play Rock, Paper, Scissors? \n(Yes, No): ").capitalize()
    while begin != "Yes":
        if begin == "No":
            print("\nGame Over")
            sys.exit()
        else:
            print("\nPlease Enter Yes or No")
            begin = input("\nWould you like to play Rock, Paper, Scissors? ").capitalize()
    play()
    while True:
        begin = input('\nPlay again? \n(Yes, No): ').capitalize()
        while begin != "Yes":
            if begin == "No":
                print("\nGame Over")
                global Player
                global Bot
                global Tied
                print("\nYour Score: ",Player)
                print("Bot Score: ",Bot)
                print("Tied Score: ",Tied)
                sys.exit()
            else:
                print("\nPlease Enter Yes or No")
                begin = input("\nPlay again? \n(Yes, No): ").capitalize()
        play()

game_start()
