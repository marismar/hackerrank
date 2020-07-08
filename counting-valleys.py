def countingValleys(n, s):
    if (n<2 and n>(10**6)):
        return -1

    for obj in s:
        if (obj != 'D' and obj != 'U'):
            return -1

    level = 0 #sea level
    count_valley = 0
    for obj in s:
        print ()
        if (obj == 'D'):
            if (level == 0):
                count_valley += 1
            level -= 1
        else:
            level += 1
    print(count_valley)
    return count_valley

n = 8
s = ['U','D','D','D','U','D','U','U']

countingValleys(n,s)