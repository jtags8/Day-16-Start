import another_module
print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()
#(ORRR)
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkGreen")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) #object.attribute
my_screen.exitonclick() #object.method (this specific code ends when clicking on screen)