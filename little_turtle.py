from turtle import Turtle

class LittleTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.color("white")
    
    def move_forward(self):
        self.forward(10)
    
    def move_backward(self):
        self.backward(10)
    
    def move_left(self):
        self.setposition(self.xcor() - 10, self.ycor())
    
    def move_right(self):
        self.setposition(self.xcor() + 10, self.ycor())

