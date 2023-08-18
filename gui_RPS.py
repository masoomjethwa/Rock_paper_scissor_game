import random
from tkinter import *

# Create a list of possible moves
moves = ["rock", "paper", "scissors"]

# Create the main window
root = Tk()
root.title("Rock Paper Scissors")

# Create a frame for the user's move
user_frame = Frame(root)

# Create a label for the user's move
user_label = Label(user_frame, text="Your Move:")

# Create a button for each possible move for the user
rock_button = Button(user_frame, text="Rock", command=lambda: user_move("rock"))
paper_button = Button(user_frame, text="Paper", command=lambda: user_move("paper"))
scissors_button = Button(user_frame, text="Scissors", command=lambda: user_move("scissors"))

# Pack the widgets in the user frame
user_label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create a frame for the computer's move
computer_frame = Frame(root)

# Create a label for the computer's move
computer_label = Label(computer_frame, text="Computer's Move:")

# Create a label to display the computer's move
computer_move_label = Label(computer_frame, text="")

# Pack the widgets in the computer frame
computer_label.pack()
computer_move_label.pack()

# Create a function to get the user's move
def user_move(move):
  # Get the computer's move
  computer_move = moves[random.randint(0, 2)]

  # Compare the moves and determine the winner
  if move == computer_move:
    winner_label.config(text="It's a tie!")
  elif move == "rock":
    if computer_move == "scissors":
      winner_label.config(text="You win!")
    else:
      winner_label.config(text="Computer wins!")
  elif move == "paper":
    if computer_move == "rock":
      winner_label.config(text="You win!")
    else:
      winner_label.config(text="Computer wins!")
  elif move == "scissors":
    if computer_move == "paper":
      winner_label.config(text="You win!")
    else:
      winner_label.config(text="Computer wins!")

# Create a label to display the winner
winner_label = Label(root, text="")

# Pack the widgets in the main window
user_frame.pack()
computer_frame.pack()
winner_label.pack()

# Start the main loop
root.mainloop()
