from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.update()

screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # snake.move()

    # Detect collision with food.
    if snake.head.distance(food)<15:
        score.increase_score()
        food.refresh()
        snake.extend()
    
    # Detect collision with wall.
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()
    
    # Detect collision with tail
    for segment in snake.turtles[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()

screen.exitonclick()