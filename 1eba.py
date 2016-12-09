def _1d(seq,k,L,t) :
    i = 0
    kmer = []
    while i < len(seq)-L+1 :
        j = i+1
        count = 1
        while j < i+L :
            if seq[i:i+k] == seq[j:j+k] :
                count += 1
            if count == t :
                if seq[i:i+k] not in kmer :
                    kmer.append(seq[i:i+k])
                break
            j += 1
        i += 1
    print " ".join(map(str,kmer))

        
