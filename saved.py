class PasswordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        label = tk.Label(frame, bg="white", text="Graphical Password Authentication System", font=("Arial", 30), pady=30)
        label.pack(pady=10,padx=10)

        def printcoords(event):
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            print(abs(count_y-25),abs(count_x-25))

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('dog.jpeg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
