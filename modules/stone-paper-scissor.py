import random as r

data = ['stone','paper','scissor']

player1 = r.choice(data)
player2 = r.choice(data)
print(f'Player 1: {player1}')
print(f'Player 2: {player2}')

if player1==player2:
    print("Match Draw")
elif player1=='scissor' and player2=='paper':
    print("Player 1 wins")
elif player1=='paper' and player2=='stone':
     print("Player 1 wins")
elif player1=='stone' and player2=='scissor':
    print("Player 1 wins")
else:
    print("Player 2 wins")