# import another_module
# print(another_module.another_variable)
#
# # import turtle
# # timmy = turtle.Turtle()
# #(ORRR)
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight) #object.attribute
# my_screen.exitonclick() #object.method (this specific code ends when clicking on screen)

#pypi.org repo of soft developed and shared by the community
#Pretty Table ASCII table format
#Settings --> Project NAme --> Python Interpreter --> + sign --> search and install package
import prettytable

from prettytable import PrettyTable
table = PrettyTable() #Pascal casing

table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"
print(table)