import random

def sevenCardGame():
    cards = ["b"] * 5 + ["r"] *2
    random.shuffle(cards)
    choices = cards[:3]
    
    #choices = random.sample(cards,3)
    if 'r' in choices:
        return False
    else:
        return True
TRIALS = 10000
wins = 0
for _ in range(TRIALS):
    result = sevenCardGame()
    if result:
        wins += 1
print(wins/TRIALS)



"""
def rollDf():
    faces = ['+', '+', '_','_', '-', '-']
    roll = random.choice(faces)
    return roll

def sim4df():
    total = 0
    for _ in range(4):
        result = rollDf()
        if result == '+':
            total += 1
        elif result == '-':
            total -= 1
    return total

TRIALS = 100000
higherThanZero = 0
for _ in range(TRIALS):
    roll = sim4df()
    if roll >= 0:
        higherThanZero += 1
print(higherThanZero/TRIALS)
"""

"""
def coinFlip():
    coin = ['H','T']
    flip = random.choice(coin)
    return flip

player1 = "THH"
player2 = "HHT"

def playGame():
    result = ''
    while True:
        result += coinFlip()
        if player1 in result:
            return 'player1win'
            break
        elif player2 in result:
            return 'player2win'
            break
        else:
            continue


player1total = 0
player2total = 0
TRIALS = 100000
for _ in range(TRIALS):
    result = playGame()
    if result == 'player1win':
        player1total += 1
    elif result == 'player2win':
        player2total += 1
print("player1's win %:", player1total/TRIALS)
print("player2's win %:", player2total/TRIALS)
"""

