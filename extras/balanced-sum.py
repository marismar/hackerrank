def balancedSum(arr):
    n = len(arr) #size of arr
    pivot = 0
    
    for i in range(1,n-1):
        if sum(arr[:i]) == sum(arr[i+1:n]):
                pivot = i
                break
    return pivot