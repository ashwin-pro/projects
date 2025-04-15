
# Importing the necessary modules and files.
from time import sleep
from keyboard import wait,is_pressed
from random import choice
from turtle import *
from game_func_class import *
'''Importing modules'''

def game():
    def get_rating_suggestion():
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
        return suggestions,rating
    '''Defining a function called get_rating_suggestion that gets a rating and suggestion for the game.'''

    # Introducing the game.
    game_intro = "Welcome to the Ninjago game. This game is a adventure game inspired by the popular TV show Lego Ninjago. Press 'q' to start."
    print(game_intro)
    wait('q')

    # Getting character name.
    name = input("Please enter your character's name")
    player_type = choice(['elemental master','ninja','spinjitsu master'])

    # Getting character type & element (if possible).
    if player_type == 'spinjitsu master':
        player = Spinjitsu_Master(name="You")
    elif player_type == 'ninja':
        player = Ninja(name="You")
    elif player_type == 'elemental master':
        player = Elemental_Master(name="You")

    if player_type == 'elemental master' or player_type == 'ninja':
        player.elemental_power = choice(['fire','water','wind','ice','lightning','earth'])

    # Introducing player & buying first weapon.
    starter_bot = Npc('Bob')
    if player_type == 'spinjitsu master':
        print(f"{starter_bot.introduce()} You are a {player_type.title()} and have {player.coins} coins. Please select a weapon from the shop. Press 'o' to open the shop.\n")
    else:
        print(f"{starter_bot.introduce()} You are a {player_type.title()} and have {player.coins} coins. Your element is {player.elemental_power}. Please select a weapon from the shop. Press 'o' to open the shop.\n")
    wait('o')
    weapon_shop(player)
    assert(player.weapon == "sword")
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
    while waiting <= 60:
        if is_pressed('t'):
            print(f"Travelling...")
            sleep(5.0)
            break
        # Asking for replay and suggestions.
        if waiting > 60:
            print(f'Sorry, you did not reach the village in time.')
            suggestions,rating = get_rating_suggestion()
            with open('game_suggestions.txt','a') as file:
                file.write(f"{suggestions} : {rating}/5 stars.\n")
            print('\nWould you like to play again?\nType 1 to play again and 2 to quit.\nYou have one minute to enter input. If no input is given, you will automatically quit.\n')
            inner_waiting = 0
            while True:
                if is_pressed(1):
                    game()
                if is_pressed(2):
                    print(f'Thank you for playing.')
                    exit()
                if inner_waiting > 60:
                    exit()
                sleep(0.1)
                inner_waiting += 0.1
        sleep(0.1)
        waiting += 0.1

    print("As you approach the village, you see a serpentine with blue stripes. It approaches you, ready to attack. Do you attack?")
    print("Press 'a' to attack, 't' to try to talk to it, and 'r' to retreat")
    timer = 0
    while timer <= 30:
        if timer == 20:
            print("The snake is approaching you fast! What do you do?")
        if is_pressed('a'):
            print("You attack it.")
            fight(player,Fighter())
            break
        elif is_pressed('r'):
            print("You retreat, clambering up to the top of a house so you can see better. You see that the whole village is being swarmed by Serpentine, who appear to be led by some sort of leader, holding up a staff.")
            print("You make a plan. You try to ")
            
        elif is_pressed('t'):
            print("You try to talk to it, but it just hisses and tries to attack you. You are forced to attack back. You fight it.")
            fight(player,Fighter())
            break
        sleep(0.1)
        timer += 0.1
if __name__ == "__main__":
    game() 