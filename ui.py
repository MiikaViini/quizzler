from tkinter import *
from quiz_brain import QuizBrain
from data import parameters
THEME_COLOR = "#375362"


class QuizIF:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = 0

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="jee",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.score_label = Label(text=f"Score: {self.score}", background=THEME_COLOR, font=("Arial", 15, "normal"), fg="white")
        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=lambda: self.check_answer("True"))
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=lambda: self.check_answer("False"))
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def check_answer(self, answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_background)

    def reset_background(self):
        self.canvas.config(bg="white")
        if self.quiz.question_number < parameters['amount']:
            self.get_next_question()
        else:
            self.game_over()

    def new_game(self):
        self.true_button.config(command=lambda: self.check_answer("True"))
        self.false_button.config(command=lambda: self.check_answer("False"))
        self.quiz.question_number = 0
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.get_next_question()

    def game_over(self):
        self.canvas.itemconfig(self.question_text, text=f"Game over, your final score is "
                                                        f"{self.score}/{parameters['amount']}. "
                                                        f"Press green to start new game, red to quit")

        self.true_button.config(command=self.new_game)
        self.false_button.config(command=quit)


