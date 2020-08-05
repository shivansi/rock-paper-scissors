import random

choices=['rock', 'paper', 'scissors']

computer=random.choice(choices)
#print(computer)

player=input("choose rock,paper,or scissors: \n")

print("player choice is: "+player)
#WHO WINS?!
if player==computer:
  print("tie")
else:
  if player =="rock":
    if computer=="paper":
      print("computer wins!")
    else:
      print("player wins!!")
  elif player=="paper":
    if computer=="scissors":
      print("computer wins!")
    else:
      print("player wins!!")
  else:
    if player=="scissors":
      if computer=="rock":
        print("computer wins!!")
      else:
        print("player wins!!!")


