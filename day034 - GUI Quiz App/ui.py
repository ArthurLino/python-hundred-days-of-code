from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, brain: QuizBrain):
        self.brain = brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=24, pady=24, bg=THEME_COLOR)

        self.score_label = Label(text="SCORE: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text="Are you ready?", font=("Arial", 16), width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=48)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.brain.still_has_questions():
            self.score_label.config(text=f'SCORE: {self.brain.score}')
            self.canvas.itemconfig(self.question_text, text=self.brain.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of this quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        feedback = self.brain.check_answer("True")
        self.give_feedback(feedback)

    def false_pressed(self):
        feedback = self.brain.check_answer("False")
        self.give_feedback(feedback)

    def give_feedback(self, feedback_value):
        self.canvas.itemconfig(self.question_text, text=feedback_value['message'])
        if feedback_value['value']:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1500, func=self.get_next_question)
