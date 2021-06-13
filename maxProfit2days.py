def main():
    prices = [int(x) for x in input().split(' ')]

    first_sell_profit = [0] * len(prices)
    
    min_so_far, max_profit = float('inf'), 0.0
    for i in range(len(prices)):
        price = prices[i]
        profit = price - min_so_far
        max_profit = max(max_profit, profit)
        min_so_far = min(min_so_far, price)
        first_sell_profit[i] = max_profit
        
    max_price = float('-inf')
    max_profit = 0.0
    for i in range(len(prices) - 1, 0, -1):
        price = prices[i]
        max_price = max(max_price, price)
        max_profit = max(
            max_profit,
            max_price - price + first_sell_profit[i - 1])
        
    print(max_profit)
    
if __name__ == '__main__':
    main()
