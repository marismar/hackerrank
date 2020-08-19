def rotLeft(a, d):
    size = len(a)
    
    for obj in range(d):
        a.append(a.pop(0))

    return a
