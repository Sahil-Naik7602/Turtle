from turtle import Turtle, Screen, pencolor
import random

race_is_on = False
screen = Screen()
bet_color = screen.textinput(title="Who will win", prompt="which turtle u wanna bet upon? Enter colour(red/ green/ orange/ blue/ yellow/ black): ")
screen.setup(height=400,width=500)

player_color=["red", "green", "orange", "blue", "yellow", "black"]
y_coordinates = [-150, -100, -50, 0, 50, 100]
all_turtle = []

if bet_color:
    race_is_on = True
    screen.title("welcome to turtle race")
    for i in range(6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.penup()
            new_turtle.color(player_color[i])
            new_turtle.goto(-230,y_coordinates[i])
            all_turtle.append(new_turtle)

    


while race_is_on:
    for i in all_turtle:
        if i.xcor() > 230:
            race_is_on = False
            winning_color = i.pencolor()
            if winning_color == bet_color:
                print(f"You won the bet :) .{winning_color} is the winner ")
            elif bet_color == None:
                print(f"{winning_color} is the winner ")
            else:
                print(f"You lost the bet :( .{winning_color} is the winner ")
        i.speed(5)
        i.forward(random.randint(0,10))

    
screen.exitonclick()
