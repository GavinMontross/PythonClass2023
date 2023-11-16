import random

def japanize(date):
    datelst = date.split('/')
    year = datelst[2]
    day = datelst[1]
    month = datelst[0]
    return year + '/' + month + '/' + day

def evenWords(list):
    count = 0
    for word in list:
        if len(word) % 2 == 0:
            count += 1
    return count

def sumOfLargests(listOfLists):
    sum = 0
    for list in listOfLists:
        sum += max(list)
    return sum

def mostCommonWord(text):
    d = {}
    wordlst = text.split(' ')
    for c in wordlst:
        if c not in d:
            d[c] = 0
        d[c] += 1
    ks = d.keys()
    key_with_max_value = list(ks)[0]

    for i in ks:
        if d[i] > d[key_with_max_value]:
            key_with_max_value = i
    return key_with_max_value

def nonFoodSum(file):
    data = open(file, 'r')
    sum = 0
    typelst = []
    pricelst = []
    for line in data:
        values = line.split(',')
        typelst.append(values[0])
        pricelst.append(values[2])
    for num in range(len(pricelst)):
        pricelst[num] = float(pricelst[num])
    for index in range(len(typelst)):
        if typelst[index] != "Food":
            sum += pricelst[index]
    return sum

def coinFlip():
    coin = ["H", "T"]
    flip = random.choice(coin)
    return flip

def tenFlips():
    fliplst = []
    Tcount = 0
    Hcount = 0
    playerWin = False
    for _ in range(10):
        fliplst.append(coinFlip())
    for i in fliplst:
        if i == 'H':
            Hcount += 1
        elif i == "T":
            Tcount += 1
    if Hcount == Tcount:
        playerWin = True
    return playerWin

def gameSim(trials):
    playerWins = 0
    RosenWins = 0
    for _ in range(trials):
        result = tenFlips()
        if result == True:
            playerWins += 1
        else:
            RosenWins += 1
    print("% Player Wins:\t% Rosen Wins:")
    print(playerWins/trials, "\t", RosenWins/trials)

gameSim(100000)
    
    
