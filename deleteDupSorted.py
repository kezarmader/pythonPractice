def main():
    a = [int(x) for x in input().split(' ')]
    print(removeDups(a))

def removeDups(a):
    i = 0
    j = i + 1
    while (j < len(a)):
        #print(i, j, a[i], a[j], a)
        if(a[i] != a[j]):
            a[i+1] = a[j]
            i += 1
        j += 1

    i += 1
    while (i < len(a)):
        a[i] = 0
        i += 1

    return a

if __name__ == '__main__':
    main()