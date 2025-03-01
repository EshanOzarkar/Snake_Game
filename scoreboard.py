from turtle import Turtle, Screen
alignment="center"
Font=("Courier", 16, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("day20_21\data.txt") as file:
            self.highscore=int(file.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,260)
        self.score_disp()
    
    def score_disp(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",align=alignment, font=Font)
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("day20_21\data.txt", "w") as file:
                file.write(str(self.score))
        self.score=0
        self.score_disp()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=alignment, font=Font)

    def increase_score(self):
        self.score+=1
        self.score_disp()