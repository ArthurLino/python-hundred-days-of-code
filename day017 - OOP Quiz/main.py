from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()
    print("-"*16)
