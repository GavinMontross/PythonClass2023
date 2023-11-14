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
            print('Roll:', roll)
        if roll == 1:
            turntotal = 0
            print('Roll:', roll)
            break
    print("Turn total:",turntotal)
    return turntotal

def holdat20noprint(limit = 20):
    turntotal = 0
    while turntotal < limit:
        roll = rolld6()
        if roll != 1:
            turntotal += roll
        if roll == 1:
            turntotal = 0
            break
    return turntotal

def holdAt20Outcomes(trials):
    results = {0:0,20:0,21:0,22:0,23:0,24:0,25:0}
    for _ in range(trials):
        turnTotal = holdat20noprint()
        results[turnTotal] += 1
    for score in results:
        results[score] = results[score]/trials
    return results


def holdAt20orGoalTurn(limit = 20, score = 0):
    turnTotal = 0
    while turnTotal < limit:
        roll = random.randrange(1,6)
        print("Roll:", roll)
        if roll == 1:
            turnTotal = 0
            break
        else:
            turnTotal += roll
    newScore = score + turnTotal
    print("Turn Total: ", turnTotal)
    print("New score: ", newScore)
    
    return newScore
#score = int(input("Score?: "))

#print(holdAt20orGoal(20,score))

def holdAt20orGoalGame():
    newScore = 0
    while newScore < 100:
        turnTotal = 0
        while turnTotal < 20 and turnTotal + newScore < 100:
            roll = random.randint(1,6)
            print("Roll:", roll)
            if roll == 1:
                turnTotal = 0
                break
            else:
                turnTotal += roll
            
        newScore += turnTotal
        print("Turn Total: ", turnTotal)
        print("New score: ", newScore)

#print(holdAt20orGoalGame())

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

def avgPigTurns(games):
    total_turns = 0
    for _ in range(games):
        turns = 0
        newScore = 0
        while newScore < 100:
            turnTotal = 0
            while turnTotal < 20 and turnTotal + newScore < 100:
                roll = random.randint(1,6)
                if roll == 1:
                    turnTotal = 0
                    break
                else:
                    turnTotal += roll
            newScore += turnTotal
            turns += 1
        total_turns += turns
    return total_turns/games
    

#games = int(input("Games?: "))
#print("Average Turns: ", avgPigTurns(games))

def twoPlayer():
    playerOneScore = 0
    playerTwoScore = 0
    turnswitch = 0
    while playerOneScore < 100 and playerTwoScore < 100:
        turnTotal = 0
        turnswitch += 1
        print("Player 1 score: ", playerOneScore)
        print("Player 2 score: ",playerTwoScore)
        if turnswitch % 2 != 0:
            print("It is player 1's turn. ")
            playerOneTurn = True
        elif turnswitch % 2 == 0:
            print("It is player 2's turn. ")
            playerOneTurn = False
        while turnTotal < 20 and turnTotal + playerOneScore < 100 and turnTotal + playerTwoScore < 100:
            roll = random.randint(1,6)
            print("Roll: ", roll)
            if roll == 1:
                turnTotal = 0
                break
            else:
                turnTotal += roll
        print("Turn total: ", turnTotal)
        if playerOneTurn == True:
            playerOneScore += turnTotal
            print("New Score: ", playerOneScore)
        elif playerOneTurn == False:
            playerTwoScore += turnTotal
            print("New Score: ", playerTwoScore)

#twoPlayer()


def pigGame1v1():
    playerOneScore = 0
    playerTwoScore = 0
    turnswitch = 0
    print("You will be player 1")
    print("Enter nothing to roll; enter anything to hold.")
    
    while playerOneScore < 100 and playerTwoScore < 100:
        turnTotal = 0
        turnswitch += 1
        print("Player 1 score: ", playerOneScore)
        print("Player 2 score: ", playerTwoScore)
        
        if turnswitch % 2 != 0:
            print("It is player 1's turn. ")
            playerOneTurn = True
        else:
            print("It is player 2's turn. ")
            playerOneTurn = False
        
        while turnTotal < 20 and turnTotal + playerOneScore < 100 and turnTotal + playerTwoScore < 100:
            if playerOneTurn:
                roll = random.randint(1, 6)
                print("Roll: ", roll)
                
                if roll == 1:
                    turnTotal = 0
                    break
                else:
                    turnTotal += roll
                    print("Turn total: ", turnTotal, end='\t')
                    choice = input("Roll/Hold?  (Enter)")
                    if choice.lower() != '':
                        break
            elif playerOneTurn == False:
                roll = random.randint(1,6)
                print("Roll: ", roll)
                if roll == 1:
                    turnTotal = 0
                    break
                else:
                    turnTotal += roll

        if playerOneTurn == True:
            playerOneScore += turnTotal
            print("New Score: ", playerOneScore)
        elif playerOneTurn == False:
            playerTwoScore += turnTotal
            print("New Score: ", playerTwoScore)

#pigGame1v1()

def main():
    whichfunc = int(input("Which function(1-8)"))
    if whichfunc == 1:
        print(holdat20())
    elif whichfunc == 2:
        trials = int(input("How many trials?: "))
        results = (holdAt20Outcomes(trials))
        print("Score\tEstimated Probability")
        for score in results:
            print(score, results[score]/trials,sep = '\t')
    elif whichfunc == 3:
        limit = int(input("What is the limit for the hold at x game?: "))
        trials = int(input("How many trials?: "))
        results = holdAtXOutcomes(limit, trials)
        print("Score\tEstimated Probability")
        for score in results:
            print(score, results[score]/trials,sep = '\t')
    elif whichfunc == 4:
        score = int(input("Score?: "))
        print(holdAt20orGoalTurn(20, score))
    
        



main()