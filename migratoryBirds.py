def migratoryBirds(arr):
  birds = [0,0,0,0,0]
  for obj in arr:
    birds[obj-1] += 1
  return birds.index(max(birds)) + 1