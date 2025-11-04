from enum import global_enum
from tkinter import *  #  using tkinter

def button_press(num):   #  function for button press with number as parameter
    global equation_text  #  variable that displays equation text 

    equation_text = equation_text + str(num)  #  text will display equation text + whatever numbers entered
    equation_label.set(equation_text)  #  set the equation label to the equation text 

def equals():  #  function for equals 
    global equation_text

    try:  #  error handling
        total = str(eval(equation_text))  #  total is the var string for equation text with eval (eval: evaluates the equation text)

        equation_label.set(total)  # set the label to the total

        equation_text = total  # equation text displayed is the total 

    except SyntaxError:  #  if syntax error
        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError: #  if try to divide by 0 (invalid)
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():  #  clear function
    global equation_text

    equation_label.set("")  #   set the equation_label to empty quotes

    equation_text = ""  #  set equation_text to empty quotes

window = Tk()  #  load window
window.title("Calculator Program")  #  title
window.geometry("500x500")  #  window size
window.configure(bg="pink")  #  configure background to pink :)

equation_text = ("")  #  declare equation_text to empty quotes

equation_label = StringVar()  #  declare equation_label to string variable

label = Label(window, textvariable=equation_label, font=("Arial", 25), bg="light pink", width=24, height=3)
label.pack()  # pack label to display equations

frame = Frame(window , bg="pink") 
frame.pack()  #  pack frame for buttons 

#button syntax: initialize button to Button function, put on frame, text = specific num, set height, width, and font, and command = appropriate function

button1 = Button(frame, text= 1, height=6, width =11, font=35, command = lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text= 2, height=6, width =11, font=35, command = lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text= 3, height=6, width =11, font=35, command = lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text= 4, height=6, width =11, font=35, command = lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text= 5, height=6, width =11, font=35, command = lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text= 6, height=6, width =11, font=35, command = lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text= 7, height=6, width =11, font=35, command = lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text= 8, height=6, width =11, font=35, command = lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text= 9, height=6, width =11, font=35, command = lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=6, width =11 , font=35, command = lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=6, width =11 , font=35, command = lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text = '-', height=6, width =11 , font=35, command = lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text = '*', height=6, width =11 , font=35, command = lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text = '/', height=6, width =11 , font=35, command = lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text = '=', height=6, width =11 , font=35, command = equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text = '.', height=6, width =11 , font=35, command = lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text = 'clear', height=6, width =15 , font=35, command = clear)
clear.pack()

window.mainloop()
