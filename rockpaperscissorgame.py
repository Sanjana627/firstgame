import random
def line():
    print("===============")

print('Rock-Paper-scissors\n')
z=0
while z==0:
    y=random.choice(['Rock','Paper','Scissors'])
    x=str(input('Input: '))
    print('computer: ',y)

    if x=='Rock' or x=='rock' or x=='1':
        if y=='Scissors': print('Output:you won')
        elif y=='Paper' : print('Output:you lost')
    else: print('Output:Stalemate')
    line()

    elif x =='Paper' or x =='paper' or x =='2':
        if y=='Rock': print('Output:you won')
        elif y=='Scissors': print('Output:you lost')
    else:print('Output:Stalemate')
    line()

    elif x=='Scissors' or x=='scissors' or x=='3':
        if y=='Paper': print('Output:you won')
        elif y=='Rock': print('Output:you lost')
    else:print('Output:Stalemate')
    line()

