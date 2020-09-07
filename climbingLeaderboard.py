""" def climbingLeaderboard(scores, alice):
  
  scores = list(dict.fromkeys(scores))  #remove duplicates
  scores.sort(reverse=True)

  pos = []
  
  for score in alice:
    for i in range(0,len(scores)):
      if score >= scores[i]:
        pos.append(i+1)
        break
      elif i + 1 == len(scores):
        pos.append(len(scores) + 1)

  print(pos)
  return pos """

def climbingLeaderboard(scores, alice):
  pos = []

  for score in alice:
    counter = 1

    for i in range(0,len(scores)):
      if score >= scores[i]:
        pos.append(counter)
        break
      elif i + 1 == len(scores):
        pos.append(counter + 1)
      try:
        if scores[i-1] == scores[i]:
          continue
        else:
          counter += 1
      except:
        pass
  print(pos)
  return pos

scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]

climbingLeaderboard(scores, alice)

scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]

climbingLeaderboard(scores, alice)
