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
    smaller = 0
    equal = 0
    larger = len(a)

    pivot = a[pi]

    while (equal < larger):
        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif a[equal] == pivot:
            equal += 1
        else: 
            larger -= 1
            a[equal], a[larger] = a[larger], a[equal]


if __name__ == '__main__':
    main()