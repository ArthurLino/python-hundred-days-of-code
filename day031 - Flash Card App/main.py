import pandas

from tkinter import *
from random import choice
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"


def remove_word():
    words_to_learn.remove(current_word)
    data = pandas.DataFrame(words_to_learn, columns=["French", "English"])
    data.to_csv("./data/words_to_learn.csv", index=False)

    get_new_card()


def get_new_card():
    global timer, current_word
    window.after_cancel(timer)
    current_word = choice(words_to_learn)

    card_canvas.itemconfig(card_image, image=card_front_image)
    card_canvas.itemconfig(card_lang, text="French", fill="#000")
    card_canvas.itemconfig(card_word, text=current_word["French"], fill="#000")

    timer = window.after(3000, flip_card)


def flip_card():
    card_canvas.itemconfig(card_image, image=card_back_image)
    card_canvas.itemconfig(card_lang, text="English", fill="#fff")
    card_canvas.itemconfig(card_word, text=current_word["English"], fill="#fff")


try:
    words_to_learn = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_to_learn = pandas.read_csv("./data/french_words.csv")
    words_to_learn = words_to_learn.to_dict(orient="records")
else:
    words_to_learn = words_to_learn.to_dict(orient="records")

window = Tk()
window.title("Flash Card App")
window.config(padx=48, pady=48, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
icon_correct = PhotoImage(file="./images/right.png")
icon_wrong = PhotoImage(file="./images/wrong.png")

card_canvas = Canvas(width=800, height=526)
card_image = card_canvas.create_image(800/2, 526/2, image=card_front_image)
card_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.grid(column=0, row=0, columnspan=2, padx=24, pady=24)

card_lang = card_canvas.create_text(400, 150, text="", font=("Arial", 32))
card_word = card_canvas.create_text(400, 253, text="", font=("Arial", 64, "bold"))

wrong_answer_button = Button(command=get_new_card, image=icon_wrong, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR)
wrong_answer_button.grid(column=0, row=1)

right_answer_button = Button(command=remove_word, image=icon_correct, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR)
right_answer_button.grid(column=1, row=1)

get_new_card()

window.mainloop()
