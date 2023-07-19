import random

print("Lets play a game")
a = input ("Do you want to play rock paper scissors? (yes or no)").lower()

pc_list=["rock","paper","scissors"]
while a=="yes":
    pc=pc_list[random.randint(0,2)]
    you=input("choose one >> rock,paper or scissors").lower()
    if (pc=="rock" and you =="scissors") or (pc=="paper" and you=="rock") or  (pc=="scissors" and you=="paper"):
        s="pc_win"
    elif (you=="rock" and pc =="scissors") or (you=="paper" and pc=="rock") or  (you=="scissors" and pc=="paper"):
        s="you_win"
    elif (you=="rock" and pc=="rock") or (you=="paper" and pc=="paper") or (you=="scissors" and pc=="scissors"):
        s="draw"
    else:
        s="please enter a valid value"

    print(s)
    a = input ("Do you want to play rock paper scissors? (yes or no)").lower()
print("Game Over")





