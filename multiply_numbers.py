def main():

    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    aSign = bSign = 1

    if (a[0] < 0):
        a[0] = -a[0]
        aSign = -1

    if (b[0] < 0):
        b[0] = -b[0]
        bSign = -1

    result = [0] * (len(a) + len(b))

    for i in reversed(range(len(a))):
        for j in reversed(range(len(b))):
            result[i+j+1] += a[i] * a[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10
            
    result[0] *= aSign * bSign

    print(result)

if __name__ == '__main__':
    main()

