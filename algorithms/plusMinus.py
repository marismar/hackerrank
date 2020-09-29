def plusMinus(arr):
  total = len(arr)  #total of numbers in arr
  positives = 0     #positives values in arr
  negatives = 0     #negatives values in arr
  zeros = 0         #zeros in arr

  for num in arr:
    if num > 0:
      positives += 1
    elif num < 0:
      negatives += 1
    else:
      zeros += 1    
  
  print(positives/total)  #proportion of positive values
  print(negatives/total)  #proportion of negative values
  print(zeros/total)      #proportion of zeros

  return