from idlelib.outwin import file_line_progs
from tkinter import *
import random

def next_turn(row,column):
    global player  #  global variable player

    if buttons[row][column]['text'] == "" and check_winner() is False:  #  move if button is empty and no one has won yet
        if player == players[0]:  #  if player is first player
            buttons[row][column]['text'] = player  #  mark player's spot on the selected button 

            if check_winner() is False:  #  if no one has won
                player = players[1]  #  next player's turn
                label.config(text=(player+" turn"))

            elif check_winner() is True:  #  if player wins
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":  #  else tie
                label.config(text=("tie!"))

        else:
            buttons[row][column]['text'] = player  #  if player is second player, mark their spot

            if check_winner() is False:  #  if no one has won
                player = players[0]  #  other player's turn
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:  #  if won, player wins
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":  #  if no one wins, and is a tie
                label.config(text=("Tie!"))

def check_winner():  #  function to check winner
    for row in range(3):  #  for row in range of grid (3)
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":  #  check rows for win
            buttons[row][0].config(fg="green")  #  turn all winning green
            buttons[row][1].config(fg="green")
            buttons[row][2].config(fg="green")
            return True

    for column in range(3):
      if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":  #  check columns for win 
            buttons[0][column].config(fg="green")  #  turn all winning green
            buttons[1][column].config(fg="green")
            buttons[2][column].config(fg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":  #  check diagonal for win 
        buttons[0][0].config(fg="green")  #  turn all winning green
        buttons[1][1].config(fg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":  #  check diagonal for win 
        buttons[0][2].config(fg="green")  #  turn all winning green
        buttons[1][1].config(fg="green")
        buttons[2][0].config(fg="green")
        return True

    elif empty_space() is False:  #  if no wins and no empty spaces = tie
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(fg='orange')  #  turn all tie orange
        return "Tie"

    else:
        return False

def empty_space():
    space = 9  #  start with 9 empty spaces

  #  count how many have text in them subtract them for total
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                space -=1
    if space == 0:  #  no spaces = false else true
        return False
    else:
        return True

def new_game():
    global player

    #  randomly choose player
    player = random.choice(["x","o"])

    #  update label to show who's turn
    label.config(text=player + " turn")

    #  reset all buttons
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0", fg= "black")

#   create  main window
window = Tk()
window.title("Tic Tac Toe")

#  list of players
players = ["x","o"]

#  player selected randomly
player = random.choice(["x","o"])

#  matrix to hold button references
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

#  label to show turn
label = Label(window, text= player + " turn", font=("Arial", 40))
label.pack(side="top")

#  reset button called new game command
reset_button = (Button(text="restart", font=('arial', 20), command= new_game))
reset_button.pack(side="top")

#  frame for grid of buttons
frame = Frame(window)
frame.pack()

#  create 3x3 grid for board
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Arial", 20),
                                      width=5,height=2, command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

#  start tkinter main loop
window.mainloop()
