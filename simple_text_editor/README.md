# Simple Tkinter Text Editor

A basic GUI text editor built with Python’s `tkinter`.  
Supports opening, editing, and saving text files, plus changing font and text color.

## Files

- `texteditor.py` – main Tkinter app.

## Features

- New file (clears the editor and resets the window title).
- Open `.txt` and other text-like files.
- Save current text to a chosen file.
- Cut / Copy / Paste using the Edit menu.
- Change text color with a color picker.
- Change font family (via dropdown).
- Change font size (via spinbox).
- Vertical scrollbar synced with the text area.
- Menu bar with File, Edit, and Help → About.

## What I Learned
- How to build a GUI window and widgets using tkinter (Tk, Text, Button, Frame, Menu).
- How to center a window on the screen using screen width/height and geometry.
- How to connect menu items and buttons to functions via the command parameter.
- How to use the Text widget for multi-line input and control it with indices like "1.0" and END.
- How to wire up a Scrollbar to a Text widget using yscrollcommand and command.
- How to use askopenfile and asksaveasfilename to open and save files via dialogs.
- How to use StringVar to change fonts dynamically from an OptionMenu and Spinbox.
- How to trigger built-in cut/copy/paste behavior with event_generate("<<Cut>>"), etc.
- How to show a simple message box with showinfo for an About dialog.

## How to Run

From the root of your repo:

```bash
cd simple_text_editor
python texteditor.py
