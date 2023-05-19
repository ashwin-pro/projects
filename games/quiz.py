# This is a trivia game for people to play with their friends.
# Importing the necessary modules.
from math import inf
from random import randint
from winsound import Beep
from time import time

# Get the number of players


num_players = int(float(input("How many people are playing?\n")))
if num_players < 0:

    num_players = int(float(input("Invalid input. Please enter a valid positive integer.\n")))
    if num_players < 0:
        print("Invalid input. Keeping number of players as 1 by default.")

        num_players = 1
# Initialize the dictionary to hold player names


player_names = {}
# Initialize the dictionary to hold player scores

player_scores = {}

# Creating a dictionary of the questions attempted by each player.

questions_attempted = {}

# Get player names from user

for i in range(num_players):
    name_asking = "Enter the name of player"

    player_names[i] = input(name_asking+" "+str(i+1)+".\n")

    player_scores[i] = 0

    questions_attempted[i] = 0

# Asking the players what mode they want


mode = input("What mode of quizzing do you want?:\n first right answer - (When a correct answer is given, the next question is immediately asked.), or \n repeating choices(Even if the right answer is given, the same question continues.)?\n")

if mode.lower() == "first right answer":

    mode = 1
elif mode.lower() == "repeating choices":

    mode = 2
else:

    mode = input(("Enter a valid mode(first right answer or repeating choices).\n"))
    if mode.lower() == "first right answer":

        mode = 1
    elif mode.lower() == "repeating choices":

        mode = 2
    else:
        print("Selecting first right answer by default.")
        print("")

        mode = 1

# Adding time feature for each question.

want_time = input("Do you want the questions to be timed?\nIf you do, input yes.\n If you don't, input no.\n")
if want_time.lower() == "yes":

    want_time = True
elif want_time.lower() == "no":

    want_time = False
else:

    want_time = input("Invalid input. Enter yes or no.\n")
    if want_time.lower() == "yes":

        want_time = True
    elif want_time.lower() == "no":

        want_time = False
    else:
        print("Setting time to on.")
        print("")

        want_time = True


# Letting the users choose how much time they want for each question.




# Creating question bank and bank of answers.

    question_bank = ["What is the fastest bird?\n","What is the fastest car ever built?\n","Who is the smartest person alive?\n"]

    answers = ["peregrine falcon","bugatti chiron supersport","johann goethe"]

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
                answer = input(question_bank[question_index])
                questions_attempted[current_player] += 1
                # Check if answer is right  
                    
                if answer.lower() == answers[question_index]:
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
            answer = input(question_bank[question_index])
            questions_attempted[current_player] += 1
            if answer.lower() == answers[question_index]:
                score = 1 - 1/num_players * num_wrong_answers
                player_scores[current_player] += score
                raw_correct_answers.append(player_names[current_player])
            else:
                num_wrong_answers += 1
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

# Asking for ratings
rating = float(input("Please rate our game out of five stars.\n"))
if rating != 5:
    if rating>=4:
        suggestions = input("Thank you for your support. Please enter your complaints or suggestions below.\n")
    elif rating >= 3:
        input("Thank you for your time. Please enter your complaints or suggestions below.\n")
    elif rating >=1:
        input("Please enter your complaints or suggestions below.\n")
    else:
        exit

else:
    print("Thank you so much for your support.")