import random

def main():
    size = 30000
    numbers = [251] * size

    '''
    for _ in range(size):
        n = 251
        numbers.append(n)
    '''
    k = 4383

    print(kth_largest_in_an_array(numbers, k))

def kth_largest_in_an_array(numbers, k):
    quickSortTopK(numbers, 0, len(numbers) - 1, len(numbers) - k)
    return numbers[-k]
    
def quickSortTopK(numbers, start, end, k):
    
    low = start
    high = end
    while low <= high:
        partitionIndex = partition(numbers, low, high)
    
        if partitionIndex == k: return

        if partitionIndex > k:
            low = start
            high = partitionIndex-1
        else:
            low = partitionIndex+1
            high = end

def partition(numbers, start, end)->int:
    pivotIndex = random.randint(start, end)
    pivot = numbers[pivotIndex]
    
    numbers[start], numbers[pivotIndex] = numbers[pivotIndex], numbers[start]
    bigger = start
    smaller = start
    for bigger in range(start + 1, end + 1):
        if numbers[bigger] <= pivot:
            smaller += 1
            numbers[smaller], numbers[bigger] = numbers[bigger], numbers[smaller]
    numbers[smaller], numbers[start] = numbers[start], numbers[smaller]

    return smaller

if __name__ == '__main__':
    main()