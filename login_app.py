import tkinter as tk

window = tk.Tk()
window.title("Login App")
window.geometry("600x500")

name_label = tk.Label(window, text = "Full Name")
name_label.grid(row=0, column = 0, padx = 15, pady = 15)

name_entry = tk.Entry(window)
name_entry.grid(row = 0, column = 1, padx = 15, pady = 15)

email_label = tk.Label(window, text = "Email Id")
email_label.grid(row = 1, column = 1, padx = 15, pady = 15)

password_label = tk.Label(window, text = "Enter Password")
password_label.grid(row = 2, column = 0, padx = 15, pady = 15)

password_entry = tk.Entry(window, show="*")
password_entry.grid(row = 2, column = 1, padx = 15, pady = 15)

def create_account():
    name = name_entry.get()
    output.config(text = "Hey " + name + "\nCongratulations for your new account!")

button = tk.Button(window, text="Create Account", command=create_account)
button.grid(row = 4, column = 0, padx = 15, pady = 15)

window.mainloop()