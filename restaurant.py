from tkinter import *

window = Tk()
window.title("Restaurant Order Management")
window.geometry("600x500")

title = Label(
    window,
    text="Restaurant Order Management",
    font=("Arial", 20, bold)
)
title.pack(pady=20)

fries = Label(window, text="FRIES MEAL ($2):", font=("Arial", 12))
fries.pack()

fries_entry = Entry(window)
fries_entry.pack()

lunch = Label(window, text="LUNCH MEAL ($2):", font="Arial", 12)
lunch.pack()

lunch_entry = Entry(window)
lunch_entry.pack()

burger = Label(window, text="BURGER MEAL ($3):", font=("Arial", 12))
burger.pack()

burger_entry = Entry(window)
burger_entry.pack()

pizza = Label(window, text="PIZZA MEAL ($4):", font=("Arial", 12))
pizza.pack()

pizza_entry = Entry(window)
pizza_entry.pack()

cheese = Label(window, text="CHEESE BURGER ($2.5):", font=("Arial", 12))
cheese.pack()

cheese_entry = Entry(window)
cheese_entry.pack()

drinks = Label(window, text="DRINKS ($1):", font=("Arial", 12))
drinks.pack()

drinks_entry = Entry(window)
drinks_entry.pack()

currency_label = Label(window, text="Currency:", font=("Arial", 12))
currency_label.pack(pady=10)

currency = StringVar()
currency.set("USD")

currency_menu = OptionMenu(window, currency, "USD", "INR")
currency_menu.pack()

def place_order():

    fries_amount = int(fries_entry.get())
    lunch_amount = int(lunch_entry.get())
    burger_amount = int(burger_entry.get())
    pizza_amount = int(pizza_entry.get())
    cheese_amount = int(cheese_entry.get())
    drinks_amount = int(drinks_entry.get())

    total = (
        fries_amount * 2 +
        lunch_amount * 2 +
        burger_amount * 3 +
        pizza_amount * 4 +
        cheese_amount * 2.5 +
        drinks_amount * 1
    )

    if currency.get() == "INR":
        total = total * 45
        result.config(text="Total: ℥" + str(total))
    else:
        result.config(text="Total: $" + str(total))

order_button = Button(
    window, 
    text="Place Order",
    font=("Arial", 15, "bold")
)
result.pack()

window.mainloop()