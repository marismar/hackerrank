def countApplesAndOranges(s, t, a, b, apples, oranges):
  fallenApples = 0
  fallenOranges = 0

  for d in apples:
    limMin = s - a
    limMax = t - a
    if d >= limMin and d <= limMax:
      fallenApples += 1 
  for d in oranges:
    limMin = s - b
    limMax = t - b
    if d >= limMin and d <= limMax:
      fallenOranges += 1 

  print(fallenApples)
  print(fallenOranges)
  
  return