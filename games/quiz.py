from random import sample
import python_module
from time import time as timer
import csv


def game():

    def player_init():
        '''A function that initializes player related necessary objects'''
        # Getting the number of players
        player_names = []
        # Adding players to a list
        num_players = python_module.input_with_validation(
            prompt="Enter the number of players (enter nothing to default to 1): ", default=1, condition="positive integer")
        for i in range(num_players):
            player_names.append(python_module.in_list(
                raw_tbc=f"Enter the name of the {i+1}{'st' if i == 0 else 'nd' if i == 1 else 'rd' if i == 2 else 'th'} player: ", condition='not in', list_=player_names,))
        # Creating dictionary for player name:player points, initializing player points to 0
        return {player_name: 0 for player_name in player_names}
    player_points = player_init()

    def get_questions_and_answers(num_questions):
        '''Getting the question bank and the corresponding answers'''
        # Efficiently getting data from a large file
        with open("questions.txt", "r") as question_file, open("answers.txt", "r") as answer_file:
            for question, answer in zip(list(question_file)[:num_questions:1], answer_file):
                yield question, answer

    def var_init(player_points=player_points):
        is_time = python_module.yes_or_no(
            "Do you want the questions to be timed? Enter 'y' / 'yes', or 'n' / 'no' (default 'n'): ", default='n')
        return python_module.in_range(
            f"Enter the number of questions (between 1 and 50) (default 25): ", 1, 50, "positive integer", default=25), dict(
            sample(list(player_points.items()), len(player_points))), is_time, python_module.input_with_validation(
            prompt="Enter the time you want for each question in seconds (default 30 seconds): ", condition="positive float", default=30) if is_time else 0, int(python_module.in_list("Enter the question type - 1 if you want to skip to the next question as soon as a question is answered correctly - or 2 if you want to give everyone a chance (defaulting to 1): ",
                                                                                                                                                                                       list_=['1', '2',], condition="in", prompt="Enter 1 or 2: ", default='1'))
    num_questions, player_points, is_time, time, question_type = var_init()

    def core_loop(player_points=player_points, num_questions=num_questions, is_time=is_time, time=time, question_type=question_type):
        '''The core question-answer loop'''
        selected, i = list(player_points.keys()), 0
        for question, answer in get_questions_and_answers(num_questions):
            for j, player in enumerate(selected):
                print('')
                start_time, guess, end_time = timer() if is_time else 0, input(
                    f"{i+1}. {question} (for {player}): ").strip().lower(), timer() if is_time else 0
                if (end_time - start_time) <= time:
                    if guess == answer.strip().lower():
                        player_points[player] += 1
                        if question_type == 1:
                            selected.append(selected.pop(0))
                            print(
                                f"\nCongrats, {player}, you got it!\nOn to the next question {f'(for {selected[0]})...' if i != num_questions-1 else '...'}: ")
                            break
                else:
                    print(f"Sorry, {player}, you took too much time")
                print((f"\nOn to the next player ({selected[j+1]})...\n") if (j !=
                      len(player_points)-1) else (f"\nOn to the next question {f'(for {selected[0]}) ...' if i != num_questions   -1 else '...'}: "))
            i += 1
            print("On to the scoring..." if i == num_questions else '')
        del i
    core_loop()

    def scoring(player_points=player_points, num_questions=num_questions):
        player_points = dict(sorted(player_points.items(),
                                    key=lambda item: item[1], reverse=True))
        for k, name in enumerate(list(player_points.keys())):
            print(
                f"{k+1}{'st' if k == 0 else 'nd' if k == 1 else 'rd' if k == 2 else 'th'} place: {name}, with {player_points[name]} answer{'' if player_points[name] == 1 else 's'} correct out of {num_questions} ({player_points[name]*100/num_questions}%){'!' if k in [0,1,2] else '.'}")
    scoring()
    if python_module.yes_or_no(
            "Do you want to play again? Enter 'y' / 'yes', or 'n' / 'no' (defaulting to 'n'): ", default='n'):
        print("Restarting game ...\n\n")
        game()
    else:
        def feedback():
            rating = python_module.in_range(
                tbc="Thank you for your time. Please rate our game out of 5 stars (defaulting to 5): ", ll=0, hl=5, condition="positive float", default=5)
            suggestions = input("Thank you for your rating. Please enter any suggestions for the game:\n" if rating == 5 else "Thank you for your rating. Please enter any suggestions you may have for our game:\n" if rating >=
                                4 else "Thank you for your time. Please enter any suggestions / complaints you may have for our game:\n" if rating >= 3 else "Please enter any complaints you may have about our game:\n")
            with open("ratings.txt", "a") as rating_file:
                rating_file.write(f"{rating}\n")
            with open("suggestions.txt", "a") as suggestions_file:
                suggestions_file.write(f"{suggestions}\n")
            print("We hope you enjoyed our game. Please play again later.")
        feedback()


if __name__ == "__main__":
    game()
