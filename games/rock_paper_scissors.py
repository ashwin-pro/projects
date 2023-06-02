from random import choice
def game():
    player_points = 0
    computer_points = 0
    for i in range(3):
        invalid_input = False
        human = input('Enter rock, paper, or scissors.\n').strip().lower()
        computer = choice(['rock','paper','scissors'])
        print(f"The computer chose {computer}")
        if human == computer:
            print('The result of this round is a tie.\n')
            player_points += 0.5
            computer_points += 0.5
        elif human == 'rock':
            if computer == 'paper':
                winner = 'The computer'
            else:
                winner = 'You'
        elif human == 'paper':
            if computer == 'rock':
                winner = 'You'
            else:
                winner = 'The computer'
        elif human == 'scissors':
            if computer == 'rock':
                winner = 'The computer'
            else:
                winner = 'You'
        else:
            print('Invalid input.\n')
            game()
            invalid_input = True
        if not invalid_input:
            print(f"{winner} won this round.\n")
            if winner == 'You':
                player_points += 1
            else:
                computer_points += 1
    print(f"The computer has {computer_points} points and you have {player_points} points.\n")
    want_to_play_again = input('Would you like to play again?\nEnter yes or no.\n').strip().lower()
    if want_to_play_again == 'yes':
        game()
    elif want_to_play_again == 'no':
        print('Thank you for playing.')
    else:
        want_to_play_again = input('Invalid input.\nEnter yes or no.\n').strip().lower()
        if want_to_play_again == 'yes':
            game()
        elif want_to_play_again == 'no':
            print('Thank you for playing.')
        else:
            print('Selecting no by defalut.\nThank you for playing.')
game()