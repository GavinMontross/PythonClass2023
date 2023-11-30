import turtle 
from turtle import *
bob = turtle.Turtle()
wn = turtle.Screen()
bob.speed(0)
def top_half():
    print('|""""""""""|')
    for i in range(4,0,-1):
        print(' ', end = '')
        for j in range(4-i):
            print(' ', end = '')
        for j in range(1,2*i+2):
            if j == 1:
                print('\\', end = '')
            else:
                print(':', end = '')
        print('/')
    print('     ||')


def bottom_half():
    for i in range(0,4,1):
        print('', end = '')
        for j in range(4-i):
            print(' ', end = '')
        for j in range(1,2*i+4):
            if j == 1:
                print('/', end = '')
            else:
                print(':', end = '')
        print('\\')
    print('|""""""""""|')       


def slash_figure(n):
    for i in range(n,0,-1):
        print(' ', end = '')
        for j in range(n-i):
            print('\\'* 2, end = '')
        for j in range(2*i-1):
            print('!'*2, end = '')
        for j in range(n-i):
            print('/'*2, end = '')
        print()


def DrawNgon(bob, numSides, sideLength):
      bob.shape('turtle')
      for i in range(numSides):
            bob.fd(sideLength)
            bob.right(360/numSides)


def super_duper_spiral(bob, numSides, sideLength, numShapes):
    r = 0
    g = 0
    b = 0
    for i in range(numShapes):
        DrawNgon(bob,numSides, sideLength)
        bob.right(720/35)
        if r>(1-0.1):
            r = 0
        elif g>(1-0.1):
            g = 0
        elif b>(1-0.1):
            b = 0
        else:
            r+=0.01
            b+=0.02
            g+=0.03   
        bob.color(r,g,b)
    wn.exitonclick()

selection = int(input("Which function?: 1. Hourglass 2. Slash Figure 3. SuperSpiral: "))
if selection == 1:
    top_half()
    bottom_half()
elif selection == 2:
    n = int(input("How big do you want the slash figure to be?: "))
    slash_figure(n)
elif selection == 3:
    numSides = int(numinput('Sides', 'How many sides?'))
    sideLength = int(numinput('Side Length', 'How long is each side?: '))
    numShapes = int(numinput('Shapes', 'How many shapes?'))
    super_duper_spiral(bob, numSides, sideLength, numShapes)