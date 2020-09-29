def sockMerchant(n, ar):       
    addedColors = []
    pairs = 0
    
    for obj in ar:
        if (obj not in addedColors):
            pairs += int(ar.count(obj)/2)
            addedColors.append(obj)
            
    return pairs