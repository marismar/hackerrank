def alternatingCharacters(s):
    deleted = 0
    for i in range(0,len(s)):
        while True:
            if i+1 < len(s):    
                if s[i] == s[i+1]:
                    s.pop(i+1)
                    deleted += 1
                else:
                    break
            else:
                return deleted
    return deleted

print(alternatingCharacters(['a','a','a','a'])) 

#WRONG ANSWERS ---- DO IT AGAIN
    