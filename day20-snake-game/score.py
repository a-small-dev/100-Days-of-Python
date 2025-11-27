import turtle

class Score:
    def __init__(self):
        self.user_score = 0
        self.high_score = []
        self.create_score()

    def create_score(self):
        score = turtle.Turtle()
        score.color("white")
        score.ht()
        score.teleport(x = 0, y = 275)
        score.write(f"Score: {self.user_score}", move = False, align = "center", font = ("Times New Roman", 16, "normal"))
        self.high_score = score

    def update_score(self):
        self.user_score += 1
        self.create_score()
