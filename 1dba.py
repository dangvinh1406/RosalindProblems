def _1c(seq,t) :
    k = len(t)
    idx = []
    i = 0
    while i < len(seq)-k+1:
        if t == seq[i:i+k] :
            idx.append(i)
        i += 1
    print " ".join(map(str,idx))



