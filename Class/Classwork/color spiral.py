import turtle
bob = turtle.Turtle()
bob.shape('turtle')
bob.speed(100)
bob.pensize(5)
exit = turtle.Screen()

colors = ['red', 'green', 'blue', 'purple', 'yellow', 'brown', 'pink']

jim = turtle.Turtle()
jim.shape('turtle')
jim.speed(100)
jim.pensize(1)

#for col in colors:
 #   jim.color(col)
  #  jim.forward(100)
   # jim.right(120)
colors = colors*30
distance = 20

for col in colors:
    bob.color(col)
    bob.forward(distance)
    bob.right(91)
    bob.fd(distance)
    bob.right(72)
    distance += 1
exit.exitonclick()