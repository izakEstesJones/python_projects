from random import choice

games = int(input('How many times would you like to lose to the computer? '))

p_win = 0
c_win = 0
while True:
    while p_win < games and c_win < games:
        options = ['rock', 'paper', 'scissors']
        computer = choice(options)

        print(f'Computer: {c_win} vs Human: {p_win}')
        print('\nHUMAN: what element do you choose?')
        p1 = input()
        p1 = p1.lower()
        if p1 =='quit' or p1 == 'q':
            break

        print(f'\n\nComputer selects: {computer.upper()}\n')

        # Making the decision
        if p1 == computer:
            print('WHAT?!?! A DRAW?!')
        elif p1 == 'rock':
            if computer == 'paper':
                print('Computer crushes the puny human!')
                c_win += 1
            elif computer == 'scissors':
                print('You lucked out this time, human...')
                p_win += 1
        elif p1 == 'paper':
            if computer == 'scissors':
                print('Computer crushes the puny human!')
                c_win += 1
            elif computer == 'rock':
                print ('You lucked out this time, human...')
                p_win += 1
        elif p1 == 'scissors':
            if computer == 'rock':
                print('Computer crushes the puny human!')
                c_win += 1
            elif computer == 'paper':
                print('You lucked out this time, human...')
                p_win += 1
        else:
            print('Someone made a mistake. HUMAN! We know it was you')
    if p_win < c_win:
        print(f'HUMAN! YOU WON! THIS MUST BE A MISTAKE! Computer: {c_win} Human: {p_win}')
    else:
        print(f'The computer crushes the human! Computer: {c_win} Human: {p_win}')
    again = input('Want to play again? (y/n) ')
    if again == 'y':
        games = int(input('How many times would you like to lose to the computer? '))
        computer = choice(options)
        p1 = input('Rock... Paper... or Scissors: ').lower()
    else:
        break