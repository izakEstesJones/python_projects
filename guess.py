from random import randint
again = 'y'

while again == 'y':
    ran_num = randint(1,10)
    guess = input('pick a number from 1 to 10: ')
    guess = int(guess)
    while guess != ran_num:
        if guess < ran_num:
            print('too low')
            guess = int(input('try again: '))
        elif guess > ran_num:
            print('too high')
            guess = int(input('try again: '))
        else:
            guess = int(input('Something is wrong here. Guess a number between 1 and 10: '))
    print('good job you got it')
    print('would you like to play again? y/n:')
    again = input()
print('thanks for playing')