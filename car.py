from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.penup()
        self.color("white")
        random_x = random.randint(-280, 280)
        self.goto(random_x, random.randint(-250, 250))
        if random_x < 0:
            self.setheading(0)
        else:
            self.setheading(180)

    def move(self):
        speed = random.randint(5,10)
        self.forward(speed)
    
    def reset_position(self, current_x):
        if current_x <= -280:
            self.goto(280, self.ycor())
        elif current_x >= 280:
            self.goto(-280, self.ycor())

