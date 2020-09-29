def twoStrings(s1, s2):
    for obj in s2:
        try:
            pos = s1.index(obj)
            return 'YES'
        except:
            pass
    return 'NO'