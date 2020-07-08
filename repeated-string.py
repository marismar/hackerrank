def repeatedString(s, n):
    size = len(s)
    if (size<1 or size>100 or n<1 or n>(10**12)):
        return -1
    mult = int(n/size)
    result = s.count('a') * mult
    rest = n - (size * mult)
    for i in range(rest):
        if (s[i] == 'a'):
            result += 1    
    return result

s = 'a'
n = 1000000000000

print(repeatedString(s,n))