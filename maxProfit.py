def main():
    prices = [int(x) for x in input().split(' ')]

    min_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        profit = price - min_so_far
        max_profit = max(max_profit, profit)
        min_so_far = min(min_so_far, price)
    
    print(max_profit)
    
if __name__ == '__main__':
    main()
