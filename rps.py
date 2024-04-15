# Rock Paper Scissors
import random

playerChoice = input(
    "Please enter:\n 1 for Rock\n 2 for Paper\n 3 for Scissors\n")

computerChoice = random.choice([1, 2, 3])
print(computerChoice)

player = int(playerChoice)
computer = int(computerChoice)
print(computer)

if player == 1 and computer == 2:
    print("Player 1 wins 🎉")
elif player == 2 and computer == 3:
    print("Player 1 wins 🎉")
elif player == 3 and computer == 1:
    print("Player 1 wins 🎉")
elif player == computer:
    print("Draw match! 😲")
else:
    print("Computer wins 🎉")
