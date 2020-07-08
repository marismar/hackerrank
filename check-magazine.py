def checkMagazine(magazine, note):
    m = len(magazine)
    n = len(note)
    if m < n:
        print('No')
        return
    for obj in note:
        try:
            magazine.remove(obj)
        except:
            print('No')
            return
    print('Yes')
    return

note = ['imjaw', 'l', 'khmla', 'x', 'imjaw', 'o', 'l', 'l', 'o', 'khmla', 'v', 'bee', 'o', 'o', 'imjaw', 'imjaw', 'o']
magazine = ['o', 'l', 'x', 'imjaw', 'bee', 'khmla', 'v', 'o', 'v', 'o', 'imjaw', 'l', 'khmla', 'imjaw', 'x']

checkMagazine(magazine,note)



