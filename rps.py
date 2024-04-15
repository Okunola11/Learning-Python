# Rock Paper Scissors
import sys
import random
from enum import Enum


def rps(name="PlayerOne"):

    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3

        playerChoice = input(
            "\nPlease enter:\n 1 for Rock\n 2 for Paper\n 3 for Scissors\n\n")

        player = int(playerChoice)

        if player < 1 or player > 3:
            sys.exit("You must enter 1, 2 or 3")

        computerChoice = random.choice([1, 2, 3])

        computer = int(computerChoice)

        print(f"\n{name} chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Computer chose {str(RPS(computer)).replace('RPS.', '')}.")

        def determineWinner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1 and computer == 2:
                result = f"\n{name} wins 🎉"
                player_wins += 1
            elif player == 2 and computer == 3:
                result = f"\n{name} wins 🎉"
                player_wins += 1
            elif player == 3 and computer == 1:
                result = f"\n{name} wins 🎉"
                player_wins += 1
            elif player == computer:
                result = "\nDraw match! 😲"
            else:
                result = "\nComputer wins 🎉"
                computer_wins += 1
            return print(result)

        determineWinner(player, computer)

        nonlocal game_count
        game_count += 1
        print(f"\nGamecount: {game_count}")
        print(f"{name} has {player_wins} wins.")
        print(f"Computer has {computer_wins} wins.")

        while True:
            playagain = input("\nPlayagain?\nEnter Y for Yes\nQ to quit.\n")

            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("🎉🎉🎉🎉")
            print("Thank you for playing")
            sys.exit(f"Bye! {name} 👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    play_game = rps(args.name)
    play_game()
