def divisibleSumPairs(n, k, ar):
  pairs = 0
  for i in range(0,len(ar)-1):
    for j in range(i+1,len(ar)):
      if (ar[i] + ar[j]) % k == 0:
        pairs += 1
  return pairs