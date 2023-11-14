import random

def weightflip():
    if random.random() < 0.55:
        return "H"
    else:
        return "T"

def fileread(filename):
    data = open(filename ,'r')
    #lines = data.readlines()[1:]
    highestTemp = -1000
    lowestTemp = 1000
    highestDay = ''
    lowestDay = ''
    totalHigh = 0
    numdates = 0
    for line in data:
        fields = line.split(',')
        date = fields[0]
        high = int(fields[1])
        low = int(fields[2])
        if high > highest_temp:
            highest_temp = high
            highestDay = date
        if low < lowest_temp:
            lowest_temp = low
            lowestDay = date
        totalHigh += high
        numdates += 1

def methodWriting(word):
    if word[0:2] == "un":
        return word[2:]
    
def minMaxDiff(numbers):
    return max(numbers)-min(numbers)

def swapEnds(numbers):
    end = numbers[-1]
    start = numbers[0]
    numbers[0] = end
    numbers[-1] = start
    return numbers
print(swapEnds([1,2,3,4,5]))

def firstHalf(theList):
    middle = len(theList) // 2
    return theList[0:middle]

def hasWildCat(word):
    hasCat = False
    letterlst = []
    for i in word:
        letterlst.append(i)
    for i in range(len(letterlst)):
        if letterlst[i] == 'c' and i < len(letterlst) - 2:
            if letterlst[i+2] == 't':
                hasCat = True
    return hasCat

def sumStringDigits(word):
    total = 0
    for letter in word:
        if letter.isdigit() == True:
            num = int(letter)
            total += num
    return total


def sumDigits(num):
    '''
    if num < 0:
        num = num *-1
    while num > 0:
    lastDigit = num % 10
    total += lastDigit
    num = num // 10
    '''
    return sumStringDigits(str(num))

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

def evenNums(file):
    total = 0
    data = open(file, 'r')
    for line in file:
        columns = line.split(',')
        for i in columns:
            i = int(i)
            if i % 2 == 0:
                total += i

def mostCommonLetter(text):
    d = {}
    for letter in text:
        if letter not in d:
            d[letter] = 0
        d[letter] += 1
    
    answer = ""
    highestCount = 0
    for letter in d:
        if d[letter] > highestCount:
            highestCount = d[letter]
            answer = letter
    return answer
