def rotLeft(a, d):
    size = len(a)
    if (size<1 or size>(10**5) or d<1 or d>size):
        return -1
    for obj in a:
        if (obj>(10**6) or obj<1):
            return -1
    for obj in range(d):
        a.append(a.pop(0))
    return a
