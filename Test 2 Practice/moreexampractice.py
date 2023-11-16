import random
import statistics
def coinFlip():
    if random.random()<0.55:
        return "T"
    else:
        return"H"
def fileReading(file):
    data = open(file, 'r')
    datelst = []
    highlst = []
    lowlst = []
    for line in data:
        values = line.split(',')
        datelst.append(values[0])
        highlst.append(values[1])
        lowlst.append(values[2])
    for value in range(len(highlst)):
        highlst[value] = int(highlst[value])
        lowlst[value] = int(lowlst[value])
    highestindex = highlst.index(max(highlst))
    lowestindex = lowlst.index(min(lowlst))
    highestday = datelst[highestindex]
    lowestday = datelst[lowestindex]
    averagehigh = statistics.mean(highlst)
    return highestday, lowestday, averagehigh

def evenNumbers(file):
    data = open(file, 'r')
    total = 0
    for line in data:
        values = line.split(',')
        for num in values:
            num = int(num)
            if num % 2 == 0:
                total += num
    return total

def unOrUn(word):
    if word[0:2] == 'un':
        return word[2:]
    else:
        return 'un' + word
def maxMinDiff(list):
    return (max(list) - min(list))

def swapEnds(list):
    last = list[-1]
    first = list[0]
    list[0] = last
    list[-1] = first
    return list

def firstHalf(list):
    middle = len(list)//2
    return list[0:middle]

def hasWildCat(word):
    hasCat = False
    for c in range(len(word)):
        if word[c] == 'c':
            if word[c+2] == 't' and c < len(word) - 2:
                hasCat = True
    return(hasCat)

def isEverywhere(nums, val):
    for i in range(len(nums) - 1):
        if nums[i] != val and nums[i + 1] != val:
            return False
    return True

def sumStringDigits(word):
    total = 0
    for c in word:
        if c.isdigit():
            c = int(c)
            total += c
    return total

def sumDigits(num):
    total = 0
    num = str(num)
    for c in num:
        if c.isdigit():
            c = int(c)
            total += c
    return total

def copyEvens(list, count):
    evens = []
    tally = 0
    for c in list:
        if c % 2 == 0 and tally < count:
            evens.append(c)
            tally += 1
    return evens

def roll():
    return random.randint(1,6)

def monoTurn():
    die1 = roll()
    die2 = roll()
    if die1 == die2:
        die1 = roll()
        die2 = roll()
        if die1 == die2:
            die1 = roll()
            die2 = roll()
            if die1 == die2:
                return 3
            return 2
        return 1
    return 0

def percentCalc():
    results = {0:0,1:0,2:0,3:0}
    trials = 100000
    for i in range(trials):
        i = monoTurn()
        results[i] += 1
    print("Number of Doubles:\tPercentage:")
    for double in results:
        print(double, results[double]/trials,sep = '\t'*3)

def mostCommon(word):
    letters = {}
    for c in word:
        if c not in letters:
            letters[c] = 0
        letters[c] += 1
    return max(letters)
print(mostCommon('aaabdcgoejtaaa'))    