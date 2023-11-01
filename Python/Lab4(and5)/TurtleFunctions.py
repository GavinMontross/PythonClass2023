import turtle
from turtle import *
exit = turtle.Screen()

def DrawSquare(myTurtle, square_size):
      myTurtle.shape('turtle')
      for i in range(4):
                myTurtle.fd(square_size)
                myTurtle.right(90)       


def DrawRow(myTurtle, length, square_size):
      myTurtle.shape('turtle')
      for i in range(length):
            DrawSquare(myTurtle, square_size)
            myTurtle.fd(square_size)


def DrawStairs(myTurtle, height, square_size):
    myTurtle.shape('turtle')
    for i in range(height):
          DrawRow(myTurtle, length-i, square_size)
          myTurtle.penup()
          myTurtle.bk(square_size*(length-i))
          myTurtle.left(90)
          myTurtle.fd(square_size)
          myTurtle.right(90)
          myTurtle.down()

def DrawGrid(myTurtle, size, square_size):
    myTurtle.shape('turtle')
    for i in range(size):
        DrawRow(myTurtle, length, square_size)
        myTurtle.penup()
        myTurtle.bk(square_size*length)
        myTurtle.left(90)
        myTurtle.fd(square_size)
        myTurtle.right(90)
        myTurtle.down()

def DrawNgon(myTurtle, numSides, sideLength):
      myTurtle.shape('turtle')
      for i in range(numSides):
            myTurtle.fd(sideLength)
            myTurtle.right(360/numSides)

def DrawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
      for i in range(numShapes):
            DrawNgon(myTurtle, numSides, sideLength)
            myTurtle.right(720/35)
global selection
selection = input('What function do you want to use? 1.) DrawSquare, 2.) DrawRow, 3.) DrawGrid, 4.) DrawStairs, 5.)DrawNgon, or 6.) DrawNgonSpiral: ')
if selection == '1':
      square_size = int(numinput('Sides',"How big is the square?: "))
      myTurtle = turtle.Turtle()
      myTurtle.speed(0)
      DrawSquare(myTurtle, square_size)
      exit.exitonclick()
elif selection == '2':
      myTurtle = turtle.Turtle()
      myTurtle.speed(0)
      length = int(numinput('Length', 'How many squares long is the row?'))
      square_size = int(numinput('Sides',"How big is each square?: "))
      DrawRow(myTurtle, length, square_size)
      exit.exitonclick()
elif selection == '3':
      myTurtle = turtle.Turtle()
      myTurtle.speed(0)
      length = int(numinput('Length', 'How many squares long is each row?'))
      size = int(numinput('Grid','How big should the grid be?: '))
      square_size = int(numinput('Sides',"How big is each square?: "))
      DrawGrid(myTurtle, size, square_size)
      myTurtle.hideturtle()
      exit.exitonclick()
elif selection == '4':
      myTurtle = turtle.Turtle()
      myTurtle.speed(0)
      height = int(numinput('Height','How tall are the stairs?: '))
      length = height
      square_size = int(numinput('Sides',"How big is each square?: "))
      DrawStairs(myTurtle, height, square_size)
      exit.exitonclick()
elif selection == '5':
      myTurtle = turtle.Turtle()
      myTurtle.speed(0)
      numSides = int(numinput('Sides','How many sides?: '))
      sideLength = int(numinput('Length','How long is each side?: '))
      DrawNgon(myTurtle, numSides, sideLength)
      exit.exitonclick()
elif selection == '6':
      myTurtle = turtle.Turtle()
      myTurtle.speed(0)
      numSides = int(numinput('Sides','How many sides?: '))
      sideLength = int(numinput('Length','How long is each side?: '))
      numShapes = int(numinput('Shapes','How many shapes?: '))
      DrawNgonSpiral(myTurtle, numSides, sideLength, numShapes)
      exit.exitonclick()