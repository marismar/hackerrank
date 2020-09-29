def makeAnagram(a, b):
    aLetters = {}
    bLetters = {}
    a = list(a)
    b = list(b)
    delChars = 0    #number of chars to be deleted

    for i in a:
        if i in aLetters:
            aLetters[i] += 1
        else:
            aLetters[i] = 1
    for j in b:
        if j in bLetters:
            bLetters[j] += 1
        else:
            bLetters[j] = 1
    
    for key, val in aLetters.items():
        if key in bLetters: 
            delChars += abs(val - bLetters[key])
        else:
            delChars += val
    for key, val in bLetters.items():
        if key not in aLetters:
            delChars += val
    return delChars