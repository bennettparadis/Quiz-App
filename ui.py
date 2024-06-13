from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    # add data type when calling a parameter--> require an object of the QuizBrain datatype
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: ", font=('Arial', 10, 'normal'), fg= 'white',bg= THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # canvas w/ question
        self.canvas = Canvas(width=300, height=250, bg= 'white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="text", fill=THEME_COLOR, font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true = Button(image= true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=2)
        false_img = PhotoImage(file='images/false.png')
        self.false = Button(image= false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    # method that taps into the quiz brain and gets the next question
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        # change canvas bg depending on user getting it right or wrong; set up a delay before getting the next question
        # can't use time, sleep module, method because mainloop is going on continuously
        self.window.after(1000, self.get_next_question)