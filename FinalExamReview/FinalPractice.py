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
print(findHighestScore("FinalExamReview/marioscores.csv"))