from random import *
options = ['rock', 'paper', 'scissors']

computer = choice(options)
# print(computer)

print("Rock\nPaper\nScissors!!!!!")
print("Player 1: what do you choose?")
p1 = input()
p1 = p1.lower()
# c1 = 'rock'
# c2 = 'paper'
# c3 = 'scissors'

# print("NO CHEATING\n"*25)

# print("Player 2: What do you choose?")
# computer = input()
# computer = computer.lower()

print(f"Computer plays: {computer}")

# Making the decision
if p1 == computer:
    print("Scratch!")
elif p1 == 'rock':
    if computer == 'paper':
        print('Computer Wins!')
    elif computer == 'scissors':
        print('Player wins!')
elif p1 == 'paper':
    if computer == 'scissors':
        print('Computer wins!')
    elif computer == 'rock':
        print ('Player wins!')
elif p1 == 'scissors':
    if computer == 'rock':
        print('Computer wins!')
    elif computer == 'paper':
        print('Player wins!')
else:
    print('Something is wrong here...')
# elif p1 == 'rock' and computer == 'scissors':
#     print("Player 1 wins!")
# elif p1 == 'scissors' and computer == 'paper':
#     print("Player 1 wins!")
# elif p1 == 'paper' and computer == 'scissors':
#     print('Player 2 wins!')
# elif p1 == 'paper' and computer == 'rock':
#     print('Player 1 wins!')
# elif p1 == 'rock' and computer == 'paper':
#     print('Player 2 wins!')
# elif p1 == 'scissors' and computer == 'rock':
#     print('Player 2 wins!')
# else:
#     print('Something is wrong')