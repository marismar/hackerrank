def runnerUp(arr):
  maxArr = max(arr)

  for i in range(arr.count(maxArr)):
    arr.remove(maxArr)

  print(max(arr))
  return 