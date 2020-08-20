def staircase(n):
  for i in range(1, n + 1):
    aux = n - i
    print(' ' * aux + '#' * i)
  return