import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.pensize(4)
exit = turtle.Screen()
def blue_circle():
    for i in range(60):
        bob.color('blue')
        bob.forward(6)
        bob.right(6)
    bob.up()
blue_circle()
def yellow_circle():
    bob.goto(70,-50)
    bob.color('yellow')
    for i in range(173):
        bob.down()
        bob.forward(2)
        bob.right(2)
    for i in range(5):
        bob.up()
        bob.forward(2)
        bob.right(2)
    for i in range(13):
        bob.down()
        bob.right(2)
        bob.fd(2)
yellow_circle()
def black_circle():
    bob.up()
    bob.color('black')
    bob.goto(150,0)
    bob.down()
    for i in range(125):
        bob.forward(2)
        bob.right(2)
    for i in range(4):
        bob.up()
        bob.forward(2)
        bob.right(2)
    for i in range(51):
        bob.down()
        bob.forward(2)
        bob.right(2)
black_circle()
def green_circle():
    bob.color('green')
    bob.up()
    bob.goto(220,-50)
    for i in range(160):
        bob.down()
        bob.forward(2)
        bob.right(2)
    for i in range(5):
        bob.up()
        bob.forward(2)
        bob.right(2)
    for i in range(15):
        bob.down()
        bob.forward(2)
        bob.right(2)
green_circle()
def red_circle():
    bob.up()
    bob.goto(280,0)
    bob.color('red')
    for i in range(126):
        bob.down()
        bob.forward(2)
        bob.right(2)
    for i in range(4):
        bob.up()
        bob.forward(2)
        bob.right(2)
    for i in range(50):
        bob.down()
        bob.forward(2)
        bob.right(2)
red_circle()
bob.hideturtle()
exit.exitonclick()