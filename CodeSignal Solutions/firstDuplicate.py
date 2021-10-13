def firstDuplicate(a):
    # i = 0 
    # j=
    # lowidx =[]
    # while (i< len(a)-1):
    #     while ()
    if(len(a)<2):
        return -1    
    else:
        lowidx = 0
        for i in range(len(a)):
            for j in range(i+1,len(a),1):
                if(a[i] ==a [j] & j <= lowidx):
                    lowidx =j
    if(lowidx == 0):
        return -1
    else:
        return lowidx
    