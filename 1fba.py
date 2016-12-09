def _1e(s) :
    skew = [0]
    GtoC = 0
    for c in s :
        if c == "G" :
            GtoC += 1
        elif c == "C" :
            GtoC -= 1
        skew.append(GtoC)
    l = min(skew)
    idx = []
    for i in range(len(skew)) :
        if skew[i] == l :
            idx.append(i)
    print " ".join(map(str,idx))



