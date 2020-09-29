def birthday(s, d, m):
  segments = 0

  for i in range(0,len(s)-m+1):
    if sum(s[i:i+m]) == d:
      segments += 1

  return segments