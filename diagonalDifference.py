def diagonalDifference(arr):
  priDiagonal = 0   #primary diagonal
  secDiagonal = 0   #secondary diagonal
  j = len(arr) - 1

  for i in range(0,len(arr)):
      priDiagonal += arr[i][i]
      secDiagonal += arr[j][i]
      j -= 1
  #return the absolute difference between primary diagonal and secondary diagonal
  return abs(priDiagonal - secDiagonal) 