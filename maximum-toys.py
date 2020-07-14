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


prices = [1,2,3,4]
k = 7

print(maximumToys(prices,k))