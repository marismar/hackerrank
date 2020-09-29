def repeatedString(s, n):
    size = len(s)
    mult = int(n/size)
    result = s.count('a') * mult
    rest = n - (size * mult)

    for i in range(rest): #if n/size is a non-integer number
        if (s[i] == 'a'):
            result += 1    

    return result