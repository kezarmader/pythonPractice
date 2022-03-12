'''
products = [5, 1, 3, 2, 4, 6]
usage = [3, 2, 1, 5, 5, 2] = max = 2, item = [2, 5], notFound = [4, 6] 

O(1)
{
    3: 1
    2: 1
    1: 1
    5: 2
}

max: 2
element: [5]

1. Products not used : 4, 6
2. Products that are used: 2, 5 
'''

def main():
    products = [5, 1, 3, 2, 4, 6]
    usage = [3, 2, 1, 5, 5, 2]
    '''
    tokens = input().split(' ')
    for token in tokens:
        products.append(int(token))

    tokens = input().split(' ')
    for token in tokens:
        usage.append(int(token))
    '''

    #[[2,5],[4,6]]
    result = productUsage(products, usage)

    print(result)

def productUsage(products, usage):
    hash = {}
    max = float('-inf')
    min = float('inf')
    
    highUsage = []
    lowUsage = []
    noUsage = []

    for product in usage:
        if hash.get(product) == None:
            hash[product] = 1
        else:
            hash[product] += 1
        
        if hash[product] > max:
            max = hash[product]
            highUsage = [product]
        elif hash[product] == max:
            highUsage.append(product)

    for product in products:
        if hash.get(product) == None:
            noUsage.append(product)
        else:
            if hash[product] < min:
                min = hash[product]
                lowUsage = [product]
            elif hash[product] == min:
                lowUsage.append(product)
    
    return [highUsage, lowUsage, noUsage]

if __name__ == '__main__':
    main()