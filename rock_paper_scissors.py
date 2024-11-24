import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

# Function to generate a biased computer choice
def generate_computer_choice(player_choice):
    # Create a biased move selection
    bias = {
        "Rock": ["Scissors", "Paper", "Rock"],  # Rock beats Scissors; lesser ties
        "Paper": ["Rock", "Scissors", "Paper"],  # Paper beats Rock; lesser ties
        "Scissors": ["Paper", "Rock", "Scissors"]  # Scissors beats Paper; lesser ties
    }
    # Randomly pick from the biased list with a higher chance of being beaten
    return random.choice(bias[player_choice])

# Function to handle player's choice
def play(choice):
    global play_again_button  # Ensure the Play Again button can be managed

    # Generate a biased computer choice
    computer_choice = generate_computer_choice(choice)
    
    # Determine the winner
    result = determine_winner(choice, computer_choice)
    
    # Display the result
    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n\n{result}")
    
    # Enable the Play Again button
    play_again_button.config(state=tk.NORMAL)

# Function to reset the game state
def play_again():
    result_label.config(text="")  # Clear the result
    play_again_button.config(state=tk.DISABLED)  # Disable the Play Again button

# Set up the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x400")

# Title Label
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

# Instructions Label
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
instructions_label.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Rock Button
rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 14), width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

# Paper Button
paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 14), width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

# Scissors Button
scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 14), width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 16), fg="blue")
result_label.pack(pady=20)

# Play Again Button
play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 14), state=tk.DISABLED, command=play_again)
play_again_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
