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
