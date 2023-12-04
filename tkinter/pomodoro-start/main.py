import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#22092C"
RED = "#BE3144"
ORANGE = "#F05941"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ''
timers = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global mark, reps
    window.after_cancel(timers)
    timer.config(text="Timer")
    canvas.itemconfig(timerText, text=f"00:00")
    mark = ''
    checkMark.config(text=mark)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", highlightthickness=0, bg=YELLOW, fg=ORANGE, font=(FONT_NAME, 55))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", highlightthickness=0, bg=YELLOW, fg=ORANGE, font=(FONT_NAME, 55))

    else:
        count_down(work_sec)
        timer.config(text="Work", highlightthickness=0, bg=YELLOW, fg=ORANGE, font=(FONT_NAME, 55))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global mark, timers
    sec = count % 60
    mins = count // 60
    if sec < 10:
        sec = f"0{sec}"
    if mins < 10:
        mins = f"0{mins}"
    canvas.itemconfig(timerText, text=f"{mins}:{sec}")
    if count > 0:
        timers = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if not reps % 2:
            mark += "✔️"
            checkMark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)


tomatoImg = PhotoImage(file='tomato.png')
# tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomatoImg)
timerText = canvas.create_text(100, 130, text="00:00", fill=BLACK, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Timer text
timer = Label(text="Timer", highlightthickness=0, bg=YELLOW, fg=RED, font=(FONT_NAME, 55))
timer.grid(column=1, row=0)

# buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

# check mark
checkMark = Label(highlightthickness=0, bg=YELLOW, fg=RED)
checkMark.grid(column=1, row=3)

window.mainloop()
