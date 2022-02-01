import colorgram
from turtle import Turtle, Screen
import random
import turtle

color = colorgram.extract('image.jpg', 50)
turtle.colormode(255)
tim = Turtle()
tim.shape("circle")
tim.shapesize(0.5,0.5)

for j in range(10):
    for i in range(10):
        tim.color(random.choice(color).rgb)
        tim.stamp()
        tim.penup()
        tim.forward(20)
    tim.goto(0,20*(j+1))
tim.ht()
    
screen = Screen()                           
screen.exitonclick()   

