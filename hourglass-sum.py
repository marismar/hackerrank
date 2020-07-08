def hourglassSum(arr):
    row = len(arr)
    col = len(arr[0])
    if (row < 6): 
        return -1
    if (col < 6):
        return -1
    for i in range(row):
        for j in range(col):
            if (arr[i][j] < -9 or arr[i][j] > 9):
                return -1          
    result = []
    for  i in range(row-2):
        for j in range(col-2):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]                
            result.append(s)
    result.sort()
    maxn = result.pop() 
    return maxn