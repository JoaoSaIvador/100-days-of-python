import random
import art

print("Welcome to a game of rock, paper, scissors")

# User input
player1 = input("What do you choose? 'Rock', 'Paper', or 'Scissors'\n").lower()
print(f"You chose {player1}!\n")
if player1 in ["rock", "paper", "scissors"]:
    print(getattr(art, player1[0]))
else:
    print("Invalid input, try again.")

# Computer response
options = ["rock", "paper", "scissors"]
cp = random.choice(options)
print(f"Computer chose {cp}!")
print(getattr(art, cp[0]))

# Determine winner
if player1 == cp:
    print("It's a draw...")
elif (player1 == "rock" and cp == "scissors") or \
        (player1 == "scissors" and cp == "paper") or \
        (player1 == "paper" and cp == "rock"):
    print("You win!")
else:
    print("You lose!")
