import random, datetime
from math import log2, floor

def main():
    a = int(input())
    b = int(input())

    print(getRandomAB(a, b))

def getRandomAB(a, b):
    MAX_NUMBER = (b - a) + 1
    MAX_DIGITS = floor(log2(MAX_NUMBER) + 1)

    result = 0

    while (result < MAX_NUMBER):
        for i in range(MAX_DIGITS):
            result = (result << 1) | getOneBitRandom()

        if(result <= MAX_NUMBER):
            break
        result = 0
    
    return result + a

def getOneBitRandom():
    return random.getrandbits(1)

if __name__ == '__main__':
    main()