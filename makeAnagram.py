def makeAnagram(a, b):
    a_letters = {}
    b_letters = {}
    a = list(a)
    b = list(b)
    del_chars = 0

    for i in a:
        if i in a_letters:
            a_letters[i] += 1
        else:
            a_letters[i] = 1
    for j in b:
        if j in b_letters:
            b_letters[j] += 1
        else:
            b_letters[j] = 1
    
    for key, val in a_letters.items():
        if key in b_letters: 
            del_chars += abs(val - b_letters[key])
        else:
            del_chars += val
    for key, val in b_letters.items():
        if key not in a_letters:
            del_chars += val
    return del_chars