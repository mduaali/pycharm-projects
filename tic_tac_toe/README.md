# Tic Tac Toe (Tkinter)

A simple 2-player Tic Tac Toe game built with Python’s `tkinter`.  
Two players (“x” and “o”) take turns clicking buttons on a 3×3 grid.  
The game highlights the winning line and detects ties.

## Files

- `tictactoe.py` – main Tkinter app.

## Features

- 3×3 button grid for the board.
- Two players: `"x"` and `"o"`.
- Random starting player each game.
- Turn indicator label at the top.
- Win detection for:
  - All rows
  - All columns
  - Both diagonals
- Winning line is highlighted (text turns green).
- Tie detection when the board is full without a winner (text turns orange).
- “Restart” button to start a new game and reset the board.

## What I Learned
- How to build a basic GUI using tkinter (Tk, Label, Button, Frame).
- How to use a 2D list (buttons[row][column]) to represent a 3×3 game board.
- How to use grid(row, column=...) to arrange widgets in a grid layout.
- How to pass coordinates into a button callback with lambda row=row, column=column: next_turn(row, column).
- How to manage and update global state (player, buttons) inside callback functions.
- How to implement Tic Tac Toe game logic:
- Checking rows, columns, and diagonals for a win.
- Detecting when the board is full to decide a tie.
- How to visually indicate game results using config(fg=...) to change text color.
- How to reset the UI and game state for a new game (clearing text and restoring colors).

## How to Run

From the root of this project:

```bash
python tictactoe.py
