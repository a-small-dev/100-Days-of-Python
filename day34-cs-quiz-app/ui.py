import tkinter as tk
import textwrap
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.score_label = tk.Label(text=f"Score: 0", pady=20, fg="White", bg=THEME_COLOR, font=("Arial", 14))
        self.score_label.grid(row=0, column=1)

        self.false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=self.false_img, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.false_button.grid(row=3, column=1)

        self.true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=self.true_img, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.true_button.grid(row=3, column=0)

        self.question_label = tk.Label(text="quiz", font=("Arial", 14, "italic"))
        self.question_label.grid(row=1, column=0, columnspan=2)

        self.get_question_text()

        self.window.mainloop()

    def get_question_text(self):
        self.question_label.configure(bg="White")
        self.canvas.configure(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_label.configure(text=textwrap.fill(q_text, 30))
            self.score_label.configure(text=f"Score: {self.quiz.score}")
        else:
            self.question_label.configure(text="You Reached the End!")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(background="green")
            self.question_label.configure(bg="green")
        else:
            self.canvas.configure(background="red")
            self.question_label.configure(bg="red")
        self.window.after(1000, self.get_question_text)
