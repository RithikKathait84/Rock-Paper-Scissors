import random

def gameWin(comp,you):
    if you==comp:
        print("Game draw")
    elif comp=="r":
        if you=="s":
            print("you lost")
        elif you =="p":
            print("you win")
    elif comp=="p":
        if you=="s":
            print("you win")
        elif you =="r":
            print("you lost")
    elif comp=="s":
        if you=="p":
            print("you lost")
        elif you =="r":
            print("you win")

print("Computer :  rock(r) paper(p)  scissor(s) ")
r=random.randint(1,3)
if r==1:
    comp="r"
elif r==2:
    comp ="p"
elif r==3:
    comp="s"
    
n=int(input("how many times you wants to play "))


for i in range(n):
    you=input("you :  rock(r) paper(p)  scissor(s) ")
    print(f"Computer choses {comp} and you choses {you}")
    gameWin(comp,you)
