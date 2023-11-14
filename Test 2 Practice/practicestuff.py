import random

def weightflip():
    if random.random() < 0.55:
        return "H"
    else:
        return "T"
