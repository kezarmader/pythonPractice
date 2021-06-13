def main():
    print('i=?')
    pi = int(input())
    print('n=?')
    n = int(input())
    print('a['+str(n)+']=?')
    a = [int(i) for i in input().split(' ')]

    pivot(a, pi)
    
    print(a)

def pivot(a, pi):
    for i in range(pi):
        print('f', i)
        if(a[i] >= a[pi]):
            swap(a, i, pi)
            print(a)
            return pivot(a, i)
    for i in range(pi, len(a)):
        print('b', i)
        if(a[i] < a[pi]):
            swap(a, i, pi)
            print(a)
            return pivot(a, i)

def swap(a, i, pi):
    t = a[i]
    a[i] = a[pi]
    a[pi] = t

if __name__ == '__main__':
    main()