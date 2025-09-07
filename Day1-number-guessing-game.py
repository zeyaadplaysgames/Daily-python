import random

number = random.randint(0, 100)
# print(number) - only for debug

guess = int(input('type in an integer from 0-100\n')) 
attempts = 1 
if guess == number:
    print('Good guess, the number was', number )
elif guess != number:
    while guess != number:
        if guess > number:
            print('The number is lower than', guess)
            guess = int(input('type in an integer from 0-100\n')) 
            attempts = attempts + 1
        elif guess < number:
            print('The number is higher than', guess)
            guess = int(input('type in an integer from 0-100\n'))
            attempts = attempts + 1
    else: 
        print('Good guess,the number was', number , 'and it took you', attempts ,'attemps')
        print('Thanks for playing! :D')
