# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
# title for name of the project
root = Tk()
root.title('Digital Clock')


# This function is used to display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# clock background and foreground colour
# will look more attractive

lbl = Label(root, font=('Arial', 40, 'bold'),
            background='black',
            foreground='blue')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()