def main():
    a = [int(x) for x in input().split(' ')]
    
    for i in range(len(a) - 1):
        if i % 2 == 0:
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
        else:
            if a[i] < a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
    print(a)

if __name__ == '__main__':
    main()