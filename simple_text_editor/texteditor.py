import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# -------------------- FUNCTIONS --------------------

#   change text color using color picker function
def change_color():
    color = colorchooser.askcolor(title="Choose Color: ")
    text_area.config(fg=color[1])

#   change font family and size
def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))

#   create file, initially call "Untitled" and clear text area
def new_file():
    window.title("Untitled")
    text_area.delete("1.0", END)

#   open existing file and load existing contents
def open_file():
    #   ask user to open file, accept all types
    file = askopenfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"), ("Rich Text Documents", "*.rtf")])

    try:
        #   set title to file's title name
        window.title(os.path.basename(file.name))
        #   clear current text
        text_area.delete("1.0", END)

        #   open file object and read
        text_area.insert(1.0, file.read())

    except Exception:
        print("couldn't read file")

    finally:
        file.close()

#   save current contents of text area to file
def save_file():
    #   ask user where to save file and with what name
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt.", defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                                   ("Rich Text Documents", "*.rtf")])

    #   if user cancels, simply just return
    if file is None:
        return
    else:
        try:
            #   set window title to saved file name
            window.title(os.path.basename(file))
            #   open path in write mode
            file = open(file, "w")

            #   write everything in text area to file
            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()

#   cut selected text
def cut():
    text_area.event_generate("<<Cut>>")

#   copy selected text
def copy():
    text_area.event_generate("<<Copy>>")

#   paste selected text
def paste():
    text_area.event_generate("<<Paste>>")

#   about dialog
def about():
    showinfo("About this program:", "This program is developed in Python using tkinter by Dua :) ")

#   close main window and exit
def quit():
    window.destroy()

# -------------------- WINDOW SETUP --------------------

window = Tk()
window.title("Text Editor")
file = None     #   placeholder variable

#   center window on screen
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height/ 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

#   StringVar to hold font family
font_name = StringVar(window)
font_name.set("Arial")

#   StringVar to hold font size
font_size = StringVar(window)
font_size.set("25")

#   main text editing area
text_area = Text(window, font=(font_name.get(), font_size.get()))

#   scrollbar
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)    #   text widget into grid stretching to all sides
scroll_bar.pack(side=RIGHT, fill=Y)     #   put scrollbar to right and fill top to bottom (y)
text_area.config(yscrollcommand=scroll_bar.set) #   connect text area widget to scrollbar
scroll_bar.config(command=text_area.yview)  #   connect so it can scroll through the text

#   frame for color button, font, and size
frame = Frame(window)
frame.grid()

#   button to change text color
color_button = Button(frame, text="Color", command=change_color)
color_button.grid(row=0, column=0)

#   dropdown optionmenu for all font families
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

#   spinbox for font size
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# -------------------- MENUBAR --------------------

menu_bar = Menu(window)
window.config(menu=menu_bar)

#   file menu (new, open, save, exit)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

#   edit menu (edit, cut, copy, paste)
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

#   help menu (about)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

#   start tkinter even loop
window.mainloop()
