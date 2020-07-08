def jumpingOnClouds(c):
    size = len(c)
    if (size < 2 and size > 100 and c[0] != 0 and c[size - 1] != 0):
        return -1
    if ((c.count(0) + c.count(1)) != len(c)):
        return -1
    index = 0
    step = 0
    #0 0 1 0 0 1 0
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