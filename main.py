from tkinter import *
from tkinter.ttk import *

master = Tk()
master.title('Graphical Password Authentication System')
master.attributes("-fullscreen", True)

def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title('Graphical Password Authentication System')
    newWindow.attributes("200x200")
    Label(newWindow,text ="This is a new window").pack()


label = Label(master, text ="This is the main window")
label.pack(pady = 10)

btn = Button(master,text ="Click to open a new window",command = openNewWindow)
btn.pack(pady = 10)
mainloop()
