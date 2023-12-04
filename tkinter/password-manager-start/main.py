import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    newPassword = ''
    text = '1234567890qwertyuiopasdfghjklzxcvbnm-_/!@#$%^&*~<>?'
    for i in range(15):
        pos = random.randint(0, len(text) - 1)
        newPassword += text[pos]
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, newPassword)
    pyperclip.copy(newPassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Error", message="Dont leave the field empty!!")
    else:
        try:
            with open("data.json", 'r') as datafile:
                data = json.load(datafile)
        except FileNotFoundError:
            with open("data.json", 'w') as datafile:
                json.dump(new_data, datafile, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as datafile:
                json.dump(data, datafile, indent=4)
        finally:
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #

def search():
    website = websiteEntry.get()
    try:
        with open("data.json", 'r') as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data available!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[ website]["password"]
            messagebox.showerror(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Error", message="Website not found!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

lockImg = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lockImg)
canvas.grid(column=1, row=0)

# website name
websiteText = Label(text="Website:")
websiteText.grid(column=0, row=1)
websiteEntry = Entry(width=18)
websiteEntry.focus()
websiteEntry.grid(column=1, row=1)

# email info
emailText = Label(text="Email/Username:")
emailText.grid(column=0, row=2)
emailEntry = Entry(width=35)
emailEntry.insert(0, "abhi@gmail.com")
emailEntry.grid(column=1, columnspan=2, row=2)

# Password
passwordText = Label(text="Password:")
passwordText.grid(column=0, row=3)
passwordEntry = Entry(width=18)
passwordEntry.grid(column=1, row=3)
passwordButton = Button(text="Generate", command=generate_password, width=12)
passwordButton.grid(column=2, row=3)

# add
addButton = Button(text='Add', width=33, command=add)
addButton.grid(columnspan=2, column=1, row=4)

search
searchButton = Button(text="Search", command=search, width=12)
searchButton.grid(column=2, row=1)
window.mainloop()
