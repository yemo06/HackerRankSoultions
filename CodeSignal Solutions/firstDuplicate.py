def firstDuplicate(a):
    if(len(a)<2):
        return -1
    else:
        lowidx = len(a)
        for i in range(len(a)):
            for j in range(i+1,len(a),1):
                if((a[i] == a[j]) & (j < lowidx)):
                        lowidx = j
    
    if(lowidx == len(a)):
        return -1
    else:
        return a[lowidx]
    
    