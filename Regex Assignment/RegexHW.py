import re

file = open("Regex Assignment\words.txt" , "r")
text = file.read()

#Question 1
pattern = "\w*cat\w*|\w*dog\w*"
answer = re.findall(pattern, text)
print (len(answer))

#Question 2


