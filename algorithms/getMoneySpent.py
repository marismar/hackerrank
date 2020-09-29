def getMoneySpent(keyboards, drives, b):
  maxPrice = -1
  for i in range(len(keyboards)):
    for j in range(len(drives)):
      if keyboards[i] + drives[j] <= b:
        maxPrice = max(maxPrice, keyboards[i] + drives[j])
  return maxPrice