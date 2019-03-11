from random import choice

going = 'good'

while going == 'good':
    options = ['rock', 'paper', 'scissors']
    computer = choice(options)
    # print(computer)

    print('"Echoing through the circuit boards:"')
    print('ROCK\nPAPER\nSCISSORS!!!!!\n\n')
    print('HUMAN: what element do you choose?')
    p1 = input()
    p1 = p1.lower()

    print(f'\n\nComputer selects: {computer.upper()}\n\n')

    # Making the decision
    if p1 == computer:
        print('WHAT?!?! A DRAW?!')
    elif p1 == 'rock':
        if computer == 'paper':
            print('Computer crushes the puny human!')
        elif computer == 'scissors':
            print('You lucked out this time, human...')
    elif p1 == 'paper':
        if computer == 'scissors':
            print('Computer crushes the puny human!')
        elif computer == 'rock':
            print ('You lucked out this time, human...')
    elif p1 == 'scissors':
        if computer == 'rock':
            print('Computer crushes the puny human!')
        elif computer == 'paper':
            print('You lucked out this time, human...')
    else:
        print('Someone made a mistake. HUMAN! We know it was you')

    print('\n' * 3)

    print('HUMAN, do you want to play again?\n')
    human = input()
    pick = human[0].lower()
    if pick == 'y' or pick == 's' or pick == 'o':
        print('\n*whispers from the dark terminal*\nBeware the wrath of a vengeful computer if you win...' + '\n' * 3)
        going = 'good'
    else:
        print('GOODBYE. DON\'T LET THE DOOR HIT YOU IN THE ASS, HUMAN!\n')
        going = 'no'