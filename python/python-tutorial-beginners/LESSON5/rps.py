import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
player_choice = input("Enter ...\n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 | player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer_choice = random.choice("123")

computer = int(computer_choice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.","") + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.","") + ".")
print("")

if player == 1 and computer == 3:
    print("You win!!  Rock beats scissors!")
elif player == 2 and computer == 1:
    print("You win!!  Paper beats rock!!")
elif player == 3 and computer == 2:
    print("You win!!  Scissors beats paper!!")
elif player == computer:
    print("TIE. You each chose the same thing!")
else:
    print("Python wins!  :(")





