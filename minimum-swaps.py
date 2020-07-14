""" def minimumSwaps(arr):
    n = len(arr) # the size of arr
    swaps = 0

    for i in range(0,n): #increment
        j = n - 1
        while arr[i] != i + 1:
            print('arr[',i,'] = ',arr[i])
            print('arr[',j,'] = ',arr[j])
            if arr[j] == i + 1:
                print(arr)
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
                swaps += 1
                print('swap')
                print(arr)
                j = n - 1
            else: 
                if j == 1:
                    print('break')
                    break
                else:
                    j -= 1
                    print('j-1')
    return(swaps)


arr = [7, 1, 3, 2, 4, 5, 6]
arr1 = [1,3,5,2,4,6,7]
i = 1
j = arr1.index(i+1)
aux = arr1[i]
arr1[i] = arr1[j]
arr1[j] = aux
print(arr1)

 """
"""
for i in range(len(nomes)-1,-1,-1):
    print(nomes[i]) """

""" def minimumSwaps(arr):
    n = len(arr) # the size of arr
    swaps = 0
    for i in range(0,n):
        j = i + 1
        while arr[i] != i + 1:
            if arr[j] == i + 1:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
                swaps += 1
                break
            j += 1
    return swaps """


def minimumSwaps(arr):
    n = len(arr) # the size of arr
    swaps = 0
    for i in range(0,n):
        print('arr[',i,'] = ',arr[i])
        print('arr[',j,'] = ',arr[j])
        print(arr)
        if arr[i] != i + 1:
            j = arr.index(i+1)
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
            swaps += 1
            print('swap')
        print(arr)
    return swaps

arr = [7, 1, 3, 2, 4, 5, 6]
arr1 = [1,3,5,2,4,6,7]

print(minimumSwaps(arr))