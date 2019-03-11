from random import *

print("Rock\nPaper\nScissors!!!!!")
print("Player 1: what do you choose?")
p1 = input()
p1 = p1.lower()
# c1 = 'rock'
# c2 = 'paper'
# c3 = 'scissors'


print("NO CHEATING\n"*25)

print("Player 2: What do you choose?")
p2 = input()
p2 = p2.lower()

# Making the decision
if p1 == p2:
    print("Scratch!")
elif p1 == 'rock' and p2 == 'scissors':
    print("Player 1 wins!")
elif p1 == 'scissors' and p2 == 'paper':
    print("Player 1 wins!")
elif p1 == 'paper' and p2 == 'scissors':
    print('Player 2 wins!')
elif p1 == 'paper' and p2 == 'rock':
    print('Player 1 wins!')
elif p1 == 'rock' and p2 == 'paper':
    print('Player 2 wins!')
elif p1 == 'scissors' and p2 == 'rock':
    print('Player 2 wins!')
else:
    print('Something is wrong')