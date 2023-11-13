import random
def rolld6():
    roll = random.randint(1,6)
    return roll


def holdat20(limit=20):
    turntotal = 0
    while turntotal < limit:
        roll = rolld6()
        if roll != 1:
            turntotal += roll
            #print('Roll:', roll)
        if roll == 1:
            turntotal = 0
            #print('Roll:', roll)
            break
    #print("Turn total:",turntotal)
    return turntotal

def holdAt20Outcomes(trials):
    results = {0:0,20:0,21:0,22:0,23:0,24:0,25:0}
    for _ in range(trials):
        turnTotal = holdat20()
        results[turnTotal] += 1
    for score in results:
        results[score] = results[score]/trials
    return results

def holdAt20orGoal(limit = 20, score = 0):
    turnTotal = 0
    while turnTotal < limit:
        roll = random.randrange(1,6)
        print("Roll:", roll)
        if roll == 1:
            turnTotal = 0
            print("Turn Total: ", turnTotal)
            break
        else:
            turnTotal += roll
    newScore = score + turnTotal
    print("Turn Total: ", turnTotal)
    print("New score: ", newScore)
    
    
    return newScore
#score = int(input("Score?: "))

#print(holdAt20orGoal(20,score))


#limit = int(input("What is the limit for the hold at x game?: "))
#trials = int(input("How many trials?: "))

def holdAtXOutcomes(limit, trials):
    results = {0:0}
    for score in range(limit, limit + 6):
        results[score] = 0
    for _ in range(trials):
        turnTotal = holdat20(limit=limit)
        score = holdat20(limit)
        results[turnTotal] += 1
    return results
#results = holdAtXOutcomes(limit, trials)
#print("Score\tEstimated Probability")
#for score in results:
#    print(score, results[score]/trials,sep = '\t')


def avgPigTurns(games):
    totalTurns = 0
    for _ in range(games):
        turnTotal = 0
        newScore = 0
        turns = 0
        while newScore < 100:
                while turnTotal < 20:
                    roll = random.randrange(1, 6)
                    if roll == 1:
                        turnTotal = 0
                        break
                    else:
                        turnTotal += roll

                newScore += turnTotal
                turns += 1
                turnTotal = 0

        totalTurns += turns

    return totalTurns / games
games = int(input("Games? "))
print("Average Turns: ", avgPigTurns(games))

