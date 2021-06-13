# same weight closet number
def main():
   a = int(input())
   b = findSameWeight(a) 
   print (b)

def findSameWeight(a):
    UNSIGNED_MAX_BITS = 64
    
    for i in range(UNSIGNED_MAX_BITS - 1):
        if ((a >> i) & 1) != ((a >> (i+1)) & 1):
            a ^= (1 << i) | (1 << (i+1))
            break

    return a

if __name__ == '__main__':
    main()