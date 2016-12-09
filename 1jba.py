def _1jba(seq,k,m) :
    from Bio.Seq import Seq
    global mis
    mis = m
    seq = Seq(seq)
    def mismatch(s,t) :
        global mis
        m = 0
        for i in range(len(s)) :
            if s[i] != t[i] :
                m += 1
                if m > mis :
                    return False
        if m == mis :
            return True
        else :
            return False
        
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
    while i < len(seq)-k+1 :
        temp = seq[i:i+k]
        reTemp = temp.reverse_complement()
        tfreq = myCount(seq,temp)+myCount(seq,reTemp)
        if tfreq > freq :
            freq = tfreq
            kmer = [temp]
            kmer.append(reTemp)
        elif tfreq == freq :
            if temp not in kmer :
                kmer.append(temp)
            if reTemp not in kmer :
                kmer.append(reTemp)
        i += 1
    print " ".join(map(str,kmer))
