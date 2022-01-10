import html
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = -1
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number].text
        unescaped_question = html.unescape(self.current_question)
        self.question_number += 1  
        # user_answer = input(f"Q.{self.question_number}: {unescaped_question} (True/False): ")
        # self.check_answer(user_answer)
        return f"Q.{self.question_number +1}: {unescaped_question}"

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number].answer

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return "You got it right!"
        else:
            return "That's wrong."

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
