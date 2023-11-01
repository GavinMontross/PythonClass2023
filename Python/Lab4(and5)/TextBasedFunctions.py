def squares(num_squares):
    total = 0
    for i in range(1,num_squares+1):
        total += i**2
    print('The sum of all the squares of', num_squares, 'is',total)

def table(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
           print(i * j, end="\t")
        print()

def bottles_of_beer(bottles):
    for i in range(bottles, 0, -1):
        print(bottles, ' bottles of beer on the wall, ', bottles, ' bottles of beer,', sep= '')
        bottles -= 1
        print('Take one down, pass it around, ', bottles, 'bottles of beer on the wall')

global selection
selection = input("Which function do you want to use?: 1.) Summation of squares   2.) Multiplication Table   3.) Bottles of Beer ")
if selection == '1':
    num_squares = int(input("What number do you need the summation for?: "))
    squares(num_squares)
elif selection =='2':
    num = int(input("What number do you need a multiplication table for?: "))
    table(num) 
elif selection == '3':
    bottles = int(input("How many bottles of beer on the wall?: "))
    bottles_of_beer(bottles)