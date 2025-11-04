# Pink Simple Calculator (Tkinter)

This folder contains a very simple, very pink calculator GUI built with Python’s built-in `tkinter` library. It supports basic arithmetic operations with a button-based interface.

## Files

- `simplecalculator.py` – main Tkinter calculator script.

## Features

- Number buttons `0–9`
- Basic operators: `+`, `-`, `*`, `/`
- Decimal point support
- `=` button to evaluate the expression
- `clear` button to reset the display
- Pink window background and display area

## What I Learned

- How to create a basic GUI window using `tkinter` (`Tk`, `Label`, `Button`, `Frame`).
- How to arrange widgets with the `grid` and `pack` geometry managers.
- How to update the display using `StringVar` and a shared `equation_text` variable.
- How to connect button clicks to functions with `command` and `lambda`.
- How to handle simple errors (like syntax errors and division by zero) with `try` / `except`.
- How to organize a small Python GUI project so it can be shared on GitHub.


## Requirements

- Python 3.x

`tkinter` is included with most standard Python installations.  
On some Linux systems, you may need to install it separately (for example: `sudo apt-get install python3-tk`).

## How to Run

From the root of this repository:

```bash
cd pink_simple_calculator
python simplecalculator.py

