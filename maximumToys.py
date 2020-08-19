def maximumToys(prices, k):
    toys = 0 
    prices.sort()

    for pos,val in enumerate(prices):
        if k >= val:
            k -= val
            toys += 1
        else:
            break
        
    return toys