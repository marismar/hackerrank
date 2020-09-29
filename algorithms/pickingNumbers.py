def pickingNumbers(a):
  solution = 0

  for num1 in a:
    if a.count(num1) + a.count(num1 + 1) > solution:
      solution = a.count(num1) + a.count(num1 + 1)
    
  return solution