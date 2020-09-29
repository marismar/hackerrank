def kangaroo(x1, v1, x2, v2):
  while (True):
    if (x2 > x1 and v2 >= v1) or (x2 < x1 and v2 <= v1):
      print('NO')
      return 'NO'
    
    x1 += v1
    x2 += v2

    if x1 == x2:
      print('YES')
      return 'YES'