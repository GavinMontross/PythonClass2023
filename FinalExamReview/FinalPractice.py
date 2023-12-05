import re

def findHighestScore(file):
    data = open(file, 'r')
    numList = []
    nameList = []
    for line in data:
        values = line.split(',')
        numList.append(values[1])
        nameList.append(values[0])
    nameIndex = numList.index(max(numList))
    return nameList[nameIndex] + " had a score of" + max(numList)
#print(findHighestScore("FinalExamReview/marioscores.csv"))

def removeEmails(inputName, outputName):
    data = open(inputName,'r')
    text = data.read()
    pattern = "tu[a-z]\d{5}@temple\.edu"
    outText = re.sub(pattern, "REDACTED", text)
    out = open(outputName, 'w')
    out.write(outText)
    out.close()

#removeEmails("FinalExamReview/emailtext.txt", "test.txt")

def makeUsername(name, n):
    result = ""
    name = name.lower()
    namelist = name.split()
    firstletters = []
    for name in namelist:
        firstletters.append(name[0])
    for letter in range(len(firstletters)):
        result += firstletters[letter]
    return result + str(n)
#print(makeUsername("Gavin Samuel Montross", 429))

def XOR(a,b):
    if (a == True and b == False) or (b == True and a == False):
        return True
    else:
        return False
#print(XOR(True,True))

def sumOfThrees(numbers):
    total = 0
    for list in numbers:
        for number in list:
            if number % 3 == 0:
                total += number
    return total
#print(sumOfThrees([[10,20],[5],[20,15,1,1,1]]))

def allDigitsProduct(nums):
    product = 1
    for num in nums:
        num = str(num)
        for digit in num:
            product *= int(digit)
    return product
#print(allDigitsProduct([44,12,3112]))




