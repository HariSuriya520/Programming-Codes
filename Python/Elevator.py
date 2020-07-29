import time

def print_sleep(intro):
    print(intro)
    time.sleep(1)
    
def enter_floor():
    print_sleep("Please enter the number for the floor you would like to visit:")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n"
                  "4. To Exit the Elevator\n")
    if floor == "1":
        print_sleep("You push the button for the first floor.")
        print_sleep("After a few moments, you find yourself in the lobby.")
        print_sleep("Where would you like to go next?")        
        enter_floor()
    elif floor == "2":  
        print_sleep("You push the button for the second floor.")
        print_sleep("After a few moments, you find yourself in the human resources department.")
        print_sleep("Where would you like to go next?")        
        enter_floor()
    elif floor == "3":
        print_sleep("You push the button for the third floor.")
        print_sleep("After a few moments, you find yourself in the engineering department.")
        print_sleep("Where would you like to go next?")        
        enter_floor()
    elif floor == "4":
        print_sleep("Have a great day!")
        print_sleep("Thank you! for using the elevator")
    else:
        print_sleep("Sorry, I can't understand!")
        print_sleep("Please select a number from the list")
        enter_floor()

def introduction():
    print_sleep("You have just arrived at your new job!")
    print_sleep("You are in the elevator.")

    
def elevator():
    introduction()
    enter_floor()

elevator()
