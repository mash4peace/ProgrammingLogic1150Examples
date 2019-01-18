""" Play rock - paper - scissors against a computer """

# This allows Python to use code to do things like choosing a random option, or random number
import random

# This line will choose a random string from the choices 'rock', 'paper', or 'scissors'
computer_choice = random.choice(['rock', 'paper', 'scissors'])

human_choice = input('Enter "rock", "paper" or "scissors": ')

if human_choice != "rock" and human_choice != 'paper' and human_choice != 'scissors':
    print('You need to enter rock, paper or scissors. Game over.')

else:

    print('The computer chooses ' + computer_choice)

    # Situations where the computer and human tie, by making the same choice
    if human_choice == computer_choice:
        print('You both chose ' + human_choice + ' so the game is tied.')

    # Situations where the human beats the computer

    elif human_choice == 'rock' and computer_choice == 'scissors':
        print('Rock beats scissors. You win')

    elif human_choice == 'scissors' and computer_choice == 'paper':
        print('Scissors beats rock. You win')

    elif human_choice == 'paper' and computer_choice == 'rock':
        print('Paper beats rock. You win')

    # If it's not a tie, and the human doesn't win, then the computer must the be winner.
    else:
        print('Sorry, ' + computer_choice + ' beats ' + human_choice + '. Computer wins.')



