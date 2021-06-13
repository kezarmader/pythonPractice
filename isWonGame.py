def main():
    a = [int(x) for x in input().split()]

    print(isGameWinable(a, 0))
    print(isGameWinableSimple(a))

def isGameWinableSimple(a):
    furthestReach, i = 0, 0
    last_index = len(a) - 1
    #print(last_index)
    while i < last_index and i <= furthestReach:
        #print(i, a[i] + i, furthestReach)
        furthestReach = max(furthestReach, i + a[i])
        i += 1
    return furthestReach >= last_index

def isGameWinable(a, i):
    if i == len(a):
        return True
    if a[i] == 0:
        return False
    
    for j in range(a[i], 0, -1):
        isWon = isGameWinable(a, i + j)
        if isWon:
            return True
    return False

if __name__ == '__main__':
    main()