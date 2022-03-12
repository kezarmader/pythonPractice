'''
[7,6,5,4,3,2,1]
[7,6,5,4,3,2,1]
'''
def main():
    a = readList()
    insertionSort(a, len(a))
    print(a)

def readList():
    arr = []
    token = input().split(' ')
    for t in token:
        arr.append(int(t))
    return arr

def insertionSort(a, n):
    if n <= 1:
        return
    
    insertionSort(a, n - 1)
    j = n - 2
    print(a, j)
    while j >= 0 and a[j] > a[j+1]:
        a[j+1],a[j] = a[j],a[j+1]
        j -= 1
        print(a, j)

if __name__ == '__main__':
    main()