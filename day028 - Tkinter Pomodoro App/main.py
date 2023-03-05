import math
import time
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
window_timer = None


def reset_timer():
    global reps

    window.after_cancel(window_timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer")
    confirmation_label.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1

    if reps == 8:
        title_label.config(text="BREAK", fg=PINK)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{str(count_min).zfill(2)}:{str(count_sec).zfill(2)}")

    if count > 0:
        global window_timer
        window_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        confirmation_label.config(text=marks)


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=64, pady=80, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(pady=32, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(command=start_timer, text="Start", bg=YELLOW, font=(FONT_NAME, 16, "bold"), highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(command=reset_timer, text="Reset", bg=YELLOW, font=(FONT_NAME, 16, "bold"), highlightthickness=0)
reset_button.grid(row=2, column=2)

confirmation_label = Label(pady=32, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
confirmation_label.grid(row=3, column=1)

window.mainloop()
