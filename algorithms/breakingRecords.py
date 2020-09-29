def breakingRecords(scores):
  breaksRecord = [0, 0]
  maxScore = scores[0]
  minScore = scores[0]

  for obj in scores:
    if obj < minScore:
      minScore = obj
      breaksRecord[1] += 1
    elif obj > maxScore:  
      maxScore = obj
      breaksRecord[0] += 1

  return breaksRecord