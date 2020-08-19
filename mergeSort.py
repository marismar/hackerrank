def mergeSort(arr):
    if len(arr) > 1:
        middle = int(len(arr)/2)
        left = arr[:middle]
        right = arr[middle:]
        n1 = n2 = 0

        left = mergeSort(left)
        right = mergeSort(right)

        for i in range(0,len(arr)):
            if n1 < len(left) and n2 < len(right):
                if (left[n1] < right[n2]):
                    arr[i] = left[n1]
                    n1 += 1
                else:
                    arr[i] = right[n2]
                    n2 += 1
            elif n1 < len(left):
                arr[i] = left[n1]
                n1 += 1
            elif n2 < len(right):
                arr[i] = right[n2]
    return arr


