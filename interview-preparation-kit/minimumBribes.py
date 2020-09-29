def minimumBribes(q):
    bribes = 0

    for position, value in enumerate(q):
        if value > position + 3:
            print('Too chaotic')
            return
        for j in range(max(0, value - 2), position):
            if q[j] > value:
                bribes += 1

    print(bribes)
    return