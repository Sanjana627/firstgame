import random
number=random.randint(1,100)
guess=0
count=0
while guess!=number and guess!="exit":
    guess=int(input("whts your guess man?\n"))
    if guess=="exit":
        break
        guess=int(guess)
        count+=1
    if guess<number:
        print("too low!")
    elif guess>number:
        print("too high!")
    else:
        print("you got it!")
        print("and it only took you",count,"tries!")