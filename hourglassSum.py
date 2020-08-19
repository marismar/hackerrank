def hourglassSum(arr):
    row = len(arr)
    col = len(arr[0])
    result = []

    for  i in range(row-2):
        for j in range(col-2):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]                
            result.append(s)

    return max(result)