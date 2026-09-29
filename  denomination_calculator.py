from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")
root.title("Denomination Counter")

l = Label(root, text="Hey User! Welcome to Denomination Counter Application.")
btn = Button(root, text="Let's get started!", command=topwin)
def topwin():
    top = Toplevel()
    top.geometry("500x400")
    top.title("Denomination Calculator")

    label = Label(top, text="Enter total amount")
    label.pack(pady=20)

    amount_entry = Entry(top)
    amount_entry.pack()

    def calculate():
        try:
            amount = int(amount_entry.get())

            if amount < 0:
                raise ValueError

            messagebox.showinfo(
                "Alert",
                "Do you want to calculate the denomination count?"
            )

            notes_2000 = amount // 2000
            remaining = amount % 2000

            notes_500 = remaining // 500
            remaining = remaining % 500

            notes_100 = remaining // 100

            result_2000.delete(0, END)
            result_2000.insert(0, notes_2000)

            result_500.delete(0, END)
            result_500.insert(0, notes_500)

            result_100.delete(0, END)
            result_100.insert(0, notes_100) 

        except ValueError:
            messagebox.showerror(
                "Error"
                "Please enter a valid number"
            )
    btn = Button(top, text="Calculate", command=calculate)
    btn.pack(pady=20)

    result_label = Label(
        top, 
        text="Here are the number of notes for each denomination"
    )
    result_label.pack(pady=10)

    label_2000 = Label(top, text="2000")
    label_2000.pack()

    result_2000 = Entry(top)
    result_2000.pack()

    label_500 = Label(top, text="500")
    label_500.pack()

    result_500 = Entry(top)
    result_500.pack()

    label_100 = Label(top, text="100")
    label_100.pack()

    result_100 = Entry(top)
    result_100.pack()

l = Label(root, text = "This is a root window")
l.pack()

btn = Button(
    root, 
    text = "Click here to open another window",
    command=topwin
)
btn.pack()

root.mainloop()