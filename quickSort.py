from math import pi
import random

def main():
    a = readList()
    quickSort(a, 0, len(a) - 1)
    print(a)

def quickSort(a, start, end):
    if start >= end:
        return
    
    pivotIndex = random.randint(start,end)

    a[start],a[pivotIndex] = a[pivotIndex],a[start]

    pivot = a[start]
    smaller = start
    bigger = start

    for bigger in range(start + 1, end + 1):
        if a[bigger] <= pivot:
            smaller += 1
            a[bigger],a[smaller] = a[smaller],a[bigger]
            
    a[start],a[smaller] = a[smaller],a[start]
    quickSort(a, start, smaller - 1)
    quickSort(a, smaller + 1, end)


def readList():
    result = []
    token = input().split(' ')
    for t in token:
        result.append(int(t))
    return result

if __name__ == '__main__':
    main()