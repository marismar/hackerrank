def catAndMouse(x, y, z):
  if abs(x - z) < abs(y - z):
    print('Cat A')
  elif abs(x - z) > abs(y - z):
    print('Cat B')
  else:
    print('Mouse C')