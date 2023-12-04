from tkinter import *

window = Tk()
window.title("Miles to Kms")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)





# entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# mile_text
mile_text = Label(text='Miles')
mile_text.grid(column=2, row=0)

text = Label(text="Is equal to")
text.grid(column=0, row=1)

def button_clicked():
    miles = entry.get()
    converted = int(int(miles) * 1.6)

    km_text = Label(text=converted)
    km_text.grid(column=1, row=1)


km = Label(text="Km")
km.grid(column=2, row=1 )

button = Button(text="Click", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
