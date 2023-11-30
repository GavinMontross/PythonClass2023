import turtle
from turtle import *
screen = turtle.Screen()
n = int(numinput('Sides', 'Enter the number of sides: '))
bob = turtle.Turtle()
bob.pensize(5)
for i in range(n):
    bob.fd(75)
    bob.right(360/n)
screen.exitonclick()