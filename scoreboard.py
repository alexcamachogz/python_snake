from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_high_score()
        self.update_scoreboard()

    def update_high_score(self):
        with open("data.txt", "r") as board:
            self.high_score = int(board.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.check_scores():
            with open("data.txt", "w") as board:
                board.write(str(self.score))
            self.update_high_score()
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def check_scores(self):
        return self.score > self.high_score
