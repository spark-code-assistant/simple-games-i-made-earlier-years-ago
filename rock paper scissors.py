''' made by atharvnubprogrammer#0 in discord'''
import random
from time import sleep
#defining variables
''' 0 : rock
    1 : paper 
    2: scisscors'''
rules = " WELCOME!!! to rps  you will be competing between ai Chose 0 as rock 1 as paper and 2 for scissors"
for i in rules:
    print(i , end ='')
    sleep(0.01)
def main_game():
    user_input1 = int(input("Enter the choice "))
    print(user_input1)
    choices = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2]
    computer_choice = random.choice(choices)
    if user_input1 == computer_choice:
        print("you bot chosse same ")
    #winning
    elif user_input1 == 0 and computer_choice == 2:
        print(f"you won computer chosse {computer_choice} and you choose {user_input1}")
    elif user_input1 == 1 and computer_choice == 0:
        print(f"you won computer chosse {computer_choice} and you choose {user_input1}")
    elif user_input1 == 2 and computer_choice == 1:
        print(f"you won computer chosse {computer_choice} and you choose {user_input1}")
    #loss
    elif user_input1 == 0 and computer_choice == 1:
        print(f" you lost computer choose {computer_choice} and you choose {user_input1}")
    elif user_input1 == 1 and computer_choice == 2:
        print(f" you lost computer choose {computer_choice} and you choose {user_input1}")
    elif user_input1 == 2 and computer_choice == 0 :
        print(f" you lost computer choose {computer_choice} and you choose {user_input1}")
    while True:
        main_game()
main_game()