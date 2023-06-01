# This is a trivia game for people to play with their friends.
# Creating a function for the game
def game():
    # Importing the necessary modules.
    from math import inf
    from random import randint
    from winsound import Beep
    from time import time

    # Get the number of players
    num_players = input("How many people are playing?\n")
    valid_input = False
    positive_input_needed = False
    while not valid_input:
        try:
            num_players = int(num_players)
            # Check if input is in expected range, else keep prompting
            if num_players > 0:
                valid_input = True
            else:
                positive_input_needed = True
        except:
            pass
        if not valid_input:
            if not positive_input_needed:
                num_players = input("Invalid input. Enter a number.\n")
            else:
                num_players = input("Invalid input. Enter a positive number.\n")
    
    # Initialize the dictionary to hold player names
    player_names = {}
    # Initialize the dictionary to hold player scores
    player_scores = {}

    # Creating a dictionary of the questions attempted by each player.
    questions_attempted = {}

    # Get player names from user

    for i in range(num_players):
        player_names[i] = input(f"Enter the name of player {i+1}.\n")
        player_scores[i] = 0
        questions_attempted[i] = 0

    # Asking the players what mode they want

    mode = input("What mode of quizzing do you want?:\n first right answer - (When a correct answer is given, the next question is immediately asked.), or \n repeating choices(Even if the right answer is given, the same question continues.)?\n")

    if mode.strip().lower() == "first right answer":
        mode = 1
    elif mode.strip().lower() == "repeating choices":
        mode = 2
    else:
        mode = input(("Enter a valid mode(first right answer or repeating choices).\n"))
        if mode.strip().lower() == "first right answer":
            mode = 1
        elif mode.strip().lower() == "repeating choices":
            mode = 2
        else:
            print("Selecting first right answer by default.")
            mode = 1

    # Asking the users whether they want time.
    is_time_wanted = input("Do you want your questions to be timed? Enter yes if you do and no if you don't.\n")
    if is_time_wanted.strip().lower() == 'yes':
        is_time_wanted = True
    elif is_time_wanted.strip().lower() == 'no':
        is_time_wanted = False
    else:
        is_time_wanted = input("Invalid input. Enter yes or no.\n")
        if is_time_wanted.strip().lower() == 'yes':
            is_time_wanted = True
        elif is_time_wanted.strip().lower() == 'no':
            is_time_wanted = False
        else:
            is_time_wanted = False
            print("Turning time on by default.\n")

    # Asking the users how much time they want for each question.
    if is_time_wanted:
        time_wanted = input("Enter how much time you want for each question in seconds.\n")
        valid_input = False
        positive_input_needed = False
        while not valid_input:
            try:
                time_wanted = float(time_wanted)
                # Check if input is in expected range, else keep prompting
                if time_wanted > 0:
                    valid_input = True
                else:
                    positive_input_needed = True
            except:
                pass
            if not valid_input:
                if not positive_input_needed:
                    time_wanted = input("Invalid input. Enter a number.\n")
                else:
                    time_wanted = input("Invalid input. Enter a positive number.\n")

    # Creating question bank and bank of answers.
    question_bank = ["What is the fastest bird?\n","What is the fastest car ever built?\n","Who is the smartest person alive?\n","What is the slowest animal?\n"]
    answers = ["peregrine falcon","bugatti chiron supersport","johann goethe","three-toed sloth"]

    # Run the quiz
    # First, decide who takes the first question
    # Randomly select the id of the player who is the lucky one!

    first_answer_from = randint(0,len(player_names)-1)
    # Ask each question to the players

    for question_index in range(len(question_bank)):
        current_player = first_answer_from
        num_wrong_answers = 0
        raw_correct_answers = []
        # Loop all players until correct answer is given

        if  mode == 1:
                correct_answer_given = False
                    
                while(not correct_answer_given):
                    # Ask the question to the next player
                    print(player_names[current_player],"should answer now.")
                    if is_time_wanted:
                        start_time = time()
                    answer = input(question_bank[question_index])
                    if is_time_wanted:
                        end_time = time()
                    questions_attempted[current_player] += 1
                    # Check if answer is right  
                    if is_time_wanted:
                        if end_time - start_time <= time_wanted:
                            if answer.strip().lower() == answers[question_index]:
                                        # Increment the score!
                                        # Compute the score between 0 and 1 depending on the number of wrong answers.
                                score = 1 - 1/num_players * num_wrong_answers
                                player_scores[current_player] += score
                                print('Congrats! Right Answer,',player_names[current_player], ":-)")
                                correct_answer_given = True
                                Beep(2500,1000)
                            else:
                                        # Wrong answer
                                num_wrong_answers += 1
                                print("Sorry, Wrong Answer,",player_names[current_player],":-(")
                                Beep(250,1000)
                                # Go to the next player
                                current_player += 1
                                # Make sure the index loops back
                                if current_player >= num_players:
                                    current_player = 0
                                # Check if everyone got a chance already
                                if current_player == first_answer_from:
                                    print("The correct answer is",answers[question_index])
                                    break
                        else:
                            num_wrong_answers += 1
                            print("Sorry, too much time was taken for this question. :( \n")
                            Beep(250,1000)
                            # Go to the next player
                            current_player += 1
                            # Make sure the index loops back
                            if current_player >= num_players:
                                current_player = 0
                            # Check if everyone got a chance already
                            if current_player == first_answer_from:
                                print("The correct answer is",answers[question_index])
                                break
                    else:
                        if answer.strip().lower() == answers[question_index]:
                                        # Increment the score!
                                        # Compute the score between 0 and 1 depending on the number of wrong answers.
                                score = 1 - 1/num_players * num_wrong_answers
                                player_scores[current_player] += score
                                print('Congrats! Right Answer,',player_names[current_player], ":-)")
                                correct_answer_given = True
                                Beep(2500,1000)
                        else:
                                    # Wrong answer
                            num_wrong_answers += 1
                            print("Sorry, Wrong Answer,",player_names[current_player],":-(")
                            Beep(250,1000)
                            # Go to the next player
                            current_player += 1
                            # Make sure the index loops back
                            if current_player >= num_players:
                                current_player = 0
                            # Check if everyone got a chance already
                            if current_player == first_answer_from:
                                print("The correct answer is",answers[question_index])
                                break
        else:
            # Putting settings for repeating choices.
            for current_player in range(num_players):
                print(player_names[current_player],"should answer now.")
                if is_time_wanted:
                    start_time = time()
                answer = input(question_bank[question_index])
                if is_time_wanted:
                    end_time = time()
                questions_attempted[current_player] += 1
                if is_time_wanted:
                    if end_time-start_time <= time_wanted:
                        if answer.strip().lower() == answers[question_index]:
                            score = 1 - 1/num_players * num_wrong_answers
                            player_scores[current_player] += score
                            raw_correct_answers.append(player_names[current_player])
                        else:
                            num_wrong_answers += 1
                    else:
                        print("Sorry, too much time was taken for this question. :( \n")
            # Printing answer and who got it right.
            print("The answer to this question is",answers[question_index]+".")
            if raw_correct_answers:
                if len(raw_correct_answers) == 1:
                    print(raw_correct_answers[0],"got this question correct.")
                elif len(raw_correct_answers) == 2:
                    print(raw_correct_answers[0],"and",raw_correct_answers[1],"got this question correct.")
                else:
                    correct_answers_1 = ', '.join(raw_correct_answers[:-1])
                    correct_answers_2 = " and"+" "+str(raw_correct_answers[-1])
                    print(correct_answers_1+correct_answers_2,"got this question correct")
            else:
                print("No one got this question correct.")
        first_answer_from += 1
        if first_answer_from >= num_players:
            first_answer_from = 0
            
        if question_index != len(question_bank)-1:
            print("")
            print("Let's go to the next question")
            print("")
        else:
            print("")

    # Announcing the results.
    for i in range(num_players):
        print(player_names[i],"got",str(int(player_scores[i]/len(question_bank)*100))+"% from his attempted questions("+str(questions_attempted[i])+").")

    # Congratulate the players based on their scores.
    for m in range(num_players):
        if player_scores[m] != 1:
            if player_scores[m]>=0.9:
                print("Congratulations!,",player_names[m],", you got a very good score. Keep on practising, and maybe you will get 100% one day.")
            elif player_scores[m]>=0.8:
                print("Congratulations!,",player_names[m],", you got a good score. Keep on practising and you might get 100% one day.")
            elif player_scores[m]>=0.7:
                print("Good attempt,",player_names[m],", try harder next time and you will definitely improve.")
            else:
                print("Nice try,",player_names[m],", try harder next time.")
        else:
            print("Congratulations!,",player_names[m],", you got a score of 100%!")
    # Creating the array which will help me find the winner.

    the_winner_array = []
    for j in range(num_players):
        current_percentage = int(player_scores[j]/len(question_bank)*100)
        the_winner_array.append(current_percentage)

    # Finding the winner

    biggest_number = -inf
    for x in range(len(the_winner_array)):
        if the_winner_array[x] > biggest_number:
            biggest_number = the_winner_array[x]
            biggest_number_index = x
            
    print("Congrats",player_names[biggest_number_index]+"!, you are the winner!")
    for i in range(5):
        Beep(randint(37,5000),500)

    # Thanking the players for playing
    print("Thank you for playing our game. We hope to see you next time.")

    # Asking for ratings and suggestions
    rating = input("Please rate our game out of five stars.\n")
    valid_input = False
    positive_input_needed = False
    while not valid_input:
        try:
            rating = float(rating)
            # Check if input is in expected range, else keep prompting
            if rating >= 0:
                valid_input = True
            else:
                positive_input_needed = True
        except:
            pass
        if not valid_input:
            if not positive_input_needed:
                rating = input("Invalid input. Enter a number.\n")
            else:
                rating = input("Invalid input. Enter a positive number.\n")
    suggestions = False
    if rating <= 5 and rating >= 0:
        if rating != 5:
            if rating>=4:
                suggestions = (input("Thank you for your support. Please enter your complaints or suggestions below.\n"))
            elif rating >= 3:
                suggestions = (input("Thank you for your time. Please enter your complaints or suggestions below.\n"))
            elif rating >=1:
                suggestions = (input("Please enter your complaints or suggestions below.\n"))
            else:
                exit

        else:
            print("Thank you so much for your support.")
    else:
        print("Invalid rating.")
    # Adding the user's suggestions to the suggestions text file
    if suggestions:
        with open("suggestions.txt","a") as suggestion:
            suggestion.write(f"{suggestions}\n")
    # Asking the user if they want to play again
    want_to_play = input('Would you like to play again?\nAnswer yes or no.\n')
    if want_to_play.strip().lower() == 'yes':
        game()
    elif want_to_play.strip().lower() == 'no':
        print('Thank you for playing.')
    else:
        want_to_play = input('Invalid input. Enter yes or no.\n')
        if want_to_play.strip().lower() == 'yes':
            game()
        elif want_to_play.strip().lower() == 'no':
            print('Thank you for playing.')
        else:
            print('Selecting no by default.')
            print('Thank you for playing.')
# Calling the game function in the beginning to run the game
game()