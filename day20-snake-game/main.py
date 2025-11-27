from turtle import Screen
from score import Score
from snake import Snake
from food import Food
import time

def move_up():
    snake.segments[0].setheading(90)

def move_down():
    snake.segments[0].setheading(270)

def move_left():
    snake.segments[0].setheading(180)

def move_right():
    snake.segments[0].setheading(0)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)
screen.update()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

game_over = False
snake = Snake()
food = Food()
score = Score()

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food.pellets.pos()) <= 20:
        food.pellets.ht()
        food.create_food()
        snake.spawn_segment()
        score.high_score.clear()
        score.update_score()

    for segment in range(len(snake.segments) - 1, 1, -1):
        snake_head_x = snake.segments[0].xcor()
        snake_head_y = snake.segments[0].ycor()
        width = screen.window_width() // 2
        height = screen.window_height() // 2

        if (snake.segments[0].distance(snake.segments[segment]) < 20 or snake_head_x <= - width or snake_head_x >= width
                or snake_head_y <= - height  or snake_head_y >= height):
            game_over = True

screen.exitonclick()