def minimumSwaps(arr):
    size = len(arr)
    if size<1 or size>10**5:
        return -1

    a = []
    for pos,val in enumerate(arr):
        if val<1 or val>size:
            return -1
        elif pos == val - 1:
            a.append(val)   #add in ordered numbers
    for i in range(size):
        
        

