import statistics
def fileread(file):
    data = open(file, 'r')
    datelst = []
    highs = []
    lows = []
    for line in data:
        values = line.split(",")
        datelst.append(values[0])
        highs.append(values[1])
        lows.append(values[2])
    for value in range(len(highs)):
        highs[value] = int(highs[value])
        lows[value] = int(lows[value])
    hottestindex = highs.index[max(highs)]
    lowestindex = lows.index[min(lows)]
    hottestday = datelst[hottestindex]
    coldestday = datelst[lowestindex]
    highaverage = statistics.mean(highs)

def evenNum(file):
    data = open(file, 'r')
    total = 0
    for line in data:
        values = line.split(',')
        for i in range(len(values)):
            values[i] = int(values[i])
            if i % 2 == 0:
                total += i
def unorUn(word):
    if word[0:2] == 'un':
        return word[2:]
    else:
        return "un" + word
def swapEnds(list):
    first = list[0]
    last = list[-1]
    list[0] = last
    list[-1] = first
    return list
def sumStringDigits(word):
    total = 0
    for c in word:
        if c.isdigit():
            c = int(c)
            total += c
    return total
print(sumStringDigits('ab12cd34das'))