def bonAppetit(bill, k, b):
  rest = b - int((sum(bill) - bill[k]) / 2)
  if rest != 0:
    print(rest)
  else:
    print('Bon Appetit')
  return