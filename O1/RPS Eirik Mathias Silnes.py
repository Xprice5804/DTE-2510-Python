import random
print('0 = rock, 1 = paper and 2 = scissors, please enter your choice')
player = int(input())
computer = random.randrange(0, 3)

if player == computer:
    print('DRAW')
#spiller velger stein
elif player == 0: 
    #hvis PC velger saks 
    if computer ==2: 
        print('Rock beats scissors, You won')
    else:
        print('Paper beats Rock, You lost')
#spiller velger papir
elif player == 1:
    #hvis PC velger stein
    if computer == 0:
        print('Paper beats rock, you won')
    else:
        print('Sicissors beat paper, you lost')
#spiller velger saks
elif player == 2:
    #hvis PC velger papir
    if computer == 1:
        print('Scissors beats paper, you won')
    else:
        print('Rock beats scissors, you lost')