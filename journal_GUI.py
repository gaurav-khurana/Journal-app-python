# GUI for journal code

import tkinter as tk
import datetime
from pathlib import Path

# App window
window = tk.Tk()
window.title("My Journal")
# window.geometry("400x400")

# Welcome msg
welcome = tk.Label(window, text="My Journal by Gaurav",
                   font=("Comic Sans MS", 30), fg="Blue")
welcome.pack()


# User name
username = tk.Label(window, text="Username - ",
                    font=("Calibri", 15), fg="Black")
username_entry = tk.Entry(window, width=15)
username.pack()
username_entry.pack()


# Password
password = tk.Label(window, text="Password - ",
                    font=("Calibri", 15), fg="Black")
password_entry = tk.Entry(window, width=15)
password.pack()
password_entry.pack()


# Click button, action & output
output = tk.Label(window, text="", font=("Courier", 15), fg="green")
output.pack()


def clicked():
    if password_entry.get() == "1234":
        output.configure(text="Access granted!!!" + username_entry.get())
    else:
        output.configure(
            text="Incorrect password. Access denied!!!" + username_entry.get())


submit_button = tk.Button(window, text="Submit", font=(
    "Calibri Bold", 10), fg="red", command=clicked)
submit_button.pack()


# entry in journal
journal_entry_label = tk.Label(
    window, text="Your journal entry - ", font=("Comic Sans MS", 15), fg="black")
journal_entry_label.pack()
journal_entry = tk.Text(window, width=40, height=20,
                        bg="light grey", fg="black")
journal_entry.pack()


def submit_entry():
    if journal_entry != "":
        output.configure(
            text="Your journal entry was Saved. Thank you " + username_entry.get())


entry_submit_button = tk.Button(window, text="Submit", font=(
    "Calibri Bold", 10), fg="red", command=submit_entry)
entry_submit_button.pack()


# Save entry in file - NOT WORKING
if password_entry.get() == "1234":
    path = Path("ecommerce/journal.txt")

    current_date_time = datetime.datetime.now()
    current_date_time_format = current_date_time.strftime(
        "%d/%m/%y %I:%M:%S %p")

    entry_save = f"{current_date_time_format} - {journal_entry}"
    with open("ecommerce/journal.txt") as file:
        path.write_text(entry_save)

window.mainloop()
