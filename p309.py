# 309. Best Time to Buy and Sell Stock with Cooldown

def create_tree(tree, prices):
    node = 0
    # root
    tree.append(node)
    for 
    while node < len(prices):
        
        while node 

def p309(prices):
    max_profit = 0
    
    while len(prices) > 0:
        tree = list()
        
        if curr_profit > max_profit:
            max_profit = curr_profit
        # remove the first element
        prices.pop(0)
    return max_profit

def main():
    prices = [2,1,2,1,0,0,1]

    profit = p309(prices)
    print(profit)

main()