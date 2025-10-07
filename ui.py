from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125,
                                                width = 280,
                                                text="Demo Question Text",
                                                font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0 , columnspan=2, padx=20, pady=20)

        # Scorer Label
        self.score_label = Label(text=f"Score : 0",
                                 bg=THEME_COLOR, fg="white",
                                 font=("Arial", 15, "normal"))
        self.score_label.grid(row=0, column=1)

        # True Button
        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, command=self.true_btn,
                               highlightthickness=0, bg=THEME_COLOR)
        self.true_btn.grid(row=2, column= 0, pady=20)
        # False Button
        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, command=self.false_btn,
                                highlightthickness=0, bg=THEME_COLOR)
        self.false_btn.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="You've Completed the Quiz.\n"
                                                       f"Your Score is '{self.quiz.score}/10' ")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_btn(self):
        self.feed_back(is_right = self.quiz.check_answer("True"))

    def false_btn(self):
        self.feed_back(is_right = self.quiz.check_answer("False"))

    def feed_back(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(250, func=self.get_next_question)
