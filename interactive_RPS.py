import random

# Create a list of possible moves
moves = ["rock", "paper", "scissors"]

# Get the user's move
user_move = input("Choose rock, paper, or scissors: ")

# Generate a random move for the computer
computer_move = moves[random.randint(0, 2)]

# Compare the moves and determine the winner
if user_move == computer_move:
  print("It's a tie!")
elif user_move == "rock":
  if computer_move == "scissors":
    print("You win!")
  else:
    print("Computer wins!")
elif user_move == "paper":
  if computer_move == "rock":
    print("You win!")
  else:
    print("Computer wins!")
elif user_move == "scissors":
  if computer_move == "paper":
    print("You win!")
  else:
    print("Computer wins!")
