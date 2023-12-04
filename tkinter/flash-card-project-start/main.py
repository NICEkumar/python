import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
curr_word = {}


def flip_card():
    global curr_word
    canvas.itemconfig(card, image=cardBack)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=curr_word["English"], fill="white")


def change_word():
    global curr_word, timer
    window.after_cancel(timer)
    canvas.itemconfig(card, image=cardFront)
    curr_word = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=curr_word["French"], fill="black")
    timer = window.after(3000, flip_card)


def known():
    global curr_word
    to_learn.remove(curr_word)
    datas = pandas.DataFrame(to_learn)
    datas.to_csv("data/words_to_learn.csv", index=False)
    change_word()


def unknown():
    change_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

# importing images
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=cardFront)
title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=2)

# right and wrong buttons
rightButton = Button(image=right, highlightthickness=0, command=known)
rightButton.grid(column=0, row=1)

wrongButton = Button(image=wrong, highlightthickness=0, command=unknown)
wrongButton.grid(column=1, row=1)

change_word()

window.mainloop()
