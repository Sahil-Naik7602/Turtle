from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
turtle.colormode(255)

tim.speed("fastest")
tim.pensize(2)

def turtle_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple = (r, g, b)
    return tuple

def draw_spirograp(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(turtle_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograp(5)       
    

screen = Screen()
screen.exitonclick()