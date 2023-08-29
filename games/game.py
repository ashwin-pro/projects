
    # Importing the necessary modules and files.
from time import sleep
from game_func_class import *
from keyboard import wait,is_pressed
from random import choice
from turtle import *

def game():
    # Introducing the game.
    game_intro = "Welcome to the Ninjago game. This game is a adventure game inspired by the popular TV show Lego Ninjago. Press 'q' to start."
    print(game_intro)
    wait('q')

    # Getting character name.
    name = input("Please enter your character's name.\n")
    player_type = choice(['elemental master','ninja','spinjitsu master'])

    # Getting character type & element (if possible).
    if player_type == 'spinjitsu master':
        global player
        player = Spinjitsu_Master(name=name)
    elif player_type == 'ninja':
        player = Ninja(name=name)
    elif player_type == 'elemental master':
        player = Elemental_Master(name=name)

    if player_type == 'elemental master' or player_type == 'ninja':
        player.elemental_power = choice(['fire','water','wind','ice','lightning','earth'])

    # Introducing player & buying first weapon.
    starter_bot = Npc('Bob')
    if player_type == 'spinjitsu master':
        get_weapon = print(f"{starter_bot.introduce()} You are a {player_type.title()} and have {player.coins} coins. Please select a weapon from the shop. Press 'o' to open the shop.\n")
    else:
        get_weapon = print(f"{starter_bot.introduce()} You are a {player_type.title()} and have {player.coins} coins. Your element is {player.elemental_power}. Please select a weapon from the shop. Press 'o' to open the shop.\n")
    wait('o')
    weapon_shop(player)

    # Give first quest.
    print("Jamanakai Village is in danger! Go save the residents of the village. Walk towards the red dot on the map to reach the village. Press 'm' to open the map. Close the pop-up window and press 'm' again to continue.\n\n")
    wait('m')

    # Creating map.
    Screen().bgcolor('light green')
    player_object = Turtle()
    player_object.shape('arrow')
    Jamanakai_Village = Turtle()
    Jamanakai_Village.shape('circle')
    Jamanakai_Village.color("red")
    Jamanakai_Village.penup()
    Jamanakai_Village.goto(350,300)
    player_object.setheading(player_object.towards(Jamanakai_Village))
    done()
    wait('m') 

    # Travelling to Jamanakai Village.
    print("Press 't' to start heading towards the village. You have 1 minute to get to the village.\n")
    waiting = 0
    while True:
        if is_pressed('t'):
            break
            
        # Asking for replay and suggestions.
        if waiting > 60:
            print('Sorry, you did not reach the village in time.')
            rating = input('Please rate this game out of 5. Your guidance and support are of paramount importance in the improvement of this game.').strip().lower()
            correct_input = False
            while not correct_input:
                try:
                    rating = float(rating)
                    if rating > 0:
                        correct_input = True
                    else:
                        rating = input('Incorrect input. Please enter a positive number.\n')
                except:
                    rating = input('Incorrect input. Please enter a positive number.\n')
            suggestions = input('Please enter your suggestions for the improvement of this game.\n')
            with open('game_suggestions.txt','a') as file:
                file.write(f"{suggestions} : {rating}/5 stars.\n")
            print('\nWould you like to play again?\nType 1 to play again and 2 to quit.\nYou have one minute to enter input. If no input is given, you will automatically quit.\n')
            inner_waiting = 0
            while True:
                if is_pressed(1):
                    game()
                if is_pressed(2):
                    print('Thank you for playing.')
                    exit()
                if inner_waiting > 60:
                    exit()
                sleep(0.1)
                inner_waiting += 0.1
        sleep(0.1)
        waiting += 0.1

