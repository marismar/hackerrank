def sockMerchant(n, ar):       
    if (n>=1 and n<=100 and len(ar)>=1 and len(ar)<=100):
        added_colors = []
        pairs = 0
        for obj in ar:
            if (obj not in added_colors):
                pairs += int(ar.count(obj)/2)
                added_colors.append(obj)
        return pairs
    else:
        return -1