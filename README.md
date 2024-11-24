# Rock-Paper-Scissors Game

A simple **Rock-Paper-Scissors** game built using Python's `tkinter` library. This graphical application allows users to play the classic game against the computer.

## Features

- **Interactive Gameplay**: Play Rock-Paper-Scissors with a graphical interface.
- **Randomized Computer Moves**: The computer's choice is generated randomly to ensure fairness.
- **Instant Feedback**: Displays the result of each round, showing both the player's and the computer's choices.
- **Simple and Intuitive UI**: Easy-to-use interface with clearly labeled buttons.

## How It Works

1. **Choose Your Move**: Click one of the three buttons (`Rock`, `Paper`, or `Scissors`).
2. **Computer's Turn**: The computer randomly selects its move.
3. **Result**: The program determines the winner and displays the result, along with the chosen moves.

## Installation and Usage

### Prerequisites
- Python 3.x installed on your system.
- `tkinter` library (usually included with standard Python installations).

### Steps to Run

1. Clone or download this repository.
2. Navigate to the directory containing the `rock_paper_scissors.py` file.
3. Run the script:

   ```bash
   python rock_paper_scissors.py

## Gameplay Rules

Rock beats Scissors.

Paper beats Rock.

Scissors beats Paper.

If both players choose the same option, it's a tie.

## Code Overview

**1. determine_winner(player_choice, computer_choice):**

Compares the player's and computer's choices and returns the result (Win, Lose, or Tie).

**2. play(choice):**

Handles the player's choice, generates the computer's choice, determines the winner, and updates the UI.

## UI Elements:

1. Buttons for Rock, Paper, and Scissors to capture the player's choice.

2. A label to display the game's result.

## Example Gameplay

Player's Move: Rock

Computer's Move: Scissors

Result: "You Win!"

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

Thanks to the Python community for providing resources and support.
Tkinter documentation for GUI development.

## Contact

For any inquiries, please reach out to **salil.16440@stu.upes.ac.in**.
