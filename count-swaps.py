def countSwaps(a):
    n = len(a)
    swaps = 0
    for i in range(0, n):
        for j in range(0, n-1):
            if a[j] > a[j+1]:
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux
                swaps += 1

    print('Array is sorted in',swaps, 'swaps')
    print ('First Element:',a.pop(0))
    print ('Last Element:',a.pop())

countSwaps([3,2,1])