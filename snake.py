from turtle import Turtle
positions=[(0,0), (-20,0), (-40,0)]
move_dist=20
up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snakes()
        self.head=self.turtles[0]

    def create_snakes(self):
        for pos in positions:
            self.add_segment(pos)
    
    def add_segment(self, position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.turtles.append(new_segment)
    
    def extend(self):
        self.add_segment(self.turtles[-1].position())
    
    def reset(self):
        for seg in self.turtles:
            seg.goto(1000,1000)
        self.turtles.clear()
        self.create_snakes()
        self.head=self.turtles[0]
    
    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
            self.move()
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)
            self.move()
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
            self.move()
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
            self.move()

    def move(self):
        for i in range(len(self.turtles)-1 ,0,-1):
            new_x=self.turtles[i-1].xcor()
            new_y=self.turtles[i-1].ycor()
            self.turtles[i].goto(new_x,new_y)
        self.turtles[0].fd(move_dist)
    
    # def increase_length(self):
    #     new_segment=Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     x_mid,y_mid=self.turtles[-2].xcor(),self.turtles[-2].ycor()
    #     x_tail,y_tail=self.turtles[-1].xcor(),self.turtles[-1].ycor()
    #     if x_tail==x_mid:
    #         y_dist=y_mid-y_tail
    #         y_cor=y_tail+y_dist
    #         new_segment.goto(x_tail,y_cor)
    #     else:
    #         x_dist=x_mid-x_tail
    #         x_cor=x_tail+x_dist
    #         new_segment.goto(x_cor,y_tail)

    #     self.turtles.append(new_segment)
