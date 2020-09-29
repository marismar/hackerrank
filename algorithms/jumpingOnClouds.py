def jumpingOnClouds(c):
    size = len(c)
    index = 0
    step = 0
    
    while(index < size - 1):
        if (index + 2 < size):
            if (c[index+2] == 0):
                index += 2
                step += 1
            else:
                index += 1
                step +=1
        else:
            index += 1
            step +=1
            
    return step