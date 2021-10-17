# 309. Best Time to Buy and Sell Stock with Cooldown
# didn't do it myself

def p309(prices):
    """
    Take maximum between today and yesterday action.
    for buying:- 2 conditions: keep the previous buy or buy today. choose max from the two scenarios
    buy today also indicate the yesterday is cooldown day. 
    for selling:- 2 conditions : keep the last sell or sell today.
    for cooldown:- 2 conditions: keep the previous cooldown or the cooldown after previous sell.
    """
    buy,sell,cool =  -prices[0], 0, 0
    for i in range(1,len(prices)):
        buy, sell, cool = max(buy, cool-prices[i]),max(sell,prices[i]+buy), max(cool, sell)
        print(buy, sell, cool)
    return max(buy, sell, cool)

def main():
    # prices = [2,1,4,5,2,9,7]
    # prices = [1,2,7,3,4,8,9]
    prices = [6,1,3,2,4,7]
    # prices = [1,2,4,2,5,7,2,4,9,0]
    profit = p309(prices)
    print(profit)

main()