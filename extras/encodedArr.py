""" def encodedArr(arr):
    arr = list(arr)
    n = len(arr)
    a = [0] * 26   #letter_code = pos + 1
    i = 0
    while i < n:
        if i + 2 < n:
            if arr[i+2] == '#':
                num = int(arr[i] + arr[i+1]) 
                if i + 3 < n:    
                    if arr[i+3] == '(':
                        j = i + 4
                        qt = ''
                        while arr[j] != ')':
                            qt += arr[j]
                            j += 1
                        a[num - 1] += int(qt)
                        i = j + 1
                    else:
                        a[num - 1] += 1
                        i += 3
                else:
                    a[num - 1] += 1
                    i += 3
            else:
                num = int(arr[i])
                if i + 1 < n:
                    if arr[i+1] == '(':
                        j = i + 2
                        qt = ''
                        while arr[j] != ')':
                            qt += arr[j]
                            j += 1
                        a[num - 1] += int(qt)
                        i = j + 1
                    else:
                        a[num - 1] += 1
                        i += 1
                else:
                    a[num -1] += 1
                    i += 1
        else:
            num = int(arr[i])
            if i + 1 < n:
                if arr[i+1] == '(':
                    j = i + 2
                    qt = ''
                    while arr[j] != ')':
                        qt += arr[j]
                        j += 1
                    a[num - 1] += int(qt)
                    i = j + 1
                else:
                    a[num - 1] += 1
                    i += 1
            else:
                a[num -1] += 1
                i += 1
    return a """

def encodedArr(arr):
    arr = list(arr)
    n = len(arr)
    a = [0] * 26   #letter_code = pos + 1
    i = 0
    while i < n:
        if i + 2 < n:
            if arr[i+2] == '#':
                num = int(arr[i] + arr[i+1]) 
                if i + 3 < n:    
                    if arr[i+3] == '(':
                        j = i + 4
                        qt = ''
                        while arr[j] != ')':
                            qt += arr[j]
                            j += 1
                        a[num - 1] += int(qt)
                        i = j + 1
                    else:
                        a[num - 1] += 1
                        i += 3
                else:
                    a[num - 1] += 1
                    i += 3
            else:
                num = int(arr[i])
                if i + 1 < n:
                    if arr[i+1] == '(':
                        j = i + 2
                        qt = ''
                        while arr[j] != ')':
                            qt += arr[j]
                            j += 1
                        a[num - 1] += int(qt)
                        i = j + 1
                    else:
                        a[num - 1] += 1
                        i += 1
                else:
                    a[num -1] += 1
                    i += 1
        else:
            num = int(arr[i])
            a[num -1] += 1
            i += 1
    return a

a = '1(2)23(3)26#22#4(5)1(2)2(1)10#'
print(a)
print(encodedArr(a))