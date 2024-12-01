import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        unescaped_q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {unescaped_q_text} (True/False): "

    def check_answer(self, user_answer: str) -> dict[str, bool]:
        feedback_message = ""
        feedback_value = False

        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            feedback_message += "You got it right!"
            feedback_value = True
        else:
            feedback_message += "That's wrong."

        return {
            'message': feedback_message + f"\nYour current score is: {self.score}/{self.question_number}\n",
            'value': feedback_value
        }
