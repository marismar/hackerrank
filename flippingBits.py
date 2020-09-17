def flippingBits(n):
  b = list(bin(n).replace('0b', '').zfill(32))
  print(b)
  for i in range(len(b)):
    if b[i] == '1':
      b[i] = '0'
    else:
      b[i] = '1'
  b = ', '.join(b)
  print(b)
  return

flippingBits(2)