def NumVowels(word):
    vowelcount = 0
    for i in word:
        if i == 'a':
            vowelcount += 1
        elif i == 'e':
            vowelcount += 1
        elif i == 'i':
            vowelcount += 1
        elif i == 'o':
            vowelcount += 1
        elif i == 'u':
            vowelcount += 1
        
    return vowelcount

print(NumVowels('aeiou'))

def NumEvenDigits(num):
    evendigitcount = 0
    strnum = str(num)
    numlst = []
    for i in strnum:
        i = int(i)
        numlst.append(i)
    for i in numlst:
        if i % 2 == 0:
            evendigitcount += 1
    return evendigitcount

print(NumEvenDigits(451231326565))

def IsItArmstrong(num):
    strnum = str(num)
    numlst = []
    for i in strnum:
        i = int(i)
        numlst.append(i)
    total = 0
    for i in numlst:
        total += i**3
    if total == num:
        return True
    elif total != num:
        return False

print(IsItArmstrong(371))

def Riddler():
    for thousands in range(1,10):
        for hundreds in range(1,10):
            for tens in range(1,10):
                for ones in range(1,10):
                    if (thousands != hundreds and thousands != tens and thousands != ones and
                        hundreds != tens and hundreds != ones and
                        ones != thousands) and (thousands == 3*tens) and (thousands + hundreds + tens + ones == 27) and ones % 2 != 0:
                        return thousands, hundreds, tens, ones
print(Riddler())
    
