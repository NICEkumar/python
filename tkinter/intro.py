from tkinter import *

window = Tk()
window.title("Intro to Tinker")
window.minsize(width=500, height=600)
window.config(padx=30, pady=30)
def button_clicked():
    data = text.get()
    label_1['text'] = data


label_1 = Label(text='This is an example', font=('Arial', 25, 'bold'))
label_1.config(pady=15, padx=15)
label_1.grid(column=0, row=0)

button = Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click", command=button_clicked)
button2.grid(column=2, row=0)

text = Entry(width=15)
text.grid(column=3, row=2)








window.mainloop()
