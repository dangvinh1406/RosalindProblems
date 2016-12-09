def _1iba(seq,k,m) :
    global mis
    mis = m
    def mismatch(s,t) :
        global mis
        m = 0
        for i in range(len(s)) :
            if s[i] != t[i] :
                m += 1
                if m > mis :
                    return False
        return True  
        
    def myCount(seq,t) :
        count = 0
        i = 0
        k = len(t)
        while i < len(seq)-k+1:
            if mismatch(seq[i:i+k],t) :
                count += 1
            i += 1
        return count
    
    i = 0
    freq = 0
    kmer = []
    while i < len(seq)-k+1:
        temp = seq[i:i+k]
        tfreq = myCount(seq,temp)
        if tfreq > freq :
            freq = tfreq
            kmer = [temp]
        elif tfreq == freq :
            if temp not in kmer :
                kmer.append(temp)
        i += 1
    print " ".join(map(str,kmer))
