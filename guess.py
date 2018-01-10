#Lab1 Jeremy Wolfe
# Guess a number

import random

random_pick = random.randint(1,10)

print('computer random number is : ' + str(random_pick))

guessed_number = input('Guess a number between 1 and 10: ')
guessed_number = int(guessed_number)

while True:
    if random_pick == guessed_number:
        print('You got it!')
        break
    elif random_pick < guessed_number:
            print('Your guess is high')
    elif random_pick > guessed_number:
            print('Your guess is low')

    guessed_number = input('Guess again ')
    guessed_number = int(guessed_number)
