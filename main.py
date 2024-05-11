from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # turns off the turtle animation (doesn't refresh screen)
# we do that so that the starting segments first go to their respective positions

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() # update screen once the whole snake has moved by 1 square
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    # considering the food is 10x10 px
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    # Using slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()








screen.exitonclick()