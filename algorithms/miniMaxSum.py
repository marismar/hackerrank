def miniMaxSum(arr):
  sumArr = sum(arr)
  minSum = None
  maxSum = None

  for num in arr:
    sumArr -= num
    if (maxSum == None) and (minSum == None):
      maxSum = sumArr
      minSum = sumArr
    elif (sumArr) > maxSum:
      maxSum = sumArr
    elif (sumArr) < minSum:
      minSum = sumArr
    sumArr += num
    
  print(minSum, maxSum)
  return