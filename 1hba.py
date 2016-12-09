def _1f(t,seq,d) :
    def mismatch(s,t,d) :
        if t == s :
            return True
        count = 0
        for i in range(len(s)) :
            if s[i] != t[i] :
                count += 1
            if count > d :
                return False
        return True
    i = 0
    idx = []
    k = len(t)
    while i < len(seq)-k+1 :
        if mismatch(seq[i:i+k],t,d) :
            idx.append(i)
        i += 1
    print " ".join(map(str,idx))
