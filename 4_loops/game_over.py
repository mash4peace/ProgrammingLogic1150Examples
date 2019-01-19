import random

game_over = False

while not game_over:

    print('The computer will flip a coin. Guess heads or tails')
    guess = input('Enter H for heads or T for tails: ')

    coin_flip = random.choice(['H', 'T'])

    print('The computer flipped a ' + coin_flip)

    if coin_flip != guess:
        print('Game over')
        game_over = True
    else:
        print('You guessed right! Try again...')

print('Thanks for playing!')


