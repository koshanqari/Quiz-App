from question_model import Question
from quiz_brain import QuizBrain
import requests
import ui



parameters = {
    "amount" : 10,
    "type" : "boolean"

}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
# print(response.json()["results"][1]["question"])
# print(response.json()["results"][1]["correct_answer"])

question_bank = []
for i in range(len(response.json()["results"])):
    question_text = response.json()["results"][i]["question"]
    question_answer = response.json()["results"][i]["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
window = ui.UI(quiz)



# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
