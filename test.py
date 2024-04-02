from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw

#30 rows 25 columns

if __name__ == "__main__":
    root = Tk()

    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    canvas = Canvas(frame, bd=0)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    frame.pack(fill=BOTH,expand=1)

    img = Image.open('dog.jpeg').resize((500, 500))
    
    draw = ImageDraw.Draw(img)
    for i in range(1,25):
        draw.line((0,i*20, 500,i*20), fill=256)
    for i in range(1,25):
        draw.line((i*20,0 , i*20, 500), fill=256)
    img = ImageTk.PhotoImage(img)
    
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    def printcoords(event):
        count_x = 0
        count_y = 0
        
        for i in range(1,25):
            if event.x <= i*20:
                count_x+=1

            if event.y <= i*20:
                count_y+=1
                
        print(abs(count_y-25),abs(count_x-25))
                
        
    canvas.bind("<Button 1>",printcoords)
    root.attributes("-fullscreen", True)
    root.mainloop()
