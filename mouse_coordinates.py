from tkinter import *

root = Tk()
root.geometry("200x200")

def click(event):
    print("x =", event.x, "y =", event.y)

root.bind("<Button-1>, click")

root.mainloop()