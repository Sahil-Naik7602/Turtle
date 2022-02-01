from turtle import Turtle,Screen
import random

timmy_the_turtle = Turtle()                 
timmy_the_turtle.shape("turtle")  
timmy_the_turtle.speed(1)  
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


no_of_sides =9                #int(input("Enter the number of sides of last shape: "))
n=3
while n <= no_of_sides:
    
    timmy_the_turtle.color(random.choice(colours))
    for i in range(n):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360/n)
    n += 1

screen = Screen()                           
screen.exitonclick()   