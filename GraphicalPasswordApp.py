import tkinter as tk
from tkinter import *
from tkinter import ttk

from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw

class GraphicalPasswordApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RegistrationPage, LoginPage, PasswordPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        label = tk.Label(frame, bg="white", text="GRAPHICAL PASSWORD AUTHENTICATION SYSTEM", font=("Arial", 30), pady=30)
        label.pack(pady=10,padx=10)

        canvas = tk.Canvas(frame, width=200, height=200)
        canvas.pack(pady=20)
        
        logo = Image.open('logo.png').resize((200, 200))

        logo = ImageTk.PhotoImage(logo)
        canvas.background = logo
        canvas.create_image(0, 0, anchor="nw", image=logo)

        button1 = tk.Button(frame, text="REGISTER NOW", width=20, height=2, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(RegistrationPage))
        button1.pack(pady=20)

        button2 = tk.Button(frame, text="LOGIN", width=20, height=2, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(LoginPage))
        button2.pack(pady=5)


class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button1 = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=20, anchor='w', padx=10)

        label = tk.Label(frame, bg="white", text="REGISTER NEW USER HERE", font=("Arial", 30), pady=30)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(frame, text = "USERNAME", bg="white")
        label2.pack()

        username = tk.Entry(frame, bd=2)
        username.pack(pady=5,ipadx=50, ipady=5)

        label3 = tk.Label(frame, text = "PASSWORD", bg="white")
        label3.pack()
        
        password = tk.Entry(frame, bd=2)
        password.pack(pady=5,ipadx=50, ipady=5)

        label4 = tk.Label(frame, text = "CONFIRM PASSWORD", bg="white")
        label4.pack()
        
        confirmpassword = tk.Entry(frame, bd=2)
        confirmpassword.pack(pady=5,ipadx=50, ipady=5)

        button2 = tk.Button(frame, text="SUBMIT", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(PasswordPage))
        button2.pack(pady=20, padx=10)


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button1 = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=20, anchor='w', padx=10)

        label = tk.Label(frame, bg="white", text="LOGIN HERE", font=("Arial", 30), pady=30)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(frame, text = "USERNAME", bg="white")
        label2.pack()

        username = tk.Entry(frame, bd=2)
        username.pack(pady=5,ipadx=50, ipady=5)

        label3 = tk.Label(frame, text = "PASSWORD", bg="white")
        label3.pack()
        
        password = tk.Entry(frame, bd=2)
        password.pack(pady=5,ipadx=50, ipady=5)

        button2 = tk.Button(frame, text="SUBMIT", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack(pady=20, padx=10)

                
class PasswordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(RegistrationPage))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('dog.jpeg').resize((500, 500))

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)

        
app = GraphicalPasswordApp()
app.title('Graphical Password Authentication System')
app.geometry('1600x800+0+0')
app.mainloop()
