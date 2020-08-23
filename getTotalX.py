def getTotalX(a, b):
  limMax = min(b) #maximum limit
  limMin = max(a) #minimum limit
  sizeA = len(a)
  sizeB = len(b)
  nums = []
  result = 0
  aux = limMin

  while (aux <= limMax):
    for j in range(0,sizeA):
      if (j == sizeA - 1) and (aux % a[j] == 0):
        nums.append(aux)
        break
      if aux % a[j] == 0:
        continue
      else: 
        break
    aux += limMin
  
  for num in nums:
    for j in range(0,sizeB):
      if (j == sizeB -1) and (b[j] % num == 0):
        result += 1
        break
      if b[j] % num == 0:
        continue
      else:
        break
      
  return result

a = [3,9,6]
b = [36,72]

print(getTotalX(a,b))