print('***********Welcome to Rock paper scissors amazing game***********')
print('rock, scissor, paper')


def whoWon(player1, player2):
    if player1 == player2:
        print('tie')
    else:
        if player1 == 'rock' and player2 == 'scissor':
            print('player1 won')
        elif player1 == 'rock' and player2 == 'paper':
            print('player2 won')
        elif player1 == 'scissor' and player2 == 'paper':
            print('player1 won')
        elif player1 == 'scissor' and player2 == 'rock':
            print('player2 won')
        elif player1 == 'paper' and player2 == 'rock':
            print('player2 won')
        elif player1 == 'paper' and player2 == 'scissor':
            print('player2 won')
        else:
            print('wrong choice')


res = 'y'


while res == 'y':
    player1 = input(' Please Enter player1: ').lower()
    player2 = input(' Please Enter player2: ').lower()
    whoWon(player1, player2)
    res = input('would you like to play again? y/n: ')
    if res =="y":
        print("let's play again...")
    else:
        print("thanks to play this game...")