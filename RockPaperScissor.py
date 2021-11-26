import random
print("WELCOME TO THE GAME OF ROCK PAPER SCISSOR\n")
print("Index-> 1-Rock, 2-Paper, 3-Scissor\n")
x = int(input("Enter number between 1, 2 & 3: ")) #User input
y = random.randint(1,3) #input from computer
print("Computer choosed:", y)
if (x>=4 or x<=0):
    print("Input Invalid")
else:
    print("Input is valid")
    if(x==1 and y==1):
        print("Draw!!")
    if(x==1 and y==2):
        print("Computer won and you lost!! :(")
    if(x==1 and y==3):
        print("You won!! :)")
    if(x==2 and y==1):
        print("You won!! :)")
    if(x==2 and y==2):
        print("Draw!!")
    if(x==2 and y==3):
        print("Computer won and you lost!! :(")
    if(x==3 and y==1):
        print("Computer won and you lost!! :(")
    if(x==3 and y==2):
        print("You won!! :)")
    if(x==3 and y==3):
        print("Draw!!")
    