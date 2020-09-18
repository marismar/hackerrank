def colorMatrix(pic):
  colors = 0

  for i in range(len(pic)):
    for j in range(len(pic[i])):
      if i == 0:
        if j == 0:
          colors += 1
        else:
          if pic[i][j-1] != pic[i][j]:
            colors += 1
      else:
        if j == 0:
          if pic[i-1][j] != pic[i][j]:
            colors += 1
        else:
          if pic[i-1][j] != pic[i][j] and pic[i][j-1] != pic[i][j]:
            colors += 1

  return colors