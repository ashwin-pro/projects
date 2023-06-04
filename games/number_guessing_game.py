import random
import os   
def game():
    # Get the lower boundary.
    start = input("Welcome to my number guessing game.\nTo start, enter the lower boundary of the possible number.\n")
    # Convert the lower boundary to a number.
    valid_input = False
    while not valid_input:
        try:
            start = float(start)
            valid_input = True
        except:
            start = input("Invalid input.\nEnter a number.\n")
    # Get the upper boundary.
    end = input("Enter the upper boundary of the possible number.\n")
    # Convert the upper boundary to a number.
    valid_input = False
    while not valid_input:
        try:
            end = float(end)
            valid_input = True
        except:
            end = input("Invalid input.\nEnter a number.\n")
    # Make sure the upper boundary is greater than the lower boundary.
    if end > start:
        pass
    else:
        end = input("The upper boundary of the number must be greater than it's lower boundary.\n")
    # Get the mode.
    mode = input("Do you want to guess an integer or a decimal number?\nEnter 1 for integers or 2 for decimal numbers.\n")
    # Convert the mode to an integer.
    valid_input = False
    while not valid_input:
        try:
            mode = int(mode)
            valid_input = True
        except:
            mode = input('Invalid input.\nEnter 1 or 2.\n')
    # Make sure the mode is 1 or 2.
    valid_input = False
    while not valid_input:
        if mode == 1 or mode == 2:
            valid_input = True
        else:
            valid_input = False
            inner_valid_input = False
            while not inner_valid_input:
                try:
                    mode = int(mode)
                    inner_valid_input = True
                except:
                    mode = input('Invalid input.\nEnter 1 or 2.\n')
    # Get the number of tries.
    num_tries = input('Enter the number of tries you want to guess the number.\n')
    # Convert the number of tries to an integer.
    valid_input = False
    positive_input_needed = False
    while not valid_input:
        try:
            num_tries = int(num_tries)
            if num_tries > 0:
                valid_input = True
            else:
                positive_input_needed = True
        except:
            pass
        if not valid_input:
            if not positive_input_needed:
                num_tries = input("Invalid input.\nEnter a number.\n")
            else:
                num_tries = input("Invalid input.\nEnter a positive number.\n")
    # Generate the number.
    if mode == 1:
        number = random.randint(start,end)
    else:
        number = random.uniform(start,end)
    # Getting the user's guesses each time.
    for i in range(num_tries):
        guess = input("Guess the number.\n")
        valid_input = False
        while not valid_input:
            try:
                guess = float(guess)
            except:
                guess = input('Invalid input.\nEnter a number.\n')
        if guess == number:
            if i == 0:
                ordinal = 'st'
            elif i == 1:
                ordinal = 'nd'
            elif i == 2:
                ordinal = 'rd'
            else:
                ordinal = 'th'
            print(f"Congratulations, you guessed the number on the {i+1}{ordinal} try!")
            want_to_play_again = input("Do you want to play again?\nEnter yes if you do and no if you don't.\n")
            if want_to_play_again.strip().lower() == 'yes':
                print('\n--------------------\n')
                game()
            elif want_to_play_again.strip().lower() == 'no':
                print('Thank you for playing.')
                os._exit()
            else:
                want_to_play_again = input('Invalid input.\nEnter yes or no.\n')
                if want_to_play_again.strip().lower() == 'yes':
                    print('\n--------------------\n')
                    game()
                elif want_to_play_again.strip().lower() == 'no':
                    print('Thank you for playing.')
                    os._exit()
                else:
                    print("Selecting no by default.")
                    print('Thank you for playing.')
                    os._exit()
        elif guess > number:
            print('Sorry, your guess is too high.\n')
        else:
            print('Sorry, your guess is too low.\n')
    print('Sorry, you did not guess the number.\n')
    print(f"the number was {number}.")
    want_to_play_again = input("Do you want to play again?\nEnter yes if you do and no if you don't.\n")
    if want_to_play_again.strip().lower() == 'yes':
        print('\n--------------------\n')
        game()
    elif want_to_play_again.strip().lower() == 'no':
        print('Thank you for playing.')
        os._exit()
    else:
        want_to_play_again = input('Invalid input.\nEnter yes or no.\n')
        if want_to_play_again.strip().lower() == 'yes':
            print('\n--------------------\n')
            game()
        elif want_to_play_again.strip().lower() == 'no':
            print('Thank you for playing.')
            os._exit()
        else:
            print("Selecting no by default.")
            print('Thank you for playing.')
            os._exit()
# Running the game in the beginning.
game()