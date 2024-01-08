from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup de screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Init classes
scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Snake moves
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extends()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        scoreboard.reset_score()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.reset_score()
            snake.reset()

    # Save high scores
    if scoreboard.check_scores():
        scoreboard.reset()

# Prevent the screen close it
screen.exitonclick()
