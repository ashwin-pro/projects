def game():
    def play_again():
        play_again = input(
            "Would you like to play again? (Y/N): ").strip().lower()
        if play_again == "y":
            print("Playing again\n\t___________________")
            game()
        elif play_again == "n":
            print("Thank you for your time.")
            exit()
        else:
            print("Choosing to exit on default.")
            print("Thank you for your time.")
            exit()

    def error_handling_float(num):
        num = num.strip()
        correct_input = False
        while not correct_input:
            try:
                num = float(num)
                correct_input = True
            except:
                num = input("Enter a number or decimal! : ")
        return num

    def error_handling_int_pos(num):
        num = num.strip()
        correct_input = False
        while not correct_input:
            try:
                num = int(num)
                if num > 0:
                    correct_input = True
                else:
                    num = input("Enter a positive number! : ")
            except:
                num = input("Enter a positive number! : ")
    round_ = True
    ll = error_handling_float(input(
        "Enter the lower limit of the number you want to guess for (number or decimal, negatives included, inclusive): "))
    hl = input("Enter the upper limit of the number: ")
    correct_input = False
    while not correct_input:
        hl = hl.strip()
        if error_handling_float(hl) <= ll:
            hl = input(
                "The upper limit should be more than the lower limit! : ")
        else:
            correct_input = True
    if int(hl)*1.0 != hl or int(ll)*1.0 != ll:
        round_ = input("Because both the limits are decimal, the number to be guessed can be decimal. Or would you prefer to round both limits to the nearest integer and make the number to be guessed an integer? (Y/N): ").strip().lower()
        correct_input = False
        while not correct_input:
            if round_ == "y":
                round_ = True
                hl = int(hl) + (hl % 1 >= 0.5)
                ll = int(ll) + (ll % 1 >= 0.5)
                from random import randint as r
                number = r(ll, hl)
            elif round_ == "n":
                round_ = False
                from random import uniform as f
                number = round(f(ll, hl), 1)
                print("The number will be a decimal with 1 decimal place.")
            else:
                round_ = input("Enter 'Y' or 'N': ").strip().lower()
    tries = input(
        "Do you want infinite tries or limited tries? Enter 'i' for infinite tries and 'l' for limited tries: ").strip().lower()
    correct_input = False
    while not correct_input:
        if tries == "i":
            tries = False
            correct_input = True
        elif tries == "l":
            num_tries = error_handling_int_pos(
                input("Enter the number of tries you want (natural number/positive integer): "))
            tries = True
            correct_input = True
        else:
            tries = input("Enter 'i' or 'l'! : ").strip().lower()
    if tries:
        for _ in range(num_tries):
            guess = input(
                f"Enter your guess between {ll} and {hl} (inclusive): ")
            correct_input = False
            while not correct_input:
                guess = guess.strip()
                try:
                    if round_:
                        guess = int(guess)
                    else:
                        guess = float(guess)
                    if ll <= guess <= hl:
                        correct_input = True
                    else:
                        guess = input(
                            f"The guess should be between {ll} and {hl} (inclusive)! : ")
                except:
                    if round_:
                        guess = input(
                            f"Enter an integer (between {ll} and {hl})! : ")
                    else:
                        guess = input(
                            f"Enter a decimal with one decimal place (between {ll} and {hl})! : ")
            if guess == number:
                print("You got it! ", end=None)
                play_again()
            else:
                if not round_:
                    if abs(guess-number) <= 1:
                        print("Hot!")
                    else:
                        print("Cold!")
                else:
                    if abs(guess-number) <= 10:
                        print("Hot!")
                    else:
                        print("Cold!")
        print("Sorry, you didn't get it in time. ", end=None)
        play_again()
    else:
        from keyboard import is_pressed as i
        print("You have unlimited tries. If you want to quit, press 'q'")
        while True:
            if i('q'):
                play_again()
            guess = input(
                f"Enter your guess between {ll} and {hl} (inclusive): ")
            correct_input = False
            while not correct_input:
                guess = guess.strip()
                try:
                    if round_:
                        guess = int(guess)
                    else:
                        guess = float(guess)
                    if ll <= guess <= hl:
                        correct_input = True
                    else:
                        guess = input(
                            f"The guess should be between {ll} and {hl} (inclusive)! : ")
                except:
                    if round_:
                        guess = input(
                            f"Enter an integer (between {ll} and {hl})! : ")
                    else:
                        guess = input(
                            f"Enter a decimal with one decimal place (between {ll} and {hl})! : ")
            if guess == number:
                print("You got it! ", end=None)
                play_again()
            else:
                if not round_:
                    if abs(guess-number) <= 1:
                        print("Hot!")
                    else:
                        print("Cold!")
                else:
                    if abs(guess-number) <= 10:
                        print("Hot!")
                    else:
                        print("Cold!")


if __name__ == "__main__":
    game()
