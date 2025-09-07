# for day 1 i decided to do a simple number guessing game

import random

number = random.randint(0, 100)
print(number)
guess = int(input('type in an integer from 0-100\n')) 

if guess == number:
    print('Good guess, the number was', number )
elif guess != number:
    while guess != number:
        if guess > number:
            print('The number is lower than', guess)
            guess = int(input('type in an integer from 0-100\n')) 
        elif guess < number:
            print('The number is higher than', guess)
            guess = int(input('type in an integer from 0-100\n'))
    else: 
        print('Good guess,the number was', number )
