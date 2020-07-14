def minimumBribes(q):
    moves = 0
    for position, value in enumerate(q):
        if value > position + 3:
            return 'Too chaotic'
        for j in range(0, position):
            if q[j] > value:
                moves += 1
        """ if value == position + 2:
            moves += 1
        elif value == position + 3:
            moves += 2 """
    return moves

q1 = [2, 5, 1, 3, 4]
q2 = [5, 1, 2, 3, 7, 8, 6, 4]
q3 = [1, 2, 5, 3, 7, 8, 6, 4]
q4 = [1, 2, 5, 3, 4, 7, 8, 6]
q5 = [2, 1, 5, 3, 4]

print(minimumBribes(q1))
print(minimumBribes(q2))
print(minimumBribes(q3))
print(minimumBribes(q4))
print(minimumBribes(q5))


""" 
def minimumBribes(q):
    bribes = 0
    for pos, val in enumerate(q):
        if val > pos + 3:
            print('Too chaotic')
            return
        elif val == pos + 2:
            bribes += 1
        elif val == pos + 3:
            bribes += 2
    print(bribes)
    return """