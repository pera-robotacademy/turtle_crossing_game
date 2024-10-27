from turtle import Turtle, Screen
from little_turtle import LittleTurtle
from car import Car
import time

CAR_NUMBER = 40

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Little Turtle Crossing Game")
screen.listen()
screen.tracer(0)

little_turtle_1 = LittleTurtle()
screen.onkey(little_turtle_1.move_forward, "Up")
screen.onkey(little_turtle_1.move_backward, "Down")
screen.onkey(little_turtle_1.move_left, "Left")
screen.onkey(little_turtle_1.move_right, "Right")

car_list = []  
for car_number in range(CAR_NUMBER):
    car_list.append(Car())

screen.update()

game_is_on = True
while game_is_on:
    for car in car_list:
        car.move()
        if car.xcor() > 280 or car.xcor() < -280:
            car.reset_position(car.xcor())
        if little_turtle_1.distance(car) < 20:
            game_is_on = False
            game_over = Turtle()
            game_over.color("white")
            game_over.write("Game Over", align="center", font=("Courier", 30, "normal"))
            break
        if little_turtle_1.ycor() > 280:
            game_is_on = False
            game_over = Turtle()
            game_over.color("white")
            game_over.write("You Win", align="center", font=("Courier", 30, "normal"))
            break
    screen.update()
    time.sleep(0.1)
screen.exitonclick()