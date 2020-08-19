def countingValleys(n, s):
    level = 0 #sea level
    valleys = 0

    for obj in s:
        if (obj == 'D'):
            if (level == 0):
                valleys += 1
            level -= 1
        else:
            level += 1
    
    return valleys