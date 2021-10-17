# 122. Best Time to Buy and Sell Stock II

def p122(prices):
    """
    Take maximum between today and yesterday action.
    for buying:- 2 conditions: keep the sell or buy today. choose max from the two scenarios
    for selling:- 2 conditions : keep the last sell or sell today.
    """
    buy,sell =  -prices[0], 0
    for i in range(1,len(prices)):
        buy, sell = max(buy, sell-prices[i]),max(sell,prices[i]+buy)
        print(buy, sell)
    return max(buy, sell)

def main():
    # prices = [2,1,4,5,2,9,7]
    # prices = [1,2,7,3,4,8,9]
    prices = [7,1,5,3,6,4]
    # prices = [1,2,4,2,5,7,2,4,9,0]
    profit = p122(prices)
    print(profit)

main()