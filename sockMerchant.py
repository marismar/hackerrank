def sockMerchant(n, ar):       
    added_colors = []
    pairs = 0
    
    for obj in ar:
        if (obj not in added_colors):
            pairs += int(ar.count(obj)/2)
            added_colors.append(obj)
            
    return pairs