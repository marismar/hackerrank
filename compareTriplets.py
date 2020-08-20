def compareTriplets(a, b):
  scores = [0,0]
  
  for i in range(0,len(a)):
      if a[i] > b[i]:
          scores[0] += 1
      elif a[i] < b[i]:
          scores[1] += 1

  return scores  