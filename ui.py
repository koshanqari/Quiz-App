THEME_COLOR = "#375362"
from tkinter import *
from question_model import Question
# import quiz_brain as qb

class UI():
    def __init__(self, quiz):
        self.num = 1
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("My Quiz App")
        self.quiz = quiz #here we are importing this object so that we can use its attributes and its methods
        #we cant directly connect call attributes and mothods just by importing quiz brain into this, we have to make an object and then use that object

        #items on the screen
        self.score_l = Label(text="Score: 0/10")
        self.question_l = Label(text="Your question will be displayed here", wraplength=200)
        self.true_b = Button(text="True", command=self.true)
        self.next_b = Button(text=">>>", command=self.next)
        self.false_b = Button(text="False", command=self.false)
        self.score = 0

        #placing the items
        self.score_l.place(x=420, y=10)
        self.question_l.place(x=160, y=200)
        self.true_b.place(x=400, y=380)
        self.false_b.place(x=70, y=380)
        self.buttons_swipe()

        self.question()
        self.root.mainloop()

    def question(self):
        self.question_l.config(text=self.quiz.next_question())
        self.question_l.place_forget()
        self.question_l.place(x= 160, y=200)

    def buttons_swipe(self):
        print("button swipe")
        if self.num%2 == 0:
            print("if statemetn")
            self.true_b.place_forget()
            self.false_b.place_forget()
            self.next_b.place(x=250, y=380)
            pass
        else:
            print("else statement")
            self.true_b.place(x=400, y=380)
            self.false_b.place(x=70, y=380)
            self.next_b.place_forget()
            pass

        self.num +=1


    def true(self):
        self.question_l.config(text= self.quiz.check_answer("true"))
        self.question_l.place_forget()
        self.question_l.place(x= 230, y=200)
        self.buttons_swipe()
        self.score_l.config(text=f"Score:{self.quiz.score}/10")
        print(self.num)
        
        if self.num >= 20:
            Label(text=f"Your Final Score:{self.quiz.score}/10").place(x=220, y=70)
            self.true_b.place_forget()
            self.false_b.place_forget()
            self.next_b.place_forget()



    def false(self):
        self.question_l.config(text= self.quiz.check_answer("false"))
        self.question_l.place_forget()
        self.question_l.place(x= 230, y=200)
        self.buttons_swipe()
        self.score_l.config(text=f"Score:{self.quiz.score}/10")

        if self.num >= 20:
            Label(text=f"Your Final Score:{self.quiz.score}/10").place(x=220, y=70)
            self.true_b.place_forget()
            self.false_b.place_forget()
            self.next_b.place_forget()
        
    
    def next(self):
        print("next fxn")
        self.buttons_swipe()
        self.question()
        print(self.num)



