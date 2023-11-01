time = int(input("How many seconds?: "))
hours = (time//3600)
minutes = ((time % 3600) //60)
seconds = (time % 60)

print(time,'seconds =', hours,'hours,' , minutes, 'minutes, and', seconds, 'seconds.')