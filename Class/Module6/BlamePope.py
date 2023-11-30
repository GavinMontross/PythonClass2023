date = input('Enter a date in the format of MM/DD/YYYY: ')
    # Turn date into list of integers
datelst = date.split('/')
for i in range(len(datelst)):
    datelst[i] = int(datelst[i])

def leapyearchecker():
    # Check if the year is a leap year
    if datelst[2] % 4 == 0 and (datelst[2] % 100 != 0 or datelst[2] % 400 == 0):
        return True
    else:
        return False

def validitycheck():
   # Check if the date is a valid date
    validity = True
    if datelst[0] == 2 and datelst[1] in range(1,29):
        validity = True
    elif datelst[0] in (2,4,6,9,11) and datelst[1] > 30:
        validity = False
    elif datelst[0] not in (2,4,6,9,11) and datelst[1] in range(1,31):
        validity = True
    elif leapyearchecker() == True and datelst[1] in range(0,30):
        validity = True
    else:
        validity = False

# Print results
    if validity == True:
        print(date)
        print('This date is valid')
    elif validity == False:
        print(date)
        print('This date is invalid')
validitycheck()
