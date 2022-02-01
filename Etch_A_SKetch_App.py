from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_backward():
    tim.backward(10)

def move_forward():
    tim.forward(10)

def anti_clockwise():
    tim.right(5)
    
def clockwise():
    tim.left(5)

def clear_screen():
    screen.resetscreen()

    


screen.listen()
screen.onkey(anti_clockwise,"a")   #Since we are giving a function as an input to a method(i.e. already a function)
                                   # we will not give parenthesis to the input function
screen.onkeypress(move_backward,"s")
screen.onkey(clockwise,"d")
screen.onkeypress(clear_screen,"c")
screen.onkeypress(move_forward,"w")
screen.exitonclick()