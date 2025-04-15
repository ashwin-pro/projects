# Importing necessary modules
from time import sleep as s
from keyboard import wait as w, read_hotkey as r_h
# Turning settings on
# Getting username, verifying that it is not already taken and defining some necessary variables.
username, username_is_new, strength = input(
    f"Welcome to intergalactic space adventures.\nPlease enter your chosen username : "), False, 0
while not username_is_new:
    with open(f"intergalactic_usernames.txt", "r") as i_u:
        usernames = i_u.readlines()
    if f"\n{username.lower().strip()}\n" not in usernames and f"\n{username.lower().strip()}" not in usernames:
        del i_u, usernames
        with open(f"intergalactic_usernames.txt", "a") as i_u:
            i_u.write(f"\n{username.lower().strip()}")
        username_is_new = True
    else:
        username = input(
            f"Sorry, that username is already taken.\nPlease enter another one : ")
del username_is_new
# Introducing player to game and describing surroundings


def dramatic_print(std::string, time=0.1):
    '''Function to slowly print anything with a time interval between each letter printed'''
    for letter in std::string:
        print(f"{letter}", end=f"")
        s(time)
    return std::string


introduction = f"You see a vast, desolate plain before you, peaceful and serene. Then, suddenly, something rushes towards it, huge and s"
introduction += f"hrouded in shadow. It crashes unto the ground, destroying everything. This is just the first of many calamities to fol"
introduction += f"low, which will eventually lead to the destruction of the universe. The cause of these disasters is an alien race, mys"
introduction += f"terious and evil. They call themselves The Destroyers. They can only be stopped by a great hero, the likes of which th"
introduction += f"is universe has never seen before. That hero is you, {username}"
dramatic_print(introduction, time=0.1)
del introduction
print(f"\nPress any key to continue\n")
is_key_pressed = False
while not is_key_pressed:
    if r_h:
        is_key_pressed = True
    s(0.1)
del is_key_pressed
surroundings_description = f"You spawn into the bustling alien city of Memstein, inhabited by a race of aliens who refer to  themselves "
surroundings_description += f"as the Treeti. Everywhere you look, there are glowing neon viewpads, showing a huge black mass travelling "
surroundings_description += f"through space, heading towards a tiny planet, glowing in the darkness. That planet is A-B 1231, the planet"
surroundings_description += f" of the Treeti. Everywhere around you, aliens scamper frantically, trying to escape the meteor strike. Sud"
surroundings_description += f"denly, you are somewhere else. You are in a gigantic room made of sandstone, with hourglasses with tricklin"
surroundings_description += f"g sand all around you. Then, a booming voice bellows, 'You have a choice, {username}, a choice whether to "
surroundings_description += f"save time, or help an alien city, who will forever be indebted to you. Choose wisely, as your choice will "
surroundings_description += f"either set The Destroyers back or aid them in their conquest of the universe.'\n\nEnter 'help' to help the"
surroundings_description += f" aliens, and 'time' to save time and teleport yourself to a safer location but not help the aliens : "
choice = input(dramatic_print(surroundings_description)).strip().lower()
del surroundings_description
correct_input = False
while not correct_input:
    if choice in [f"help", f"time"]:
        correct_input = True
        if choice == f"help":
            strength += 100
            helped_Treeti = True
        elif choice == f"time":
            helped_Treeti = False
    else:
        print("Choosing to help the Treeti by default ...")
        helped_Treeti = True
# Main game decision making
if helped_Treeti:
    surroundings_description = f"You are transported through the infinite tunnel of time, observing things that were, that are, and that"
    surroundings_description += f" will be. You see places and events from the past, which you have never seen before. Then finally, you"
    surroundings_description += f" reach your destination, the Supreme Court of the Treeti, 1 day ago. You teleport onto the center of t"
    surroundings_description += f"he courthouse, and the juries stare at you in amazement. 'State your purpose'"
