consonants = "pkhlmnw"
singleVowels = {"a":"ah",'e':'eh','i':'ee','o':'oh','u':'oo'}
doubleVowels = {'ai':'eye', 'ae':'eye','ao':'ow','au':'ow','ei':'ay','eu':'eh-oo','iu':'ew','oi':'oyo','ou':'ow','ui':'ooey'}
hawaiianword = input('Enter a hawaiian word to pronounce ==> ')

def validate(word):
    word = word.lower()
    for char in word:
        if char not in 'aeiouphklmnw':
            validity = False

        elif char in 'aeiouphklmnw':
            validity = True
    return validity

def reason(word):
    word = word.lower()
    for char in word:
        if char not in 'aeiouphklmnw':
            why = (char.upper() + ' is not a valid Hawaiian character')
            break
        else: 
            continue  
    print(why)

        


def pronounce(word, singleVowels, doubleVowels):
    result = ''
    index = 0
    word = word.lower()
    while index < len(word):
        if word[index] not in 'aeiou' and index == 0 and word[index] != ' ' and word[index] != "'":
            result += word[index]
            index += 1
        elif word[index] not in 'aeiou' and index != 0 and word[index] != ' ' and word[index] != "'":
            if word[index-1] != ' ':
             result += '-' + word[index]
             index += 1
            else:
                result += word[index]
                index += 1
        elif index < len(word) - 1 and word[index] in 'aeiou' and word[index + 1] in 'aeiou':
            if word[index:index + 2] in doubleVowels:
                result += doubleVowels[word[index:index + 2]] + '-'
                index += 2
            else:
                result += singleVowels[word[index]] + '-'
                index += 1
        elif word[index] == ' ':
            result += ' '
            index += 1
        elif word[index] == "'":
            result += "'"
            index += 1
        elif word[index] != ' ' and word[index] != "'":
            result += singleVowels[word[index]]
            index += 1
        
        if '--' in result:
            result = result.replace('--','-') 
        if 'w' in result:
            if result[index-1] in ['i','e']:
                result = result.replace('w','v')
            else:
                continue
    result = result.capitalize()  
    return result.rstrip('-')


def mainLoop(hawaiianword):
    answer = ''
    while answer not in ['n','no']:
        if validate(hawaiianword) == True:   
            print(hawaiianword.upper(), 'is proncounced',(pronounce(hawaiianword,singleVowels, doubleVowels)))
            answer = input("Do you want to enter another word? Y/YES/N/NO ==> ")
            answer = answer.lower()
            if answer == 'y' or answer == 'yes':
                    print()
                    hawaiianword = input('Enter a hawaiian word to pronounce ==> ')
            while answer not in ['y','yes','n','no']:
                print("Enter Y, YES, N, or NO")
                answer = input("Do you want to enter another word? Y/YES/N/NO ==> ")
                answer = answer.lower()
                if answer == 'y' or answer == 'yes':
                    hawaiianword = input('Enter a hawaiian word to pronounce ==> ')
        if validate(hawaiianword) == False:
            reason(hawaiianword)
            print()
            hawaiianword = input('Enter a hawaiian word to pronounce ==> ')

        
mainLoop(hawaiianword)
        
        

