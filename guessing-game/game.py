"""A number-guessing game."""
intro = input('Hello, What is your name? ')
name = 'Hello {}! Try to guess a number between 1 and 10'.format(intro)
print(name)

import random
number = random.randrange(1,10)
guess = int(input('Your guess: '))
count = 1

while guess != number: 
    if guess < number:
        print('Your guess is too low, try again.')
        guess = int(input('Your guess: '))
    else:
        print('Your guess is too high, try again.')
        guess = int(input('Your guess: '))
    count += 1
print('Great, you guessed my number in', count,'attempt(s)!')

# Put your code here
