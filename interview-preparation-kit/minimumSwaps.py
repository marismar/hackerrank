def minimumSwaps(arr):
    swaps = 0

    for i in range(len(arr)-1):
        if arr[i] != i + 1:
            j = arr.index(i+1)
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
            swaps += 1

    return swaps

#This code did not execute within the time limits for larger arrays as input
#Optimize it