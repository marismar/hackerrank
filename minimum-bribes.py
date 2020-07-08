def minimumBribes(q):
    moves = 0
    for position, value in enumerate(q):
        if ((value - 1) - position > 2):
            return 'Too chaotic'
        for j in range(max(0, value - 2), position):
            if q[j] > value:
                moves += 1
            print(moves)
    return moves

q = [2, 1, 5, 3, 4]

minimumBribes(q)