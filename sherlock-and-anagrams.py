""" def checkPair(p1,p2):
    copy = p2.copy()
    for obj in p1:
        try:
            copy.remove(obj)
        except:
            return False
    return True
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    pair = 0
    print('pair', pair)
    for pos in range(0,len(s)):
        for pos_aux in range(pos + 1,len(s)):
            i = 0
            print('i', i)
            p1 = []
            p2 = []
            while True:
                a = s[pos+i]
                b = s[pos_aux-i]
                p1.append(a)
                p2.append(b)
                print('a', a)
                print('b', b)
                print('p1', p1)
                print('p2', p2)
                if checkPair(p1, p2):
                    pair +=1
                i += 1
                print('pair', pair)
                if (pos_aux-i<0 or pos+i>=len(s) or pos_aux-i<pos+i-2):
                    print(pos_aux-i<0)
                    print(pos+i>=len(s))
                    print(pos_aux-i<pos+i)
                    print('oi')
                    break
    print(pair)
    return pair
 """


def getStrings(s):
    arr = []
    x = 0
    for i in range(1,len(s)):
        arr.append(s[0:0+i])
        x += 1
        print('arr = ',arr)
        for pos in range(1,len(s)+1):
            aux = s[pos:pos+i]
            print('aux = ',aux)
            if len(arr[x-1]) != len(aux):
                break
            arr.append(aux)
            x += 1
    return arr


                


""" def sherlockAndAnagrams(s):
    arr1 = []
    arr2 = []
    pairs = 0
    for j in range(len(s)):
        for i in range(1,len(s)):
            arr1 = s[j:j+i]
            print('arr1 = ',arr1, '\n')
            for pos in range(1,len(s)+1):
                arr2 = s[pos:pos+i]
                print('arr1 = ',arr1)
                print('arr2 = ',arr2)
                if len(arr1) != len(arr2):
                    break
                print('pairs = ', pairs)
    return pairs """


def getPairs(s):
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

s = ['a','b','b','a']
print(s)
print(getPairs(s))

                
                    