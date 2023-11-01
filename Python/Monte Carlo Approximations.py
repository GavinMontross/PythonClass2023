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
