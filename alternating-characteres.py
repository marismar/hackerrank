def alternatingCharacters(s):
    delete = 0
    for i in range(0,len(s)):
        while True:
            if i+1 < len(s):    
                if s[i] == s[i+1]:
                    s.pop(i+1)
                    delete += 1
                else:
                    break
            else:
                return delete
    return delete

print(alternatingCharacters(['a','a','a','a']))     
    