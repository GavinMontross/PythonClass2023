import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    irma_setup()
    # your code to animate Irma here
    data = open("data/irma.csv","r")

#Get all latitudes into a list
    latlst = []
    for line in data:
        values = line.split(",")
        latlst.append(values[2])
    latlst.pop(0)
    for i in range(len(latlst)):
        latlst[i] = float(latlst[i])

    data = open("data/irma.csv","r")

#Get all longitudes in a list
    longlst = []
    for line in data:
        values = line.split(",")
        longlst.append(values[3])
    longlst.pop(0)
    for i in range(len(longlst)):
        longlst[i] = float(longlst[i])
    data = open("data/irma.csv","r")

    WindNums = []
    for line in data:
        value = line.split(',')
        WindNums.append(value[4])
    WindNums.pop(0)
    for i in range(len(WindNums)):
        WindNums[i] = int(WindNums[i])

#Change colors
    def GetColors(i, data):
        
        if (data[i]) < 74:
            category = ''
            pensize = 1
            color = 'white'
        elif (data[i]) in range(74,96):
            category = '1'
            pensize = 3
            color = 'blue'
        elif (data[i]) in range(96,111):
            category = '2'
            pensize = 5
            color = 'green'
        elif (data[i]) in range(111,130):
            category = '3'
            pensize = 7
            color = 'yellow'
        elif (data[i]) in range(130,157):
            category = '4'
            pensize = 9
            color = 'orange'
        elif (data[i]) >= 157:
            category = '5'
            pensize = 11
            color = 'red'
        return color, category, pensize 
    
  

#Move the Turtle
    t.penup()
    t.goto(longlst[0],latlst[0])
    t.down()
    for i in range(len(latlst)):
        color, category, pensize = GetColors(i, WindNums)
        t.down()
        t.color(color)
        t.pensize(pensize)
        t.write(category)
        t.goto(longlst[i],latlst[i])


if __name__ == "__main__":
    irma()
