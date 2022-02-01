from turtle import Turtle,Screen
import random

timmy_the_turtle = Turtle()                 
timmy_the_turtle.shape("turtle")  
timmy_the_turtle.speed(5)  
timmy_the_turtle.pensize(5)
def random_colours():
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    return random.choice(colours)

def random_direction():
    face_direction = [0, 90, 180, 270]
    return random.choice(face_direction)


for i in range(200):
    timmy_the_turtle.left(random_direction())
    timmy_the_turtle.color(random_colours())
    timmy_the_turtle.forward(10)


    

    

screen = Screen()                           
screen.exitonclick()   