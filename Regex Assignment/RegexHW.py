import re

file = open("Regex Assignment\words.txt" , "r")
text = file.read()

#Question 1
catDogPattern = "\w*cat\w*|\w*dog\w*"
answer = re.findall(catDogPattern, text)
#print (len(answer))

#Question 2
fourPattern = "\\b\\w{4}\\b"
answer = re.findall(fourPattern, text)
#print(len(answer))

#Question 3
hunPattern = "\w*hun\w*"
answer = re.findall(hunPattern, text)
#print (len(answer))

#Question 4
ingPattern = "\\b(\w+ing)\\b"
ionPattern = "\\b(\w+ion)\\b"
ingTotal = re.findall(ingPattern, text)
ionTotal = re.findall(ionPattern, text)
if len(ingTotal) > len(ionTotal):
    print("There are more words ending in ing")
else:
    print("There are more words ending in ion")

#Questionm 5
