import re

file = open("Regex Assignment\words.txt" , "r")
text = file.read()

#Question 1
pattern = "\w*cat\w*|\w*dog\w*"
answer = re.findall(pattern, text)
#print (len(answer))

#Question 2
pattern = "\\b\\w{4}\\b"
answer = re.findall(pattern, text)
#print(len(answer))

#Question 3
pattern = "\w*hun\w*"
answer = re.findall(pattern, text)
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
