from itertools import *

def formingMagicSquare(s):
  minCost = 81
  magicSquare = []

  for obj in s:
    magicSquare.extend(obj)

  for perm in permutations(range(1,10)):
    perm = list(perm) #convert tuple to list
    if sum(perm[0:3]) == 15 and sum(perm[3:6]) == 15 and sum(perm[6:9]) == 15:  #rows
      if sum(perm[0::3]) == 15 and sum(perm[1::3]) == 15 and sum(perm[2::3]) == 15: #columns
        if sum(perm[0:9:4]) == 15 and sum(perm[2:7:2]) == 15: #diagonals
          minCost = min(minCost, sum(abs(perm[i] - magicSquare[i]) for i in range(0,9)))
  return minCost