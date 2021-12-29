BUY = 1
SELL = 2

def max_profit(prices):
    n = len(prices)
    max_so_far = 0
    profit = 0
    
    for i in reversed(range(n)):
        max_so_far = max(max_so_far, prices[i])
        profit += max_so_far - prices[i]
        
    return profit

for t in range(int(input())):
    n = int(input())
    prices = [int(x) for x in input().split()]
    print(max_profit(prices))