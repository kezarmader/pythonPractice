def main():
    a = readList()
    mergeSort(a)
    print(a)

def mergeSort(a) -> list:
    mergeSortReq(a, 0, len(a) - 1)

def mergeSortReq(a, start, end):
    if end <= start:
        return

    mid = ((end - start) // 2) + start
    mergeSortReq(a, start, mid)
    mergeSortReq(a, mid + 1, end)

    res = []
    
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if a[i] <= a[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(a[j])
            j += 1
        
    while i <= mid:
        res.append(a[i])
        i += 1
        
    while j <= end:
        res.append(a[j])
        j += 1
    
    k = 0
    for i in range(start, end+1):
        a[i] = res[k]
        k += 1
    
def readList() -> list:
    result = []
    tokens = input().split(' ')
    for t in tokens:
        result.append(int(t))
    return result

if __name__ == '__main__':
    main()