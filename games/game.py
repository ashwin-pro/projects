# Importing the necessary modules and files.
from game_func_class import *
from keyboard import *
from random import *
from turtle import *

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
print("Jamanakai Village is in danger! Go save the residents of the village. Walk towards the red dot on the map to reach the village. Press 'm' to open the map.")
wait('m')
Screen().bgcolor('light green')

# Creating map
player_object = Turtle('classic')
Jamanakai_Village = Turtle()
Jamanakai_Village.shape('circle')
Jamanakai_Village.color("red")
Jamanakai_Village.penup()
Jamanakai_Village.goto(350,300)
setheading(player_object.towards(Jamanakai_Village))
done()