import random

def coinFlip():
    coin = ["H", "T"]
    flip = random.choice(coin)
    return flip

def tenFlips():
    fliplst = []
    Tcount = 0
    Hcount = 0
    playerWin = False
    for _ in range(10):
        fliplst.append(coinFlip())
    for i in fliplst:
        if i == 'H':
            Hcount += 1
        elif i == "T":
            Tcount += 1
    if Hcount == Tcount:
        playerWin = True
    return playerWin

def gameSim(trials):
    playerWins = 0
    RosenWins = 0
    for _ in range(trials):
        result = tenFlips()
        if result == True:
            playerWins += 1
        else:
            RosenWins += 1
    print("% Player Wins:\t% Rosen Wins:")
    print(playerWins/trials, "\t", RosenWins/trials)

gameSim(100000)