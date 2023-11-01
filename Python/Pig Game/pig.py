import random
def rolld6():
    roll = random.randint(1,6)
    return roll


def holdat20():
    turntotal = 0
    while turntotal < 20:
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
holdat20()


def holdAt20Outcomes(trials):
    results = {0:0,20:0,21:0,22:0,23:0,24:0,25:0}
    for _ in range(trials):
        turnTotal = holdat20()
        results[turnTotal] += 1
    for score in results:
        results[score] = results[score]/trials
    return results


results = holdAt20Outcomes(100000)
print("Score\tEstimated Probability")
for score in results:
    print(score,results[score],sep="\t")