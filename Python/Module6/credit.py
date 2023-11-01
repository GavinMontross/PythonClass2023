num = (input("What is your card number?: "))
letters = 'abcdefghijklmnopqrstuvwxyz'

while True:
    for i in letters:
        if i in num:
            num = (input("What is your card number?: "))
        else: 
            continue
    break
    

#Convert numbers into a list
numlist = list(num)
for i in range(0,len(numlist)):
    numlist[i] = int(numlist[i])

#Luhn's Algorithm
luhnlist = []
total = 0
for i in numlist[-2::-2]:
    luhnlist.append(i*2)
for i in luhnlist:
    if i > 9:
        j = str(i)
        c = [int(x) for x in j]
        for h in c:
            total += h  
    else:
        total += i

for i in numlist[-1::-2]:
    total += i

#Find the type of card
def type():
    if len(numlist) == 15 and numlist[0] == 3:
        typeofcard = 'American Express'
    elif len(numlist) == 16 and numlist[0] == 5:
        typeofcard = 'MasterCard'
    elif numlist[0] == 4:
        typeofcard = 'VISA'
    else:
        False
    print(typeofcard)

if total%10 == 0:
    print('Number:',num)
    type()
else:
    print('Number:', num)
    print('INVALID')


#Use This Number For Demo: 4003600000000014
