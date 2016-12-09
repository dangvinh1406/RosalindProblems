def _1a(seq,k) :

    def myCount(seq,t) :
        count = 0
        i = 0
        k = len(t)
        while i < len(seq)-k+1:
            if seq[i:i+k] == t :
                count += 1
            i += 1
        return count
    i = 0
    freq = 0
    kmer = []
    while i < len(seq)-k+1:
        temp = seq[i:i+k]
        if myCount(seq,temp) > freq :
            freq = myCount(seq,temp)
            kmer = [temp]
        elif myCount(seq,temp) == freq :
            if temp not in kmer :
                kmer.append(temp)
        i += 1
    print len(kmer)
    print " ".join(map(str,kmer))




