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