def sherlockAndAnagrams(s):
    arr = []
    x = 0
    pairs = 0
    for i in range(1,len(s)):
        arr.append(s[0:0+i])
        x += 1
        for pos in range(1,len(s)+1):
            aux = s[pos:pos+i]
            if len(arr[x-1]) != len(aux):
                break
            arr.append(aux)
            x += 1
    
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if len(arr[i]) != len(arr[j]):
                break
            for m in range(0,len(arr[i])):
                if arr[i][m] not in arr[j]:
                    break
                print(arr[i])
                print(arr[j])
                pairs += 1
    
    return int(pairs/2)

#WRONG ANSWERS for the following inputs: ifailuhkqq 3 and kkkk 10

                
                    