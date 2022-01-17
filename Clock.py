# programming a clock showing on screen as a widget when running code

from tkinter import *
from tkinter.ttk import *
from time import strftime

from tkinter import *

# tkinter window
root = Tk()
root.title("Clock")

# widget appearance
label = Label(root, font=('Times New Roman', 50, 'bold'), background='black', foreground='lime')


# if this section is commented then widget frame size is automatically adapted
# root.geometry("450x300")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


# placing widget at center of screen
label.pack(anchor=CENTER)

time()

root.mainloop()
