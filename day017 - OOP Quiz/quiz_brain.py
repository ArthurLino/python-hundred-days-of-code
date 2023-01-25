class QuizBrain:

    def __init__(self, questions_list):
        self.user_score = 0
        self.question_number = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer.lower() or user_answer == current_answer[0:1].lower():
            print("You got it right! :)")
            self.user_score += 1
        else:
            print("That's wrong. :(")
            print(f"That was actually {current_answer.lower()}")

        if self.question_number == 12:
            print("You've completed the quiz!")
            print(f"Your final score is: {self.user_score}/{self.question_number}")
            return

        print(f"Your current score is: {self.user_score}/{self.question_number}")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1

        print(f"Question {self.question_number}: {current_question.text}")
        answer = input("True or False?: ").lower()
        self.check_answer(answer, current_question.answer)
