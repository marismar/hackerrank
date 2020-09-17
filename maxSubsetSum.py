def maxSubsetSum(arr):
  odd = []
  even = []
  for i in range(0, len(arr)):
    if i % 2 == 0:
      even.append(arr[i])
    else:
      odd.append(arr[i])
  return

maxSubsetSum()