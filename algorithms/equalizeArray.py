def equalizeArray(arr):
  n = len(arr)  #size of arr
  elements = {} #arr elements and their quantities
  lastValue = [None,0]  #the element with more occurrences on array and his quantity

  for obj in arr:
    actualValue = elements.get(obj, None) #Test if obj is in elements
    if actualValue == None:
      elements[obj] = 1 #first occurrence of this element
    else:
      elements[obj] += 1  #one more occurrence of this element

    if elements[obj] > lastValue[1]:  #update the element with more occurrences
      lastValue[0] = obj
      lastValue[1] = elements[obj]

  return n - lastValue[1] #return the number of exclusions needed to equalize the array