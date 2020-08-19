def decresingArr(arr):
    n = len(arr) # size of arr
    qt = 0
    
    for i in range(0,n-2):
        for j in range(i+i,n-1):
            if arr[i] > arr[j]:
                for k in range(j+1, n):
                    if arr[j] > arr[k]:
                        qt += 1 
    return qt